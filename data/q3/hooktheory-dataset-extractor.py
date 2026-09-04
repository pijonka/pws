import json
import chord_analyzer
import playwright.sync_api

SONG_LINK_LIST = [
  "https://www.hooktheory.com/theorytab/view/olivia-rodrigo/drivers-license",
  #"https://www.hooktheory.com/theorytab/view/alex-g/sarah"
]

def retrieve_chords_from_hooktheory_link(link) -> str:
    with playwright.sync_api.sync_playwright() as p:
        # initialize the browser session with clipboard permissions
        browser = p.chromium.launch()
        context = browser.new_context(permissions=["clipboard-read", "clipboard-write"])
        page = context.new_page()
        page.goto(link)


        # retrieve and click the copy button which gives the "copy chords" drop down
        init_copy_button = page.get_by_title("Copy to clipboard (Alt-click for song ID)")
        init_copy_button.click()

        # retrieve and click the "copy chords" button, copying JSON data to clipboard
        copy_chords_button = page.get_by_text("Copy Chords")
        copy_chords_button.click()

        # save the data copied to clipboard
        hooktheory_chords_string = page.evaluate("navigator.clipboard.readText()")

        # close browser
        browser.close()

        return hooktheory_chords_string

def parse_chords_from_hooktheory_to_pi_list(hooktheory_chords_string):
    # format example of this variable = {"chords": [{chord 1 data}, {chord 2 data}]}
    hooktheory_chords_dict = json.loads(hooktheory_chords_string)

    # format example of this variable = [{'beat': 1, 'root': 6}, {'beat': 1, 'root': 6}]
    chords_of_hooktheory_chords_list = hooktheory_chords_dict["chords"]
    print(json.dumps(chords_of_hooktheory_chords_list, indent=2))

    # format example of this variable when all values are appended: [1, 5, 3, 4]
    pi_chord_roots_list = []
    # for every object in this chords list
    for element in chords_of_hooktheory_chords_list:
        pi_chord_roots_list.append(int(element["root"]))

    print(pi_chord_roots_list)

    

# for each link in link_list
for link in SONG_LINK_LIST:
    hooktheory_chords_string = retrieve_chords_from_hooktheory_link(link)
    # pi_chords_list =  parse_chords_from_hooktheory_to_pi_list(hooktheory_chords_json)
    parse_chords_from_hooktheory_to_pi_list(hooktheory_chords_string)

    # use_of_chord_prog_counter(pi_chords_list, CHORD_PROGS_TO_COUNT)

    # dataset.append({data})

# write to dataset