import tkinter as tk
from tkinter import ttk
window = tk.Tk()

#定義繪製斜線的function
def draw_slash(canvas, x, y, size):
    canvas.create_line(x, y, x + size, y + size, width=2)

#定義畫布
canvas_width = 550
canvas_height = 645
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.place(anchor='center',x=275,y=270)

#定義window
window.title('Nash Equilibrium 計算小幫手')
window.geometry('550x600')
window.resizable(0,0)
title_label = tk.Label(window, text='''1. 請輸入兩位玩家的payoff(數值)，並完成payoff matrix
2. 請輸入player 1的strategies(player2 會自動輸入)''',bg='#2a75a1', fg='yellow',font=('Arial', 16))
title_label.place(x=90,y=10)
A_player=tk.Label(window, text="Player 1 's   strategies",fg='#ed0e81', font=('Arial', 16))
A_player.place(x=195,y=65)
B_player=tk.Label(window, text='''Player 2 's
strategies''',fg='#0e9fed', font=('Arial', 16))
B_player.place(x=20,y=240)

#定義'計算Nash equilibrium'的function
def calculate():
    # 先找A player的best strategy
    if int_value1.get() > int_value2.get() and int_value5.get() > int_value6.get():
        strategy_rowA = 'a'
    elif int_value1.get() < int_value2.get() and int_value5.get() < int_value6.get():
        strategy_rowA = 'b'
    else:
        strategy_rowA = 'none'

    # 再找B player的best strategy
    if int_value3.get() > int_value7.get() and int_value4.get() > int_value8.get():
        strategy_rowB = 'a'
    elif int_value3.get() < int_value7.get() and int_value4.get() < int_value8.get():
        strategy_rowB = 'b'
    else:
        strategy_rowB = 'none'
    # 根據策略設置背景顏色
    if strategy_rowA == strategy_rowB == 'a':
        input1.config(bg='#ed9b0e')
        input3.config(bg='#ed9b0e')
        result_label.config(text='Result : 存在單一Nash equilibrium(橘色標示的地方)',bg='yellow',fg='red',font=('Arial', 15))
        result_label.place(x=110,y=470)
        title_label.config(text='''計算成功！結果已顯示！
        請先按"Clear and Redo"按鈕再行操作！''')
        title_label.place(x=110,y=10)
    elif strategy_rowA == strategy_rowB == 'b':
        input6.config(bg='#ed9b0e')
        input8.config(bg='#ed9b0e')
        result_label.config(text='Result : 存在單一Nash equilibrium(橘色標示的地方)',bg='yellow',fg='red',font=('Arial', 15))
        result_label.place(x=110,y=470)
        title_label.config(text='''計算成功！結果已顯示！
        請先按"Clear and Redo"按鈕再行操作！''')
        title_label.place(x=110,y=10)
    elif strategy_rowA == 'a' and strategy_rowB == 'b':
        input5.config(bg='#ed9b0e')
        input7.config(bg='#ed9b0e')
        result_label.config(text='Result : 存在單一Nash equilibrium(橘色標示的地方)',bg='yellow',fg='red',font=('Arial', 15))
        result_label.place(x=110,y=470)
        title_label.config(text='''計算成功！結果已顯示！
        請先按"Clear and Redo"按鈕再行操作！''')
        title_label.place(x=110,y=10)
    elif strategy_rowA == 'b' and strategy_rowB == 'a':
        input2.config(bg='#ed9b0e')
        input4.config(bg='#ed9b0e')
        result_label.config(text='Result : 存在單一Nash equilibrium(橘色標示的地方)',bg='yellow',fg='red',font=('Arial', 15))
        result_label.place(x=110,y=470)
        title_label.config(text='''計算成功！結果已顯示！
        請先按"Clear and Redo"按鈕再行操作！''')
        title_label.place(x=110,y=10)
    else:
        result_label.config(text='Result : 不存在單一Nash equilibrium.This is a "Game of Chicken"',bg='yellow',fg='red',font=('Arial', 15))
        result_label.place(x=70,y=470)
        title_label.config(text='''計算成功！結果已顯示！
        請先按"Clear and Redo"按鈕再行操作！''')
        title_label.place(x=110,y=10)

    return strategy_rowA, strategy_rowB

