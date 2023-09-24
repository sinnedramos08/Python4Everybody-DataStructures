# Use the file name mbox-short.txt as the file name

fh = open(r"C:\Users\denni\OneDrive\Desktop\Coding\Python\Coursera\Python4Everybody-DataStructures\Files\mbox.txt")
float_add=0
counter=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    index_zero=line.find("0")
    float_number=float(line[index_zero:])
    float_add=float_number+float_add
    counter=counter+1

float_ave=float_add/counter
print(f"Average spam confidence: {float_ave}")


