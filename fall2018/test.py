temp = 'alejandro, britney, christina, dennis, emily'
print(
    "@gmail.com; ".join(map(lambda s: s.strip(), temp.split(',')))+"@gmail.com"
)