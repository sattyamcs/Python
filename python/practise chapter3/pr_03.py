# Ques.3 write a program to detect double spaces in a string and replace it with single space

st= "i am from farrukhabad. I am intrested in  learning python."
doubleSpaces= st.find("  ")
print(doubleSpaces)


st= st.replace("  "," ")
print(st)