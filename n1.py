import pandas as pd

# Leer CSV unificado
df = pd.read_csv("Consolidado.csv", encoding="utf-8-sig")

# Crear la columna Nom.estab. = nombre + " - " + RBD
df["Nom.estab."] = df["Nom.estab."].astype(str).str.strip() + " - " + df["RBD"].astype(str).str.strip()

# Crear columna tipo_establecimiento según si RBD contiene "-"
df["tipo_establecimiento"] = df["RBD"].apply(lambda x: "Colegio" if "-" in str(x) else "Junji")

# Guardar CSV final
df.to_csv("Consolidado_normalizado.csv", index=False, encoding="utf-8-sig")

print("✅ CSV final generado con Nom.estab. unificado y tipo_establecimiento")
