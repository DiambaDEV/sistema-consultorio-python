def formatar_telefone(telefone: str) -> str:
    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    elif len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    else:
        return telefone
    
def validar_telefone(telefone: str) -> bool:
    telefone = ''.join(filter(str.isdigit, telefone))

    return len(telefone) in [10, 11]
