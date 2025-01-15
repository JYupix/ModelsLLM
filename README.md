# Modelos Locales y Hugging Face

## Archivos Aplicativo

Los siguientes son tres carpetas y su contenido:

1. **multiple_models**: Tiene un archivo de jupyter notebook que usa tres modelos de hugging face.
2. **ollama_local**: Acá se hizo la prueba de el modelo Ollama de forma local.
3. **quest_answer**: Un modelo simple donde le das la pregunta y el contexto y el te retorna la respuesta en base a ese contexto y a la pregunta.

---

## Librerías Usadas

Para el desarrollo de este aplicativo, se han utilizado las siguientes librerías:

1. **diffusers**
2. **huggingface-hub**
3. **pillow**
4. **streamlit**
5. **transformers**
6. **torch**

---

## Imágenes del Aplicativo

### Carpeta `multiple_models`

![Primer Modelo](/img/gpt2.PNG)

- **Descripción:** Con una frase pequeña puedo generar un prompt con este modelo.

![Segundo Modelo](/img/flux.PNG)
- **Descripción:** Con el anterior prompt puedo usarlo para generar mi imagen con este modelo.

![Tercer Modelo](/img/resnet.PNG)
- **Descripción:** Ya usando la imagen, se usará este modelo para detectar los objetos presentes de la imagen.

---

### Carpeta `quest_answer`

![Primer Modelo](/img/quest-answer.PNG)

- **Descripción:** En la interfaz debes proporcionar una pregunta y un contexto, para que el te responda la pregunta dada.

---
### Carpeta `ollama_model`

![Primer Modelo](/img/ollama_model.PNG)

- **Descripción:** Contiene el modelo usado de forma local, pero en este caso debemos usar `HTTP API` en nuestro `localhost`: `http://127.0.0.1:11434/`. Si este no está activado debemos activarlo y será el mismo puerto, haciendolo de forma manual con
   ```bash
   ollama serve
   ```

---

## Cómo Ejecutar el Aplicativo

1. Clona este repositorio en tu máquina local.
   ```bash
   git clone git@github.com:JYupix/ModelsLLM.git
   ```
2. Crea un entorno virtual.
   ```bash
   python -m venv env
   env/Scripts/activate
   ```
3. Y activalo de la siguiente manera.
   ```bash
   env/Scripts/activate
   ```
3. Luego Instala las dependencias necesarias.
   ```bash
   pip install -r requirements.txt
   ```
4. El único que usó streamlit fue el de la carpeta `quest_answer`
   ```bash
   streamlit run main.py
   ```
5. El de `multiple_models` debes correrlo en Jupyter Notebook.

---

## Cómo Ejecutar el Modelo de Forma Local
1. Para el `ollama_local` toca instalar ollama en tu pc primeramente
   ```bash
   https://ollama.com/download
   ```
2. Y debes revisar que modelo quieres instalar
   ```bash
   https://github.com/ollama/ollama
   ```
3. Luego en tu terminal debes descargarlo y usarlo usando el mismo comando
   ```bash
   ollama run nameModel
   ```
4. Para cerrar el modelo se usará
   ```bash
   /bye
   ```
5. Y para ejecutarlo
   ```bash
   python request.py
   ```

---