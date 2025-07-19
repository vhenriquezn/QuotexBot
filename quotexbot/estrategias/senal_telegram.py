senal_recibida = None

def set_senal_externa(tipo):
    global senal_recibida
    senal_recibida = tipo.lower()

def calcular_senal(df=None):
    global senal_recibida
    if senal_recibida:
        senal = senal_recibida
        senal_recibida = None
        return senal  # 'call' o 'put'
    return None
