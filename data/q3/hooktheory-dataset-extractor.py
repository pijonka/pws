import json
import chord_analyzer
import playwright.sync_api

TEST_LINK = "https://www.hooktheory.com/theorytab/view/olivia-rodrigo/drivers-license"

def retrieve_chords_from_hooktheory_link(link):
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
        # copy_chords_button = page.get("copy_chords")
        # copy_chords_button.click()

        # save the data copied to clipboard
        # hooktheory_chords_json = page.evaluate("navigator.clipboard.geyt")

        # close browser

        # return hooktheory_chords_json

# for each link in link_list
    # hooktheory_chords_json = retrieve_chords_from_hooktheory_link()

    # pi_chords_list =  parse_chords_from_hooktheory_to_pi_list()

    # use_of_chord_prog_counter(pi_chords_list, CHORD_PROGS_TO_COUNT)

    # dataset.append({data})

# write to dataset