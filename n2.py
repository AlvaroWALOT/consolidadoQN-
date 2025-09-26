import pandas as pd

# Leer el CSV final que ya tienes
df = pd.read_csv("output_final_columnas.csv", encoding="utf-8-sig")


# Eliminar duplicados (manteniendo la primera ocurrencia)
df_final = df.drop_duplicates()

# Guardar CSV final limpio
df_final.to_csv("output_final_limpio.csv", index=False, encoding="utf-8-sig")

print("✅ CSV final generado con columnas seleccionadas y duplicados eliminados")
