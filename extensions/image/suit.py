from io import BytesIO

import discord
from aiohttp import ClientSession
from discord import app_commands
from discord.ext import commands
from PIL import Image, ImageChops, ImageDraw

import config


class SuitCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def create_suit(self, member: discord.Member):
        image_bytes = await member.display_avatar.read()  # Get the bytes of the member'S avatar
        image = Image.open(BytesIO(image_bytes)).convert("RGBA").resize((1000, 1000))  # Get the avatar image, convert it to the RGBA color format and then resize it to 1000x1000
        template = Image.open("data/suit.png").convert("RGBA")  # Get the template image and convert it to the RGBA color format

        mask = Image.new("L", image.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0) + image.size, fill=255)
        image.putalpha(mask)  # Puts an alpha mask on the avatar image to make it circular

        width = (template.width - image.width) // 2  # The X coordinate of where the avatar should be pasted
        height = ((template.height - image.height) // 2) - 105  # The Y coordiante of where the avatar should be pasted
        template.paste(image, (width, height), image)  # Pasting the avatar onto the template
        template.save("profile.png")  # Saves the image locally to send it
    
    @app_commands.command(description="Turns the member's into a circle avatar and then adds it onto an image.")
    @app_commands.checks.cooldown(1, 10)  # This adds a cooldown, because trust me, you don't want people spamming Pillow
    async def suit(self, interaction: discord.Interaction, member: discord.Member | None = None, ephemeral: bool | None = None):
        member = member or interaction.user  # Set the member to the member or the author, depends if its specified or not
        ephemeral = ephemeral or False

        await interaction.response.defer(thinking=True)  # Defer because Pillow sometimes takes long

        await self.bot.loop.run_in_executor(None, self.create_suit, member)

        return await interaction.followup.send(file=discord.File("profile.png"), ephemeral=ephemeral)

    @suit.error
    async def error_suit(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        return await interaction.response.send_message(f"{error}", ephemeral=True)