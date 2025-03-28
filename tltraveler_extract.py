import pathlib

file1 = open(r'saveDataArc.txt', 'rb')
seek_point = 1668536
times_repeated = 0
while times_repeated < 21: 
    file1.seek(seek_point, 0)
    
    filename_str = "output" + str(times_repeated + 1) + ".tltraveler"
    
    with open(filename_str, 'w') as create_file:
        create_file.write("")

    output_file = open(filename_str, 'r+b')

    bytes_chunk = file1.read(687)
    output_file.write(bytes_chunk)

    file2 = open(r'FIX', 'rb')
    fix_bytes = file2.read()
    output_file.seek(687, 0)
    output_file.write(fix_bytes)
    file2.close()

    bytes_chunk_2 = file1.read(3072 - 687)

    output_file.write(bytes_chunk_2)
    output_file.close()

    seek_point += 3072
    times_repeated += 1

file1.close()
