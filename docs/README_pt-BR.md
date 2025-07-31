# Genpass

Genpass é um gerador de senhas fortes, simples e direto, criado em **Python 3.13**. Ele permite que você crie senhas seguras e personalizadas diretamente da sua linha de comando.

## Instalação

Para usar o Genpass, você precisa ter o python Python313 ou superior instalado. O projeto não requer nenhuma biblioteca externa, então você pode executá-lo diretamente.
1. Clone o repositório:
```bash
git clone https://github.com/devtools-py/genpass.git
cd genpass
```

2. Execute o programa:
```bash
python3 genpass.py
```

## Como Usar

O Genpass oferece algumas opções de linha de comando para personalizar a senha gerada.

### Opções

- `-l <tamanho>`: Define o **tamanho da senha**. O valor deve ser um número inteiro. O **mínimo é 12** e o **padrão é 16** caso não seja especificado.

- `-d <caracteres>`: Permite **remover caracteres indesejados** do conjunto de caracteres. O programa garante que a senha sempre conterá letras maiúsculas, minúsculas, números e símbolos. Gerando um error caso tente remover todos os caracteres de um dos conjuntos citados anteriormente.

### Exemplos

1. **Gerar uma senha com o tamanho padrão (16):**
```bash
python3 genpass.py
```

2. **Gerar uma senha com 24 caracteres:**
```bash
python3 genpass.py -l 24
```

3. **Gerar uma senha removendo as caracteres "i" e "o":**
```bash
python3 genpass.py -d io
```

4. **Gerar uma senha com 18 caracteres, removendo o caractere "@":**
```bash
python3 genpass.py -l 18 -d @
```
