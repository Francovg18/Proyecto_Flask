def render_recordatorio_list(recordatorios):
    # Representa una lista de recordatorios como una lista de diccionarios
    return [
        {
            "ID_R": recordatorio.ID_R,
            "ID_C": recordatorio.ID_C,
            "TipoRecordatorio": recordatorio.TipoRecordatorio,
            "FechaHoraEnvío": recordatorio.FechaHoraEnvío.strftime("%Y-%m-%d %H:%M:%S"),
            "Estado": recordatorio.Estado,
        }
        for recordatorio in recordatorios
    ]


def render_recordatorio_detail(recordatorio):
    # Representa los detalles de un recordatorio como un diccionario
    return {
        "ID_R": recordatorio.ID_R,
        "ID_C": recordatorio.ID_C,
        "TipoRecordatorio": recordatorio.TipoRecordatorio,
        "FechaHoraEnvío": recordatorio.FechaHoraEnvío.strftime("%Y-%m-%d %H:%M:%S"),
        "Estado": recordatorio.Estado,
    }
