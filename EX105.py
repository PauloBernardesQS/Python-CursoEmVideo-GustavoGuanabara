def notas(*n, sit=False):
    resp = dict()
    resp["Total"] = len(n)
    resp["Maior"] = max(n)
    resp["Menor"] = min(n)
    resp["Media"] = sum(n)/ resp["Total"]
    if sit:
        if resp["Media"] >= 7:
            resp["Situação"] = "OTIMO"
        elif resp["Media"] == 6:
            resp["Situação"] = "OK"
        else:
            resp["Situação"] = "REPROVADO"
    return resp

r = notas(5,6,7,6,6, sit=True)
print(r)