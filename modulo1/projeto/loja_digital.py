from banco_dados import banco_dados

def comprar_item_digital(banco_dados, id_pedido, id_item, qtd): 
    
    loja_digital = banco_dados["loja_digital"]
    match id_item:
        case 501 | 502 | 503:
            item = loja_digital[id_item]
        case _:
            return False

    if qtd <= 0:
        return False
    if item["licencas_estoque"] < qtd:
        return False

    pedido = banco_dados["pedidos"].get(id_pedido)    
    if pedido is None:
        return False
    
    subtotal = round(item["preco"] * qtd, 2)
    pedido["itens"].append({
        "id_item": id_item,
        "item": item["item"],
        "preco": item["preco"],
        "qtd": qtd,
        "subtotal": subtotal,
        "categoria": "LOJA_DIGITAL"
    })

    item["licencas_bruto"] -= qtd

    pedido["valor_bruto"] += subtotal
    pedido["valor_liquido"] += subtotal

    return True