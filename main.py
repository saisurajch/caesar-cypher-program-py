from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction,text,shift):
  word = ''
  for i in text:
    if i not in alphabet:
      continue
    else:
      x = alphabet.index(i)
      if(direction == "encode"):
        if shift+x not in range(0,26):
          new_shift = (shift+x)%26
          i = alphabet[new_shift]
        else:
          i = alphabet[shift+x]
      elif(direction == "decode"):
        i = alphabet[x - shift]
      word = word + i
  print(word)

print(logo)

loop = True
while (loop == True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(direction,text,shift)
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
  if(restart=="yes"):
    loop = True
  else:
    loop = False
