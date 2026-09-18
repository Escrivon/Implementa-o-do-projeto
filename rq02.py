def verificar_autorizacao(placa, veiculos_autorizados):
    """
    Verifica se uma placa está presente na lista
    de veículos autorizados.

    RQ02:
    - Retorna autorizado ou não autorizado.
    - Gera alerta para veículos não autorizados.
    """

    if placa in veiculos_autorizados:
        status = "autorizado"
        alerta = False
    else:
        status = "não autorizado"
        alerta = True

    return {
        "placa": placa,
        "status": status,
        "alerta": alerta
    }