# Tienda API — Tutorial 05

Proyecto preparado para el laboratorio de Docker, Gunicorn, Nginx y despliegue en AWS EC2. La arquitectura usa tres servicios: PostgreSQL, Django servido por Gunicorn y Nginx como proxy inverso.

## Arquitectura

- `nginx`: único servicio expuesto a Internet en el puerto `80`.
- `web`: Django + Gunicorn en `0.0.0.0:8000`, aislado en la red interna de Docker.
- `db`: PostgreSQL con volumen persistente.

## Ejecutar localmente

```bash
docker compose up -d --build
docker compose ps
```

API a través de Nginx: `http://localhost/api/v1/comprar/`

El acceso directo a `http://localhost:8000` debe fallar porque Django ya no publica ese puerto en el host.

## Despliegue en AWS Academy

En el Security Group de la instancia permita SSH (`22`) y HTTP (`80`) desde su configuración de laboratorio. No es necesario abrir el puerto `8000`.

```bash
sudo dnf update -y
sudo dnf install git docker -y
sudo systemctl enable --now docker
sudo usermod -aG docker ec2-user
exit
```

Vuelva a conectarse y ejecute:

```bash
git clone <URL_DE_ESTE_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
docker compose up -d --build
docker ps
```

Si la instancia no incluye Docker Compose como subcomando, instale el plugin y repita:

```bash
sudo dnf install docker-compose-plugin -y
docker compose version
```

## Evidencias del laboratorio

1. **Enrutamiento:** capture el navegador en `http://<IP_PUBLICA_EC2>/api/v1/comprar/`, sin `:8000`, mostrando la respuesta JSON.
2. **Aislamiento:** capture el intento de acceder a `http://<IP_PUBLICA_EC2>:8000`; debe producir timeout o conexión rechazada.
3. **Orquestación:** capture `docker ps` en AWS mostrando `nginx`, `web` y `db` en estado `Up`.

> En AWS Academy no se incluyen credenciales en el repositorio. Si cambia el nombre del repositorio, use su URL real en `git clone`.
