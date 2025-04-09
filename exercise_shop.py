products = [
{"name": "macbook air", "price":600$},
{"name": "dell", "price":450$},
{"name": "levono", "price":450$},
{"name": "HP", "PRICE":300$}, 
]

deliveries = [
{"name": "national post", "fees":5},
{"name": "DHL express", "frees":10},



]
for index, product in enumerate(products):
   print(f"for {product["name"]} press {index}")

   while true:
   user_product_index = (input("please enter the product number:/n"))
   try:
       user_product_index = int(user_product_index)
       if user_product_index > = 0 and user_product_index < len (products):
         break
       else:
         print("this product does not exist")
       except valueerror:
       print("please enter only numbers")
       user_product = product[user_product_index]:


       
       
       
       
       
       
       
       
       except valueerror:
       print("please enter only numbers")
