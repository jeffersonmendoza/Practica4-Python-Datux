from configuracion.app import *
import pandas as pd

# crear un reporte diferente
def GenerateReportVentas(app:App):
    conn=app.bd.getConection()
    query="""
        SELECT 
            p.pais,
            SUM(v.quantity) AS total_vendido
        FROM 
            VENTAS v
        JOIN 
            POSTALCODE p ON v.postal_code = p.code
        GROUP BY 
            p.pais
        ORDER BY 
            total_vendido DESC
        LIMIT 1;
    """
    df=pd.read_sql_query(query,conn)
    fecha="08-02"
    path=f"/workspaces/Practica4-Python-Datux/proyecto/archivos/data-Jefferson.csv"
    df.to_csv(path)
    sendMail(app,path)

def sendMail(app:App,data):
    # cambiar el asunto 
    app.mail.send_email('from@example.com','Reportemaxi','Reporteventa',data)