from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_folder="static", static_url_path="/yeet") # 建立 app 變數為 Flask 物件，__name__ 表示目前執行的程式

# @app.route("/<host>")
# def index(host):
#     return render_template("spring_class1.html", host=host)     

# @app.route("/", methods=["GET"])
# def index():
#     print("請求方法: ", request.method)
#     print("通訊協定: ", request.scheme)
#     print("主機名稱: ", request.host)
#     print("路徑: ", request.path)
#     print("完整的網址: ", request.url)
#     print("瀏覽器作業系統: ", request.headers.get("user-agent"))
#     print("語言偏好: ", request.headers.get("accept-language"))
#     print("引薦網址: ", request.headers.get("referrer"))
#     name = request.args.get("name")
#     print("使用者名字是: ", name)
#     return "Hello Flask"

@app.route("/login")
def login():
    return "<form method='post' action='/submit'> <input type='text' name = 'username' /> <button type='submit'> Submit </button></form>"

@app.route("/submit", methods=["POST"])
def submit():
    username = request.values["username"]
    return "Hello "+ username

app.run() # 執行