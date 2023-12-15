def hamming_distance(s, t):
    count = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1
    return count

s = "GTACAGTGCCACTACCTCCAGAATCCTTTCTCGGAGGGAGTATCAACCCTAGGTATCGCAACCGAGCGGTGGCTCAGTTTGTGCACTTGGCCTATTGACCTCATTCGCTTGGGATCTCAACAAGGAAGTCGATGGCAAATCCGGAGTATCAAGTCAGGAATAGATCGCCCTTACTGCCTTGATGAGGATGTGCCAGATAAGCCCCCACTCGCAAGAGACTCTATGTGGATGATTGTAGTCTCTCAAATACCCATCTCGACGTCAGTGATACAGAGATCATCTTCAGCATTGTGTCGTTCTACTGCTGCGGACGATGCAGATCTAGCCCCGCCCTAGGAGACGTTAACTAAATCGCAGATGTGAAGCGTAAGTGCCCAGTCAGGCTCTGGTTACCTCAGTTCACTAATCGCTCGATCCGTAGGTTGGAACAAATTCGTACCATCTCGGACCGCGCCAGAGTTTCGCGTGCCGTTGGGCTGCATCCTACGTAAGAGCGTACAATTTTCGAGGCCAATTGAGGGATTTCGGGGTTCGTGCTAGCCATTCTCGTCATAATACGGATTGGTACACGGTCGTACTTGGCAATGCTCTTCTAAACGCAGATGTTACCCTTGTTGGGTCGCCATCCGGTTAGTCATTCAGAGCACAGGGGAAACTAAGCTTATAGGAGGGTTAGGGACCGGAAGTGTTTTACTCGATGTAGCTCGTATGAGCTCAAACTCGCTATACTGTGCTTTTGAAATGATAAAAGAGTAGAAATCTTGGCCACGAATCCCAAGCCATTCGTCCAGTACGACCCTCTTGAACCGTAAGAGAGGCTTTTTATGGATCGGCTACCCCACATGAAACCGCAGACAGCTTATCATTTATAAACGGCACCCTGCCTCCCTAGGCCCGGGAGGTTGTTAACAAGGCGACATAGGCGCATTATAAAAATATTGTCGCGCGATTTC"
t = "GTACAGCCTCACTACCCCGAGTAACAGTTATCGGACTGTGGCTAAGTAATGGGTTTATCGGCCGAGCGGTGGATCTCCTGCTGCACTTCGAGCCTGAACCGCATCCCCTGTGGACGTCGTTTACCAACTCGAAGACAGCTTGTTAATCTCAAGTGAACAATGCACCCGGCTTTCCGCCTAGAGGGGGATGTGCCGCATGAGGGGCCTTAGGCAAGGGGGTATTCGGTTACGATTTTGGTTGTTCAACTCGCTAACAGTACTGAAGTTTACCAGAAGTTAGCTTACGCTTGGGTCCGTTATAGACCCCCAAGTGCGCCACCGCTCTCTGCGGCCTGGGAGTCATGAACTAGTGAATAGATGAGAAGTGTACCCGCCCCACCTCACTAAGCTTACCTGGGATGACGTCGGGCGCGATACATCGGTTGGCTTATAGACGGACCGTCGCGGAAAGTGCTCGGAGGCCCCCTTAAAACTGGCGTTAAATATGGTAGCACCGTCAACTCTTGCTGTGCGTTTAAGGGTTTAAGAGCTTCCTTCTCGCAAATGGTCTCGCAAGAAGTGGTTTTACAGGTCACTAGTTGGTAATGTTCCTGCGAACGCAGACTCACCAAGGGATTGGACGTCATCCGCTGGGGCATTGTGGCGTCAGGTGAGTCTTAGCTTATCTGATACATTCGGGACTGATGCCTTTTAAGAGTCGTTGCTAGTGGGTCCTCAAACACGACTTAAGGCACTATCCACGTTATAAATCCAAACTATAATTGATCGGGATTCCCTGGCCGGACCTCCTTTATATCCCTGTGCCACCGTCAGGAACACGGGTCCAAGCGCGTCTCACGTCTTTAATATTGGACATTATTAACTATGTATAAGCGGCATGCTCTCGTCGCGGGCACCCGCGCTGGAGGACCCGTTACAATCGCCCTACGACTATTATAATATCGCCCGGATTC"

distance = hamming_distance(s, t)
print(distance)