#清除輸入框的值
def clear_input():
    input1.delete(0, 'end')
    input1.insert(0, '0')  # 設置輸入框的預設值為0
    input1.configure(bg='#ed0e81',fg='white')  # 設置輸入框的背景顏色為白色
    input2.delete(0, 'end')
    input2.insert(0, '0')
    input2.configure(bg='#ed0e81',fg='white')
    input3.delete(0, 'end')
    input3.insert(0, '0')
    input3.configure(bg='#0e9fed',fg='white')
    input4.delete(0, 'end')
    input4.insert(0, '0')
    input4.configure(bg='#0e9fed',fg='white')
    input5.delete(0, 'end')
    input5.insert(0, '0')
    input5.configure(bg='#ed0e81',fg='white')
    input6.delete(0, 'end')
    input6.insert(0, '0')
    input6.configure(bg='#ed0e81',fg='white')
    input7.delete(0, 'end')
    input7.insert(0, '0')
    input7.configure(bg='#0e9fed',fg='white')
    input8.delete(0, 'end')
    input8.insert(0, '0')
    input8.configure(bg='#0e9fed',fg='white')
    result_label.config(bg='#f0f0f0')  # 將背景顏色恢復為視窗顏色
    result_label.config(text='')  # 清除文本内容
    A_player.config(text="Player 1 's   strategies")
    B_player.config(text='''Player 2 's
strategies''')
    title_label.config(text='''1. 請輸入兩位玩家的payoff(數值)，並完成payoff matrix
2. 請輸入player 1的strategies(player2 會自動輸入)''')
    title_label.place(x=90,y=10)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

#定義prisonersdilemma的模板
def prisonersdilemma():
    clear_input()
    input1.delete(0, 'end')
    input1.insert(0, '3  years')  # 設置輸入框的預設值為0
    input1.configure(bg='#ed9b0e',fg='white')  # 設置輸入框的背景顏色為白色
    input2.delete(0, 'end')
    input2.insert(0, '10  years ')
    input2.configure(bg='#ed0e81',fg='white')
    input3.delete(0, 'end')
    input3.insert(0, '3  years')
    input3.configure(bg='#ed9b0e',fg='white')
    input4.delete(0, 'end')
    input4.insert(0, '1  years')
    input4.configure(bg='#0e9fed',fg='white')
    input5.delete(0, 'end')
    input5.insert(0, '1  years')
    input5.configure(bg='#ed0e81',fg='white')
    input6.delete(0, 'end')
    input6.insert(0, '2  years')
    input6.configure(bg='#ed0e81',fg='white')
    input7.delete(0, 'end')
    input7.insert(0, '10  years')
    input7.configure(bg='#0e9fed',fg='white')
    input8.delete(0, 'end')
    input8.insert(0, '2  years')
    input8.configure(bg='#0e9fed',fg='white')
    result_label.config(text='Result : 存在單一Nash equilibrium(橘色標示的地方)',bg='yellow',fg='red',font=('Arial', 15))
    result_label.place(x=110,y=470)
    A_player.config(text="Prisoner 1 's   strategies")
    B_player.config(text='''Prisoner 2 's
strategies''')
    title_label.config(text='''計算成功！結果已顯示！
    請先按"Clear and Redo"按鈕再行操作！''')
    title_label.place(x=110,y=10)
    entry1.insert(0, 'Confess')
    entry2.insert(0, 'Deny')

#定義一個Label會根據entry做改變的function
def update_label1(*args):
    input_text = input_var1.get()
    label1.config(text=input_text)

def update_label2(*args):
    input_text = input_var2.get()
    label2.config(text=input_text)

#設置輸入strategy的輸入框和其他Label
# 創建輸入框和標籤所需的StringVar對象
input_var1 = tk.StringVar()
input_var2 = tk.StringVar()

# 創建輸入框和標籤
entry1 = tk.Entry(window, width=9,justify='center',textvariable=input_var1,font=('Arial', 14))
entry2 = tk.Entry(window,width=9,justify='center', textvariable=input_var2,font=('Arial', 14))
label1 = tk.Label(window, textvariable=input_var1,bg='white',font=('Arial', 14))
label2 = tk.Label(window, textvariable=input_var2,bg='white',font=('Arial', 14))

