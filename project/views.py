from flask import render_template

from app import app, pages


@app.route('/')
def home():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('index.html', pages=sorted_posts)

@app.route('/adayinthelife/')
def adayinthelife():
    return render_template('adayinthelife.html')

@app.route('/torontotransit/')
def torontotransit():
    return render_template('torontotransit.html')

@app.route('/konigsberg/')
def konigsberg():
    return render_template('konigsberg.html')

@app.route('/fat/')
def fat():
    return render_template('fat.html')

@app.route('/flights/')
def flights():
    return render_template('flights.html')

@app.route('/statscan/')
def statscan():
    return render_template('statscan.html')

@app.route('/fearboners/')
def fearboners():
    return render_template('fearboners.html')

@app.route('/lotto/')
def lotto():
    return render_template('lotto.html')

@app.route('/voronoi/')
def voronoi():
    return render_template('voronoi.html')

@app.route('/foxy/')
def foxy():
    return render_template('foxy.html')

@app.route('/profilepyc/')
def profilepyc():
    return render_template('profilepyc.html')

@app.route('/aboutme/')
def aboutme():
    return render_template('aboutme.html')

@app.route('/bigmclargehuge/')
def bigmclargehuge():
    return render_template('bigmclargehuge.html')

@app.route('/apply/')
def apply():
    return render_template('apply.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

