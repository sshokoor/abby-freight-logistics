from jinja2 import Template, Environment, FileSystemLoader

company_name = "Abby's Freight Logistics"

file_loader = FileSystemLoader('src/templates')
env = Environment(loader=file_loader)


def process_html(file_name):
    content = open(f'src/{file_name}', 'r').read()
    template = env.get_template('index.html')
    output = template.render(company_name=company_name, content=content)
    with open(f'docs/{file_name}', "w") as file:
        file.write(output)

if __name__ == '__main__':
    process_html("index.html")
    process_html("contact.html")

    print("hello w!")