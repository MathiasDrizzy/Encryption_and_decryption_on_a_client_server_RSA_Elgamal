import requests,os, time,rsa,pickle
from elgamal.elgamal import Elgamal

def getPath():
    global A
    temp = time.time()
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    A = os.chdir(dname)
    Mensaje = os.getcwd() + str('\\mensajeentrada.txt')
    with open(Mensaje) as f:
        lines = f.readlines()
        for i in lines:
            A = i


def RSARun():
    global message
    message = bytes(A, encoding='utf-8')
    public_key, private_key = rsa.newkeys(1024)
    encrypted_message = rsa.encrypt(message, public_key)
    s = pickle.dumps(private_key,protocol=2)
    response1 = requests.post(f'http://127.0.0.1:5000/getKey', data=s)
    response2 = requests.get("http://127.0.0.1:5000/getMSG", data=encrypted_message)
    print(response1.text)
    print(response2.text)


def ElgamalRUN():
    public_key, private_key= Elgamal.newkeys(64)
    encrypted_message = Elgamal.encrypt(message, public_key)
    s = pickle.dumps(private_key,protocol=2)
    response1 = requests.post(f'http://127.0.0.1:5000/getKey2', data=s)
    s2 = pickle.dumps(encrypted_message,protocol=2)
    response2 = requests.post(f'http://127.0.0.1:5000/getMSG2', data=s2)
    print(response1.text)
    print(response2.text)


if __name__ == "__main__":
    getPath()
    RSARun()
    ElgamalRUN()