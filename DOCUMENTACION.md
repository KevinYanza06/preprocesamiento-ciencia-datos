#  Documentación del Proyecto: Preprocesamiento de Datos en Ciencia de Datos

##  Introducción
Este proyecto aplica el control de versiones con Git y GitHub para un entorno de Ciencia de Datos.  
Se implementó un script en Python que realiza un preprocesamiento completo de datos usando **Pandas**, incluyendo:
- Eliminación de duplicados  
- Manejo de valores nulos  
- Codificación de variables categóricas  
- Normalización de datos numéricos  

##  Comandos Git usados
- `git init` → crea un repositorio local  
- `git add .` → agrega archivos  
- `git commit -m "mensaje"` → guarda cambios localmente  
- `git push origin main` → sube los cambios a GitHub  
- `git pull origin main` → descarga los cambios desde GitHub  
- `git branch` y `git checkout` → crean y cambian de rama  
- `git merge` → fusiona ramas  

## Automatización (GitHub Actions)
Se configuró un workflow que ejecuta automáticamente el script en cada actualización de la rama `main`.

```yaml
name: Python CI
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: "3.9"
      - run: pip install pandas scikit-learn
      - run: python preprocesamiento.py
