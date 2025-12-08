import pyfiglet
from colorama import init, Fore

init()

ascii_art = pyfiglet.figlet_format("Haxxor Tool", font="cards")
print(ascii_art)


print(Fore.RED + "Critical vuln found")
print(Fore.GREEN + "No vulns found")
print(Fore.BLUE + "Connecting...")

# fonts = pyfiglet.FigletFont.getFonts()
# print(fonts)

