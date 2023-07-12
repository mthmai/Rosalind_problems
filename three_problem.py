def read_file(path: str) -> str:
    with open(path, "r") as file_seq:
        seq = file_seq.read().replace('\n', '')

    return seq

def complement_DNA(seq : str) -> str:
    
