# Sección 2: Anatomía de la Complejidad (Módulos Profundos vs. Superficiales)

Fundamentado en los principios de John Ousterhout (*A Philosophy of Software Design*), auditamos la estructura del código de VocalStream AI para evaluar la relación entre la complejidad oculta y la simplicidad de las interfaces.

## 1. Módulos Profundos (Deep Modules)
El mejor componente diseñado por el flujo de desarrollo fue el módulo de lógica de negocio localizado en `backend/app/services/audio_processor.py`. 

Este es un **Módulo Profundo** clásico porque su interfaz (firma del método) es hermosamente minimalista, ocultando una inmensa complejidad algorítmica por debajo:
- **Interfaz Simple:** `await processor.process_chunk(bytes)`
- **Complejidad Oculta:** Por debajo de esta llamada de una sola línea, el módulo gestiona colas asíncronas (`asyncio.Queue`), decodifica el codec de audio crudo, controla los umbrales de silencio para segmentar la voz y despacha hilos de ejecución concurrentes sin que las capas superiores se enteren de ello.

## 2. Módulos Superficiales (Shallow Modules) y Corrección Humana
Durante las etapas intermedias, la IA falló al intentar atomizar el sistema siguiendo un criterio de sobre-ingeniería. Intentó crear archivos pequeños y vacíos como `services/stream_validator.py`, `services/buffer_helper.py` y `services/header_parser.py`. Cada uno tenía solo 5 líneas de código, pero requería que el desarrollador entendiera llamadas e interconexiones sumamente complejas entre ellos para lograr una sola tarea (**Módulos Superficiales**).

**Directriz Humana Aplicada:** Actuando como arquitectos senior, detuvimos el bucle e instruimos al agente unificar estos ayudantes superficiales dentro de la clase principal del servicio. Logramos ensanchar la profundidad del módulo, reduciendo la carga cognitiva total del sistema.

## 3. Fuga de Información (Information Leakage) y Solución
Detectamos una **Fuga de Información** crítica en la fase del MVP: el endpoint del WebSocket (`api/main.py`) estaba exponiendo directamente excepciones crudas y tipos de datos nativos de la librería de audio del sistema hacia los componentes de la interfaz de usuario de React en el Frontend. Si la tasa de muestreo (sample rate) fallaba en el sistema operativo, la UI se congelaba al recibir un string de error técnico inesperado.

**Corrección mediante Ocultamiento de Información (Information Hiding):** Introdujimos un bloque de captura en el adaptador del servicio que traduce cualquier falla interna de bajo nivel a un enumerado estándar de la aplicación (`AudioStatus.ERROR`). Los detalles de implementación de red e infraestructura quedaron sellados dentro de la capa correspondiente, protegiendo la abstracción de las interfaces superiores.