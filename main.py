from jinja2 import Template, Environment, FileSystemLoader

company_name = "Abby's Freight Logistics"
company_number = '510-990-0487'
company_address = '2223 Mount Pellier St'
company_city = 'Tracy'
company_state = 'CA'
company_zip = '95304'

file_loader = FileSystemLoader('src/templates')
env = Environment(loader=file_loader)


def process_html(file_name):
    content = open(f'src/{file_name}', 'r').read()
    content_template = Template(content)
    content_output = content_template.render(company_name=company_name, company_number=company_number, company_address=company_address, company_city=company_city, company_state=company_state, company_zip=company_zip)
    template = env.get_template('index.html')
    output = template.render(company_name=company_name, company_number=company_number, company_address=company_address, company_city=company_city, company_state=company_state, company_zip=company_zip, content=content_output)
    with open(f'docs/{file_name}', "w") as file:
        file.write(output)

if __name__ == '__main__':
    process_html("index.html")
    process_html("contact.html")

    print("hello w!")