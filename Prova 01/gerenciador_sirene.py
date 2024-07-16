class Sirene:
    def tocar(self):
        print("Sirene tocando")

class Relogio:
    def hora_atual(self):
        pass

class HorarioAulaOuIntervalo:
    def proximo_evento(self):
        pass

class Evento:
    def __init__(self, hora):
        self.hora = hora

class GerenciadorSirene:
    def __init__(self, sirene: Sirene, relogio: Relogio, horario: HorarioAulaOuIntervalo):
        self.sirene = sirene
        self.relogio = relogio
        self.horario = horario

    def verificar_eventos(self):
        hora_atual = self.relogio.hora_atual()
        proximo_evento = self.horario.proximo_evento()
        if hora_atual == proximo_evento.hora:
            self.sirene.tocar()