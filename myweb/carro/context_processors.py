def importe_total_carro (request):
    total=0
    for key, value in request.session["carro"].items():
        total=total + float(value["precio"])
    return{"importe_total_carro":total}