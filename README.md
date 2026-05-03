# VocalStream AI 🎙️

Agente de voz inteligente construido con una **Arquitectura de Capas** profesional, utilizando procesamiento asíncrono para baja latencia.

## 🏗️ Arquitectura del Proyecto
Este proyecto sigue el patrón de diseño de capas:
- **Presentation Layer:** FastAPI (WebSockets) y React.
- **Business Logic Layer:** Servicios de procesamiento de audio asíncronos.
- **Data Access Layer:** Modelos de persistencia para transcripciones.

## 🚀 Tecnologías
- **Python 3.12**
- **FastAPI** (Backend)
- **Asyncio** (Programación asíncrona)
- **WebSockets** (Transmisión en tiempo real)

## 🛠️ Instalación
1. Clona el repo.
2. Instala dependencias: `pip install -r backend/requirements.txt`
3. Ejecuta: `uvicorn backend.main:app --reload`