import pandas as pd

import duckduckgo_images_api.api_py3 as ddg_api



boeing_types = ['737', '747', '767', '777', '787']
boeing_search_key_words = ['boeing ' + number for number in boeing_types]

for keyword in boeing_search_key_words:
    ddg_api.search(keyword)

airbus_types = ['A320', 'A330', 'A350', 'A380']
airbus_search_key_words = ['airbus ' + number for number in airbus_types]

for keyword in airbus_search_key_words:
    ddg_api.search(keyword)
