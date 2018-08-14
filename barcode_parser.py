import os
os.chdir('/Users/whitneyware/IER_Sleeve/sleeve_seqs')

barcodeLen = 17

with open('barcodes.fastq', 'r') as bc:
    with open("corrected_barcodes.fastq", 'w') as out:
        for line in bc.readlines():
            line = line.rstrip()
            if line.startswith("@" or "+" or "'"):
                print(line, file=out)
            else:
                line = line[:barcodeLen]
                print(line, file=out)

bc.close()
out.close()
