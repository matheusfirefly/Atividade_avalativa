from CBD import conectar
import mysql.connector
from tkinter import messagebox

def inserir(dt,pr,di,dat, qp,ti,ob):
    conexao, cursor = conectar()
    try:
        sql = f"""INSERT INTO tb_Xetario
                ( des_tar, pes_res, data_ini, data_ter, quanti_pro, tip, obs)
                VALUES
                ('{dt}','{pr}','{di}','{dat}','{qp}','{ti}','{ob}')
                """

        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Cadastrado","Cadastrado com sucesso!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha", "Falha ao cadastrar: "+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()