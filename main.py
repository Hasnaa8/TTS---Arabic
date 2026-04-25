import subprocess
import os

from tkinter import messagebox

def run(g):
    txt = g.get()
    if not txt.strip():
        messagebox.showwarning("تحذير", "الرجاء إدخال نص.")
        return
    try:
        script_path = os.path.join(os.path.dirname(__file__), "execute.sh")
        
        subprocess.run([script_path, txt], check=True)
        messagebox.showinfo("Done", "Done.")

    except FileNotFoundError:
        messagebox.showerror("خطأ", "لم يتم العثور على الملف التنفيذي execute.sh. تأكد من وجوده في نفس المجلد.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء تنفيذ الملف التنفيذي: {e}")
    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ غير متوقع: {e}")


