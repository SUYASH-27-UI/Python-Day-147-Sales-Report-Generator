import csv
from collections import defaultdict

FILE_NAME = "sales.csv"
REPORT_FILE = "sales_report.txt"


def load_sales():
    sales = []

    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                quantity = int(row["Quantity"])
                price = float(row["Price"])

                if quantity <= 0 or price < 0:
                    continue

                row["Quantity"] = quantity
                row["Price"] = price
                sales.append(row)

    except FileNotFoundError:
        print("Sales file not found!")

    except (ValueError, KeyError):
        print("Invalid sales data!")

    return sales


def generate_report(sales):
    if not sales:
        print("No sales records available.")
        return

    revenue = defaultdict(float)
    quantity_sold = defaultdict(int)

    total_revenue = 0

    for item in sales:
        product = item["Product"]
        amount = item["Quantity"] * item["Price"]

        revenue[product] += amount
        quantity_sold[product] += item["Quantity"]
        total_revenue += amount

    best_product = max(
        quantity_sold,
        key=quantity_sold.get
    )

    report = []

    report.append("===== SALES REPORT =====")
    report.append(f"Total Revenue: Rs. {total_revenue:.2f}")
    report.append(f"Total Products Sold: {sum(quantity_sold.values())}")
    report.append(f"Best Selling Product: {best_product}")

    report.append("\n--- Product Revenue ---")

    for product, amount in revenue.items():
        report.append(f"{product}: Rs. {amount:.2f}")

    final_report = "\n".join(report)

    print("\n" + final_report)

    with open(REPORT_FILE, "w") as file:
        file.write(final_report)

    print("\nReport saved successfully!")


sales = load_sales()
generate_report(sales)
