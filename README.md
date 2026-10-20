# Spoken Page

Converte um livro em PDF num audiolivro, diretamente no browser.

- `index.html`: a fonte da página (é também a versão publicada no claude.ai).
- `docs/index.html`: a versão completa que o GitHub Pages publica. Gera-se com `python3 build.py`.

## Vozes Piper (vozes neurais, mais humanas)

As vozes Piper correm no teu dispositivo. Na primeira vez, cada voz descarrega um modelo
do Hugging Face (cerca de 63 MB) e fica guardada no browser para as vezes seguintes.
Com uma voz Piper ativa aparece o botão **Save track**, que grava o capítulo num ficheiro `.wav`.

Dentro do claude.ai as vozes Piper não funcionam, porque essas páginas não podem descarregar ficheiros externos.
Para as usares, publica a pasta `docs` num destes serviços (todos gratuitos):

### GitHub Pages
1. No repositório, vai a **Settings › Pages**.
2. Em *Build and deployment*, escolhe **Deploy from a branch**, a branch `main` e a pasta `/docs`, e guarda.
3. Ao fim de um minuto, o site fica disponível em `https://pedrobd.github.io/audiobook/`.

### Netlify Drop (alternativa)
Abre https://app.netlify.com/drop e arrasta a pasta `docs` para a página.

## Vozes incluídas

| Língua | Vozes |
| --- | --- |
| Português | Tugão (Portugal), Faber (Brasil) |
| Inglês | HFC Female, Lessac, Ryan (EUA); Alba, Jenny (Reino Unido) |
| Espanhol | Davefx (Espanha), Claude (México) |
| Francês | Siwis, Tom |
| Alemão | Thorsten |
| Italiano | Riccardo |

Para adicionar outra voz, junta-a à lista `PIPER_VOICES` em `index.html`.
O catálogo completo está em https://huggingface.co/rhasspy/piper-voices
