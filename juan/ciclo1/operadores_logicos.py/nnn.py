dic = {
    "1": {"nombre": "juan", "sexo": "M", "grado": 1, "notas": [2.0], "promedio": 2.0},
    "2": {"nombre": "carlos", "sexo": "M", "grado": 1, "notas": [2.0, 4.0], "promedio": 3.0},
    "3": {"nombre": "diana", "sexo": "F", "grado": 1, "notas": [0.2], "promedio": 0.2},
    "4": {"nombre": "sandra", "sexo": "F", "grado": 1, "notas": [1.0], "promedio": 1.0},
    "5": {"nombre": "carolina", "sexo": "F", "grado": 1, "notas": [1.0], "promedio": 1.0},
    "6": {"nombre": "santiago", "sexo": "M", "grado": 1, "notas": [1.0], "promedio": 1.0},
    "7": {"nombre": "diego", "sexo": "M", "grado": 1, "notas": [3.0], "promedio": 3.0},
    "8": {"nombre": "sebas", "sexo": "M", "grado": 1, "notas": [1.0], "promedio": 1.0},
    "9": {"nombre": "dario", "sexo": "M", "grado": 1, "notas": [2.0], "promedio": 2.0},
    "10": {"nombre": "angel", "sexo": "M", "grado": 1, "notas": [2.0, 3.0, 5.0], "promedio": 3.3333333333333335}
}

dic_ordenado = dict(sorted(dic.items(), key=lambda x: x[1]['promedio'], reverse=True))

print(dic_ordenado)