otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5
crudo_promedio = 5
crudo_dalto = 3.5



diferencia_curso_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_curso_max = 100 - (dalto_curso / otros_cursos_max * 100)
diferencia_curso_prom = 100 - (dalto_curso / otros_cursos_prom * 100)





print(f"la diferencia de procentajes es del: {diferencia_curso_min}%")
print(f"la diferencia de procentajes es del: {round(diferencia_curso_max, 1)}%")
print(f"la diferencia de procentajes es del: {diferencia_curso_prom}%")

