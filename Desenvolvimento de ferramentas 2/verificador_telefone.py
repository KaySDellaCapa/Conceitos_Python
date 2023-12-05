import phonenumbers

from phonenumbers import geocoder

phone = input('Digite o telefone no formato: +551195628922 -- ')

phone_number = phonenumbers.parse(phone) # Vai entender que é um telefone e jogada para dentro da var

print(geocoder.description_for_number(phone_number, 'pt'))