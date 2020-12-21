email = "ceng113@example.com"
e_mail = str(input("Type email: "))
e_mail_l = e_mail.lower()
e_mail_part = e_mail_l.split("@")
e_mail_p1 = e_mail_part[0].replace(".","")
final = e_mail_p1 + "@" + e_mail_part[1]
print(final)