class ArrHelper:
  def getSum(self,arr):
    res = 0 
    for num in arr:
      res += num 
		
    return res 

  def getAvg(self,arr):
    if (len(arr) > 0):
      sum = self.getSum(arr) 
      return sum / len(arr) 
    else:
      return 0 

arrHelper = ArrHelper()

sum1 = arrHelper.getSum([1, 2, 3]) 
print(sum1) 

sum2 = arrHelper.getSum([3, 4, 5]) 
print(sum2) 

class Validator:
  text = None
  email = None
  domain = None
  num = None

  def isString(self, text):
    if isinstance(text, str) == True:
      return 'String is correct'
    else:
      raise Exception("String is incorrect!")
  def isEmail(self, email):
    if isinstance(email, 'example@gmail.com') == True:
      return 'Email is correct'
    else:
      raise Exception("Email is incorrect!")
  def isDomain(self, dns):
    if isinstance(dns, 'dns.com') == True:
      return ('Domain is correct')
    else:
      raise Exception("Domain is incorrect!")
  def isNumber(self, num):
    if isinstance(num, (int or float)) == True:
      return 'Number is correct'
    else:
      raise Exception("Number is incorrect!")
  
validator = Validator()

print(validator.isString('text'))
print(validator.isNumber(15))
  



