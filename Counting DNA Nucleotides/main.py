Nucleotids = ["A" ,"T", "G", "C"]

fasta1 = "AAGCAAGCGAGAAGTGCAAACTTTTAATGGATCAGGAATCGACCAGCAATAGTCGAACCGACAGCGCCAATGTCCGCGATTTGGTGATGATAGGCCGCGTACACTGTATACCTTGTACTATATTTGGACCCCCAAGGATTTCGTACATGAAGCCCCAAGTATGACGTCGAGCACCTATAGTACCTGACACTTGACACCGGGAGAAGCTGCTCAAACGCGCCTTATACCAATTTCGGTCGGCTCCGCCATGGCAGTTCAGTCCATGGTCTTAGGAGAGCCAATCCTAGACGTTTCAACCCCTATGTAAGCTGAGATATTTAGTCGGTTACATTAGGTTCGCCCTCAGCTTCTCCCTCCCATTTATGACTAGCGCACAACTTCTCATCCTTCTGCTAAGTGACCGGGTCCCCTTCTGTTGAAGCGGAACGGCACTTCGGGGAAAACAGCTTTTGCAGGGCTGGTTTGGCACGTTAGCGATGAGCCGCAAGAAGGTGAGAGACGTCACTTCACGGGAATGACAAAATACAAAACCCAACGAGCGTGGACTATGAAGCTCAATTCTCTATTGCTACAAGGTGTAGTGATGACTGCAAGATTTCCGAACATGGTTTGATGCGTCGCACATACTTTCAATCCAGTGACAGTCGGCTCCTAGGGGGGCCCCAGTCCGTCCGTACACGTGATTCATGCCGGATTAACTACAAGAGCTACACAAAACTCGACTGCCACTTGCAGGGGGCCCTTGCAAACAGGTTCGAAGGAGGTCGATCGCCCAAAAGACAGTGATTATCCCGTTGGTCCCCGAATCCTCTACTTTGAATGCCTCTATTTTGTCTCGAGATAGTTTGGAAGGATGCGGATATGGATGTTGGTGCCCTTTTCTATAGACTCCGCCAACCTGCA"

fasta = fasta1.upper()

print(fasta.count("A"),fasta.count("C"),fasta.count("G"),fasta.count("T"))


#20 12 17 21
