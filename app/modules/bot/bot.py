import os
import discord
import requests
from discord.ext import commands

# Configuración de intents del bot
intents = discord.Intents.default()
intents.message_content = True  # Habilitar acceso al contenido de los mensajes
bot = commands.Bot(command_prefix="!", intents=intents)

# Determinar la URL base según el entorno
def get_api_base_url():
    # Comprobar si estamos en un entorno de despliegue
    api_url = os.getenv("API_BASE_URL", "http://127.0.0.1:5000/api/v1/")
    print(f"Usando la API en: {api_url}")
    return api_url

# Inicializar la URL base
API_BASE_URL = get_api_base_url()

# Evento de inicio
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print(f'Listo para usar la API en {API_BASE_URL}')

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("¡Hola desde el bot!")

@bot.command(name="datasets")
async def list_datasets(ctx):
    try:
        # Solicitar datos al endpoint de datasets
        response = requests.get(f"{API_BASE_URL}datasets/", timeout=10)
        response.raise_for_status()

        # Parsear el JSON
        data = response.json()

        if "items" in data and isinstance(data["items"], list):
            datasets = data["items"]

            if datasets:
                message = "Datasets disponibles:\n"
                for dataset in datasets:
                    message += f"- ID: {dataset['dataset_id']}, Nombre: {dataset['name']}, DOI: {dataset['doi']}\n"
            else:
                message = "No hay datasets disponibles."
        else:
            message = "Error: La API devolvió un formato inesperado."

        await ctx.send(message)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Error al conectar con la API: {e}")
    except KeyError as e:
        await ctx.send(f"Error en el formato de los datos: Clave faltante {e}")
    except Exception as e:
        await ctx.send(f"Error inesperado: {e}")

@bot.command(name="dataset")
async def dataset_details(ctx, dataset_id: int):
    try:
        response = requests.get(f"{API_BASE_URL}datasets/{dataset_id}", timeout=10)
        response.raise_for_status()

        dataset = response.json()
        message = (
            f"**Detalles del Dataset**\n"
            f"ID: {dataset['dataset_id']}\n"
            f"Nombre: {dataset['name']}\n"
            f"DOI: {dataset['doi']}\n"
            f"Archivos:\n"
        )
        for file in dataset["files"]:
            message += f"- {file['file_name']} ({file['size']})\n"

        await ctx.send(message)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Error al conectar con la API: {e}")
    except KeyError as e:
        await ctx.send(f"Error en el formato de los datos: Clave faltante {e}")
    except Exception as e:
        await ctx.send(f"Error inesperado: {e}")

@bot.command(name="search")
async def search_datasets(ctx, *, query: str):
    try:
        response = requests.get(f"{API_BASE_URL}datasets/", timeout=10)
        response.raise_for_status()

        data = response.json()
        datasets = data.get("items", [])
        results = [d for d in datasets if query.lower() in d["name"].lower()]

        if results:
            message = f"**Resultados de la búsqueda para '{query}':**\n"
            for dataset in results:
                message += f"- ID: {dataset['dataset_id']}, Nombre: {dataset['name']}\n"
        else:
            message = f"No se encontraron datasets para '{query}'."

        await ctx.send(message)

    except requests.exceptions.RequestException as e:
        await ctx.send(f"Error al conectar con la API: {e}")
    except Exception as e:
        await ctx.send(f"Error inesperado: {e}")

@bot.command(name="info")
async def bot_info(ctx):
    message = (
        "**UVLHubBot**\n"
        "Versión: 1.0.0\n"
        "Comandos disponibles:\n"
        "- !datasets: Lista todos los datasets.\n"
        "- !dataset <ID>: Muestra detalles de un dataset.\n"
        "- !search <nombre>: Busca datasets por nombre.\n"
        "- !info: Muestra esta información."
    )
    await ctx.send(message)
