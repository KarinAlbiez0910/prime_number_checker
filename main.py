

def prime_checker(number):
  if (number % 2 == 0 and not (number/2 == 1)) | \
  (number % 3 == 0 and not (number/3 == 1)) | \
  (number % 5 == 0 and not (number/5 == 1)):
    print(f'{number} is NOT a prime number.')
  else:
    print(f'{number} IS a prime number.')

n = int(input("Check this number: "))
prime_checker(number=n)

