import pandas as pd

from logger import logging


def cambiar_url():
    dataframe = pd.read_excel("Modificado.xlsx", sheet_name=None)
    hoja1 = dataframe.get("limpios")
    cambiado = {"res_id": [], "res_years": [], "res_name": [], "res_link": []}

    for index, serie in hoja1.iterrows():
        id, year, t, u = serie
        title = str(t).strip() if t else ""
        url = str(u).strip() if u else ""
        if (
            title
            and len(title) != 0
            and url
            and len(url) != 0
            and url.lower() != "null"
        ):
            url = url.replace("web.senave.gov.py", "192.168.10.61")
            cambiado["res_id"].append(id)
            cambiado["res_years"].append(year)
            cambiado["res_name"].append(title)
            cambiado["res_link"].append(url)
        logging.info(f"Recorriendo {index}")
    data = {
        "cambiados": pd.DataFrame(
            cambiado, columns=["res_id", "res_years", "res_name", "res_link"]
        ),
    }

    with pd.ExcelWriter("Cambiado.xlsx") as writer:
        for sheet_name, df in data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)


if __name__ == "__main__":
    cambiar_url()
