from browser_use import Agent, ChatOpenAI
from dotenv import load_dotenv
import asyncio
import json
from datetime import datetime

load_dotenv()


class BrowserChat:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini")  # Corrigido o modelo
        self.agent = None
        self.session_history = []
        self.current_task = None
    
    async def initialize_agent(self, task_description):
        """Inicializa o agente com uma nova tarefa"""
        try:
            self.agent = Agent(task=task_description, llm=self.llm)
            self.current_task = task_description
            return True
        except Exception as e:
            print(f"❌ Erro ao inicializar agente: {e}")
            return False
    
    def format_response(self, result, action_type="execute"):
        """Formata a resposta do agente de forma conversacional"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if action_type == "thinking":
            return f"🤔 [{timestamp}] Pensando sobre: {result}"
        elif action_type == "executing":
            return f"⚡ [{timestamp}] Executando: {result}"
        elif action_type == "completed":
            return f"✅ [{timestamp}] Concluído!\n\n{result}"
        elif action_type == "error":
            return f"❌ [{timestamp}] Erro: {result}"
        else:
            return f"💬 [{timestamp}] {result}"
    

    async def chat_loop(self):
        """Loop principal do chat"""
        print("🤖 Browser Chat Agent - Digite 'sair' para encerrar\n")
        print("💡 Exemplos de comandos:")
        print("   - 'Visite a página do Google'")
        print("   - 'Encontre o post #1 do Hacker News'")
        print("   - 'Pesquise por Python no GitHub'")
        print()
        
        while True:
            try:
                # Input do usuário
                user_input = input("\n👤 Você: ").strip()
                
                if user_input.lower() in ['sair', 'exit', 'quit']:
                    print("\n👋 Até logo!")
                    break
                
                if not user_input:
                    continue
                
                # Salvar no histórico
                self.session_history.append({
                    "user": user_input,
                    "timestamp": datetime.now().isoformat()
                })
                
                # Feedback de que está processando
                print(f"\n🤖 Agente: {self.format_response('Entendi! Vou executar essa tarefa para você.', 'thinking')}")
                print("⏳ Processando...")
                
                # Inicializar agente
                success = await self.initialize_agent(user_input)
                if not success:
                    continue
                
                # Executar tarefa
                print(f"\n🤖 Agente: {self.format_response(user_input, 'executing')}")
                
                try:
                    result = await self.agent.run()
                    
                    # Formatar resultado
                    response = self.format_response(
                        f"Aqui está o que consegui fazer:\n\n{result}",
                        "completed"
                    )
                    print(f"\n🤖 Agente: {response}")
                    
                    # Salvar resultado no histórico
                    self.session_history[-1]["agent_response"] = str(result)
                    self.session_history[-1]["status"] = "success"
                    
                except Exception as e:
                    error_msg = self.format_response(f"Não consegui executar a tarefa: {str(e)}", "error")
                    print(f"\n🤖 Agente: {error_msg}")
                    
                    # Salvar erro no histórico
                    self.session_history[-1]["agent_response"] = str(e)
                    self.session_history[-1]["status"] = "error"
                
            except KeyboardInterrupt:
                print("\n\n👋 Chat encerrado pelo usuário!")
                break
            except Exception as e:
                print(f"\n❌ Erro inesperado: {e}")
    
    
    def save_session(self, filename="chat_session.json"):
        """Salva o histórico da sessão em arquivo JSON"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.session_history, f, indent=2, ensure_ascii=False)
            print(f"💾 Sessão salva em {filename}")
        except Exception as e:
            print(f"❌ Erro ao salvar sessão: {e}")

async def main():
    chat = BrowserChat()
    
    try:
        await chat.chat_loop()
    finally:
        # Salvar sessão ao encerrar
        chat.save_session()

if __name__ == "__main__":
    asyncio.run(main())