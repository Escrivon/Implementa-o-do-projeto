import time


def processar_camera(vaga, placa, ocupada, tempo_processamento=2.0):
    """
    Simula o processamento de uma câmera com IA.

    RQ01:
    - Identifica se a vaga está ocupada ou livre.
    - Reconhece a placa do veículo.
    - O processamento deve ocorrer em até 5 segundos.
    """

    inicio = time.time()

    # Simulação do processamento da câmera
    time.sleep(tempo_processamento)

    fim = time.time()
    tempo_total = fim - inicio

    if ocupada:
        status = "ocupada"
    else:
        status = "livre"

    # Simulação de reconhecimento da placa
    placa_reconhecida = placa if placa else None

    sucesso_tempo = tempo_total <= 5
    sucesso_placa = placa_reconhecida is not None

    return {
        "vaga": vaga,
        "status": status,
        "placa": placa_reconhecida,
        "tempo_processamento": tempo_total,
        "tempo_atendido": sucesso_tempo,
        "placa_reconhecida": sucesso_placa
    }