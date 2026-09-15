# Exercícios de Python — Curso em Vídeo

Resoluções dos exercícios do curso "Python 3 - Curso em Vídeo" (Gustavo Guanabara).
O repositório cobre o **Mundo 1 (Fundamentos, ex001–ex022)** e o **Mundo 2 (Estruturas de Controle, ex023–ex035)**.

Os arquivos ficam em `Pythonexercicios/`, separados por mundo:

```
Pythonexercicios/
├── ex0.mp3
├── mundo1/
└── mundo2/
```

## Mundo 1 - Fundamentos

| Arquivo | Descrição |
| --- | --- |
| `mundo1/ex001_ola_mundo.py` | Exibe a mensagem "Olá, Mundo!" no terminal. |
| `mundo1/ex002_leitura_nome.py` | Lê o nome do usuário e exibe uma mensagem de boas-vindas. |
| `mundo1/ex003_soma_dois_numeros.py` | Lê dois números inteiros e mostra a soma entre eles. |
| `mundo1/ex004_analise_string.py` | Lê um valor e mostra seu tipo primitivo e várias verificações de string (numérico, alfabético, maiúsculo etc.). |
| `mundo1/ex005_antecessor_sucessor.py` | Lê um número inteiro e mostra seu antecessor e sucessor. |
| `mundo1/ex006_dobro_triplo_raiz.py` | Lê um número e mostra seu dobro, triplo e raiz quadrada. |
| `mundo1/ex007_media_notas.py` | Lê duas notas de um aluno e calcula a média entre elas. |
| `mundo1/ex008_conversao_medidas.py` | Lê uma medida em metros e converte para centímetros e milímetros. |
| `mundo1/ex009_tabuada.py` | Lê um número e exibe sua tabuada de 1 a 10. |
| `mundo1/ex010_reais_para_dolar.py` | Lê um valor em reais e mostra quantos dólares é possível comprar. |
| `mundo1/ex011_pintura_parede.py` | Lê altura e largura de uma parede e calcula a área e a tinta necessária para pintá-la. |
| `mundo1/ex012_desconto_produto.py` | Lê o preço de um produto e mostra o valor com 5% de desconto. |
| `mundo1/ex013_aumento_salario.py` | Lê um salário e mostra o novo valor com 15% de aumento. |
| `mundo1/ex014_conversao_temperatura.py` | Lê uma temperatura em Celsius e converte para Kelvin e Fahrenheit. |
| `mundo1/ex015_aluguel_carro.py` | Calcula o valor a pagar pelo aluguel de um carro conforme dias e km rodados. |
| `mundo1/ex016_parte_inteira.py` | Lê um número real e mostra sua porção inteira usando `math.trunc()`. |
| `mundo1/ex017_hipotenusa.py` | Lê os catetos de um triângulo retângulo e calcula a hipotenusa. |
| `mundo1/ex018_seno_cosseno_tangente.py` | Lê um ângulo e mostra seu seno, cosseno e tangente. |
| `mundo1/ex019_sorteio_aluno.py` | Lê o nome de quatro alunos e sorteia um deles aleatoriamente. |
| `mundo1/ex020_ordem_apresentacao.py` | Lê o nome de quatro alunos e embaralha a ordem de apresentação dos trabalhos. |
| `mundo1/ex021_tocar_musica.py` | Toca um arquivo de áudio MP3 usando a biblioteca `pygame`. |
| `mundo1/ex022_analise_nome.py` | Lê o nome completo e mostra em maiúsculas, minúsculas, o total de letras e as letras do primeiro nome. |

## Mundo 2 - Estruturas de Controle

| Arquivo | Descrição |
| --- | --- |
| `mundo2/ex023_separar_digitos.py` | Lê um número e mostra separadamente unidade, dezena, centena e milhar. |
| `mundo2/ex024_cidade_santo.py` | Lê o nome de uma cidade e informa se ele começa com "Santo". |
| `mundo2/ex025_nome_silva.py` | Lê o nome completo e informa se "Silva" aparece nele. |
| `mundo2/ex026_ocorrencias_letra.py` | Lê uma frase e mostra quantas vezes a letra "a" aparece e suas primeira e última posições. |
| `mundo2/ex027_primeiro_ultimo_nome.py` | Lê o nome completo e mostra separadamente o primeiro e o último nome. |
| `mundo2/ex028_jogo_adivinhacao.py` | Sorteia um número de 0 a 5 e verifica se o palpite do jogador acertou. |
| `mundo2/ex029_multa_velocidade.py` | Lê a velocidade de um carro e aplica multa se ultrapassar 80 km/h. |
| `mundo2/ex030_par_ou_impar.py` | Lê um número e informa se ele é par ou ímpar. |
| `mundo2/ex031_preco_viagem.py` | Lê a distância de uma viagem e calcula o preço conforme a passagem seja de até ou mais de 200 km. |
| `mundo2/ex032_ano_bissexto.py` | Lê um ano (ou usa o atual) e informa se ele é bissexto. |
| `mundo2/ex033_maior_menor.py` | Lê três números e mostra qual é o maior e qual é o menor. |
| `mundo2/ex034_aumento_por_faixa.py` | Lê um salário e aplica 10% de aumento acima de R$ 1250 ou 15% caso contrário. |
| `mundo2/ex035_analise_triangulo.py` | Lê três segmentos e informa se eles podem formar um triângulo. |

## Como executar

Cada exercício é um script independente:

```bash
python Pythonexercicios/mundo1/ex001_ola_mundo.py
python Pythonexercicios/mundo2/ex030_par_ou_impar.py
```

### Observações

- `mundo1/ex021_tocar_musica.py` depende da biblioteca `pygame` (`pip install pygame`) e carrega o arquivo de áudio `ex0.mp3` a partir do diretório de execução. O arquivo está em `Pythonexercicios/ex0.mp3`, então execute o script a partir de um diretório que contenha um `ex0.mp3` (por exemplo, copiando o arquivo para o diretório atual).
- Os demais exercícios usam apenas a biblioteca padrão do Python 3.
