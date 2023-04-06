# Product manager - Data science challenge manager

https://nuwe.io/dev/train/hubs/nuwe/nuwe-open-positions/data-science-challenge-manager

Train > Nuwe > Nuwe open positions > **Data science challenge manager**

- **From**: Tuesday, March 14, 2023 at 9:00 AM
- **To**: Thursday, April 13, 2023 at 11:59 AM
- **Category**: Data Science
- **Level**: Junior
- **Suggested stack**: Python

## ➡️ Contexto:

Somos un banco que dispone de una base de datos con una gran cantidad de información sobre nuestros clientes. Nuestro objetivo es ayudar a los analistas a predecir la tasa de abandono de estos clientes para así poder reducirla. La base de datos incluye información demográfica como la edad, el sexo, el estado civil y la categoría de ingresos. También contiene información sobre el tipo de tarjeta, el número de meses en cartera y los periodos inactivos. Además, dispone de datos clave sobre el comportamiento de gasto de los clientes que se acercan a su decisión de cancelación. Entre esta última información hay el saldo total renovable, el límite de crédito, la tasa media de apertura a la compra y métricas analizables como el importe total del cambio del cuarto trimestre al primero o el índice medio de utilización.

Frente a este conjunto de datos podemos capturar información actualizada que puede determinar la estabilidad de la cuenta a largo plazo o su salida inminente.

## 📄 Dataset:

- CLIENTNUM: Identificador único para cada cliente. (Integer)
- Attrition_Flag: Indicador de si el cliente ha abandonado el banco o se queda (Boolean)
  - Attrited Customer -> 0
  - Existing Customer -> 1
- Customer_Age: Edad del cliente. (Integer)
- Gender: Sexo del cliente. (String)
- Dependent_count: Número de personas a cargo que tiene el cliente. (Integer)
- Education_Level: Nivel educativo del cliente. (String)
- Marital_Status: Marital status of customer. (String)
- Income_Category: Categoría de ingresos del cliente. (String)
- Card_Category: Tipo de tarjeta del cliente. (String)
- Months_on_book: El tiempo que el cliente ha estado en los libros. (Integer)
- Total_Relationship_Count: Número total de relaciones que tiene el cliente con el proveedor de la tarjeta de crédito. (Integer)
- Months_Inactive_12_mon: Número de meses que el cliente ha estado inactivo en los últimos doce meses.(Integer)
- Contacts_Count_12_mon: Número de contactos que ha tenido el cliente en los últimos doce meses. (Integer)
- Credit_Limit: Límite de crédito del cliente. (Integer)
- Total_Revolving_Bal: Saldo renovable total del cliente. (Integer)
- Avg_Open_To_Buy: Ratio medio de apertura a la compra del cliente. (Integer)
- Total_Amt_Chng_Q4_Q1: Importe total cambiado del trimestre 4 al trimestre 1. (Integer)
- Total_Trans_Amt: Importe total de la transacción. (Integer)
- Total_Trans_Ct: Recuento total de transacciones. (Integer)
- Total_Ct_Chng_Q4_Q1: Recuento total cambiado del trimestre 4 al trimestre 1. (Integer)
- Avg_Utilization_Ratio: Ratio de utilización media del cliente. (Integer)

Para este desafío, tendrás que predecir el **Attrition_Flag**.

Hay dos archivos descargables:

1. **train.csv**: Son los datos descritos anteriormente que se utilizarán para entrenar el modelo. [Descargar archivo de training](https://storage.googleapis.com/challenges_events/03_2023/Pre-Selection%20JOBarcelona/Data/supply_chain_train.csv)

1. **test.csv**: Son los datos descritos anteriormente que se utilizarán en la predicción. [Descargar archivo de testing](https://www.google.com/url?sa=j&url=https%3A%2F%2Fstorage.googleapis.com%2Fchallenges_events%2F03_2023%2FPre-Selection%2520JOBarcelona%2FData%2Fsupply_chain_test.csv&uct=1678720074&usg=i2vAYtRo1zZgLlmykiXHb_CxUCw.&source=meet)

## 🎯 Objetivo:

Crea un modelo predictivo de clasificación para poder clasificar los datos del archivo de testing. Primero entrena tu modelo con el conjunto de datos de training y una vez que tengas el modelo que maximice la puntuación f1 (macro.) utiliza los datos de testing como entrada para tu modelo.

## ✅ Submission:

1. **predicciones.json**:

- Las predicciones deben estar en un archivo JSON llamado predictions.json, un ejemplo se puede encontrar en lo siguiente [link](https://storage.googleapis.com/challenges_events/03_2023/Pre-Selection%20JOBarcelona/Data/template.json).

- En este fichero de predicciones, en formato json, cada fila corresponderá al valor predicho del test_idx, es decir, si el primer valor es un 2 significa que este 2 corresponde al primer fichero del conjunto de datos de prueba. Es IMPORTANTE llamar a la columna target tal y como se especifica en el formato. Recuerda que puedes utilizar la función to_json de pandas para convertir tu dataframe a json, la longitud de las predicciones tiene que ser la misma que en test.csv.

- La puntuación de los objetivos vendrá de aplicar la puntuación f1 de las predicciones que hayas hecho al conjunto de datos de prueba con nuestra verdad fundamental.

**IMPORTANTE**: Las predicciones deben estar en formato int (0 o 1).

**⚠️ CONDICIONES PARA QUE SU SOLUCIÓN SEA EVALUADA CORRECTAMENTE:**

1. Su repositorio debe ser público.

1. Tu repositorio debe estar en la rama 'main'. Si creaste tu repo desde VSCode y tu rama principal superior es 'master'. Necesitas crear una rama llamada 'main' y mover todo a esta rama.

1. Dentro de tu repositorio debe estar el archivo 'predictions.json'.

1. Si tu enlace termina en '.git' quita el '.git' de la url y pégalo.

   - 👍 Link correcto: https://github.com/CarlosIbCu/example_se

   - 👎 Link incorrecto: https://github.com/CarlosIbCu/example_se.git

## ✍️ Evaluación:

En la evaluación se tendrá en cuenta lo siguiente:

- 100/1200: (DOCUMENTACIÓN): Documentación aportada.

- 900/1200: (OBJETIVOS) Se obtendrá a partir de la f1-score (macro) del modelo predictivo. Comparación de las predicciones que su modelo ha hecho sobre frente a la verdad del terreno.

- 200/1200: (CALIDAD) Calidad y automatización del código, complejidad, mantenibilidad, fiabilidad y seguridad.
