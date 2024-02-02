from typing import List

def read_file(path: str) -> str:
    with open(path, "r") as file_seq:
        seq = file_seq.read().replace('\n', '')

    return seq


def DNA_to_list(seq : str) -> List[str]:

    list_seq = list()
    seq = seq.upper()
    for letter in seq:
        list_seq.append(letter)

    return list_seq


def DNA_complement(list_seq: List[str]) -> str:

    list_seq_complement = list()
    for letter in list_seq:
        if letter == 'A':
            list_seq_complement.append('T')
        elif letter == 'T':
            list_seq_complement.append('A')
        elif letter == 'C':
            list_seq_complement.append('G')
        elif letter == 'G':
            list_seq_complement.append('C')
        else:
            raise ValueError(f'A letra {letter} não é nucleotídeo')
    
    seq_return = ''.join(list_seq_complement)
    return seq_return

def DNA_reverse(seq: str) -> str:
    seq_reverse = seq[::-1]
    return seq_reverse

if __name__ == '__main__':

    seq_DNA = read_file('rosalind_seq_3.txt')
    seq = DNA_to_list(seq_DNA)
    seq_complement = DNA_complement(seq)
    seq_reverse = DNA_reverse(seq_complement)
    #print(seq_complement)
    print(seq_reverse)
