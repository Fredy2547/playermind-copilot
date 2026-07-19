# PlayerMind Copilot

## Engineering Decisions

---

### ED-001 - Arquitectura Base

**Fecha:** 2026-07-15

**Decisión**

La plataforma separará completamente la orquestación del procesamiento de la inteligencia artificial.

- Python será responsable del flujo del sistema.
- Los modelos multimodales realizarán el análisis del video.
- El sistema no dependerá de un proveedor específico de IA.
- Será posible cambiar entre GPT, Gemini o Claude sin modificar la arquitectura principal.

**Motivación**

Los modelos de IA evolucionan rápidamente. La arquitectura debe permitir reemplazar el proveedor sin afectar el resto del sistema.

**Estado**

✅ Aprobada

### ED-006 - Simplificación del Downloader

Para el MVP se descargará un único archivo MP4 progresivo.

No se descargará video y audio por separado.

FFmpeg será incorporado únicamente cuando sea necesario para el procesamiento avanzado del video.

Estado:
✅ Aprobada