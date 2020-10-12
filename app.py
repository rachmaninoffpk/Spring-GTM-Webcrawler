from flask import Flask, render_template
from SpringerMathWebscraper import main
app = Flask(__name__) #four underscores total

@app.route('/')
def springer_mathematics_dashboard():
    springer_mathematics_data = main(40)
    return render_template('home.html', springer_mathematics_data = springer_mathematics_data)

if __name__ == '__main__':
    app.run()