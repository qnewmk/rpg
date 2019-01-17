itens = {'espada media':{'maos':1,'dano':2},'espada grande':{'maos':2,'dano':3},'adaga':{'maos':1,'dano':1},'escudo':{'maos':1,'defesa':2}}
def pega_item(nome_item):
    descricao_item = list()
    for item in itens :
        if item == nome_item :
            descricao_item.append(item)
            for coisa in itens[item] :
                descricao_item.append(itens[item][coisa])
    if descricao_item[0]=='escudo':
        return({'nome' : {descricao_item[0]},
'maos' : {descricao_item[1]},
'defesa' : {descricao_item[2]}} )
    return({'nome' : {descricao_item[0]},
'maos' : {descricao_item[1]},
'dano' : {descricao_item[2]}} )

