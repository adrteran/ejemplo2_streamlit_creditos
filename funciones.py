tasa=0.02

def get_cuota(monto,plazo,tasa):
    cuota = monto * (tasa*(1+tasa)**plazo)/((1+tasa)**plazo-1)
    return cuota

def get_tabla(monto,plazo,tasa):
    import pandas as pd
    cuota = get_cuota(monto,plazo,tasa)
    l_deuda = []
    l_amort = []
    l_inter = []
    l_saldo = []
    for t in range(plazo):
        inter = monto * tasa
        l_inter.append(round(inter,2))
        monto = monto * (1+tasa)
        l_deuda.append(round(monto,2))
        amorti = cuota - inter
        l_amort.append(round(amorti,2))
        monto = monto - cuota
        l_saldo.append(round(monto,2))
    tabla = pd.DataFrame({'Saldo_ini':l_deuda,'Amort':l_amort,'Intereses':l_inter,'Saldo_fin':l_saldo})
    return tabla
