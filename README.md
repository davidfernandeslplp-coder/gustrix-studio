# Gustrix Studio
Site estático com painel gratuito Pages CMS. Os arquivos e imagens ficam no GitHub.

## Publicar no GitHub
1. Crie um repositório público chamado gustrix-studio, branch main.
2. Envie TODO o conteúdo desta pasta, incluindo .github e .pages.yml. Não envie apenas dist.
3. Em Settings → Pages → Source, selecione GitHub Actions.
4. Na aba Actions, aguarde o fluxo Publicar site concluir. Abra o endereço mostrado em Settings → Pages.
5. Acesse https://app.pagescms.org/ e entre com sua conta GitHub. Autorize o aplicativo apenas para este repositório.
6. Abra o repositório no painel. As áreas Jogos, Novidades e Estúdio e contato estarão configuradas.

## Administrar
- Jogos: clique em novo item, preencha nome e endereço curto (ex.: meu-novo-jogo), capa, textos, galeria e links. Ative Publicado para aparecer. Destaque escolhe o portal da página inicial; mantenha apenas um jogo em destaque. A menor Ordem aparece primeiro.
- Novidades: cadastre título, endereço curto, data, categoria, imagem e texto. Separe os parágrafos por uma linha vazia. Publicado controla a presença no site.
- Estúdio e contato: altere a frase inicial, apresentação, logo, e-mail e redes. Links vazios não aparecem.
- Upload de imagens: use os campos de imagem do painel. Os arquivos serão guardados em media.
- Salvar dispara uma nova publicação no GitHub Actions. Aguarde o fluxo terminar antes de conferir.
- Rascunhos não aparecem no site, mas continuam visíveis no repositório público. Não guarde segredos, senhas ou documentos privados.
- O botão Área do estúdio abre o Pages CMS. O site não simula login nem grava senhas.
- O post de boas-vindas é um texto inicial editável; revise antes do lançamento.
- Ecos está identificado como Em teste. Adicione a URL pública do Google Play quando estiver disponível.
- Somente contas autorizadas no repositório podem editar. Não adicione colaboradores se quiser manter apenas você como administrador.

## Desenvolvimento
Python 3.10+; sem dependências. Execute python3 scripts/build.py. A pasta dist contém o site gerado e pode ser hospedada em qualquer serviço estático. Caminhos relativos funcionam no GitHub Pages de projeto e em domínio próprio.

## Verificação da integração
O esquema foi configurado segundo a documentação Pages CMS. O login, autorização do aplicativo e o primeiro ciclo de salvar/publicar só podem ser validados após conectar o repositório à sua conta.
