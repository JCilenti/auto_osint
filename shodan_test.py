from shodan import Shodan
import colorama
from colorama import Fore

def read_key():
    key_file = open("../shodan_key.txt", "r")
    key = key_file.read(32)
    #print(key)
    key_file.close()
    return key

# give the user a menu to select what to search
def user_prompt():
    prompt_file = open("prompt.txt", "r")
    print(Fore.YELLOW + ''.join([line for line in prompt_file]))
    user_selection = input("What would you like to do? ")
    if int(user_selection) == 1:
        print("YOU SELECTED IP ADDRESS SEARCH")
        shodan_ip_search()
    prompt_file.close()

def shodan_ip_search():
    chosen_ip = input("ENTER THE IP ADDRESS YOU'D LIKE TO SEARCH: ")
    ipinfo = api.host(str(chosen_ip))
    print(ipinfo)


if __name__ == "__main__":
    read_key()
    api = Shodan(read_key())
    user_prompt()
