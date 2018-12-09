from flask import Flask, render_template, request
import os
app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
@app.route("/about.html")
@app.route("/contact.html")
def main_page():
    print(request.path)
    return render_template("index.html", page=request.path)

@app.route("/products.html")
def products_page():
    print(request.path)
    product_names = os.listdir("static/images/Peces")
    product_names = [os.path.splitext(i) for i in product_names]
    print(product_names)
    return render_template("index.html", page=request.path, filenames=product_names)


if __name__ == "__main__":
    app.run()
