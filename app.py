import os,logging, rsa,pickle
from flask import Flask, request
from elgamal.elgamal import Elgamal


app = Flask(__name__)

#Desactivate log messages
log = logging.getLogger('werkzeug')
log.disabled = True

#Load the private key RSA
@app.route('/getKey',methods=['POST'])
def key():
    global private_key
    private_key = pickle.loads(request.get_data())
    print('Synchronized key')
    return 'Synchronized key'

#Load the message an decryption RSA
@app.get('/getMSG/')
def getMSG():
    global file1
    encrypted_message= request.get_data()
    decrypted_message = rsa.decrypt(encrypted_message, private_key)
    WriteMessage = os.getcwd() + str('\\mensajerecibido.txt')
    file1 = open(WriteMessage, "w")
    line = str('Decrypted message with RSA:  ') + str(decrypted_message.decode("utf-8")) + str(" \n")
    file1.write(line)
    print('RSA Decrypt done, it has been written to the txt file: mensajerecibido')
    return 'RSA Decrypt done, it has been written to the txt file: mensajerecibido'

#Load the private key Elgamal
@app.route('/getKey2',methods=['POST'])
def key2():
    global private_key
    private_key = pickle.loads(request.get_data())
    print('Synchronized key ')
    return 'Synchronized key'

#Load the message an decryption Elgamal
@app.route('/getMSG2',methods=['POST'])
def getMSG2():
    encrypted_message= pickle.loads(request.get_data())
    decrypted_message = Elgamal.decrypt(encrypted_message, private_key)
    line = str('Decrypted message with Elgamal:  ') + str(decrypted_message.decode("utf-8")) + str(" \n")
    file1.write(line)
    file1.close()
    print('Elgamal Decrypt done, it has been written to the txt file: mensajerecibido')
    return 'Elgamal Decrypt done, it has been written to the txt file: mensajerecibido'


if __name__ == "__main__":
    app.run()

