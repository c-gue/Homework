secret = {'A':'%','a':'9','B':'@','b':'#','C':'!','c':'8','D':'$','d':'7','E':'^','e':'7','F':'&','f':'6','G':'*','g':'5','H':'(','h':'4','I':')','i':'3','J':'-','j':'2','K':'_','k':'1','L':'+','l':'=','M':'[','m':'/','N':']','n':'|','O':'{','o':',','P':'<','p':'.','Q':'>','q':'?','R':'~','r':'`','S':'<3','s':':','T':';','t':':)','U':'2.','u':'*_*','V':'$P$','v':'#@','W':'</3','w':';)','X':'0','x':'()','Y':'10010010','y':'^_^','Z':':@','z':':P'}

isec = open('info_security.txt','r')

letters = isec.read()

isec.close()

outfile = open('info_security_new.txt','w')

for text in letters:
    if text in secret:
        key = secret[text]

        outfile.write(key)
    else:
        outfile.write(text)

outfile.close()


#github link
#https://github.com/c-gue/Homework.git