from flask import Flask, send_file
app = Flask(__name__)
# servzakat33
# API
# localhost:8080/api/set/<int:x>/<int:y>/<col:hex>
wid = 20
hei = 60
matrix = [[0 for j in range(hei)] for i in range(wid)]

@app.route('/')
def home():
    return send_file('data/index.html')


@app.route('/files/<name>')
def files_service(name):
    return send_file('data/' + name)

# Out API
@app.route('/api/set/<int:x>/<int:y>/<int:r>/<int:g>/<int:b>')
def api(x, y, r, g, b):
    matrix[x][y] = rgb_to_hex(r, g, b)
    return 'ok'

# Internal API for js
@app.route('/api/get/')
def in_api():
    res = "["
    for i in range(wid):
        for j in range(hei):
            r, g, b = hex_to_rgb(matrix[i][j])
            res += '''{"x":''' + str(i) + ''',"y":''' + str(j) + ''',"col":{"r":''' + str(r) + ''',"g":''' + str(g) + ''',"b":''' + str(b) + '}},'
    res = res[:-1] + ']'
    return res


def rgb_to_hex(r, g, b):
    return r << 16 | g << 8 | b

def hex_to_rgb(val):
    return (val >> 16) & 0xff, (val >> 8) & 0xff, (val & 0xff)


app.run(host='0.0.0.0', port=8080)