# TestFlow - Browser Chat Agent

Um agente de navegação web automatizada que funciona como um chat interativo, permitindo que você dê comandos em linguagem natural para navegar na web.

## 🚀 Funcionalidades

- **Chat Interativo**: Interface conversacional similar ao ChatGPT
- **Navegação Automatizada**: Executa tarefas na web usando comandos em português
- **Histórico de Sessão**: Salva todas as conversas em arquivo JSON
- **Interface Amigável**: Emojis e formatação clara para melhor experiência

## 📋 Pré-requisitos

- Python 3.8+
- Chave API do OpenAI
- Navegador web (Chrome/Chromium)

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/nun3/testFlow.git
cd testFlow
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure sua chave API:
```bash
# Crie um arquivo .env com sua chave OpenAI
echo "OPENAI_API_KEY=sua_chave_aqui" > .env
```

## 🎯 Como Usar

Execute o agente:
```bash
python agent.py
```

### Exemplos de Comandos:

- `Visite a página do Google`
- `Encontre o post #1 do Hacker News`
- `Pesquise por Python no GitHub`
- `Vá para o site da Wikipedia e procure por inteligência artificial`

## 📁 Estrutura do Projeto

```
testFlow/
├── agent.py              # Código principal do agente
├── requirements.txt      # Dependências Python
├── chat_session.json    # Histórico de conversas
├── .env                 # Configurações (não versionado)
└── README.md           # Este arquivo
```

## 🔧 Tecnologias Utilizadas

- **browser-use**: Framework de automação web
- **OpenAI GPT-4**: Modelo de linguagem para interpretação de comandos
- **Python asyncio**: Programação assíncrona
- **dotenv**: Gerenciamento de variáveis de ambiente

## 📝 Funcionalidades Técnicas

- **Inicialização de Agente**: Cria uma nova instância para cada tarefa
- **Formatação de Respostas**: Timestamps e emojis para melhor UX
- **Tratamento de Erros**: Feedback claro em caso de falhas
- **Histórico Persistente**: Salva conversas automaticamente

## 🤖 Como Funciona

1. **Entrada do Usuário**: Você digita um comando em linguagem natural
2. **Processamento**: O agente interpreta o comando e planeja as ações
3. **Execução**: Navega automaticamente na web executando a tarefa
4. **Resposta**: Retorna o resultado de forma conversacional
5. **Histórico**: Salva a interação para referência futura

## 📊 Exemplo de Uso

```
👤 Você: Visite o Google e pesquise por "inteligência artificial"

🤖 Agente: 🤔 [14:30:15] Pensando sobre: Entendi! Vou executar essa tarefa para você.
⏳ Processando...

🤖 Agente: ⚡ [14:30:16] Executando: Visite o Google e pesquise por "inteligência artificial"

🤖 Agente: ✅ [14:30:20] Concluído!

Aqui está o que consegui fazer:
[Navegou para google.com, digitou a pesquisa e retornou os resultados...]
```

## 🔒 Segurança

- Mantenha sua chave API segura no arquivo `.env`
- O arquivo `.env` não é versionado no Git
- Use apenas em ambientes confiáveis

## 📈 Próximas Funcionalidades

- [ ] Suporte a múltiplos navegadores
- [ ] Interface web gráfica
- [ ] Comandos de voz
- [ ] Integração com outras APIs
- [ ] Modo headless configurável

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer fork do projeto
2. Criar uma branch para sua feature
3. Fazer commit das mudanças
4. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👨‍💻 Autor

**nun3** - [GitHub](https://github.com/nun3)

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
