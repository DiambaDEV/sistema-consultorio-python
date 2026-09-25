from repositorio.BancoDeDados import BancoDeDados
from repositorio.PacienteRepository import PacienteRepository
from repositorio.AgendamentoRepository import AgendamentoRepository
from services.PacienteService import PacienteService
from services.AgendamentoService import AgendamentoService
from views.MainWindow import MainWindow

db = BancoDeDados()
service = PacienteService(PacienteRepository(db))
agendamento_service = AgendamentoService(AgendamentoRepository(db))

app = MainWindow(service, agendamento_service)
app.mainloop()