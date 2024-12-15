<p align="left" style="font-size: small;">
    Universidad de Sevilla  
    <br>Escuela Técnica Superior de Ingeniería Informática
</p>

<p align="center">
    <img src="media/3490fac9907787381d76ea6e20c541f4.gif" alt="Imagen del proyecto">
</p>

# Acta Fundacional del Proyecto

**Grupo:** 2  
**Tutor:** Belen Ramos  
**Repositorio:** https://github.com/Lidiajim/montaito-hub.git  
**Tipo:** Single  

**Integrantes:**
- **Óscar Menéndez Márquez** - oscmenmar@alum.us.es
- **Jun Yao** - junyao@alum.us.es
- **Lidia Jiménez Soriano** - lidjimsor@alum.us.es
- **Álvaro Ruiz Gutiérrez** - alvruigut@alum.us.es
- **Carlos Martín de Prado Barragán** - carmarbar9@alum.us.es
- **Francisco Capote García** - fracapgar@alum.us.es

## Índice
1. Descripción del Proyecto
2. Tabla de versiones
3. Hitos
4. Políticas de Mensajes de Commit
5. Políticas de Ramas
6. Políticas de Issues
7. Políticas de Pull Requests
8. Aprobación y Firma de los Integrantes

## 1. Descripción del Proyecto
El proyecto consiste en un fork o una evolución de la aplicación UVLHub, en el cual se desarrollarán nuevas características para mejorar su funcionalidad. El objetivo principal será integrar los flujos de trabajo (workflows) actuales, configurarlos adecuadamente para ajustarse a las nuevas necesidades y diseñar otros workflows que complementen o extiendan los ya existentes. Además, se explorará la posibilidad de utilizar herramientas de integración y entrega continua (CI/CD) que no han sido implementadas previamente en el sistema. Esto permitirá optimizar los procesos de despliegue y asegurar una mejor automatización en el ciclo de desarrollo. A lo largo del proyecto, se priorizará la innovación y la eficiencia, garantizando que los nuevos workflows y herramientas CI/CD contribuyan a un desarrollo más ágil y robusto de la aplicación.

## 2. Tabla de versiones
| Fecha       | Versión | Descripción de los cambios |
|-------------|---------|----------------------------|
| 16/10/2024  | 1.0     | Creación del documento     |
| 18/10/2024  | 1.1     | Desarrollo del documento   |
| 16/11/2024  | 1.2     | Modificación politicas     |
| 01/12/2024  | 1.3     | Actualización política PR  |

## 3. Hitos
| ID | Descripción                      | Fecha de Entrega |
|----|----------------------------------|------------------|
| M0 | Inscripción de los equipos       | 04/10/2024       |
| M1 | Sistema funcionando y pruebas    | 23/10/2024       |
| M2 | Sistema funcionando y con incrementos | 13/11/2024 |
| M3 | Entrega de proyectos y defensas  | 18/12/2024       |

## 4. Políticas de Mensajes de Commit
Los mensajes de commit deberán ser descriptivos y concisos, incluyendo información relevante sobre los cambios realizados. Se siguen las siguientes convenciones:
- Uso de verbos en modo imperativo en el título.
- Uso del Inglés.
- Prefijar los mensajes de commit con uno de los siguientes tipos:
  - `feature`: para las tareas relacionadas con los WI.
  - `fix`: para correcciones de errores.
  - `docs`: para cambios en la documentación.
  - `test`: para cuando se añadan tests.
  - `config`: para cuando se modifica la configuración del proyecto.
- No usar puntos finales ni suspensivos al final del título.
- Ser corto y conciso en los títulos, para ello se establecen un máximo de 50 caracteres.

