import discord
import requests
import os
from discord.ext import commands

DEFAULT_API_BASE_URL = "http://127.0.0.1:5000"
PRODUCTION_API_BASE_URL = "https://montaito-hub-h34c.onrender.com"
API_BASE_URL = os.getenv("API_BASE_URL", PRODUCTION_API_BASE_URL if "RENDER" in os.getenv("ENV", "").upper() else DEFAULT_API_BASE_URL)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')
    print(f'Usando la API en: {API_BASE_URL}')

@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("¡Hola desde el bot!")

@bot.command(name="datasets")
async def list_datasets(ctx):
    try:
        response = requests.get(f"{API_BASE_URL}/api/v1/datasets/")
        response.raise_for_status()
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
        response = requests.get(f"{API_BASE_URL}/api/v1/datasets/{dataset_id}")
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
        response = requests.get(f"{API_BASE_URL}/api/v1/datasets/")
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
