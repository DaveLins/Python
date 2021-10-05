# Lista com os valores
lista_precos = [500, 1500, 2000, 100, 25]

# Varíavel com a nova lsita de preços
nova_lista_precos = []

# Modo convencional - for
for preco in lista_precos: # Definindo preco, na lista (lista_precos)

    nova_lista_precos.append(preco * 2) # Na nova lista, adicionando na varíavel preco (2 *)

print(nova_lista_precos)

# Modo otimizado - List comprehension
nova_lista_precos2 = [preco * 2 for preco in lista_precos] # Para a nova lista, definindo em preco, 2 *, para preco em lista_precos.

print(nova_lista_precos2)
