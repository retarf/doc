    num = Doc.objects.get(pk=doc_id).number

    if num < 10:
        num = "00" + str(num)
    elif num < 100:
        num = "0" + str(num)
    else:
        num = str(num)



'num': num