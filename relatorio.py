from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Oportunidades de ingresso ao Ensino Superior")
pdf.sub_titulo("Regiões Norte e Sudeste")
pdf.imagem("img_capa.jpg", 30, 90, 150)
pdf.ln(170)
pdf.linha_centralizada("Autor: Felipe Barreiro Nascimento")
pdf.linha_centralizada("Data: 9 de Setembro de 2024")

# ------------- 1 pagina -------------
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("O acesso ao Ensino Superior no Brasil é marcado por desigualdades regionais que afetam diretamente as oportunidades dos estudantes. As regiões Norte e Sudeste, em particular, apresentam realidades distintas no que se refere à oferta de vagas, à infraestrutura educacional e às condições socioeconômicas dos alunos.")

pdf.paragrafo("Esta análise de dados tem como objetivo investigar as diferenças no acesso ao Ensino Superior entre as regiões Norte e Sudeste do Brasil, identificando os principais fatores que influenciam esse processo. A partir de uma abordagem quantitativa, serão examinados indicadores como a quantidade de cursos disponíveis, o total de vagas ofertadas, a faixa etária dos ingressantes e a distribuição de vagas nos cursos mais concorridos.")

pdf.paragrafo("Para ilustrar o impacto dessas diferenças, o gráfico a seguir destaca a quantidade de cursos ofertados por região, proporcionando uma visão clara da distribuição das oportunidades de formação superior entre o Norte e o Sudeste.")

pdf.imagem("Gráfico_Cursos_Ofertados.png", 30, 135, 150)
pdf.ln(120)

pdf.paragrafo("A disparidade na quantidade de cursos oferecidos entre as regiões Norte e Sudeste do Brasil reflete profundas desigualdades socioeconômicas e históricas. O Sudeste, com sua maior urbanização e industrialização, concentra uma infraestrutura educacional mais robusta e recursos financeiros mais abundantes, resultando em uma oferta significativamente maior de cursos. Em contraste, a região Norte enfrenta desafios como menor densidade populacional, infraestrutura limitada e dificuldades de acesso, que acentuam as desigualdades regionais e restringem as oportunidades de ingresso ao ensino superior para os seus moradores.")

# ------------- 2 pagina -------------
pdf.paragrafo("A quantidade de vagas ofertadas também reflete as desigualdades regionais entre o Norte e o Sudeste. Com mais instituições, o Sudeste oferece um número significativamente maior de vagas, ampliando as oportunidades de ingresso ao Ensino Superior. Já o Norte, com infraestrutura mais limitada, enfrenta dificuldades para atender à demanda. O gráfico a seguir destaca essa diferença na distribuição de vagas entre as duas regiões.")

pdf.image("Gráfico_Vagas_Ofertadas.png", 30, 90, 150)
pdf.ln(120)

pdf.paragrafo("O gráfico revela uma diferença significativa entre o Norte e o Sudeste do Brasil. Enquanto o Sudeste apresenta uma oferta muito maior de vagas, refletindo sua infraestrutura educacional mais desenvolvida, o Norte enfrenta uma limitação expressiva na quantidade de vagas disponíveis. Essa disparidade não apenas limita o acesso ao Ensino Superior para os estudantes do Norte, mas também evidencia a necessidade de estratégias para equilibrar a oferta de vagas e melhorar as oportunidades educacionais em regiões menos favorecidas.")

# ------------- 3 pagina -------------
pdf.add_page()

pdf.paragrafo("O gráfico a seguir ilustra a distribuição etária dos ingressantes no Ensino Superior, fornecendo uma visão clara sobre as faixas etárias predominantes entre os estudantes. Com base nos dados apresentados, é possível observar a quantidade de ingressos distribuídos entre diferentes grupos etários, desde os jovens de 18 a 24 anos até os mais velhos, com 60 anos ou mais.")

pdf.imagem("Gráfico_Faixa_Etária.png", 22, 50, 175)
pdf.ln(120)

