import psycopg2

db_host = '127.0.0.1'
db_name = 'santa_luzia'
db_port = '5432'
db_user = 'postgres'
db_password = '20101997'

connect = psycopg2.connect(host=db_host, dbname=db_name, port = db_port, user=db_user, password=db_password)

cur = connect.cursor()

nome =input("Nome:")
data =input("Data de Nascimento: ")

cur.execute("insert into comunidade.tbcomunitarios(nome, dn)values ('{}','{}')".format(nome,data))
print('\nnome inserido com sucesso!')

#sql = "SELECT id, cpf, upper(nome), tel, cep, num_casa, ponto_referencia FROM cadastro.cliente order by nome"
#cur.execute(sql)
#result=cur.fetchall()
#for row in result:
    #print(row[2])
cur.close()
connect.commit()
connect.close()