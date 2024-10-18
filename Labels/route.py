def performance():
    return render_template("performance.html")

@app.route('/chart')
def chart():
    return render_template("chart.html")   