# 綁定輸入框值的變化事件
input_var1.trace('w', update_label1)
input_var2.trace('w', update_label2)
# 布局組件
entry1.place(x=156, y=95)
label1.place(x=60, y=180)
entry2.place(x=298, y=95)
label2.place(x=60, y=330)

# 定義方形的大小和位置
square_size = 123
gap = 20  # 方形之間的間隔
x1 = (canvas_width - (2 * square_size + gap)) / 2
y1 = (canvas_height - (2 * square_size + gap)) / 2
x2, y2 = x1 + square_size, y1 + square_size

# 創建儲存值的變量
int_value1 = tk.IntVar()
int_value2 = tk.IntVar()
int_value3 = tk.IntVar()
int_value4 = tk.IntVar()
int_value5 = tk.IntVar()
int_value6 = tk.IntVar()
int_value7 = tk.IntVar()
int_value8 = tk.IntVar()

int_values = [int_value1, int_value2, int_value3, int_value4, int_value5, int_value6, int_value7, int_value8]

# 繪製四个方形
for i in range(2):
    for j in range(2):
        x = x1 + (square_size + gap) * i
        y = y1 + (square_size + gap) * j

        canvas.create_rectangle(x, y, x + square_size, y + square_size)
        draw_slash(canvas, x, y, square_size)

#在每個方形的上下空白區域内添加文本輸入框
input1 = tk.Entry(window, width=7,justify='center',textvariable=int_value1,bg='#ed0e81',fg='white')
input1.place(x=187, y=153)

input2 = tk.Entry(window, width=7,justify='center',textvariable=int_value2,bg='#ed0e81',fg='white')
input2.place(x=330,y=153)

input3=tk.Entry(window,width=7,justify='center',textvariable=int_value3,bg='#0e9fed',fg='white')
input3.place(x=142,y=213)

input4 = tk.Entry(window, width=7,justify='center',textvariable=int_value4,bg='#0e9fed',fg='white')
input4.place(x=285,y=213)
 
input5 = tk.Entry(window, width=7,justify='center',textvariable=int_value5,bg='#ed0e81',fg='white')
input5.place(x=187, y=296)

input6 = tk.Entry(window, width=7,justify='center',textvariable=int_value6,bg='#ed0e81',fg='white')
input6.place(x=330,y=296)

input7=tk.Entry(window,width=7,justify='center',textvariable=int_value7,bg='#0e9fed',fg='white')
input7.place(x=142,y=356)

input8 = tk.Entry(window, width=7,justify='center',textvariable=int_value8,bg='#0e9fed',fg='white')
input8.place(x=285,y=356)

#按鈕設置
button = tk.Button(window, text="Calculate Nash Equilibrums", command=calculate)
button.place(anchor='center',x=235,y=435)
button = tk.Button(window, text="Clear and Redo", command=clear_input)
button.place(anchor='center',x=65,y=435)
button = tk.Button(window, text="templates: prisonersdilemma", command=prisonersdilemma)
button.place(anchor='center',x=442,y=435)

#結果的label設置
result_label = tk.Label(window, text='')

#動畫效果
dx = 5  # 水平方向移動量

def move_image():
    global dx  # 告知函數使用全局範圍的 dx 變量
    x1, y1, x2, y2 = canvas.bbox(image_id)
    
    # 檢查圖片是否超出視窗範圍
    if x2 >= window_width or x1 <= 0:
        dx = -dx  # 改變水平方向
    
    # 移動圖片
    canvas.move(image_id, dx, 0)
    
    # 設定定時器
    window.after(16, move_image)

window_width = 550
window_height = 645
# 載入圖片並縮小
image = tk.PhotoImage(file="coin3.png")
scaled_image = image.subsample(3, 3)  # 將圖片縮小至合適大小

# 獲取圖片寬度和高度
image_width = scaled_image.width()
image_height = scaled_image.height()

# 計算圖片起始位置
image_x = window_width - image_width  # 將圖片置於視窗右側
image_y = window_height - image_height  # 將圖片置於視窗底部 

# 在Canvas上繪製圖片
image_id = canvas.create_image(image_x, image_y, image=scaled_image, anchor=tk.NW)

move_image()




window.mainloop()
