a = "assdfhhu"
print(a.split('d'))
format(42,'.2f')
round(4458.1242, ndigits=-3)
customers = ['Alice', 'Bob', 'Carl', 'Dave', 'Elena', 'Frank']
iterator = iter(customers)
print(next(iterator))
customers.extend([1, 2, 3])
lst = [8, 2, 6, 4, 3, 1]
# Filter all elements <8
small = filter(lambda x: x<8, lst)
print(list(small))
print(any([1, 2, -1]))
zip([1,2,3],[4,5,6])
a = list(zip([1,2,3],[4,5,6]))
print(a)
sorted(customers)
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)
type(df.iloc[:,-1].to_frame())
a = df.query('duration>45')
%history -g
