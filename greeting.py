#!/home/layonthehorn/.config/zsh_functions/env/bin/python3

import random

# This script will print a random greeting when you start the terminal
message = "Welcome to zsh, Vern MacCaster.\n{0}"
greeting = random.choice(["Aren't you a handsome lion?",
                          "Your tail is the best.",
                          "Such a handsome mane.",
                          "Your nose is really cute.",
                          "You're looking gorgeous today, Mr. Lion",
                          "Lion love is the best love.",
                          "You're a very pretty lion, aren't you?"])
print(message.format(greeting))
