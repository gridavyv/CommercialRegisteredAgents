# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_agents.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for i in range(len(lines)-2):
#         if lines[i] == "\n" and lines[i+2] == "Physical Address\n":
#             out_f.write(lines[i+1])
#             count += 1
# print(count)


# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         if "Phone:" in line:
#             out_f.write(line)
#             count += 1
# print(count)


# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails.txt", 'w') as out_f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         if "Email:" in line:
#             out_f.write(line)
#             count += 1
# print(count)

# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_phones_v1.txt", 'w') as out_f:
#     lines = f.readlines()
#     for line in lines:
#         part_1 = line.split(" ")[1].strip("\n")
#         part_2 = line.split(" ")[2].strip("\n")
#         out_f.write(part_1 + " " + part_2 + "\n")


# with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails.txt") as f, \
#      open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/filtered_emails_v1.txt", 'w') as out_f:
#     lines = f.readlines()
#     var = ""
#     for line in lines:
#         line_list = line.split(" ")
#         if len(line_list) == 1:
#             var = "no_email"
#         else:
#             var = line_list[-1].strip("/n")
#         out_f.write(var)


def split_by_empty_line() -> list:
    with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.txt") as f:
        lines = f.readlines()
        print(len(lines))
        filt_lines = []
        l = 0
        for i in range(len(lines)):
            if lines[i] == "\n":
                filt_lines.append(lines[l:i])
                l = i+1
        return filt_lines

def remove_mailing_address(input_list: list) -> list:
        output_list = []
        for sub_list in input_list:
            if "Mailing Address\n" not in sub_list:
                output_list.append(sub_list)
        return output_list

def extract_names(input_list: list) -> list:
    names = []
    for sub_list in input_list:
        if len(sub_list) > 1:
            name = sub_list[0].strip("\n")
            clean_name = name.replace(",", "")
            names.append(clean_name)
    return names

def extract_phones(input_list: list) -> list:
    phones = []
    for sub_list in input_list:
        if len(sub_list) > 1:
            for element in sub_list:
                if "Phone:" in element:
                    phone_part_1 = element.split(" ")[1].strip("\n")
                    phone_part_2 = element.split(" ")[2].strip("\n")
                    phone = phone_part_1 + " " + phone_part_2
            phones.append(phone)
    return phones

def extract_emails(input_list: list) -> list:
    emails = []
    for sub_list in input_list:
        if len(sub_list) > 1:
            for element in sub_list:
                if "Email:" in element:
                    emails.append(element.split(" ")[-1].strip("\n"))
    return emails

def define_status(names: list) -> list:
    statuses = []
    for name in names:
        if "llc" in name.lower():
            status = "company" 
        elif "inc" in name.lower():
            status = "company" 
        else:
            status = "individual"
        statuses.append(status)
    return statuses

def potential_web_page(emails: list) -> list:
    potentail_web_pages = []
    for email in emails:
        if "@gmail.com" in email:
            web_page = "n/a"
        elif "@" in email:
            web_page = email.split("@")[1]
        else:
            web_page = "n/a"
        potentail_web_pages.append(web_page)
    return potentail_web_pages

def write_to_csv(names: list, phones: list, emails: list, statuses: list, potential_web_pages: list):
    assert len(names) == len(phones) == len(emails) == len(statuses) == len(potential_web_pages), "Lenght of lists is not equal!"
    with open("/Users/gridavyv/Python_projects/CommercialRegisteredAgents/agents.csv", 'w') as f:
        f.write("Name, Phone, Email, Status, Potential_web_page\n")
        for i in range(len(names)):
            f.write(names[i] + ", " + phones[i] + ", " + emails[i] + ", " + statuses[i] + ", " + potential_web_pages[i] + "\n")

filt_list = split_by_empty_line()
filt_list_no_mailing_address = remove_mailing_address(filt_list)
names = extract_names(filt_list_no_mailing_address)
phones = extract_phones(filt_list_no_mailing_address)
emails = extract_emails(filt_list_no_mailing_address)
statuses = define_status(names)
potential_web_pages = potential_web_page(emails)
write_to_csv(names, phones, emails, statuses, potential_web_pages)
# print(extract_names(filt_list_no_mailing_address))
# print(len(extract_names(filt_list_no_mailing_address)))
# phones = extract_phones(filt_list_no_mailing_address)
# for phone in phones:
#     print(phone)
# print(len(extract_phones(filt_list_no_mailing_address)))
# emails = extract_emails(filt_list_no_mailing_address)
# for email in emails:
#     print(email)