owner_age = int(input("AGE? ----> "))
monthly_revenue = float(input("REVENUE? ----> "))
credit_score = int(input("CC? =----> "))
yrs_in_business = float(input("YEARS IN THE BUSINESS INDUSTRY? ----> "))
has_defaults = bool(input("FILE FOR BANKCRUPTCY? ----> "))
c_name = str(input("NAME? ----> "))
c_value = float(input("VALUE? ----> "))

max_loan = 0
base_rate = 0

if owner_age >= 21 and yrs_in_business >= 2.0 and has_defaults == False:
   print("BASELINE PASSED")
   if credit_score >=720:#tier1
      print("HIGH CREDIT SCORE")
      max_loan * 3
      print("Your Max_loan is", max_loan)
   if monthly_revenue >= 50000:
      print("HIGH REVENUE")
      base_rate * 0.0015
      print("your base rate is", base_rate)
   else:
      base_rate = 0.025
      print("your base rate is", base_rate)

elif credit_score <= 620 < 720: 
      print("MID CREDIT SCORE") 
      max_loan = 1.5 * monthly_revenue
      print("your max loan is", max_loan)

else:
   print("BASELINE NOT PASSED") 