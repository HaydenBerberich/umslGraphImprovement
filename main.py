import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
data = pd.read_csv('data.csv')

# Extract the relevant columns
models = data['Model']
lr_469 = data['LR 469']
sl_469 = data['SL 469']
lr_1875 = data['LR 1875']
sl_1875 = data['SL 1875']
parameters = data['Parameters']

# Normalize the parameters for marker size and increase the size
marker_size = (parameters - parameters.min()) / (parameters.max() - parameters.min()) * 200 + 70

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the lines
plt.plot(models, lr_469, label='LR', color='b', linestyle='-')
plt.plot(models, sl_469, label='SL', color='g', linestyle='-')
plt.plot(models, lr_1875, label='LR', color='b', linestyle='--')
plt.plot(models, sl_1875, label='SL', color='g', linestyle='--')

# Plot the scatter points with varying marker sizes and different markers for batch sizes
plt.scatter(models, lr_469, s=marker_size, color='b', alpha=0.6, edgecolors='w', linewidth=0.5, marker='o')
plt.scatter(models, sl_469, s=marker_size, color='g', alpha=0.6, edgecolors='w', linewidth=0.5, marker='o')
plt.scatter(models, lr_1875, s=marker_size, color='b', alpha=0.6, edgecolors='w', linewidth=0.5, marker='s')
plt.scatter(models, sl_1875, s=marker_size, color='g', alpha=0.6, edgecolors='w', linewidth=0.5, marker='s')

plt.xlabel('Model')
plt.ylabel('Time (seconds)', labelpad=40, rotation=0)
plt.title('Execution times for SL vs. LR and scale factor of 10')

# Create a custom legend for batch sizes
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='b', lw=2, label='LR'),
    Line2D([0], [0], color='g', lw=2, label='SL'),
    Line2D([0], [0], marker='o', color='w', markerfacecolor='k', markersize=10, label='469 Batches'),
    Line2D([0], [0], marker='s', color='w', markerfacecolor='k', markersize=10, label='1,875 Batches')
]
plt.legend(handles=legend_elements)

# Add a note about the point size
plt.text(0.2, -0.12, '* Point size represents number of parameters', ha='center', va='center', transform=plt.gca().transAxes)

# Remove the top and right spines
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.grid(axis='y')  # Show only horizontal grid lines
plt.show()