#from django.shortcuts import render
import pymssql
#201.182.222.33:3390

con = pymssql.connect(host = '192.168.20.250',
                      port = '1433',
                      user = 'sa',
                      password = 'R2018c',
                      database = 'Marca_Evolution'
     )
# TESTE PALLET 8707R8021
cursor = con.cursor()

buscar = raw_input("Digito:")

cursor.execute("""SELECT [Codigo]
      ,[Dt_Hr_Digitacao]
      ,[Nr_Pallet]
      ,[Classe]
      ,[Pes2]
      ,[Pecas]
      ,[Peso_Pallet]
      ,[Couros_Pes2]
      ,[Couros_Pesos]
      ,[Cd_Fornecedor]
  FROM [Marca_Evolution].[dbo].[Estoque_Expedicao] WHERE Nr_Pallet = %s""",(buscar))

for i in cursor:
  print i
