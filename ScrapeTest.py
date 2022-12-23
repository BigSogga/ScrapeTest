from bs4 import BeautifulSoup, Tag, NavigableString
import requests


def extractText(imslp_element):
    text = ""
    for element in imslp_element.contents:
        if isinstance(element, NavigableString):
            text += element.replace("\n", "")
        elif isinstance(element, Tag):
            if "class" in element.attrs:
                classes = element.attrs["class"]
                if "mh555" in classes:
                    text_extract = element.get_text()
                    text += text_extract
    return text


def extractTextTd(td_elements):
    text = ""
    td_element_text = td_element.get_text()
    td_element_text = td_element_text.replace("\n", "")
    text += td_element_text
    return text


# Prepare the resources
link = requests.get("https://imslp.org/wiki/Piano_Sonata_No.9,_Op.14_No.1_(Beethoven,_Ludwig_van)")
soup = BeautifulSoup(link.content, "html.parser")

algemene_informatie = soup.find(class_="wi_body")
tr_elements = algemene_informatie.find_all("tr")

table = {}

# Save the tabel to a dict
for tr_element in tr_elements:
    th_element = tr_element.findNext("th")
    th_element_text = extractText(th_element)
    td_element = tr_element.findNext("td")
    td_element_text = extractTextTd(td_element)
    table[th_element_text] = td_element_text