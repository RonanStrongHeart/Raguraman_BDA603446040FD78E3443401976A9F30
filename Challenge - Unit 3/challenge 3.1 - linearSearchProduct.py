
def linearSearchProduct(productList, targetProduct):
  indices = []

  for i in range(len(productList)):
    product = productList[i]
    if product == targetProduct:
      indices.append(i)

  if len(indices)==0:
    print("\n" +targetProduct+" does not exist in the list")
  else:
    print("\n{} occured in {}".format(targetProduct,indices))



products = ["paper", "pencil", "eraser", "paper", "paper", "eraser","pencil","pen"]
target = "paper"
target2 = 'ruler'
result = linearSearchProduct(products, target)
result = linearSearchProduct(products, target2)

print("\nSayonera")
