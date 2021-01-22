def airport(initial, final, number):
    if initial == "Gauteng":
        if final == "Limpopo":
            price = float(200.00 * number)
        elif final == "Mpumalanga":
            price = float(250.00 * number)
        elif final == "North West":
            price = float(270.00 * number)
        elif final == "Eastern Cape":
            price = float(300.00 * number)
        elif final == "Northern Cape":
            price = float(600.00 * number)
        elif final == "Free State":
            price = float(550.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(500.00 * number)
        elif final == "Western Cape":
            price = float(650.00 * number)
        else:
            price = " Error \n('GP from GP)'"

        return price

    elif initial == "Limpopo":
        if final == "Gauteng":
            price = float(200.00 * number)
        elif final == "Mpumalanga":
            price = float(150.00 * number)
        elif final == "North West":
            price = float(300.00 * number)
        elif final == "Free State":
            price = float(400.00 * number)
        elif final == "Northern Cape":
            price = float(700.00 * number)
        elif final == "Eastern Cape":
            price = float(650.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(600.00 * number)
        elif final == "Western Cape":
            price = float(800.00 * number)
        else:
            price = " Error\n('L from L')"

        return price

    elif initial == "Mpumalanga":
        if final == "Limpopo":
            price = float(150.00 * number)
        elif final == "Gauteng":
            price = float(250.00 * number)
        elif final == "North West":
            price = float(270.00 * number)
        elif final == "Free State":
            price = float(400.00 * number)
        elif final == "Northern Cape":
            price = float(600.00 * number)
        elif final == "Eastern Cape":
            price = float(550.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(250.00 * number)
        elif final == "Western Cape":
            price = float(650.00 * number)
        else:
            price = " Error\n('MP from MP')"

        return price

    elif initial == "North West":
        if final == "Limpopo":
            price = float(300.00 * number)
        elif final == "Mpumalanga":
            price = float(350.00 * number)
        elif final == "Gauteng":
            price = float(270.00 * number)
        elif final == "Free State":
            price = float(200.00 * number)
        elif final == "Northern Cape":
            price = float(500.00 * number)
        elif final == "Eastern Cape":
            price = float(600.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(450.00 * number)
        elif final == "Western Cape":
            price = float(600.00 * number)
        else:
            price = " Error\n('NW from NW')"

        return price

    elif initial == "Kwa-Zulu Natal":
        if final == "Limpopo":
            price = float(400.00 * number)
        elif final == "Mpumalanga":
            price = float(250.00 * number)
        elif final == "North West":
            price = float(400.00 * number)
        elif final == "Free State":
            price = float(300.00 * number)
        elif final == "Northern Cape":
            price = float(600.00 * number)
        elif final == "Eastern Cape":
            price = float(550.00 * number)
        elif final == "Gauteng":
            price = float(500.00 * number)
        elif final == "Western Cape":
            price = float(700.00 * number)
        else:
            price = " Error\n('KZN from KZN')"

        return price

    elif initial == "Free State":
        if final == "Limpopo":
            price = float(400.00 * number)
        elif final == "Mpumalanga":
            price = float(200.00 * number)
        elif final == "North West":
            price = float(300.00 * number)
        elif final == "Gauteng":
            price = float(300.00 * number)
        elif final == "Northern Cape":
            price = float(600.00 * number)
        elif final == "Eastern Cape":
            price = float(550.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(450.00 * number)
        elif final == "Western Cape":
            price = float(650.00 * number)
        else:
            price = " Error\n('FS from FS')"

        return price

    elif initial == "Northern Cape":
        if final == "Limpopo":
            price = float(700.00 * number)
        elif final == "Mpumalanga":
            price = float(500.00 * number)
        elif final == "North West":
            price = float(450.00 * number)
        elif final == "Free State":
            price = float(300.00 * number)
        elif final == "Gauteng":
            price = float(600.00 * number)
        elif final == "Eastern Cape":
            price = float(350.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(500.00 * number)
        elif final == "Western Cape":
            price = float(150.00 * number)
        else:
            price = " Error\n('NC from NC')"

        return price

    if initial == "Western Cape":
        if final == "Limpopo":
            price = float(800.00 * number)
        elif final == "Mpumalanga":
            price = float(450.00 * number)
        elif final == "North West":
            price = float(370.00 * number)
        elif final == "Free State":
            price = float(300.00 * number)
        elif final == "Northern Cape":
            price = float(200.00 * number)
        elif final == "Eastern Cape":
            price = float(550.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(500.00 * number)
        elif final == "Gauteng":
            price = float(700.00 * number)
        else:
            price = " Error\n('WC from WC')"

        return price

    elif initial == "Eastern Cape":
        if final == "Limpopo":
            price = float(700.00 * number)
        elif final == "Mpumalanga":
            price = float(500.00 * number)
        elif final == "North West":
            price = float(400.00 * number)
        elif final == "Free State":
            price = float(300.00 * number)
        elif final == "Northern Cape":
            price = float(200.00 * number)
        elif final == "Gauteng":
            price = float(650.00 * number)
        elif final == "Kwa-Zulu Natal":
            price = float(350.00 * number)
        elif final == "Western Cape":
            price = float(250.00 * number)
        else:
            price = " Error\n('EC from EC')"

        return price
        