from CBD import conectar
import mysql.connector
from tkinter import messagebox

def atualizarCadastro(cs,dt,pr,di,dat, qp,ti,ob):
    conexao, cursor = conectar()
    try:
        sql = f"""UPDATE  tb_Xetario
                SET  des_tar='{dt}', pes_res='{pr}', data_ini='{di}', data_ter='{dat}', quanti_pro='{qp}', 
        tip='{ti}', obs='{ob}' WHERE cod_ser='{cs}'
              """
        cursor.execute(sql)
        conexao.commit()
        messagebox.showinfo("Atualizar",
            "Cadastro atualizado!")
        return True
    except mysql.connector.Error as falha:
        messagebox.showerror("Falha",
            "Falha ao atualizar"+str(falha))
        return False
    finally:
        conexao.close()
        cursor.close()