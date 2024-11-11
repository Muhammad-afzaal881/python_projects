menu = {"baryani":100,"colddrink":50,"pasta":80,"Tea":30,"snadwich":90,"beaf":300}#dictonary
seconds=''#empty variable
print("WELCOME TO YOUR RESTURANT")#print
print(",baryani:100\n,colddrink:50\n,pasta:80\n,Tea:30\n,snadwich:90\n,beaf:300")
order = 0
costomer = input("place your order ")#beaf
if(costomer in menu):
    order += menu[costomer]
    print("sir any more order" )
else:
    print("sorry sir this item not available you choice any item ")
second_item = input("sir you are like any more item (yes/no) ")
if(second_item == "yes"):
    seconds = input("ENTER second item ")
else:
    print("OK SIR")
if(seconds in menu):
    order += menu[seconds]
else:
    print("sorry sir this item not avaiable")
print(f"Your order bill is {order}Rs and pay the counter") 