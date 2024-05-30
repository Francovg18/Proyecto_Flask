def render_paciente_list(pacientes):
    # Representa una lista de pacientes como una lista de diccionarios
    return [
        {
            "ID_P": paciente.ID_P,
            "Nombre": paciente.Nombre,
            "Email": paciente.Email,
            "Teléfono": paciente.Teléfono,
            "FechaNacimiento": paciente.FechaNacimiento.strftime("%Y-%m-%d"),
            "Género": paciente.Género,
            "Dirección": paciente.Dirección,
        }
        for paciente in pacientes
    ]


def render_paciente_detail(paciente):
    # Representa los detalles de un paciente como un diccionario
    return {
        "ID_P": paciente.ID_P,
        "Nombre": paciente.Nombre,
        "Email": paciente.Email,
        "Teléfono": paciente.Teléfono,
        "FechaNacimiento": paciente.FechaNacimiento.strftime("%Y-%m-%d"),
        "Género": paciente.Género,
        "Dirección": paciente.Dirección,
    }
