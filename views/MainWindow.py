import customtkinter as ctk

class MainWindow(ctk.CTk):
    def __init__(self, paciente_service, agendamento_service):
        super().__init__()
        self.paciente_service = paciente_service
        self.agendamento_service = agendamento_service
        self.title("Renascer consultório fonoauiológico")
        self.geometry("900x600")

        # Frame lateral — menu
        self.frame_lateral = ctk.CTkFrame(self, width=200, fg_color="#1a1a2e")
        self.frame_lateral.pack(side="left", fill="y")
        

        self.label_logo = ctk.CTkLabel(
            self.frame_lateral, 
            text="Renascer",
            font=("Arial", 18, "bold"),
            text_color="white"  
        )
        self.label_logo.pack(pady=20)

        self.botao_dashboard = ctk.CTkButton(
            self.frame_lateral, 
            text="🏠 Dashboard",
            width=180,
            anchor="w"  # alinha o texto à esquerda
        )
        self.botao_dashboard.pack(pady=5)

        self.botao_pacientes = ctk.CTkButton(self.frame_lateral, text="👤 Pacientes", width=180, anchor="w")
        self.botao_pacientes.pack(pady=5)

        self.botao_agendamentos = ctk.CTkButton(self.frame_lateral, text="📅 Agendamentos", width=180, anchor="w")
        self.botao_agendamentos.pack(pady=5)

        # Frame conteúdo — área principal
        self.frame_conteudo = ctk.CTkFrame(self)
        self.frame_conteudo.pack(side="left", fill="both", expand=True)