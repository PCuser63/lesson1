threshold = 11.0  

filtered_freqs = []  


with open('freqs.txt', 'r') as file:
    for line in file:
        frequencies = line.strip().split(';')  
        for freq in frequencies:
            if float(freq) >= threshold:  
                filtered_freqs.append(freq)


output_string = ' '.join(filtered_freqs)
print(output_string)


