input_path = "./1.Input.txt"

f = open(input_path, "r")
if f.mode == "r":
    long_text = f.read()
f.close()

print(len(long_text))

short_text = "1 2 2 6 7   3 5 6 9   3 16 19"
list_nums = short_text.split()
#print(short_text)

list_nums = long_text.split()

actual_lenght = 0
max_length = 0

for i in list_nums:

  i = int(i)
  #print(i)
  i_is_even = (i % 2 == 0)

  if actual_lenght != 0 and ((i < prev) or not(i_is_even ^ p_is_even)):
    #print("Reset: ", prev, i)
    #print (p_is_even, i_is_even, i_is_even ^ p_is_even)
    
    
    if (max_length < actual_lenght):
      max_length = actual_lenght
    actual_lenght = 1
  
  else:
    #print(i, prev, actual_lenght)
    p_is_even = i_is_even
    actual_lenght += 1
    
  #print(i, actual_lenght)
  prev = i
  

if (max_length < actual_lenght):
  max_length = actual_lenght

print()
print("Max: ", max_length)