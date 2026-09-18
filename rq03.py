from datetime import datetime


def verificar_vaga_reservada(
    vaga,
    placa,
    vagas_reservadas,
    funcionarios
):
    """
    Verifica se um veículo ocupou indevidamente
    uma vaga reservada para funcionários.

    RQ03:
    - Identifica ocupação indevida.
    - Registra placa, data e hora.
    - Notifica o responsável.
    """

    if vaga not in vagas_reservadas:
        return {
            "ocorrencia": False,
            "mensagem": "A vaga não é reservada para funcionários."
        }

    if placa in funcionarios:
        return {
            "ocorrencia": False,
            "mensagem": "Veículo cadastrado como funcionário."
        }

    agora = datetime.now()

    ocorrencia = {
        "vaga": vaga,
        "placa": placa,
        "data": agora.strftime("%d/%m/%Y"),
        "hora": agora.strftime("%H:%M:%S"),
        "responsavel_notificado": "Segurança/Administração"
    }

    return {
        "ocorrencia": True,
        "ocorrencia_dados": ocorrencia,
        "mensagem": "Ocupação indevida registrada."
    }