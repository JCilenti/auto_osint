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
        shodan_host_search()
    elif int(user_selection) == 2:
        print("YOU SELECTED KEYWORD SEARCH")
        shodan_keyword_search()
    prompt_file.close()

def shodan_host_search():
    # Lookup the host
    chosen_host = input("ENTER THE IP ADDRESS YOU'D LIKE TO SEARCH: ")
    host = api.host(str(chosen_host))

    # Print general info
    print("""
        IP: {}
        Organization: {}
        Operating System: {}
    """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

    # Print all banners
    for item in host['data']:
        print("""
            Port: {}
            Banner: {}
        """.format(item['port'], item['data']))

    #ipinfo = api.host(str(chosen_ip))
    #print(ipinfo)

def shodan_keyword_search():
    user_search = input("Enter the service you would like to search for: ")
    try:
        # Search Shodan
        results = api.search(str(user_search))

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
    except Shodan.APIError as e:
        print('Error: {}'.format(e))

if __name__ == "__main__":
    read_key()
    api = Shodan(read_key())
    user_prompt()
