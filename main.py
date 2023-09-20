import pandas as pd
import requests

from logger import logging


def main():
    dataframe = pd.read_excel(
        "ResolucionesSENAVE.xlsx", sheet_name=None
    )
    hoja1 = dataframe.get("Hoja1")
    limpios = {
        "res_id": [], "res_years": [], "res_name": [], "res_link": []
    }
    errores = {
        "res_id": [], "res_years": [], "res_name": [], "res_link": []
    }

    for index, serie in hoja1.iterrows():
        id, year, t, u = serie
        title = str(t).strip() if t else ""
        url = str(u).strip() if u else ""
        if (
            title and len(title) != 0 and
            url and len(url) != 0 and url.lower() != 'null'
        ):
            try:
                resp = requests.get(url)
                print(f"content = {resp.content}")
                if resp.status_code == 200 and resp.content:
                    limpios["res_id"].append(id)
                    limpios["res_years"].append(year)
                    limpios["res_name"].append(title)
                    limpios["res_link"].append(url)
            except Exception:
                errores["res_id"].append(id)
                errores["res_years"].append(year)
                errores["res_name"].append(title)
                errores["res_link"].append(url)
        else:
            errores["res_id"].append(id)
            errores["res_years"].append(year)
            errores["res_name"].append(title)
            errores["res_link"].append(url)
        logging.info(f"Recorriendo {index}")

    data = {
        "limpios": pd.DataFrame(
            limpios, columns=["res_id", "res_years", "res_name", "res_link"]
        ),
        "errores": pd.DataFrame(
            errores, columns=["res_id", "res_years", "res_name", "res_link"]
        ),
    }

    with pd.ExcelWriter("Modificado.xlsx") as writer:
        for sheet_name, df in data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)


if __name__ == "__main__":
    main()
