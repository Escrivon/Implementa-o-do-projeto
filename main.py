"""
PLANO DE IMPLEMENTAÇÃO

RQ01 - Detecção de vagas:
Simular câmera identificando ocupação e placa.
Tempo: 15 minutos.

RQ02 - Verificação de autorização:
Comparar placa detectada com lista de veículos autorizados.
Tempo: 15 minutos.

RQ03 - Vagas reservadas:
Verificar se veículo é funcionário e registrar ocorrência.
Tempo: 20 minutos.

Uso de IA:
IA utilizada para auxiliar na estruturação do código e
verificação dos critérios de aceitação.
"""


from rq01 import processar_camera
from rq02 import verificar_autorizacao
from rq03 import verificar_vaga_reservada


def executar_rq01():
    print("\n" + "=" * 50)
    print("RQ01 - DETECÇÃO DE VAGAS")
    print("=" * 50)

    resultado = processar_camera(
        vaga=12,
        placa="ABC1D23",
        ocupada=True
    )

    print(f"Vaga: {resultado['vaga']}")
    print(f"Status: {resultado['status']}")
    print(f"Placa reconhecida: {resultado['placa']}")
    print(
        f"Tempo de processamento: "
        f"{resultado['tempo_processamento']:.2f} segundos"
    )

    if resultado["tempo_atendido"]:
        print("✓ Detecção realizada em até 5 segundos.")
    else:
        print("✗ O tempo de detecção ultrapassou 5 segundos.")

    if resultado["placa_reconhecida"]:
        print("✓ Placa reconhecida.")
    else:
        print("✗ Placa não reconhecida.")


def executar_rq02():
    print("\n" + "=" * 50)
    print("RQ02 - VERIFICAÇÃO DE VEÍCULOS")
    print("=" * 50)

    veiculos_autorizados = [
        "ABC1D23",
        "DEF4G56",
        "HIJ7K89"
    ]

    placa = "XYZ9A99"

    resultado = verificar_autorizacao(
        placa,
        veiculos_autorizados
    )

    print(f"Placa analisada: {resultado['placa']}")
    print(f"Status: {resultado['status']}")

    if resultado["alerta"]:
        print("⚠ ALERTA: veículo não autorizado!")
    else:
        print("✓ Veículo autorizado.")


def executar_rq03():
    print("\n" + "=" * 50)
    print("RQ03 - VAGAS RESERVADAS")
    print("=" * 50)

    vagas_reservadas = [10, 11, 12]

    funcionarios = [
        "ABC1D23",
        "DEF4G56"
    ]

    vaga = 10
    placa = "XYZ9A99"

    resultado = verificar_vaga_reservada(
        vaga,
        placa,
        vagas_reservadas,
        funcionarios
    )

    if resultado["ocorrencia"]:
        ocorrencia = resultado["ocorrencia_dados"]

        print("⚠ OCUPAÇÃO INDEVIDA DETECTADA")
        print(f"Vaga: {ocorrencia['vaga']}")
        print(f"Placa: {ocorrencia['placa']}")
        print(f"Data: {ocorrencia['data']}")
        print(f"Hora: {ocorrencia['hora']}")
        print(
            f"Responsável notificado: "
            f"{ocorrencia['responsavel_notificado']}"
        )

    else:
        print(resultado["mensagem"])


def main():
    print("=" * 50)
    print("SISTEMA DE ESTACIONAMENTO")
    print("PROTÓTIPO - REQUISITOS RQ01, RQ02 E RQ03")
    print("=" * 50)

    executar_rq01()
    executar_rq02()
    executar_rq03()

    print("\n" + "=" * 50)
    print("PROTÓTIPO FINALIZADO")
    print("=" * 50)


if __name__ == "__main__":
    main()


"""
AUTOAVALIAÇÃO

Critérios atingidos:
- RQ01: detecção de vaga e reconhecimento de placa simulados.
- RQ02: veículos autorizados e não autorizados identificados.
- RQ03: ocupações indevidas em vagas reservadas registradas.

Critérios não totalmente implementados:
- O reconhecimento da placa é simulado, não utiliza uma câmera ou
  modelo real de inteligência artificial.
- O banco de dados real de veículos não foi implementado.
- A notificação é apenas simulada no terminal.

Requisito mais difícil:
RQ03, pois foi necessário relacionar a vaga reservada,
o cadastro de funcionários e o registro da ocorrência.

Como foi resolvido:
Foram utilizadas listas para representar os cadastros e um
dicionário para representar a ocorrência registrada.
"""