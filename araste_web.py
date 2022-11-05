from flask import Flask, request
from araste.araste import render
from os import listdir
import araste
fonts_dir = '/'.join(araste.__file__.split('/')[:-1]) + '/fonts'
fonts_list = listdir(fonts_dir)
fonts_list_html = '\n'.join(
    [f'<option value="{font}">{font}</option>' for font in fonts_list]
)
app = Flask(__name__)
homepage = f'''
<!doctype html>
<head>
<title>hi</title>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>
<form action="/t/", method="post">
  <label for="fname">your text:</label><br>
  <input type="text" id="text" name="text" value="TEXT"><br>

  <label for="lname">font name:</label><br>
  
  <select id="lname" name="font">
    {fonts_list_html}
  </select>

  <input type="submit" id="submit" value="submit" method="post">
</form> 
</body>
    '''
 
@app.route('/')
def home_page():
    homepage = '''
<!doctype html>
<head>
<title>hi</title>
<body>
<form action="/t/", method="post">
  <label for="fname">your text:</label><br>
  <input type="text" id="text" name="text" value="نوشته"><br>
  <label for="lname">font name:</label><br>
  <input type="text" id="lname" name="font" value="aipara"><br>
  <input type="submit" id="submit" value="submit" method="post">
</form> 
</body>
    '''
    return homepage

@app.route('/t/', methods=['POST'])
def give_output():
    print(request.form)
    text = request.form['text']
    font = request.form['font']

    art = render(text, font)

    o = homepage.replace('TEXT', text) + '<textarea rows="40" cols="180">' + art + '</textarea>'
    return o




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
