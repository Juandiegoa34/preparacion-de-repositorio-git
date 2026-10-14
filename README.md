# Tienda API — Tutorial 04

Proyecto preparado para el laboratorio de Dockerización y despliegue en AWS EC2. Incluye Django REST Framework, PostgreSQL, Docker Compose y configuración mediante variables de entorno.

## Ejecutar localmente

```bash
docker compose up --build
```

API: `http://localhost:8000/api/v1/comprar/`

## Despliegue en AWS Academy

1. Cree una instancia EC2 Amazon Linux 2023 `t2.micro` con la key pair `vockey`.
2. Permita SSH, HTTP, HTTPS y agregue una regla TCP para el puerto `8000` desde `0.0.0.0/0`.
3. En EC2 Instance Connect ejecute:

```bash
sudo dnf update -y
sudo dnf install git docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
exit
```

Vuelva a conectarse y ejecute:

```bash
git clone <URL_DE_ESTE_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
docker compose up -d --build
docker ps
```

Valide en `http://<IP_PUBLICA_EC2>:8000/api/v1/comprar/` y tome la captura solicitada por el tutorial.

## Entregables cubiertos

- `settings.py` con credenciales y host PostgreSQL parametrizados.
- `requirements.txt` con Django REST Framework y `psycopg2-binary`.
- `Dockerfile` reproducible.
- `docker-compose.yml` con servicios `web` y `db` y volumen persistente.
- Endpoint JSON `/api/v1/comprar/` para validar el despliegue.
- Esta guía de comandos para EC2.

> En AWS Academy no se incluyen credenciales en el repositorio. Si cambia el nombre del repositorio, use su URL real en el comando `git clone`.
