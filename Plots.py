import matplotlib.pyplot as plt
import pandas as pd
import csv


# Read CSV into pandas dataframe
data = pd.read_csv(r'Scraped Data\Satozim -iPhone- Prices.csv')

# Shorten Product Names
stripped_names = []
file = r'Scraped Data\Satozim -iPhone- Prices.csv'

with open(file, 'r') as file_open:
    heading = next(file_open)
    csv = csv.reader(file_open)

    for row in csv:
        stripped_name = row[1].replace('Apple ', '').strip()
        stripped_names.append(stripped_name)

file_open.close()


def Models_X_Prices():

    # Extract product names and prices
    product_names = stripped_names
    prices = data['Price']

    # Create a horizontal bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(product_names, prices, color='skyblue')

    # Customize the plot
    ax.set_xlabel('Price (ZAR)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Product Name', fontsize=12, fontstyle='italic')
    ax.set_title('iPhone Prices vs Models', fontsize=14, fontweight='bold')
    ax.grid(axis='x', linestyle='--', alpha=0.7)

    # Rotate y-axis labels for better visibility
    plt.yticks(rotation=45)

    # Save the graph as an image
    plt.savefig(r'plots\Models_X_Prices.png')

    # Show the plot (optional)
    plt.tight_layout()
    plt.show()
