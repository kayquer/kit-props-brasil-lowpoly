# Kit Props Brasil Low Poly: props 3D low poly gratuitos (CC0) de cenário brasileiro

**🇧🇷 Português** · 🇬🇧 [Read in English](README.md)

![Todos os props do Kit Props Brasil Low Poly lado a lado: natureza, fauna, rua, rural, rio, tecnologia sustentável e sinais de poluição](previews/capa.jpg)

▶️ **[Assista ao vídeo no YouTube](https://www.youtube.com/watch?v=QNr0wf4MUew)** · **[Baixe no itch.io](https://kkyqr.itch.io/low-poly-brazil-props-kit)** (grátis, doação opcional)

> **Resposta curta:** o Kit Props Brasil Low Poly é um pacote **gratuito e em domínio público (CC0 1.0)** de
> **props 3D low poly em glTF/GLB** com a cara do Brasil: flores do campo, cupinzeiro, mandacaru, vitória-régia,
> capivara, garça, o cachorro caramelo, o orelhão, barraca de feira, fardo de feno, trapiche, barril de chuva,
> poste solar e **sinais de poluição** (monte de lixo, plástico boiando, espuma no rio, manilha de esgoto). Quase
> todos têm **até 150 triângulos**, cores chapadas e nenhuma textura: dá para espalhar centenas. Funciona no Godot,
> Unity, Unreal, three.js, Babylon.js e Blender. Pode usar comercialmente; atribuição é opcional.

**Props low poly leves** para contar histórias com o cenário: natureza num mapa novo, o dia a dia aparecendo
conforme a cidade cresce, tecnologia sustentável ao lado dos prédios que a trazem, e a poluição *visível* (sumindo
quando o jogador resolve a causa). Tudo em **glTF binário (`.glb`)**, cores chapadas, sem textura. Feito para
**jogos educativos, city builders, simulação, game jams e protótipos**.

**Domínio público ([CC0 1.0](LICENSE)).** Use como quiser, em projetos pessoais, educativos ou comerciais;
modifique e redistribua. Atribuição é opcional (veja [CITATION.cff](CITATION.cff)). Sem garantia.

**Conteúdo:** [Como usar](#como-usar) · [Catálogo](#catálogo) · [Gerar ou modificar](#gerar-ou-modificar-os-modelos) ·
[Perguntas frequentes](#perguntas-frequentes) · [Origem e créditos](#origem-e-créditos)

## Como usar

- Baixe o repositório (**Code → Download ZIP**) ou só os `.glb` que precisar em [`models/`](models).
- **Escala:** "de brinquedo", para uma grade de cidade em que **1 lote = 2 × 2 unidades** (o hidrante tem cerca de
  0,3 de altura e o banco de praça 0,72 de largura), a mesma do [Kit Cidade Low Poly](https://github.com/kayquer/kit-cidade-lowpoly).
- **Orientação:** Y para cima, frente do modelo para **-Z** (padrão glTF). Props de terra ficam em y = 0; props de
  água (vitória-régia, aguapé, lixo boiando, espuma, boia, canoa, peixes) ficam **na superfície da água, em y = 0**.
- **A frente importa** em alguns: `rio/trapiche` (o píer avança 1,4 unidade para a frente, -Z, a partir da base na
  margem), `poluicao/manilha_esgoto` (o cano despeja para -Z) e as placas, o orelhão e o hidrômetro (olham para
  -Z). Vire a frente para a água ou para a rua.
- **Materiais:** um material por cor (PBR, só cor base, rugosidade 0,85). Para desenhar tudo numa chamada só,
  converta as cores dos materiais em cor de vértice e junte ou instancie os props na sua engine.
- **Orçamento:** natureza, fauna, rua, rural, rio, tecnologia e poluição têm **até 150 triângulos** por prop (a
  maioria entre 50 e 140); `detalhados/` e `arvores/` vão até 1.500. Todo arquivo tem menos de 150 KB.

## Catálogo

<!-- catalogo:inicio -->
**100 modelos** em 9 categorias.

### Natureza · Nature (16)

![Modelos 3D low poly: Natureza](previews/natureza.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/natureza/aguape.jpg" width="120" alt="Aguapés"> | [`aguape`](models/natureza/aguape.glb) | Aguapés | 132 |
| <img src="previews/natureza/arbustos.jpg" width="120" alt="Arbustos de canteiro"> | [`arbustos`](models/natureza/arbustos.glb) | Arbustos de canteiro | 128 |
| <img src="previews/natureza/bambu.jpg" width="120" alt="Moita de bambu"> | [`bambu`](models/natureza/bambu.glb) | Moita de bambu | 132 |
| <img src="previews/natureza/bananeira.jpg" width="120" alt="Bananeira"> | [`bananeira`](models/natureza/bananeira.glb) | Bananeira | 112 |
| <img src="previews/natureza/bromelia.jpg" width="120" alt="Bromélia"> | [`bromelia`](models/natureza/bromelia.glb) | Bromélia | 116 |
| <img src="previews/natureza/capim_alto.jpg" width="120" alt="Capim alto"> | [`capim_alto`](models/natureza/capim_alto.glb) | Capim alto | 54 |
| <img src="previews/natureza/coqueiro.jpg" width="120" alt="Coqueiro"> | [`coqueiro`](models/natureza/coqueiro.glb) | Coqueiro | 140 |
| <img src="previews/natureza/cupinzeiro.jpg" width="120" alt="Cupinzeiro"> | [`cupinzeiro`](models/natureza/cupinzeiro.glb) | Cupinzeiro | 54 |
| <img src="previews/natureza/flores_campo.jpg" width="120" alt="Flores do campo"> | [`flores_campo`](models/natureza/flores_campo.glb) | Flores do campo | 136 |
| <img src="previews/natureza/mandacaru.jpg" width="120" alt="Mandacaru"> | [`mandacaru`](models/natureza/mandacaru.glb) | Mandacaru | 88 |
| <img src="previews/natureza/matacao.jpg" width="120" alt="Matacão"> | [`matacao`](models/natureza/matacao.glb) | Matacão | 78 |
| <img src="previews/natureza/pedras.jpg" width="120" alt="Pedras de beira de rio"> | [`pedras`](models/natureza/pedras.glb) | Pedras de beira de rio | 84 |
| <img src="previews/natureza/taboa.jpg" width="120" alt="Taboas de brejo"> | [`taboa`](models/natureza/taboa.glb) | Taboas de brejo | 136 |
| <img src="previews/natureza/toco.jpg" width="120" alt="Toco de árvore cortada"> | [`toco`](models/natureza/toco.glb) | Toco de árvore cortada | 96 |
| <img src="previews/natureza/tronco_caido.jpg" width="120" alt="Tronco caído"> | [`tronco_caido`](models/natureza/tronco_caido.glb) | Tronco caído | 88 |
| <img src="previews/natureza/vitoria_regia.jpg" width="120" alt="Vitória-régia"> | [`vitoria_regia`](models/natureza/vitoria_regia.glb) | Vitória-régia | 148 |

### Fauna · Wildlife and animals (13)

![Modelos 3D low poly: Fauna](previews/fauna.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/fauna/arara.jpg" width="120" alt="Arara-vermelha pousada num galho seco baixo"> | [`arara`](models/fauna/arara.glb) | Arara-vermelha pousada num galho seco baixo | 118 |
| <img src="previews/fauna/cachorro_caramelo.jpg" width="120" alt="Cachorro caramelo"> | [`cachorro_caramelo`](models/fauna/cachorro_caramelo.glb) | Cachorro caramelo | 108 |
| <img src="previews/fauna/capivara.jpg" width="120" alt="Capivara"> | [`capivara`](models/fauna/capivara.glb) | Capivara | 116 |
| <img src="previews/fauna/garca.jpg" width="120" alt="Garça branca"> | [`garca`](models/fauna/garca.glb) | Garça branca | 80 |
| <img src="previews/fauna/lambaris.jpg" width="120" alt="Cardume de lambaris"> | [`lambaris`](models/fauna/lambaris.glb) | Cardume de lambaris | 120 |
| <img src="previews/fauna/ninho_joao_de_barro.jpg" width="120" alt="Ninho de joão-de-barro"> | [`ninho_joao_de_barro`](models/fauna/ninho_joao_de_barro.glb) | Ninho de joão-de-barro | 72 |
| <img src="previews/fauna/quati.jpg" width="120" alt="Quati"> | [`quati`](models/fauna/quati.glb) | Quati | 112 |
| <img src="previews/fauna/sapo.jpg" width="120" alt="Sapo verde sentado numa pedrinha da margem, com os olhos saltados em cima e as patas dobradas dos lados"> | [`sapo`](models/fauna/sapo.glb) | Sapo verde sentado numa pedrinha da margem, com os olhos saltados em cima e as patas dobradas dos lados | 104 |
| <img src="previews/fauna/tamandua.jpg" width="120" alt="Tamanduá-bandeira"> | [`tamandua`](models/fauna/tamandua.glb) | Tamanduá-bandeira | 84 |
| <img src="previews/fauna/tartaruga.jpg" width="120" alt="Tartaruga de rio"> | [`tartaruga`](models/fauna/tartaruga.glb) | Tartaruga de rio | 110 |
| <img src="previews/fauna/tatu.jpg" width="120" alt="Tatu"> | [`tatu`](models/fauna/tatu.glb) | Tatu | 128 |
| <img src="previews/fauna/tucano.jpg" width="120" alt="Tucano"> | [`tucano`](models/fauna/tucano.glb) | Tucano | 108 |
| <img src="previews/fauna/vaca.jpg" width="120" alt="Vaca malhada de pasto"> | [`vaca`](models/fauna/vaca.glb) | Vaca malhada de pasto | 128 |

### Rua e bairro · Street and neighborhood (20)

![Modelos 3D low poly: Rua e bairro](previews/rua.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/rua/banco_praca.jpg" width="120" alt="Banco de praça"> | [`banco_praca`](models/rua/banco_praca.glb) | Banco de praça | 96 |
| <img src="previews/rua/barraca_feira.jpg" width="120" alt="Barraca de feira"> | [`barraca_feira`](models/rua/barraca_feira.glb) | Barraca de feira | 140 |
| <img src="previews/rua/bebedouro.jpg" width="120" alt="Bebedouro público"> | [`bebedouro`](models/rua/bebedouro.glb) | Bebedouro público | 128 |
| <img src="previews/rua/bicicletario.jpg" width="120" alt="Bicicletário"> | [`bicicletario`](models/rua/bicicletario.glb) | Bicicletário | 148 |
| <img src="previews/rua/botijao.jpg" width="120" alt="Botijão de gás cinza de cozinha, com base, ombro arredondado, válvula e a alça de proteção no alto"> | [`botijao`](models/rua/botijao.glb) | Botijão de gás cinza de cozinha, com base, ombro arredondado, válvula e a alça de proteção no alto | 120 |
| <img src="previews/rua/bueiro.jpg" width="120" alt="Bueiro"> | [`bueiro`](models/rua/bueiro.glb) | Bueiro | 92 |
| <img src="previews/rua/caixa_dagua.jpg" width="120" alt="Caixa d'água de polietileno"> | [`caixa_dagua`](models/rua/caixa_dagua.glb) | Caixa d'água de polietileno | 80 |
| <img src="previews/rua/carrinho_mao.jpg" width="120" alt="Carrinho de mão de obra"> | [`carrinho_mao`](models/rua/carrinho_mao.glb) | Carrinho de mão de obra | 100 |
| <img src="previews/rua/carrinho_pipoca.jpg" width="120" alt="Carrinho de pipoca"> | [`carrinho_pipoca`](models/rua/carrinho_pipoca.glb) | Carrinho de pipoca | 112 |
| <img src="previews/rua/cavalete_pf.jpg" width="120" alt="Cavalete de calçada em A, de madeira, com um quadro-negro que só mostra o desenho de um prato (sem letras)"> | [`cavalete_pf`](models/rua/cavalete_pf.glb) | Cavalete de calçada em A, de madeira, com um quadro-negro que só mostra o desenho de um prato (sem letras) | 84 |
| <img src="previews/rua/cone_transito.jpg" width="120" alt="Cone de trânsito laranja com faixa branca, sobre a base quadrada"> | [`cone_transito`](models/rua/cone_transito.glb) | Cone de trânsito laranja com faixa branca, sobre a base quadrada | 52 |
| <img src="previews/rua/hidrante.jpg" width="120" alt="Hidrante de rua"> | [`hidrante`](models/rua/hidrante.glb) | Hidrante de rua | 98 |
| <img src="previews/rua/lixeira_grade.jpg" width="120" alt="Lixeira de grade"> | [`lixeira_grade`](models/rua/lixeira_grade.glb) | Lixeira de grade | 140 |
| <img src="previews/rua/mesa_cadeiras.jpg" width="120" alt="Mesa e duas cadeiras de plástico brancas na calçada, como as de bar de bairro (sem logotipo)"> | [`mesa_cadeiras`](models/rua/mesa_cadeiras.glb) | Mesa e duas cadeiras de plástico brancas na calçada, como as de bar de bairro (sem logotipo) | 128 |
| <img src="previews/rua/monte_areia.jpg" width="120" alt="Monte de areia de obra na calçada, com uma pá fincada no alto"> | [`monte_areia`](models/rua/monte_areia.glb) | Monte de areia de obra na calçada, com uma pá fincada no alto | 48 |
| <img src="previews/rua/orelhao.jpg" width="120" alt="Orelhão"> | [`orelhao`](models/rua/orelhao.glb) | Orelhão | 84 |
| <img src="previews/rua/placa_rua.jpg" width="120" alt="Placa de rua"> | [`placa_rua`](models/rua/placa_rua.glb) | Placa de rua | 36 |
| <img src="previews/rua/poste_concreto.jpg" width="120" alt="Poste de concreto de rua"> | [`poste_concreto`](models/rua/poste_concreto.glb) | Poste de concreto de rua | 96 |
| <img src="previews/rua/tanque_lavar.jpg" width="120" alt="Tanque de lavar roupa de cimento"> | [`tanque_lavar`](models/rua/tanque_lavar.glb) | Tanque de lavar roupa de cimento | 84 |
| <img src="previews/rua/varal.jpg" width="120" alt="Varal de quintal"> | [`varal`](models/rua/varal.glb) | Varal de quintal | 84 |

### Rural · Countryside (12)

![Modelos 3D low poly: Rural](previews/rural.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/rural/caixotes.jpg" width="120" alt="Caixotes de madeira empilhados com laranjas e tomates, como os da colheita no sítio"> | [`caixotes`](models/rural/caixotes.glb) | Caixotes de madeira empilhados com laranjas e tomates, como os da colheita no sítio | 108 |
| <img src="previews/rural/cerca_mourao.jpg" width="120" alt="Cerca de mourões"> | [`cerca_mourao`](models/rural/cerca_mourao.glb) | Cerca de mourões | 60 |
| <img src="previews/rural/cocho_gado.jpg" width="120" alt="Cocho de madeira para o gado com água, sobre dois pés, e um bloco de sal mineral branco ao lado"> | [`cocho_gado`](models/rural/cocho_gado.glb) | Cocho de madeira para o gado com água, sobre dois pés, e um bloco de sal mineral branco ao lado | 96 |
| <img src="previews/rural/colmeia.jpg" width="120" alt="Colmeia de abelhas"> | [`colmeia`](models/rural/colmeia.glb) | Colmeia de abelhas | 72 |
| <img src="previews/rural/espantalho.jpg" width="120" alt="Espantalho"> | [`espantalho`](models/rural/espantalho.glb) | Espantalho | 120 |
| <img src="previews/rural/fardo_feno.jpg" width="120" alt="Fardo de feno redondo"> | [`fardo_feno`](models/rural/fardo_feno.glb) | Fardo de feno redondo | 84 |
| <img src="previews/rural/horta.jpg" width="120" alt="Canteiro de horta"> | [`horta`](models/rural/horta.glb) | Canteiro de horta | 144 |
| <img src="previews/rural/latao_leite.jpg" width="120" alt="Latões de leite de alumínio num estrado de madeira na beira da estrada, esperando a coleta"> | [`latao_leite`](models/rural/latao_leite.glb) | Latões de leite de alumínio num estrado de madeira na beira da estrada, esperando a coleta | 108 |
| <img src="previews/rural/moinho_vento.jpg" width="120" alt="Cata-vento de bombear água"> | [`moinho_vento`](models/rural/moinho_vento.glb) | Cata-vento de bombear água | 136 |
| <img src="previews/rural/pilha_lenha.jpg" width="120" alt="Pilha de lenha de eucalipto cortada e arrumada entre duas estacas, toras finas deitadas em três camadas"> | [`pilha_lenha`](models/rural/pilha_lenha.glb) | Pilha de lenha de eucalipto cortada e arrumada entre duas estacas, toras finas deitadas em três camadas | 120 |
| <img src="previews/rural/poco_caipira.jpg" width="120" alt="Poço caipira de tijolo"> | [`poco_caipira`](models/rural/poco_caipira.glb) | Poço caipira de tijolo | 124 |
| <img src="previews/rural/porteira.jpg" width="120" alt="Porteira de fazenda"> | [`porteira`](models/rural/porteira.glb) | Porteira de fazenda | 84 |

### Rio e beira d'água · River and riverside (6)

![Modelos 3D low poly: Rio e beira d'água](previews/rio.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/rio/bombona_flutuante.jpg" width="120" alt="Flutuante de bombonas"> | [`bombona_flutuante`](models/rio/bombona_flutuante.glb) | Flutuante de bombonas | 116 |
| <img src="previews/rio/canoa.jpg" width="120" alt="Canoa de madeira de pescador boiando"> | [`canoa`](models/rio/canoa.glb) | Canoa de madeira de pescador boiando | 132 |
| <img src="previews/rio/covo.jpg" width="120" alt="Covo de pesca"> | [`covo`](models/rio/covo.glb) | Covo de pesca | 100 |
| <img src="previews/rio/pescaria.jpg" width="120" alt="Pescaria na margem"> | [`pescaria`](models/rio/pescaria.glb) | Pescaria na margem | 98 |
| <img src="previews/rio/rede_pesca.jpg" width="120" alt="Rede de pesca verde secando ao sol, pendurada e caída entre duas estacas na beira do rio, com boias laranja"> | [`rede_pesca`](models/rio/rede_pesca.glb) | Rede de pesca verde secando ao sol, pendurada e caída entre duas estacas na beira do rio, com boias laranja | 120 |
| <img src="previews/rio/trapiche.jpg" width="120" alt="Trapiche"> | [`trapiche`](models/rio/trapiche.glb) | Trapiche | 120 |

### Tecnologia sustentável · Sustainable technology (7)

![Modelos 3D low poly: Tecnologia sustentável](previews/tecnologia.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/tecnologia/barril_chuva.jpg" width="120" alt="Barril de captação de chuva"> | [`barril_chuva`](models/tecnologia/barril_chuva.glb) | Barril de captação de chuva | 124 |
| <img src="previews/tecnologia/boia_rio.jpg" width="120" alt="Boia de monitoramento do rio"> | [`boia_rio`](models/tecnologia/boia_rio.glb) | Boia de monitoramento do rio | 128 |
| <img src="previews/tecnologia/hidrometro.jpg" width="120" alt="Hidrômetro"> | [`hidrometro`](models/tecnologia/hidrometro.glb) | Hidrômetro | 80 |
| <img src="previews/tecnologia/lixeiras_coleta.jpg" width="120" alt="Lixeiras de coleta seletiva simples"> | [`lixeiras_coleta`](models/tecnologia/lixeiras_coleta.glb) | Lixeiras de coleta seletiva simples | 120 |
| <img src="previews/tecnologia/placa_educativa.jpg" width="120" alt="Placa educativa de beira de rio"> | [`placa_educativa`](models/tecnologia/placa_educativa.glb) | Placa educativa de beira de rio | 132 |
| <img src="previews/tecnologia/pluviometro.jpg" width="120" alt="Pluviômetro"> | [`pluviometro`](models/tecnologia/pluviometro.glb) | Pluviômetro | 88 |
| <img src="previews/tecnologia/poste_solar.jpg" width="120" alt="Poste solar"> | [`poste_solar`](models/tecnologia/poste_solar.glb) | Poste solar | 112 |

### Sinais de poluição · Pollution signs (19)

![Modelos 3D low poly: Sinais de poluição](previews/poluicao.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/poluicao/barranco_erodido.jpg" width="120" alt="Barranco erodido sem mata ciliar"> | [`barranco_erodido`](models/poluicao/barranco_erodido.glb) | Barranco erodido sem mata ciliar | 140 |
| <img src="previews/poluicao/cacamba_entulho.jpg" width="120" alt="Caçamba de entulho amarela, pequena, transbordando de tijolos, restos de concreto e tábuas quebradas"> | [`cacamba_entulho`](models/poluicao/cacamba_entulho.glb) | Caçamba de entulho amarela, pequena, transbordando de tijolos, restos de concreto e tábuas quebradas | 88 |
| <img src="previews/poluicao/cano_pvc.jpg" width="120" alt="Cano de PVC improvisado saindo do barranco e despejando um fio de esgoto escuro para a frente, na água"> | [`cano_pvc`](models/poluicao/cano_pvc.glb) | Cano de PVC improvisado saindo do barranco e despejando um fio de esgoto escuro para a frente, na água | 92 |
| <img src="previews/poluicao/carcaca_carro.jpg" width="120" alt="Carcaça de carro abandonado"> | [`carcaca_carro`](models/poluicao/carcaca_carro.glb) | Carcaça de carro abandonado | 96 |
| <img src="previews/poluicao/carrinho_mercado.jpg" width="120" alt="Carrinho de supermercado jogado no córrego"> | [`carrinho_mercado`](models/poluicao/carrinho_mercado.glb) | Carrinho de supermercado jogado no córrego | 68 |
| <img src="previews/poluicao/entulho.jpg" width="120" alt="Entulho"> | [`entulho`](models/poluicao/entulho.glb) | Entulho | 102 |
| <img src="previews/poluicao/espuma_rio.jpg" width="120" alt="Espuma de poluição"> | [`espuma_rio`](models/poluicao/espuma_rio.glb) | Espuma de poluição | 100 |
| <img src="previews/poluicao/galao_agrotoxico.jpg" width="120" alt="Galões de agrotóxico vazios jogados no chão (sem rótulo), um tombado, com uma mancha escura de vazamento"> | [`galao_agrotoxico`](models/poluicao/galao_agrotoxico.glb) | Galões de agrotóxico vazios jogados no chão (sem rótulo), um tombado, com uma mancha escura de vazamento | 104 |
| <img src="previews/poluicao/geladeira_velha.jpg" width="120" alt="Geladeira velha tombada no terreno baldio"> | [`geladeira_velha`](models/poluicao/geladeira_velha.glb) | Geladeira velha tombada no terreno baldio | 60 |
| <img src="previews/poluicao/lixo_flutuante.jpg" width="120" alt="Lixo boiando no rio"> | [`lixo_flutuante`](models/poluicao/lixo_flutuante.glb) | Lixo boiando no rio | 128 |
| <img src="previews/poluicao/manilha_esgoto.jpg" width="120" alt="Manilha de esgoto"> | [`manilha_esgoto`](models/poluicao/manilha_esgoto.glb) | Manilha de esgoto | 128 |
| <img src="previews/poluicao/monte_lixo.jpg" width="120" alt="Monte de lixo"> | [`monte_lixo`](models/poluicao/monte_lixo.glb) | Monte de lixo | 136 |
| <img src="previews/poluicao/peixe_morto.jpg" width="120" alt="Peixes mortos boiando"> | [`peixe_morto`](models/poluicao/peixe_morto.glb) | Peixes mortos boiando | 92 |
| <img src="previews/poluicao/pilha_toras.jpg" width="120" alt="Pilha de toras grossas de mata derrubada, empilhadas na clareira esperando o caminhão, com as pontas cortadas claras"> | [`pilha_toras`](models/poluicao/pilha_toras.glb) | Pilha de toras grossas de mata derrubada, empilhadas na clareira esperando o caminhão, com as pontas cortadas claras | 144 |
| <img src="previews/poluicao/pneus_velhos.jpg" width="120" alt="Pneus velhos"> | [`pneus_velhos`](models/poluicao/pneus_velhos.glb) | Pneus velhos | 136 |
| <img src="previews/poluicao/saco_lixo.jpg" width="120" alt="Sacos de lixo"> | [`saco_lixo`](models/poluicao/saco_lixo.glb) | Sacos de lixo | 78 |
| <img src="previews/poluicao/sofa_velho.jpg" width="120" alt="Sofá velho abandonado na calçada"> | [`sofa_velho`](models/poluicao/sofa_velho.glb) | Sofá velho abandonado na calçada | 72 |
| <img src="previews/poluicao/tambor_enferrujado.jpg" width="120" alt="Tambor enferrujado"> | [`tambor_enferrujado`](models/poluicao/tambor_enferrujado.glb) | Tambor enferrujado | 132 |
| <img src="previews/poluicao/toco_serrado.jpg" width="120" alt="Toco recém-serrado"> | [`toco_serrado`](models/poluicao/toco_serrado.glb) | Toco recém-serrado | 102 |

### Detalhados (até 1.500 tris) · Detailed (up to 1,500 tris) (4)

![Modelos 3D low poly: Detalhados (até 1.500 tris)](previews/detalhados.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/detalhados/cisterna.jpg" width="120" alt="Cisterna de placas (semiárido)"> | [`cisterna`](models/detalhados/cisterna.glb) | Cisterna de placas (semiárido) | 600 |
| <img src="previews/detalhados/composteira.jpg" width="120" alt="Composteira de dois módulos de ripas de madeira"> | [`composteira`](models/detalhados/composteira.glb) | Composteira de dois módulos de ripas de madeira | 1332 |
| <img src="previews/detalhados/lixeira_seletiva.jpg" width="120" alt="Lixeira seletiva de rua"> | [`lixeira_seletiva`](models/detalhados/lixeira_seletiva.glb) | Lixeira seletiva de rua | 936 |
| <img src="previews/detalhados/ponto_onibus.jpg" width="120" alt="Ponto de ônibus com telhado verde"> | [`ponto_onibus`](models/detalhados/ponto_onibus.glb) | Ponto de ônibus com telhado verde | 480 |

### Árvores nativas (até 1.500 tris) · Native trees (up to 1,500 tris) (3)

![Modelos 3D low poly: Árvores nativas (até 1.500 tris)](previews/arvores.jpg)

| | Modelo | Descrição | Tris |
|---|---|---|---:|
| <img src="previews/arvores/araucaria.jpg" width="120" alt="Araucária (pinheiro-do-paraná)"> | [`araucaria`](models/arvores/araucaria.glb) | Araucária (pinheiro-do-paraná) | 548 |
| <img src="previews/arvores/buriti.jpg" width="120" alt="Buriti (palmeira das veredas)"> | [`buriti`](models/arvores/buriti.glb) | Buriti (palmeira das veredas) | 636 |
| <img src="previews/arvores/ipe_amarelo.jpg" width="120" alt="Ipê-amarelo (árvore nativa)"> | [`ipe_amarelo`](models/arvores/ipe_amarelo.glb) | Ipê-amarelo (árvore nativa) | 388 |

<!-- catalogo:fim -->

## Gerar ou modificar os modelos

Cada modelo é um script Python curto em `src/<categoria>/<id>.py` que usa as peças de [`src/lib.py`](src/lib.py)
(caixas, cilindros, cones, canos, icoesferas baixas…) e uma única paleta de cores. Precisa do Blender 4.5 LTS.

```bash
blender -b --factory-startup --python src/rua/orelhao.py              # um modelo → models/rua/orelhao.glb
blender -b --factory-startup --python src/gerar_todos.py              # todos (+ models/catalogo.json)
blender -b --factory-startup --python src/gerar_todos.py -- poluicao  # uma categoria
blender -b --factory-startup --python src/vitrine.py -- tudo --cada   # imagens em previews/
blender -b --factory-startup --python src/vitrine.py -- todos         # previews/todos.jpg (renomeie para capa.jpg)
py -3 tools/atualizar_readme.py                                       # refaz o catálogo dos dois READMEs
```

Para um prop novo: copie um script parecido, monte com a **frente para -Y do Blender** (`exportar` gira 180°, e a
frente fica em -Z no glTF), use só cores da `PALETA`, sem chanfro (custa triângulos), e ponha o nome em inglês em
[`tools/nomes_en.json`](tools/nomes_en.json).

## Perguntas frequentes

**Posso usar num jogo comercial?**
Sim. Tudo é domínio público (CC0 1.0): uso comercial, modificação e redistribuição liberados, sem pedir
permissão nem pagar.

**Preciso dar crédito?**
Não, é opcional. Para citar, os dados estão em [CITATION.cff](CITATION.cff).

**São leves mesmo?**
Quase todos têm até 150 triângulos e nenhuma textura: centenas de props custam muito pouco. Junte por área ou use
instâncias na GPU (uma chamada de desenho por tipo).

**Por que props de poluição?**
Para o impacto ambiental ficar visível: num jogo educativo, lixo, espuma e esgoto podem aparecer quando a poluição
sobe e sumir quando o jogador resolve a causa. Os peixes mortos são de desenho, sem sangue.

## Origem e créditos

O kit nasceu do jogo educativo [Guardião da Água](https://github.com/kayquer/guardiao_da_agua_js), produto da
pesquisa de mestrado de Cláudia Dias Roxinol (Unesp, Presidente Prudente), desenvolvido com Kayque Rotondo. Ele
complementa o [Kit Cidade Low Poly](https://github.com/kayquer/kit-cidade-lowpoly) (prédios, ruas e veículos). Os
modelos e scripts foram feitos com o Blender e com o Claude (Anthropic) como assistente. Nenhum modelo de terceiros
faz parte deste repositório.
