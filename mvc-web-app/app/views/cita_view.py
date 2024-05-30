def render_cita_list(citas):
    # Representa una lista de citas como una lista de diccionarios
    return [
        {
            "ID_C": cita.ID_C,
            "ID_P": cita.ID_P,
            "ID_D": cita.ID_D,
            "FechaHora": cita.FechaHora.strftime("%Y-%m-%d %H:%M:%S"),
            "Estado": cita.Estado,
            "Motivo": cita.Motivo,
        }
        for cita in citas
    ]


def render_cita_detail(cita):
    # Representa los detalles de una cita como un diccionario
    return {
        "ID_C": cita.ID_C,
        "ID_P": cita.ID_P,
        "ID_D": cita.ID_D,
        "FechaHora": cita.FechaHora.strftime("%Y-%m-%d %H:%M:%S"),
        "Estado": cita.Estado,
        "Motivo": cita.Motivo,
    }
