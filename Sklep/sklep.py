
from flask import Flask, render_template, request, url_for
import json
import openpyxl

app = Flask(__name__)
app.debug = False

@app.route('/')
def main_page():
    return render_template('main_page.html')

@app.route('/koszyk')
def cart():
    return render_template('cart.html')
    print(url_for('cart'))

@app.route('/potop')
def show_product_potop():
    return render_template('potop.html')
    print(url_for('potop'))

@app.route('/krzyzacy')
def show_product_krzyzacy():
    return render_template('krzyzacy.html')
    print(url_for('krzyzacy'))

@app.route('/wladca_pierscieni')
def show_product_wladca_pierscieni():
    return render_template('wladca_pierscieni.html')
    print(url_for('wladca_pierscieni'))

app.run()
