def count_Adenina(nucleotideos: str) -> int:
    sequencia = nucleotideos.lower()

    return(sequencia.count('a'))


def count_Timina(nucleotideos: str) -> int:
    sequencia = nucleotideos.lower()

    return(sequencia.count('t'))


def count_Citosina(nucleotideos: str) -> int:
    sequencia = nucleotideos.lower()

    return(sequencia.count('c'))

def count_Guanina(nucleotideos: str) -> int:
    sequencia = nucleotideos.lower()

    return(sequencia.count('g'))


def read_file(path: str) -> str:
    with open(path, "r") as file_seq:
        seq = file_seq.read().replace('\n', '')

    return seq

if __name__  == '__main__':
    
    path_file = '/home/ubuntu/Área de Trabalho/rosalind_dna.txt'
    seq = read_file(path_file)
    adenina = count_Adenina(seq)
    timina = count_Timina(seq)
    citosina = count_Citosina(seq)
    guanina = count_Guanina(seq)
    
    print(f'As quantidades são:\n -Adenina:{adenina}\n -Timina:{timina}\n -Citosina:{citosina}\n -Guanina:{guanina}')