## 5. Políticas de Ramas
El proyecto tendrá tantas ramas como issues creadas, excepto para las issues de documentación o configuración. Cada rama estará dedicada al desarrollo de la tarea correspondiente a la issue asignada. Estas son algunas pautas clave a seguir en cuanto a las políticas de ramas:
- **Nomenclatura de las ramas:** Las ramas deben nombrarse de manera consistente y descriptiva. Se sugiere un formato que incluya el número del issue y una breve descripción de la tarea, por ejemplo: `feature/#45-mejora-login`.
- **Ramas principales:** Se mantendrán dos ramas principales:
  - `main`: Esta rama contendrá siempre el código en producción, estable y sin errores. No se permitirán commits directamente a `main`.
  - `develop`: Esta rama se utilizará para integrar el trabajo de las ramas de características antes de pasarlo a `main`. Además, todos los commits realacionados con documentación o configuración se realizarán directamente a `develop`. Es la versión candidata para la siguiente liberación.
- **Ramas de características (feature branches):** Para cada nueva funcionalidad o cambio, se creará una rama a partir de `develop`, y al finalizar el trabajo, se realizará una fusión a `develop` mediante un pull request. Ejemplo de nombre de rama: `feature/#45-mejora-login`.
- **Ramas de test (test branches):** Para cada nuevo test, se creará una rama a partir de `develop`, y al finalizar el trabajo, se realizará una fusión a `develop` mediante un pull request. Ejemplo de nombre de rama: `test/#50-test-mejora-login`.
- **Ramas de mejoras (upgrade branches):** Para cada nueva mejora en una funcionalidad, se creará una rama a partir de `develop`, y al finalizar el trabajo, se realizará una fusión a `develop` mediante un pull request. Ejemplo de nombre de rama: `upgrade/#55-upgrade-mejora-login`.
- **Ramas de corrección de errores (bugfix branches):** Cuando se identifiquen errores en el código, se crearán ramas específicas para su corrección. Estas ramas pueden derivarse de `main` (si es un error en producción) o de `develop` (si es un error en desarrollo). Ejemplo de nombre de rama: `bugfix/#53-correccion-buglogin`.
- **Ramas de hotfix:** Si es necesario corregir un error crítico en producción o un fallo en uno de los workflows, se creará una rama de hotfix directamente desde `main` y, una vez corregido, se fusionará tanto en `main` como en `develop`. Ejemplo de nombre de rama: `hotfix/#101-parche-seguridad`.

## 6. Políticas de Issues
Se creará una issue para cada WI, mejora, test, documento o problema que surja durante el proyecto. Con esto crearemos ramas independientes con el nombre de estas tareas, marcándola inicialmente como issues abiertas. A cada issue se le asignará una etiqueta o label que identificará el problema a abordar:
- `upgrade`: Esta tarea es una mejora para una funcionalidad.
- `config`: Tarea relacionada con la configuración del proyecto.
- `1`: Esta tarea debe resolverse cuando sea posible, pero no es urgente.
- `2`: Esta tarea debe resolverse rápidamente.
- `3`: Esta tarea debe resolverse inmediatamente.
- `bug`: Algo no está funcionando correctamente.
- `documentation`: Mejoras o adiciones a la documentación.
- `feature`: Nueva funcionalidad o solicitud.
- `fix`: Esta tarea necesita ser corregida.
- `high`: Tarea con alta dificultad.
- `in progress`: La tarea está actualmente en progreso y no se ha completado.
- `low`: Tarea con baja dificultad.
- `M2`: Tarea del Hito 2.
- `M3`: Tarea del Hito 3.
- `medium`: Tarea con dificultad media.
- `test`: Nueva prueba para una funcionalidad.

Cada issue deberá contener una descripción que siga la siguiente plantilla:
- As a user I want...
- `Estimation`: 1h estimated.
- `Impacted Modules`: Dataset and Public.

Además, se asignarán uno o varios miembros a cada issue, con la finalidad de tener un control sobre la carga equitativa de trabajo y sobre el desarrollo de cada tarea, marcando en todo momento el estado en el que se encuentra.

## 7. Políticas de Pull Requests

