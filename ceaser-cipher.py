alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

import art

def ceaser(message, number, position):
  list = ""
  if position == "decode":
    number *= -1
  for i in range(len(message)):
      letter = message[i]
      if letter in alphabet:
        index = alphabet.index(letter)
        index_to_call = index + number
        if index_to_call >= len(alphabet):
          index_to_call = (index + number) - len(alphabet) 
        list += alphabet[index_to_call]
      else:
        list += letter
  print(f"Your {position}d word is {list}")
print(art.logo)
while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction != "encode" and direction != "decode":
    print("Invalid input!")
    continue
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > len(alphabet):
    shift = shift % len(alphabet)
  ceaser(text, shift, direction)
  go_on = input("Do you want to go on? (Yes or No)").lower()
  if go_on != "yes" and go_on != "no":
    print("Invalid input!")
    break
  else:
    if go_on == "yes":
      continue
    elif go_on == "no":
      break