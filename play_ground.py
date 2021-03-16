from flask import Flask, render_template

app = Flask(__name__)


@app.route('/user/play')
def play_ground1():
    return render_template("play_ground.html", boxes=3)

@app.route('/user/play/<int:times>')
def play_ground2(times):
    return render_template("play_ground.html", boxes=times)

@app.route('/user/play/<int:times>/<colors>')
def play_ground3(times, colors):
    return render_template("play_ground.html", boxes=times, color=colors)

if __name__ == "__main__":
    app.run(debug=True)