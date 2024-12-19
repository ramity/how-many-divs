from bs4 import BeautifulSoup
import os

template_path = "/root/src/template.html"

def generate_divs(num_divs, height):

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found: {template_path}")

    # Load the template HTML file
    with open(template_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")

    # Find the <body> tag
    body = soup.body
    if not body:
        raise ValueError("No <body> tag found in the template.")

    style_tag = soup.new_tag("style")
    style_tag.string = "div { height: "+str(height)+"px; }"
    soup.head.append(style_tag)

    # Generate and append the div elements
    for i in range(num_divs):
        new_div = soup.new_tag("div")
        new_div.string = f"Generated Div {i + 1}"
        body.append(new_div)

    # Save the updated HTML to the output file
    output_path = f"/root/rendered/{num_divs}-{height}px.html"
    html = soup.prettify("utf-8")
    with open(output_path, "wb") as file:
        file.write(html)

for divs in range(1000, 10100, 100):
    for height in range(1, 36):
        generate_divs(divs, height)
