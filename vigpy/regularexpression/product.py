# #print (product(2,3,4))

# def product(*args):
#     res=1
#     for n in args:
#         res*=n
#         print(res)


# product(1,2,3,4)

# product(10,20)


# def greetings(**kwargs):
    # print(f"hello {kwargs.get('msg')} app user {kwargs.get('useer_name')}")


# greetings(msg="good morning",user_name="vig")

#hello user vijay your oder 123bc ucb shirt is ready to deliver
def dispatch_oder(**kwargs):
    print(f"hello user {kwargs.get('name')} your order {kwargs.get('code')} {kwargs.get('item')} is ready to {kwargs.get('status')}")

dispatch_oder(item="ucb shirt",code="123bc",status="deliver",name="vijay")


