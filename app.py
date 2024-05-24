# from flask import Flask, render_template  ## flask 라이브러리에서 Flask import
# app = Flask(__name__)
 
# @app.route('/')
# def hello_world():
#     return  "<div>Hello, World</div>"
# # render_template("index.html")
 
# from markupsafe import escape

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # 유저의 이름을 출력
#     return f'User {escape(username)}'

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # 주어진 id 를 정수로 변환함
#     return f'Post {post_id}'

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # /path/ 이후의 경로를 출력
#     return f'Subpath {escape(subpath)}'

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello():                           
    return render_template("index.html")

@app.route("/profile/<username>")
def get_profile(username):
    return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"

@app.route('/post', methods=['GET','POST'])
def post():
    if request.method == 'POST':
        value = request.form['id_name']
        value = str(value)
        print(value)
    return render_template('post.html')

@app.route('/tmp', methods=['GET','POST'])
def tmp():
    value = 'hello, world'
    return render_template('index.html', value = value)

if __name__ == "__main__":              
    app.run(host="0.0.0.0", port="8080")