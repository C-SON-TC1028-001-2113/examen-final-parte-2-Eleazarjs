def imatriz():
    lista = []
    fila = int(input())
    columna = int(input())
    if fila > 0 and columna > 0: 
        for i in range(fila):
            lista.append([])
            for j in range(columna):
                n = int(input())
                lista[i].append(n)
    else: 
        print('Error')
    return lista

def main():
  matriz = imatriz()
  lista_c = []
  if len(matriz) > 0:
        for i in range(len(matriz[0])):
            count = 0
            for j in range(len(matriz)):
                count += matriz[j][i] 
            lista_c.append(count)
        print(lista_c)

if __name__=='__main__':
    main()
