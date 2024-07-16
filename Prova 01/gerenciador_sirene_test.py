from unittest.mock import Mock
import unittest
from gerenciador_sirene import Evento, GerenciadorSirene

class TestGerenciadorSirene(unittest.TestCase):
    def test_tocar_sirene_no_horario1_manha(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "7:00"
        horario.proximo_evento.return_value = Evento("7:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_intevalo_manha(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "8:30"
        horario.proximo_evento.return_value = Evento("8:30")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_horario2_manha(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "9:00"
        horario.proximo_evento.return_value = Evento("9:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_horario3_manha(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "10:30"
        horario.proximo_evento.return_value = Evento("10:30")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()

    def test_tocar_sirene_no_horario4_manha(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "12:00"
        horario.proximo_evento.return_value = Evento("12:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()

    def test_tocar_sirene_no_horario1_tarde(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "13:00"
        horario.proximo_evento.return_value = Evento("13:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_horario2_tarde(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "14:30"
        horario.proximo_evento.return_value = Evento("14:30")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_intevalo_tarde(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "16:00"
        horario.proximo_evento.return_value = Evento("16:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
    
    def test_tocar_sirene_no_horario3_tarde(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "16:30"
        horario.proximo_evento.return_value = Evento("16:30")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()
        
    def test_tocar_sirene_no_horario4_tarde(self):
        sirene = Mock()
        relogio = Mock()
        horario = Mock()

        relogio.hora_atual.return_value = "18:00"
        horario.proximo_evento.return_value = Evento("18:00")

        gerenciador = GerenciadorSirene(sirene, relogio, horario)
        gerenciador.verificar_eventos()
        sirene.tocar.assert_called_once()

if __name__ == "__main__":
    unittest.main()