pdf.paragrafo("A redução do número de ingressos no Ensino Superior com o avanço da idade não necessariamente reflete uma desigualdade, mas pode ser atribuída a diversos fatores contextuais e individuais. Para muitos adultos mais velhos, a decisão de retornar aos estudos pode ser influenciada por considerações práticas e financeiras, como a necessidade de estabilidade no emprego e responsabilidades familiares que tornam a dedicação ao estudo mais desafiadora.")

pdf.paragrafo("Além disso, o mercado de trabalho frequentemente valoriza a experiência prática e habilidades adquiridas ao longo da carreira, o que pode reduzir o incentivo para buscar um diploma acadêmico adicional. Programas de educação continuada e treinamento profissional também oferecem alternativas mais flexíveis e diretamente aplicáveis, o que pode ser preferível para muitos adultos. Assim, a diminuição nos ingressos por faixa etária mais avançada pode refletir escolhas ponderadas com base em circunstâncias pessoais e oportunidades alternativas, em vez de uma falha no sistema educacional.")

# ------------- 4 pagina -------------
pdf.add_page()

pdf.paragrafo("O gráfico a seguir apresenta a quantidade de vagas ofertadas por região para os cinco cursos mais concorridos, oferecendo uma visão detalhada da distribuição das oportunidades educacionais nas diferentes regiões do país. Este gráfico destaca como a oferta de vagas varia entre as regiões Norte e Sudeste para cursos altamente procurados, como Arquitetura, Direito, Engenharia Civil, Medicina e Psicologia. A análise revela disparidades significativas, refletindo a capacidade das instituições de ensino e a demanda regional por esses cursos.")

pdf.image("Gráfico_Cinco_Cursos.png", 15, 65, 190)
pdf.ln(130)

pdf.paragrafo("Enquanto a região Sudeste tende a oferecer um maior número de vagas devido à sua infraestrutura mais desenvolvida e maior concentração de instituições educacionais, a região Norte pode enfrentar limitações relacionadas à infraestrutura e recursos. Compreender essas diferenças é crucial para identificar e abordar as desigualdades no acesso ao Ensino Superior e para desenvolver estratégias que possam equilibrar a oferta educacional e atender melhor às necessidades dos estudantes em todas as regiões.")

# ------------- 5 página -------------
pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo("A análise das oportunidades de ingresso ao Ensino Superior nas regiões Norte e Sudeste do Brasil revela uma discrepância significativa na oferta de cursos e vagas, com o Sudeste apresentando uma infraestrutura educacional mais desenvolvida e uma maior quantidade de oportunidades, enquanto o Norte enfrenta desafios relacionados à infraestrutura e recursos limitados. A distribuição etária dos ingressantes mostra uma predominância de jovens entre 18 e 24 anos, com uma diminuição acentuada nas faixas etárias mais avançadas, o que pode ser atribuído a barreiras econômicas e responsabilidades pessoais. Essas diferenças destacam a necessidade urgente de políticas que promovam a equidade regional, melhorando a infraestrutura educacional e criando programas de apoio que atendam às necessidades de estudantes de todas as idades e regiões, visando um acesso mais justo e amplo ao Ensino Superior em todo o país.")
pdf.ln(15)

pdf.paragrafo("Links utilizados para pesquisa:")
pdf.paragrafo("1 - https://www.semesp.org.br/mapa/edicao-10/regioes/sudeste/")
pdf.paragrafo("2 - https://www.semesp.org.br/mapa/edicao-10/regioes/")
pdf.paragrafo("3 - www.semesp.org.br/wp-content/uploads/2023/06/mapa-do-ensino-superior-no-brasil-2023.pdf")
pdf.paragrafo("4 - blog.unopar.com.br/conheca-os-cursos-mais-concorridos-do-sisu/#:~:text=Medicina%2C%20Direito%2C%20Engenharia%20Civil%2C,fazer%20a%20diferen%C3%A7a%20na%20sociedade.")

pdf.output("relatório.pdf")