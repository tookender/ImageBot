# ImageBot
This is the repository of a bot I made for a customer.
It has a `/suit` command which turns your image into a circle and puts it on a image stored in `data/image.png`

## Syncing Commands
To sync the slash commands command, you must use `?sync`
Please do not over use this command, it has a daily rate limit.

## Additional Info
The `/suit` command has a 10 second cooldown. It will send an error if the cooldown is hit.
It also has a `member` argument which allows you to generate the suit avatar for the specified user. If no user is specified, it defaults to the author.
It also has a `ephemeral` argument which sends the response ephemerally meaning only the author can see it.
The code uses Pillow, which shouldn't be blocking as the code is running it in an executor using bot.loop.

Lastly, if you would like to to add another generator, follow the guide below:
0. Create a new fiel in the `data/` folder. Make sure it has a `.png` extension, this is the background the command will use.
1. Create a new file under the `extensionse/image` with the name being whatever you want. Make sure it has a `.py` extension.
2. Copy the contents of the `extensions/image/suit.py` file and paste them into the newly created file.
3. Change the name of all functions and the command
4. In the `create_xxxxx` function, edit the `data/suit.png` file into the file you have created previously in the data directory.
5. If you wish to align the avatar which is pasted onto the background, change the `width` and `height` variable in the `create_xxxxx` function.
6. Make sure to sync the command using `?sync` and you should be done.