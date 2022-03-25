def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Pressione A para adicionar um produto ou S para sair:')
        if details == 'A':
            product = input('Produto:')
            quantity= int(input('Quantidade:'))
            buyingData.update({product:quantity})
        elif details == 'S':
                enterDetails = False
        else:
            print ('Digite uma resposta válida')
            return buyingData
def getPrice (product, quantity):
    priceData = {
        'Bolacha':3,
        'Peito de frango':15,
        'Ovos':5,
    }
    subtotal = priceData[product]*quantity
    print(product+':$'+ str(priceData[product]+'x'+str(quantity+'='+str(subtotal))))
    return subtotal

enterProducts()