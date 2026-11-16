import tkinter as tk
from tkinter import ttk, messagebox
import math

# Define your specific orders and their parameters
orders = {
    "Exclusive Order": {"a": 0.15, "b": 0.0075},
    "Special Order": {"a": 0.25, "b": 0.0075},
    "Order 1a": {"a": 0.5, "b": 0.013},
    "Order 2": {"a": 1.0, "b": 0.023}
}


def calculate_tvumax():
    """Reads the depth input, calculates TVUmax for all orders, and updates the display."""
    try:
        # Get the depth from the input field
        d = float(depth_entry.get())

        # Enable the text box to update results
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)  # Clear previous results

        # Insert Header and Math Format Formula
        result_text.insert(tk.END, f"--- TVUmax Results for Depth (d) = {d} m ---\n\n")
        # Using Unicode characters for square root (√), squared (²), and multiply (×)
        result_text.insert(tk.END, "Formula: TVUmax = \u221A(a\u00B2 + (b\u00D7d)\u00B2)\n")
        result_text.insert(tk.END, "-" * 50 + "\n\n")

        # Loop through orders and calculate
        for order_name, params in orders.items():
            a = params["a"]
            b = params["b"]

            # TVUmax calculation
            tvumax = math.sqrt((a ** 2) + ((b * d) ** 2))

            # Get the specific color tag for this order
            color_tag = f"color_{order_name}"

            # Append results to the text box with styling
            result_text.insert(tk.END, f"{order_name}:\n", color_tag)
            result_text.insert(tk.END, f"  a = {a} m | b = {b}\n", color_tag)

            # Apply BOTH the color tag and the bold/large font tag to the TVUmax line
            result_text.insert(tk.END, f"  TVUmax = {tvumax:.5f}\n", (color_tag, "tvumax_style"))

            result_text.insert(tk.END, "-" * 50 + "\n", color_tag)

        # Disable the text box so the user can't type in it
        result_text.config(state=tk.DISABLED)

    except ValueError:
        # Show an error pop-up if the user types letters or leaves it blank
        messagebox.showerror("Invalid Input", "Please enter a valid number for the depth.")


# --- UI Setup ---
root = tk.Tk()
root.title("TVUmax Calculator - LCDR ESTROPIA")
root.geometry("450x550")
root.resizable(False, False)

# Main frame for padding
frame = ttk.Frame(root, padding="15")
frame.pack(fill=tk.BOTH, expand=True)

# Input Label
input_label = ttk.Label(frame, text="Enter depth (d) in meters:", font=("Arial", 10, "bold"))
input_label.pack(anchor=tk.W, pady=(0, 5))

# Input Field
depth_entry = ttk.Entry(frame, width=20, font=("Arial", 12))
depth_entry.pack(anchor=tk.W, pady=(0, 10))

# Calculate Button
calc_button = ttk.Button(frame, text="Calculate TVUmax", command=calculate_tvumax)
calc_button.pack(anchor=tk.W, pady=(0, 15))

# Results Display Area
result_text = tk.Text(frame, height=20, width=55, font=("Courier", 10), bg="#f4f4f4")
result_text.pack(fill=tk.BOTH, expand=True)

# --- Define Text Styles (Tags) ---
# Colors for the specific orders
result_text.tag_config("color_Exclusive Order", foreground="green")
result_text.tag_config("color_Special Order", foreground="blue")
result_text.tag_config("color_Order 1a", foreground="purple")
result_text.tag_config("color_Order 2", foreground="red")

# Larger, bold font specifically for the TVUmax result line
result_text.tag_config("tvumax_style", font=("Courier", 13, "bold"))

# Set initial text and disable
result_text.insert(tk.END, "Results will appear here...")
result_text.config(state=tk.DISABLED)

# Run the application
root.mainloop()