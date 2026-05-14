def formatar_cpf(cpf):
        return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}."


def validar_cpf(cpf):
    if not cpf.isdigit():
        return False

    if len(cpf) != 11:
        return False

    return True