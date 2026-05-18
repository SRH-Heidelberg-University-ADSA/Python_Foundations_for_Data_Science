# =============================================================================
# WEEK 4 EXERCISE SOLUTIONS- Disclaimer: this is one of the possible solutions
# =============================================================================

# =============================================================================
# PROBLEM 1: Student Grade Analytics System
# =============================================================================

def calculate_average(grades):
    """Returns the average of a list of numbers."""
    return sum(grades) / len(grades)


def assign_letter_grade(average, passing_mark=60):
    """Assigns a letter grade based on average score."""
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= passing_mark:
        return "D"
    else:
        return "F"


def generate_report(student_dict):
    """Returns a report dict with average and grade for each student,
    sorted by average descending."""
    report = {}
    for name, grades in student_dict.items():
        avg = round(calculate_average(grades), 2)
        grade = assign_letter_grade(avg)
        report[name] = {"average": avg, "grade": grade}

    # Sort by average, highest first
    sorted_report = dict(
        sorted(report.items(), key=lambda x: x[1]["average"], reverse=True)
    )
    return sorted_report


def main():
    students = {
        "Alice": [85, 90, 78],
        "Bob": [70, 88, 92],
        "Charlie": [95, 100, 93],
        "Diana": [60, 75, 72],
    }

    report = generate_report(students)
    print("=== Problem 1: Student Grade Report ===")
    for name, info in report.items():
        print(f"{name}: Average = {info['average']}, Grade = {info['grade']}")
    print()


main()


# =============================================================================
# PROBLEM 2: Expense Tracker Module
# =============================================================================

def monthly_total(expense_list):
    """Returns the total expenses for a month."""
    return sum(expense_list)


def highest_month(expense_dict):
    """Returns the month with the highest total spending."""
    return max(expense_dict, key=lambda month: monthly_total(expense_dict[month]))


def filter_expenses(expense_list, threshold=300):
    """Returns expenses above the given threshold using list comprehension."""
    return [expense for expense in expense_list if expense > threshold]


def main():
    expenses = {
        "January":  [120, 340, 560],
        "February": [400, 150],
        "March":    [800, 200, 100],
    }

    print("=== Problem 2: Expense Tracker ===")
    for month, exp_list in expenses.items():
        print(f"{month}: Total = {monthly_total(exp_list)}")

    print(f"Highest spending month: {highest_month(expenses)}")

    for month, exp_list in expenses.items():
        filtered = filter_expenses(exp_list)
        print(f"{month} expenses above 300: {filtered}")
    print()


main()


# =============================================================================
# PROBLEM 3: Inventory Restocking System
# =============================================================================

def needs_restock(product_info):
    """Returns True if the product's quantity is below minimum required."""
    return product_info["quantity"] < product_info["min_required"]


def restock_amount(product_info):
    """Returns the number of items needed to reach minimum stock."""
    return product_info["min_required"] - product_info["quantity"]


def generate_restock_report(inventory):
    """Returns a dict of products that need restocking and how many items
    are required, sorted by highest restock amount."""
    report = {
        product: restock_amount(info)
        for product, info in inventory.items()
        if needs_restock(info)
    }

    # Sort by restock amount descending using lambda
    sorted_report = dict(
        sorted(report.items(), key=lambda x: x[1], reverse=True)
    )
    return sorted_report


def main():
    inventory = {
        "Apples":  {"quantity": 20, "min_required": 25},
        "Bananas": {"quantity": 40, "min_required": 30},
        "Oranges": {"quantity": 15, "min_required": 20},
    }

    report = generate_restock_report(inventory)
    print("=== Problem 3: Restock Report ===")
    for product, amount in report.items():
        print(f"{product}: needs {amount} more units")
    print()


main()


# =============================================================================
# PROBLEM 4: Voting Analysis with Sets
# =============================================================================

def common_voters(A, B):
    """Returns voters appearing in both sets."""
    # another option: A.intersection(B) 
    return A & B


def unique_voters(A, B):
    """Returns voters appearing in only one set (symmetric difference)."""
    # another option: A.symmetric_difference(B)
    return A ^ B


def all_voters(A, B):
    """Returns the union of both voter sets."""
    # another option: A.union(B)
    return A | B


def analyse_turnout(A, B):
    """Returns a summary dictionary of total, common, and unique voter counts."""
    return {
        "total":  len(all_voters(A, B)),
        "common": len(common_voters(A, B)),
        "unique": len(unique_voters(A, B)),
    }


def main():
    station_A = {"Alice", "Bob", "Charlie", "Diana"}
    station_B = {"Charlie", "Diana", "Edward"}

    print("=== Problem 4: Voting Analysis ===")
    print(f"Common voters:  {sorted(common_voters(station_A, station_B), key=lambda x: x)}")
    print(f"Unique voters:  {sorted(unique_voters(station_A, station_B), key=lambda x: x)}")
    print(f"All voters:     {sorted(all_voters(station_A, station_B), key=lambda x: x)}")
    print(f"Turnout stats:  {analyse_turnout(station_A, station_B)}")
    print()


main()
