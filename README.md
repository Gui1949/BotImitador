# Bot Imitador

Um bot que grava e reproduz ações do mouse e teclado com timing preciso.

## Funcionalidades

- Grava movimentos do mouse, cliques e teclas pressionadas
- Registra o tempo exato entre cada ação
- Reproduz as ações com o mesmo timing
- Suporta modo loop para repetição contínua

## Como usar

1. **Gravar ações:**
   - Execute `gravador.py`
   - Realize as ações que deseja gravar
   - Pressione `ESC` para parar a gravação
   - As ações serão salvas em `mouse_log.txt`

2. **Reproduzir ações:**
   - Mova o arquivo `mouse_log.txt` para a pasta `presets/`
   - Execute `bot.py`
   - Selecione o arquivo de preset
   - Escolha se deseja executar em loop

## Atalhos

- `ESC` - Para parar a gravação
