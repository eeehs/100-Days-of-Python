# π¨ Don't change the code below π
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# π¨ Don't change the code above π


#Write your code below this row π

# lenλ§κ³  μ΄ λ¦¬μ€νΈ κ°―μ μΈλ λ°©λ²

student_len = 0
student_sum = 0


for A in student_heights:
    student_sum = student_sum + A 
    student_len = student_len + 1

Average_Height = round(student_sum / student_len)

print(Average_Height)




# sum λ§κ³  μ΄ ν© λνλ λ°©λ²