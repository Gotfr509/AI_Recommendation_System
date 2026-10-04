# 🤖 AI_Recommendation_System

Sistema de recomendación de productos con Python, scikit-learn y GitHub Copilot.

Proyecto desarrollado para explorar las tendencias emergentes en inteligencia artificial usando **GitHub Copilot** como herramienta práctica de desarrollo.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-orange?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green)

## 🛠️ Tecnologías
- Python
- pandas y numpy
- scikit-learn (`KNeighborsClassifier`)
- GitHub Copilot
- Visual Studio Code
- Git y GitHub

## 📂 Estructura del proyecto
```
AI_Recommendation_System/
├── screenshots/
│   ├── 01-repositorio.png
│   ├── 02-copilot-codigo.png
│   └── 03-resultado.png
├── generate_data.py
├── products.csv
├── recommendation_system.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## 📝 Proceso paso a paso

### 1. Creación del repositorio
Creé mi cuenta de GitHub y un repositorio llamado `AI_Recommendation_System`, inicializado con un archivo README, un `.gitignore` para Python y la licencia MIT.

![Repositorio](screenshots/01-repositorio.png)

### 2. Configuración del entorno
Abrí Visual Studio Code, conecté la carpeta del proyecto con el repositorio de GitHub e instalé las librerías necesarias con:
```bash
python -m pip install numpy pandas scikit-learn
```

### 3. Generación del código con GitHub Copilot
Creé el archivo `recommendation_system.py` y usé GitHub Copilot para generar el código inicial. Le pedí un sistema de recomendación de productos con scikit-learn que cargara un archivo `products.csv`, entrenara un modelo `KNeighborsClassifier`, calculara la precisión y tuviera una función `recommend()`. El código resultante carga los datos, separa entrenamiento y prueba (80/20), entrena el modelo con 5 vecinos, evalúa la precisión y recomienda un producto a partir de sus características.

![Código con Copilot](screenshots/02-copilot-codigo.png)

### 4. Generación de datos
El código necesita un archivo `products.csv`, así que creé `generate_data.py`, que genera 100 productos de ejemplo con tres características numéricas (`feature1`, `feature2`, `feature3`) y una etiqueta (`label`) que puede ser `Producto_A` o `Producto_B`.

### 5. Ejecución y resultado
Ejecuté `python recommendation_system.py`. El modelo obtuvo una precisión de **95 %** y recomendó **Producto_B** para el producto de ejemplo `[1.0, 2.0, 3.0]`.

![Resultado](screenshots/03-resultado.png)

### 6. Commit y push
Subí los cambios a GitHub con:
```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

## 🚀 Cómo ejecutarlo
```bash
git clone https://github.com/WidjyMarcellus/AI_Recommendation_System.git
cd AI_Recommendation_System
pip install -r requirements.txt
python generate_data.py
python recommendation_system.py
```

## 💡 Aprendizajes
Con este proyecto aprendí a crear y configurar un repositorio en GitHub, a trabajar con Git desde la terminal de Visual Studio Code y a usar GitHub Copilot para generar código a partir de descripciones en lenguaje natural. También resolví errores reales, como la falta de librerías (`ModuleNotFoundError`) y de un archivo de datos (`FileNotFoundError`). Entendí que Copilot acelera el trabajo, pero es necesario revisar y comprender el código que genera.

## 👤 Autor
**[Tu nombre completo]** · [GitHub](https://github.com/WidjyMarcellus)