# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 22:32:36 2023

@author: k3nj115h1kawa
"""

import tkinter as tk
from tkinter import filedialog

# ファイル名を保持する変数
file_name = ""

# ボタンのコマンド処理
### 名前を付けて保存ボタン処理
def save_file():
    global file_name # ファイル名を更新するためにグローバル変数として宣言
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file:
        text_content = text_widget.get("1.0", tk.END)
        file.write(text_content)
        file.close()
        # ファイル名を更新
        file_name = file.name

### 上書き保存ボタン処理
def overwrite_save_file():
    global file_name # ファイル名を参照するためにグローバル変数として宣言
    if file_name: # ファイル名が空でない場合
        text_content = text_widget.get("1.0", tk.END)
        # ファイルオブジェクトを作成
        file = open(file_name, mode='w')
        file.write(text_content)
        file.close()
    else: # ファイル名が空の場合は名前を付けて保存と同じ処理
        save_file()

### 開くボタン処理
def open_file():
    global file_name # ファイル名を更新するためにグローバル変数として宣言
    file = filedialog.askopenfile(mode='r', defaultextension=".txt")
    if file:
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0", file.read())
        file.close()
        # ファイル名を更新
        file_name = file.name
        

root = tk.Tk()

# タイトル設定
root.title("メモ帳")

# 文字入力設定
text_widget = tk.Text(root)
text_widget.pack()

# ボタン設置
save_button = tk.Button(root, text="名前を付けて保存", command=save_file)
save_button.pack(side=tk.LEFT)

# --- 追加 ---
overwrite_save_button = tk.Button(root, text="上書き保存", command=overwrite_save_file)
overwrite_save_button.pack(side=tk.LEFT)
# ------------

open_button = tk.Button(root, text="開く", command=open_file)
open_button.pack(side=tk.LEFT)

root.mainloop()
