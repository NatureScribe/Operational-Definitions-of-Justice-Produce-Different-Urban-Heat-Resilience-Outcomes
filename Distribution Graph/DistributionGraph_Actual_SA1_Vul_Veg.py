import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import FuncFormatter
import seaborn as sns
from matplotlib.ticker import ScalarFormatter
import matplotlib as mpl


########################## Plot distributional graphs at SA1 level for all justice theories  ############################

df = pd.read_excel('SA1_Integrated_Dataset_Filtered_Vul_Veg.xlsx')

plt.figure(figsize=(9, 5))

# Updating matplotlib configuration to use Helvetica
mpl.rcParams['font.size'] = 13
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'Helvetica'  # Ensure Helvetica is installed, otherwise use 'Arial' or another sans-serif font.


legend_names = {
    'Egalitarian Difference': 'egalitarian',
    'Prioritarian Difference': 'prioritarian',
    'Sufficientarian Difference': 'sufficientarian'
}


for column in ['Egalitarian Difference', 'Prioritarian Difference', 'Sufficientarian Difference']:
    sns.kdeplot(df[column], fill=True, label=f'Deviation from {legend_names[column]} \n (Mean: {df[column].mean()/100:.2f}%, Std: {df[column].std()/100:.2f}%)', clip=(-3000, 3000))


plt.ylim(-0.00004, 0.0014)
# plt.ylim(-0.00025, 0.0100) ###zero

plt.xlim(-3000, 3000)

# Create a gradient from red to yellow to green
def get_gradient_colors(start_color, mid_color, end_color, n=100):
    # Create a color map from start to end color
    cmap = mcolors.LinearSegmentedColormap.from_list("", [start_color, mid_color, end_color])
    return cmap(np.linspace(0, 1, n))

# Apply gradient
ax = plt.gca()
xmin, xmax = -700, 700  # -7% to +7%
ymin, ymax = -0.00004, -0.000005
# ymin, ymax = -0.00025, -0.00001 ###zero
colors = get_gradient_colors('red', 'yellow', 'green')


# Fill areas under -700 with red
ax.fill_between([ax.get_xlim()[0], xmin], ymin, ymax, color='red', edgecolor=None)
# ax.fill_between([-3000, xmin], ymin, ymax, color='red', edgecolor=None)  ### zero

# Fill gradient between -700 and +700
for i, color in enumerate(colors):
    x_start = xmin + (xmax - xmin) * i / len(colors)
    x_end = xmin + (xmax - xmin) * (i + 1) / len(colors)
    if x_start >= xmin and x_end <= xmax:
        ax.fill_between([x_start, x_end], ymin, ymax, color=color, edgecolor=None)

# Fill areas above +700 with green
ax.fill_between([xmax, ax.get_xlim()[1]], ymin, ymax, color='green', edgecolor=None)
# ax.fill_between([xmax, 3000], ymin, ymax, color='green', edgecolor=None)  ### zero


# Adding specific ticks for -700 and +700 in x-axis
def to_percent(x, _):
    return f"{x / 10000:.0%}"

custom_ticks = np.array([-3000, -1500, 0, 1500, 3000, -700, 700])  # These correspond to -30%, -15%, 0%, 15%, 30%, -7%, 7%
plt.xticks(custom_ticks, labels=[to_percent(tick, None) for tick in custom_ticks])  # Convert each tick value to a percentage label


# Applying the custom formatter to the x-axis
plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))



plt.legend(ncol=1)
ax = plt.gca()  # Get the current Axes instance on the current figure
y_formatter = ScalarFormatter(useMathText=True)
y_formatter.set_scientific(True)
y_formatter.set_powerlimits((-2, 2))  # Use scientific notation if exponent is greater than 3 or less than -3
ax.yaxis.set_major_formatter(y_formatter)
plt.xlabel("Deviation from justice (%)")  # Set the x-axis label
plt.ylabel("Kernel density estimates")  # Set the x-axis label

# Draw a vertical dashed line at 0%
plt.axvline(x=0, color='k', linestyle='--', linewidth=1)  # Adds a vertical dashed line at 0%


# Get legend and extract colors
legend = plt.legend()
legend_colors = {text.get_text(): handle.get_facecolor()[:3] for handle, text in zip(legend.legendHandles, legend.get_texts())}  # Extract only RGB, discard Alpha

# Print RGB legend colors
print("Legend Colors (RGB):")
for name, color in legend_colors.items():
    print(f"{name}: {tuple(int(c * 255) for c in color)}")  # Convert from [0, 1] to [0, 255] scale

plt.tight_layout()
plt.subplots_adjust(left=0.07, right=0.98, top=0.95, bottom=0.1)  # Further adjust margins manually

plt.show()


########################################################################################################################
