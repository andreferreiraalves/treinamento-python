try:
    # ronaldo()
    10 / 0
except ZeroDivisionError:
    print('divisão por zero')
except Exception as err:
    print('erro geral', err)
finally:
    print('finally')
