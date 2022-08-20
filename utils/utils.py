from string import Template

def get_contacts(filename):
    civs = []
    comps = []
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            civs.append(a_contact.split()[0])
            names.append(a_contact.split()[1])
            comps.append(a_contact.split()[2])
            emails.append(a_contact.split()[3])
    return civs,names,comps, emails


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)