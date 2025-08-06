def get_input(months):
    while True:
        try:
            m_d_y = input("Date: ")
            if '/' in m_d_y:
                date = m_d_y.split("/")
                date[0].strip()
            else:
                date = m_d_y.split()
                if date[0].strip() in months and ',' in date[1]:
                    date[0] = int(months.index(date[0].strip()))+1
                    date[1] = date[1].strip(",")
            if len(date) == 3 and int(date[0]) < 13 and int(date[1]) < 32:
                return (date[0], date[1].strip(), date[2].strip())
        except NameError:
            pass
        except ValueError:
            pass


def main():
    month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month, date, year = get_input(month)
    print(f"{year}-{int(month):02}-{int(date):02}")


main()
