import tkinter as tk
from tkinter import messagebox

def giai_pt_bac_nhat():
    try:
        # Lấy giá trị của a và b từ các Entry
        a = entry_a.get().strip()
        b = entry_b.get().strip()

        # Kiểm tra các ô nhập liệu có bị bỏ trống không
        if not a or not b:
            messagebox.showwarning("Cảnh báo", "Vui lòng nhập đầy đủ giá trị a và b.")
            return
        
        a = float(a)
        b = float(b)

        # Kiểm tra giá trị của a
        if a == 0:
            if b == 0:
                result_label.config(text="Phương trình có vô số nghiệm", fg="blue")
            else:
                result_label.config(text="Phương trình vô nghiệm", fg="red")
        else:
            # Tính nghiệm của phương trình
            x = -b / a
            result_label.config(text=f"Nghiệm của phương trình: x = {x:.2f}", fg="green")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng định dạng số cho a và b.")
        
def reset():
    # Xóa các giá trị đã nhập và kết quả
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    result_label.config(text="")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Giải phương trình bậc nhất ax + b = 0")
root.geometry("400x300")
root.config(bg="#f0f0f0")

# Tạo tiêu đề
title_label = tk.Label(root, text="Giải phương trình bậc nhất ax + b = 0", font=("Arial", 16), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Frame để chứa các widget nhập liệu
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

# Tạo các label và entry cho giá trị a và b
label_a = tk.Label(input_frame, text="Nhập a:", font=("Arial", 12), bg="#f0f0f0")
label_a.grid(row=0, column=0, padx=10, pady=10)

entry_a = tk.Entry(input_frame, font=("Arial", 12), width=10)
entry_a.grid(row=0, column=1, padx=10, pady=10)

label_b = tk.Label(input_frame, text="Nhập b:", font=("Arial", 12), bg="#f0f0f0")
label_b.grid(row=1, column=0, padx=10, pady=10)

entry_b = tk.Entry(input_frame, font=("Arial", 12), width=10)
entry_b.grid(row=1, column=1, padx=10, pady=10)

# Nút Giải phương trình
solve_button = tk.Button(root, text="Giải phương trình", font=("Arial", 12), command=giai_pt_bac_nhat, bg="#4CAF50", fg="white", width=15)
solve_button.pack(pady=10)

# Nút Reset
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), command=reset, bg="#f44336", fg="white", width=15)
reset_button.pack(pady=5)

# Label hiển thị kết quả
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f0f0")
result_label.pack(pady=10)

# Chạy vòng lặp giao diện
root.mainloop()
