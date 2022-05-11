## Alertas backend
Api construida con Django rest framework y postgres

#### Requisitos
- Tener Docker y Docker Compose instalados
- Git

#### Configuración
1. Clonar el repositorio:  `git clone https://github.com/robinqc/alertas-backend.git`
2. Entrar a la  carpeta del proyecto: `cd alertas-backend/`
3. Construir contenedores: `docker-compose up --build`
4. El servidor estará escuchando en `http://localhost:8000`

No es necesario construir los contenedores cada vez, se puede usar `docker-compose up`
