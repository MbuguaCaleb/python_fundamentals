has_high_income=True
has_good_credit=False
has_criminal_record=True
 
#and operator
# if has_high_income and has_good_credit:
#     print('Eligible for HIgh Loan')

# #or operator
# if has_high_income or has_good_credit:
#     print("Eligible for mid loan")

##NOT NEGATION
if has_high_income and not has_criminal_record:
    print('ELigible for Loan')

