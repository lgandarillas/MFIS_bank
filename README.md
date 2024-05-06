# Sistema de Ayuda a la Decisión para Préstamos Personales
Este proyecto implica la creación de un Sistema de Ayuda a la Decisión para evaluar solicitudes de préstamos personales. Se utiliza un Sistema de Inferencia Borroso de Mamdani (MFIS) implementado en Python. El código fuente proporcionado incluye clases para representar conjuntos borrosos, reglas de inferencia y la aplicación del sistema.

1. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)
2. [Descripción del Código](#descripción-del-código)
   - [Fase 1: Definición de Variables](#fase-1-definición-de-variables)
   - [Fase 2: Definición de Reglas de Inferencia](#fase-2-definición-de-reglas-de-inferencia)
   - [Funcionamiento del Sistema de Inferencia](#funcionamiento-del-sistema-de-inferencia)
3. [Desarrollado por](#desarrollado-por)


## Cómo ejecutar el proyecto
#### Clonar el repositorio
```bash
git clone git@github.com:lgandarillas/MFIS_banco.git && cd MFIS_banco
```
#### Setup inicial
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
```
#### Ejecutar el Código
```bash
python3 main.py
```
## Descripción del Código
El código proporcionado consta de varias clases que representan componentes clave del sistema de inferencia borrosa:
- **FuzzySetsDict**: Representa un diccionario de conjuntos borrosos.
- **FuzzySet**: Representa un conjunto borroso individual.
- **RuleList**: Representa una lista de reglas de inferencia.
- **Rule**: Representa una regla de inferencia individual.
- **Application**: Representa una solicitud de préstamo individual.

El archivo **main.py** contiene la lógica principal del programa, que implica leer archivos de entrada, procesar datos y escribir resultados en un archivo de salida. Se utilizan funciones proporcionadas en los archivos MFIS_Read_Functions.py y MFIS_Classes.py para leer archivos de texto y manejar objetos de clases respectivamente.

### Fase 1: Definición de Variables
El sistema utiliza varias variables para evaluar la solicitud de préstamo, como el nivel de ingresos, bienes en posesión, estabilidad laboral, entre otros. Cada variable se define mediante conjuntos borrosos con funciones de pertenencia trapezoidales o triangulares.

### Fase 2: Definición de Reglas de Inferencia
Expertos del banco proporcionan reglas de inferencia en el archivo Rules.txt, donde cada regla especifica el antecedente y el consecuente.

### Funcionamiento del Sistema de Inferencia
Una vez construido y aceptado el sistema, se aplica diariamente a solicitudes de préstamo en el archivo Applications.txt, generando un archivo de resultados Results.txt con los niveles de riesgo correspondientes.

## Desarrollado por:
- Iván Aranguren Ripoll: **100474767@alumnos.uc3m.es**
- Carlos Bravo Garrán: **100474964@alumnos.uc3m.es**
- Luis Gandarillas Fernández: **100454201@alumnos.uc3m.es**
