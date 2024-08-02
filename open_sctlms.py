# seleniumの必要なライブラリをインポート
from selenium import webdriver
from selenium.webdriver.common.by import By

# tkinter（メッセージボックス表示）の必要なライブラリをインポート
import tkinter
from tkinter import messagebox

# その他モジュール
from time import sleep
import os
import signal
    
# ログイン情報の文字列を準備
url_login = "https://sct-lms.com/login/index.php"
url_course = "https://sct-lms.com/my/courses.php"
    
# ログイン情報の文字列を準備
login_name = ""	# ID
login_pass = "" # Password 
    
# メイン処理
try:
    # Chrome Webドライバー の インスタンスを生成
    driver = webdriver.Chrome()

    # Webドライバーでログインページを起動
    driver.get(url_login)
    sleep(0.5)

    # ID属性が "username" であるHTML要素を取得し、文字列をキーボード送信
    driver.find_element(By.ID,"username").clear()
    driver.find_element(By.ID,"username").send_keys(login_name)
    
    # ID属性が "password" であるHTML要素を取得し、文字列をキーボード送信
    driver.find_element(By.ID,"password").clear()
    driver.find_element(By.ID,"password").send_keys(login_pass)
    
    # CLASS属性が "btn btn-primary btn-lg"* であるHTML要素を取得してクリック    * CLASS属性が複数あるので、"." で繋いで取得
    driver.find_element(By.CLASS_NAME,"btn.btn-primary.btn-lg").click()
    sleep(0.5)
    
    # マイコースへ移動
    driver.get(url_course)
    sleep(0.5)
    
    try:
        # 進行中のコースのみに絞り込む
        driver.find_element(By.ID,"groupingdropdown").click()
        sleep(1.0)
        menu_group = driver.find_element(By.CLASS_NAME, "dropdown-menu.show")
        inprogerss = menu_group.find_element(By.XPATH, "//*[@id=\"yui_3_18_1_1_1722579338400_36\"]/ul/li[4]/a")     
        # ↑ no such element: Unable to locate element: {"method":"xpath","selector":"//*[@id="yui_3_18_1_1_1722579338400_36"]/ul/li[4]/a"}
        inprogerss.click() 

        # メッセージボックス表示
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("selenium sapmle", "ログインに成功！")
        
    except Exception as e:
        print("Error WebDriver: ", e)
        # メッセージボックス表示
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showinfo("selenium sapmle", "ログインに失敗！")

# 例外発生して終了するとプロセスが残ってしまうため、finallyの中に入れて必ず終了させる
finally:
    os.kill(driver.service.process.pid,signal.SIGTERM)