from flask import Flask

app = Flask(__name__, static_folder="static", static_url_path="/yeet") # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

@app.route("/") # 使用函式裝飾器，建立一個路由 ( Routes )，可針對主網域 / 發出請求
def index(): # 發出請求後會執行 home() 的函式
    return "Welcome to my web!" # 執行函式後會回傳特定的網頁內容，以HTML格式以方便瀏覽器來做網頁的展示

@app.route("/member/<name>")
def sayHi(name):
    return "Hello, our favorite member: " + name


@app.route("/admin/<level>")
def login(level):
    if level == "A":
        return "Login here!"
    else:
        return "You can not login in!"
    

    

app.run() # 執行