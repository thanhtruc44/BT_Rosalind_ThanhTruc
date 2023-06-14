import argparse
import logging
from Bio import SeqIO

def construct_de_bruijn_graph(reads, k):
    graph = {}
    for read in reads:
        for i in range(len(read) - k + 1):
            kmer = read[i:i+k]
            if kmer not in graph:
                graph[kmer] = set()
            if i+k < len(read):
                next_kmer = read[i+1:i+k+1]
                graph[kmer].add(next_kmer)
    return graph

def find_eulerian_path(graph):
    path = []
    stack = []
    node = list(graph.keys())[0]
    while True:
        if len(graph[node]) > 0:
            stack.append(node)
            next_node = graph[node].pop()
            node = next_node
        else:
            path.append(node)
            if len(stack) == 0:
                break
            node = stack.pop()
    path.reverse()
    return path

def reconstruct_sequence(path, k):
    sequence = path[0]
    for i in range(1, len(path)):
        sequence += path[i][k-1:]
    return sequence

def de_bruijn_assembly(reads, k):
    graph = construct_de_bruijn_graph(reads, k)
    path = find_eulerian_path(graph)
    sequence = reconstruct_sequence(path, k-1)
    return sequence

def main(args):
    # Set up logging
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    
    logging.info("Reading sequences from file: %s", args.fasta_file)
    # Read sequences from the input FASTA file
    reads = []
    try:
        with open(args.fasta_file, "r") as file:
            for record in SeqIO.parse(file, "fasta"):
                reads.append(str(record.seq))
        logging.info("Read %d sequences from file", len(reads))
    except Exception as e:
        logging.error("Error reading sequences from file: %s", str(e))
        return

    # Perform de Bruijn assembly
    assembled_sequence = de_bruijn_assembly(reads, args.k)
    
    logging.info("DNA sequence assembly completed")
    print(f"Assembled DNA sequence: {assembled_sequence}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="DNA sequence assembly using overlap")
    parser.add_argument("fasta_file", type=str, help="Path to the input FASTA file")
    parser.add_argument("-k", type=int, default=3, help="K-mer length (default: 3)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed log")
    args = parser.parse_args()
    
main(args)
