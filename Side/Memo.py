import tkinter
import tkinter.font
from tkinter.filedialog import *

window = tkinter.Tk() # 가장 상위 레벨의 윈도우 창 생성
window.title("Notepad")
window.geometry("600x500+500+200") # "너비x높이+x좌표+y좌표"

def close():
    window.quit()
    window.destroy()

def new_file():
    text_area.delete(1.0, tkinter.END)

def save_file():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    if f is None:
        return
    text_save = str(text_area.get(1.0, tkinter.END))
    f.write(text_save)
    f.close()

def maker():
    help_view = tkinter.Toplevel(window)
    help_view.geometry("300x50+850+400")
    help_view.title('만든 이')
    lb = tkinter.Label(help_view, text = '\nGithub >> https://github.com/Minji287\n')
    lb.pack()

font = tkinter.font.Font(size=12)


#메뉴

menubar = tkinter.Menu(window)

menu_1 = tkinter.Menu(menubar, tearoff=0)
menu_1.add_command(label="새로 만들기", command=new_file)
menu_1.add_command(label="저장", command=save_file)
menu_1.add_separator()
menu_1.add_command(label="닫기", command=close)
menubar.add_cascade(label="파일", menu=menu_1)

menu_2 = tkinter.Menu(menubar, tearoff=0)
menu_2.add_command(label="만든 이", command=maker)
menubar.add_cascade(label="정보", menu=menu_2)

# 텍스트 창

text_area = tkinter.Text(window, font=font)
sb = tkinter.Scrollbar(text_area)
sb.config(command=text_area.yview)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
sb.pack(side="right",fill="y")
text_area.grid(sticky = "n, e, s, w")

window.config(menu=menubar) # 메뉴 구성

window.mainloop() # 윈도우 이름의 윈도우 창을 윈도우가 종료될 때 까지 실행

print("Window Close")