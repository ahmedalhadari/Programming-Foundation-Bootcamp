# try: 
#     risky code 
# except ErrorName:
#     # runs ONLY if an error happned 
# else: 
#     Runs ONLY if NO error happend
# finally: 
#     # ALWAYS runs at the end (error or no error)


# try:
#     print (x)
# except:
#     print ("An Error Occurred")
    
# print (x)
# try:
#     print (10/0)
# except NameError:
#     print ("An Error Occurred")
# except: 
#     print ("Something Else went wrong")

# print (10/0)
# try:
#     print (10/0)
# except NameError:
#     print ("An Error Occurred")
# except ZeroDivisionError: 
#     print ("Something Else went wrong")  


try:
    print (10/0)
except NameError, ZeroDivisionError:
    print ("An Error Occurred")
     