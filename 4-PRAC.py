#For every 3rd letter write it to console lowercase##
import string
alphabetstring=string.ascii_uppercase
alphabet=list(string.ascii_uppercase)

alphabet[2: :3]= [x.lower() for x in alphabet[2: :3]]
 
alphabetstring=' '.join(alphabet)
for i in alphabetstring:
    print (i)