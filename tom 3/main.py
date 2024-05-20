def calculate_si_amount(principal, rate, time):
  interest =  (principal*rate*time)/100
  return principal+interest

print (calculate_si_amount(3,10,100))