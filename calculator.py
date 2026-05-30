import tkinter as tk
from tkinter import messagebox


def calculate(x, y, op):
    if op == "+":
        return x + y
    if op == "-":
        return x - y
    if op == "*":
        return x * y
    if op == "/":
        if y == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return x / y
    raise ValueError("Unsupported operation")


def on_calculate(op, entry_a, entry_b, result_label):
    try:
        x = float(entry_a.get())
        y = float(entry_b.get())
        result = calculate(x, y, op)
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
    except ZeroDivisionError as exc:
        messagebox.showerror("Math Error", str(exc))


def on_clear(entry_a, entry_b, result_label):
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="Result: ")


def main():
    root = tk.Tk()
    root.title("Python Calculator")
    root.geometry("320x220")
    root.resizable(False, False)

    frame = tk.Frame(root, padx=15, pady=15)
    frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(frame, text="First number:").grid(row=0, column=0, sticky="w")
    entry_a = tk.Entry(frame, width=15)
    entry_a.grid(row=0, column=1, pady=6)

    tk.Label(frame, text="Second number:").grid(row=1, column=0, sticky="w")
    entry_b = tk.Entry(frame, width=15)
    entry_b.grid(row=1, column=1, pady=6)

    result_label = tk.Label(frame, text="Result: ", font=(None, 12), anchor="w")
    result_label.grid(row=2, column=0, columnspan=2, pady=(10, 12), sticky="w")

    button_frame = tk.Frame(frame)
    button_frame.grid(row=3, column=0, columnspan=2, pady=4)

    buttons = [('+', 'Add'), ('-', 'Subtract'), ('*', 'Multiply'), ('/', 'Divide')]
    for index, (symbol, label) in enumerate(buttons):
        tk.Button(
            button_frame,
            text=label,
            width=8,
            command=lambda op=symbol: on_calculate(op, entry_a, entry_b, result_label)
        ).grid(row=index // 2, column=index % 2, padx=4, pady=4)

    tk.Button(frame, text="Clear", width=20, command=lambda: on_clear(entry_a, entry_b, result_label)).grid(row=4, column=0, columnspan=2, pady=(10, 0))

    root.mainloop()


if __name__ == "__main__":
    main()
