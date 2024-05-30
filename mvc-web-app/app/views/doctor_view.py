def render_doctor_list(doctores):
    # Representa una lista de doctores como una lista de diccionarios
    return [
        {
            "ID_D": doctor.ID_D,
            "Nombre": doctor.Nombre,
            "Especialidad": doctor.Especialidad,
            "Email": doctor.Email,
            "Teléfono": doctor.Teléfono,
            "HorariosConsulta": doctor.HorariosConsulta,
        }
        for doctor in doctores
    ]


def render_doctor_detail(doctor):
    # Representa los detalles de un doctor como un diccionario
    return {
        "ID_D": doctor.ID_D,
        "Nombre": doctor.Nombre,
        "Especialidad": doctor.Especialidad,
        "Email": doctor.Email,
        "Teléfono": doctor.Teléfono,
        "HorariosConsulta": doctor.HorariosConsulta,
    }
