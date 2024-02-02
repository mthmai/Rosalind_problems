def read_file(path: str) -> str:
    with open(path, "r") as file_seq:
        seq = file_seq.read().replace('\n', '')

    return seq

def seq_RNA(seq: str) -> str:

    sequencia_DNA = seq.lower()
    
    sequencia_RNA = sequencia_DNA.replace('t', 'u')
    return sequencia_RNA.upper()


if __name__ == '__main__':

   seq = read_file('/home/ubuntu/Área de Trabalho/rosalind_rna.txt')
   print('Aqui está o RNA: ', seq_RNA(seq))