### Requisitos Generales para Pull Requests
- Se debe abrir un Pull Request (PR) para cualquier cambio destinado a las ramas `main` o `develop`.
- Todo PR debe ser revisado por al menos un integrante del equipo antes de ser fusionado, especialmente si:
  - Afecta al menos a un módulo del proyecto.
  - Surge como resultado de la colaboración entre varios integrantes.
- El PR deberá cumplir con todas las políticas del proyecto, incluidas las relacionadas con ramas, commits e issues.
- Los cambios introducidos en un PR deben superar todas las pruebas automatizadas configuradas en el proyecto (si las hay).

### Requisitos para Colaboradores Externos
- Los colaboradores externos deben realizar un fork del repositorio principal y trabajar sobre este.
- Todos los cambios deben realizarse en una rama independiente dentro del fork, siguiendo la convención de nombres definida en las [Políticas de Ramas](#5-políticas-de-ramas). Ejemplo: `feature/#45-mejora-login`.
- Abrir un PR desde la rama del fork hacia la rama `develop` del repositorio principal.
- Asegúrate de que el PR cumpla con las mismas reglas aplicables a los miembros del equipo, incluyendo el formato de commits y la descripción.

### Descripción Obligatoria para Pull Requests
Cada PR debe incluir una descripción detallada para facilitar la revisión y el entendimiento del propósito de los cambios. Utiliza la siguiente plantilla para estructurar tu descripción:

#### Plantilla de Descripción:
- **Resumen del Cambio:** Explicación breve y concisa sobre qué problema se resuelve o qué funcionalidad se añade.  
  Ejemplo: "Se implementa la validación de datos en el formulario de registro."
- **Issue Relacionada:** Referencia directa al número de issue asociada, si aplica.  
  Ejemplo: "Issue #45."
- **Impacto en el Proyecto:** Indica los módulos o funcionalidades que se ven afectados por los cambios realizados.  
  Ejemplo: "Auth y Dataset."
- **Pasos para Probar:** Proporciona instrucciones claras para que los revisores puedan verificar los cambios.  
  Ejemplo:
  1. Clonar la rama y ejecutar el comando `npm start`.
  2. Acceder al formulario de registro.
  3. Completar los campos del formulario con datos inválidos y confirmar que aparecen los mensajes de error esperados.
- **Dependencias Nuevas:** Indica cualquier librería, herramienta o configuración adicional necesaria para que los cambios funcionen.  
  Ejemplo: "Se añadió la librería `express-validator`. Ejecutar `npm install` antes de probar."
- **Notas Adicionales:** Cualquier detalle importante que no esté cubierto en los puntos anteriores.  
  Ejemplo: "Incluye pruebas unitarias para los casos de validación de formulario."

### Proceso de Revisión y Aprobación
- Cada PR deberá ser revisado por al menos un miembro del equipo. Los cambios críticos o colaborativos requerirán la aprobación de al menos dos personas.
- Los revisores deben proporcionar comentarios claros y específicos sobre cualquier problema identificado en el PR. El autor del PR deberá resolver todas las observaciones antes de que se apruebe.
- Los conflictos con la rama base deben resolverse antes de solicitar la aprobación final.
- Ningún PR será aceptado si falla en las pruebas automatizadas configuradas en el proyecto.
- La fusión del PR solo podrá ser realizada por integrantes del equipo con permisos de escritura en el repositorio una vez que se haya aprobado.


## 8. Aprobación y Firma de los Integrantes
Por la presente, los integrantes del equipo aceptan y se comprometen a seguir las políticas establecidas en esta acta.
- Óscar Menéndez Márquez - Firma:
[GitHub](https://github.com/oscarmenendezz)
- Jun Yao - Firma:
[GitHub](https://github.com/yaospain)
- Lidia Jiménez Soriano - Firma:
[GitHub](https://github.com/Lidiajim)
- Álvaro Ruiz Gutiérrez - Firma:
[GitHub](https://github.com/alvruigut)
- Carlos Martín de Prado Barragán - Firma:
[GitHub](https://github.com/carmarbar9)
- Francisco Capote García - Firma:
[GitHub](https://github.com/franciiscocg)
