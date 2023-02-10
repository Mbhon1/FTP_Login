import ftplib

def testAnonymousLogin(hostname):
    try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous", "abc@gmail.com')
        'print' '\n[*] ' + str(hostname) +\
            ' FTP Anonymous Logon Succeeded. '
        ftp.quit()
        return True
    except Exception as e:
        'print' '\n[-] ' + str(hostname) +\
            '  Anonymous Logon Failed! '
        return False
host = 'abc_website.com'
testAnonymousLogin(host)