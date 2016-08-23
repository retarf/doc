    num = Doc.objects.get(pk=doc_id).number

    if num < 10:
        num = "00" + str(num)
    elif num < 100:
        num = "0" + str(num)
    else:
        num = str(num)



'num': num



<!-- onclick="document.location='{% url 'doc:DocumentDetail' doc.id %}'" -->


    # income_form.html
    < !-- { %
    for field in form %}

    {{field.error}}
    < label > {{field.label_tag}} < / label >
    < div > {{field}} < / div >