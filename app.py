from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def About_me():
    return 'Nama: Muhamad Riki Efendi, NIM: 251111049' 
    
@app.route('/profile')   
def Profile():
    return 'Saya adalah mahasiswa informatika di Universitas Nahdlatul Ulama Yogyakarta, dan saya memiliki hobi main voli'

if __name__ == '__main__':
    app.run(debug=True)