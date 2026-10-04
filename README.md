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

## 📂 Estructura del proyecto
```
AI_Recommendation_System/
├── screenshots/
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
Creé mi cuenta en GitHub y un repositorio llamado `AI_Recommendation_System` con README, `.gitignore` para Python y licencia MIT.

![Repositorio] ![alt text](<Captura de pantalla 2026-10-03 224218.png>)

### 2. Clonado y configuración del entorno
Abrí Visual Studio Code, conecté la carpeta del proyecto con el repositorio de GitHub e instalé las librerías necesarias con:
```bash
python -m pip install numpy pandas scikit-learn
```

### 3. Generación del código con GitHub Copilot
Creé el archivo `recommendation_system.py` y usé GitHub Copilot para generar el código inicial. El código carga los datos, entrena un modelo KNN, calcula la precisión y define una función `recommend()`.
[Explica aquí qué le pediste a Copilot y si hiciste cambios al código.]

![Código con Copilot] ![alt text](<Captura de pantalla 2026-10-03 222436.png>)

### 4. Generación de datos
El código necesita un archivo `products.csv`, así que creé `generate_data.py`, que genera 100 productos de ejemplo con tres características (`feature1`, `feature2`, `feature3`) y una etiqueta (`label`).

### 5. Ejecución y resultado
Ejecuté `python recommendation_system.py`. El modelo obtuvo una precisión de **[X]%** y recomendó **[producto]** para el producto de ejemplo.

![Resultado] ![alt text](<Captura de pantalla 2026-10-03 222436-1.png>)

### 6. Commit y push
Subí los cambios a GitHub con:
```bash
git add .
git commit -m "Add recommendation system example"
git push -u origin main
```

## 🚀 Cómo ejecutarlo
```bash
git clone https://github.com/TU_USUARIO/AI_Recommendation_System.git
cd AI_Recommendation_System
pip install -r requirements.txt
python generate_data.py
python recommendation_system.py
```

## 💡 Aprendizajes
[Escribe 2 o 3 líneas: qué te pareció Copilot, en qué te ayudó, qué errores tuviste que resolver y qué aprendiste sobre IA.]

## 👤 Autor
**[Tu nombre completo]** · [GitHub](https://github.com/TU_USUARIO)