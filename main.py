from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_restful import Api
import datetime
import json


app = Flask(__name__)
api = Api(app)


flag = 0


class MyException(Exception):
    pass


@app.route('/', methods=["GET", "POST"])
def posttextarea():
    global flag
    if flag == 0:
        flag += 1
        return render_template('billing.html', data5=0)
    else:
        try:
            n_data = request.form['text']
            if request.form['text'] is None:
                raise MyException
            else:
                j_data = json.loads(n_data)
                data = sorted(j_data, key=lambda k: k['item'], reverse=False)  # sorts the obtained json input data in alphabetical order with respect to a value
                total_price = 0
                gross_price = 0
                grand_total = 0
                tax = 0
                ttax = 0
                my_data = []
                for i in range(len(data)):
                    item = data[i]['item']
                    category = data[i]['itemCategory']
                    quantity = data[i]['quantity']
                    price = data[i]['price']
                    if str(category).lower() == "medicine" or str(category).lower() == "food":
                        total_price = ((0.05 * float(price)) + float(price)) * quantity
                        gross_price = gross_price + price
                        tax = 5
                        ttax = ttax + 5
                    elif str(category).lower() == "imported":
                        total_price = ((0.18 * float(price)) + float(price)) * quantity
                        gross_price = gross_price + price
                        tax = 18
                        ttax = ttax + 18
                    elif str(category).lower() == "book":
                        total_price = float(price) * quantity
                        gross_price = gross_price + price
                        tax = 0
                        ttax = ttax + 0
                    elif str(category).lower() == "music":
                        total_price = ((0.03 * float(price)) + float(total_price)) * quantity
                        gross_price = gross_price + price
                        tax = 3
                        ttax = ttax + 3
                    elif str(category).lower() == "clothes":
                        if float(price) < 1000:
                            total_price = ((0.05 * float(price)) + float(price)) * quantity
                            gross_price = gross_price + price
                            tax = 5
                            ttax = ttax + 5
                        elif float(price) > 1000:
                            total_price = ((0.12 * float(price)) + float(price)) * quantity
                            gross_price = gross_price + price
                            tax = 12
                            ttax = ttax + 12

                    grand_total = float(grand_total) + total_price

                    product = {'item': item, 'price': price, 'quantity': quantity, 'tax': tax, 'gross_price': gross_price, 'total_price': total_price}
                    my_data.append(product)
                    print('ITEM = {} , ACTUAL PRICE = {}, QUANTITY = {}, TOTAL PRICE = {}'.format(item, price, quantity, total_price))
                    total_price = 0
                    product = {}
                print('Grand total before  = {}'.format(grand_total))
                if grand_total > 2000:
                    grand_total = (grand_total - (0.05 * grand_total))
                    grand_total = str(round(grand_total, 2))

                print('GRAND_TOTAL = {}'.format(grand_total))
                print(my_data)
                date = datetime.datetime.now().date()
                time = datetime.datetime.now().strftime("%H:%M:%S")
                return render_template('billing.html', data=my_data, data2=grand_total, data3=gross_price, content=date, content2=time, content3=ttax, data5=1)
                # return redirect(url_for('posttextarea'))

        except Exception:
            return "Error reading JSON request!"

        except TypeError:
            return "Please provide valid input"

        except KeyError:
            return "Please provide valid JSON input, or recheck the input JSON once again, one of the keys that you are requesting might not be present"

        except MyException as error:
            return "The Text Area field cannot be left blank!"

            # return "There was an error processing your request! Possibly your input was wrong. Please provide JSON input!"


if __name__ == "__main__":
    app.run(debug=True)
