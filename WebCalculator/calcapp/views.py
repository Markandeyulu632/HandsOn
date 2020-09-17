from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request):

    if request.method == 'POST':
        option = request.POST['option']
        num2 = ""
        try:
            num1 = float(request.POST['num1'])
            num2 = float(request.POST['num2'])
        except ValueError:
            if option not in ['1', '2', '3', '4']:
                op_des = " Invalid option and values "
            else:
                op_des = " Invalid values "
            num1 = 'X'
            return render(request, 'calc_app.html',
                          {'sel': op_des, 'option': option, 'num1': num1, 'num2': num2, })

        op_des = ""
        mes = ""
        sign = ""
        result = 0

        if option == '1':
            option = 1
            op_des = "Addition"
            sign = '+'
            result = num1 + num2
        elif option == '2':
            option = 2
            op_des = "Subtraction"
            sign = '-'
            result = num1 - num2
        elif option == '3':
            option = 3
            op_des = 'Multiplication'
            sign = '*'
            result = num1 * num2
        elif option == '4':
            option = 4
            op_des = 'Division'
            sign = '/'
            if num2 == 0:
                mes = 'N'
            else:
                result = num1 / num2
        elif option not in ['1', '2', '3', '4']:
            op_des = " Invalid option "

        result = "{:.2f}".format(result)
        return render(request, 'calc_app.html',
                      {'sign': sign, 'mes': mes, 'sel': op_des, 'option': option, 'num1': num1, 'num2': num2,
                       'result': result})

    return render(request, 'calc_app.html', {})
