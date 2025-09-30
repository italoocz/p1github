#if, else

#>
#>=
#<
#<=
#==  <----- Igualdade
#!=  <----- Diferença

# else:  -------> se não..

print('Hora de comprar pão')
chuva = input('Está chovendo? (y/n): ')

if chuva == 'y' or chuva == 'yes' or chuva == 's' or chuva == 'sim':
    print("Como está chovendo, não vou à padaria")

else:
    print('Como não está chovendo, vou á padaria')
