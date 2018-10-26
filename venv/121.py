# ! /bin/python3

# imports with mangodb and flask and other stuff
import os, re, sys
import models
from flask import *
app = Flask(__name__, template_folder='templates')
# import database here


@app.route('/', methods=['POST','GET'])
def index():
    print(request.args.to_dict())
    return render_template('homepage.html')




@app.route('/services', methods=['GET'])
def services():
    # add credential check here
    # all_args = request.args
    # print(all_args)
    # data = services_arg_handler(all_args)
    return render_template('services.html')

@app.route('/homepage',  methods=['GET'])
def homepage():
    
    return render_template('homepage.html')



    # if request.method == 'POST':
    #     result = request.form.to_dict()
    #     beds = 0
    #     if int(result['bedroom']) > 1:
    #         for i in range(0, int(result['bedroom'])):
    #             beds += int(result['bedroom' + str(i)])
    #             result.pop('bedroom' + str(i))
    #     result['beds'] = beds
    #     if result['atype'] == 'hotel':
    #         result['atype'] = 'house'
    #         result['sub_type'] = result['type-house']
    #     else:
    #         result['sub_type'] = result['type-apa']
    #
    #     result['amenities'] = request.form.getlist('amenities')
    #     result['facilities'] = request.form.getlist('facilities')
    #     result['rules'] = request.form.getlist('rule')
    #     result['photos'] = []
    #     for i in list(result.keys()):
    #         if 'pic' in i:
    #             result['photos'].append(result[i])
    #             result.pop(i)
    #     print(result)
    #     models.insertData(result)
@app.route('/accommodation', methods=['GET', 'POST'])
def accommodation():
    d = models.select_all()
    return render_template('accommodation.html', data=d)

@app.route('/detail/<int:prop_id>', methods=['GET','POST'])
def detail(prop_id):
    d = models.select_all()
    for i in d:
        if i[0] == prop_id:
            print(i)
    return render_template('detail.html', data=i)

@app.route('/search', methods=['GET', 'POST'])
def search():
    arg_dicts = request.args.to_dict()
    a = models.select(arg_dicts)
    return render_template('accommodation.html', data=a)

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')



def services_arg_handler(arg_dict):
    data = {}
    prop_type = arg_dict['atype']
    data.update({'prop_type': prop_type})

    sub_type = None
    if prop_type == 'apartment':
        sub_type = arg_dict['type-apa']
    elif prop_type == 'house':
        sub_type = arg_dict['type-house']

    data.update({'sub_type': sub_type})
    # for n many bedrooms, there will be a dictionary
    # of form {bedroom_name: number_of_beds}
    bedroom = int(arg_dict['bedroom'])
    if bedroom >= 1:
        temp = {}
        for i in range(bedroom):
            temp_name = 'bedroom'+str(i)
            temp.update({temp_name: arg_dict[temp_name]})
        data.update({'bedrooms': temp})
    bathroom = int(arg_dict['quantity'])
    guest_nb = int(arg_dict['quantity1'])
    data.update({'bathroom': bathroom, 'guest_nb':guest_nb})
    message = arg_dict['message']
    name = arg_dict['name']
    email = arg_dict['email']
    phone = arg_dict['phone']
    pictures = {'pic1': arg_dict['pic1'], 'pic2': arg_dict['pic2'], 'pic3': arg_dict['pic3'], 'pic4': arg_dict['pic4'], 'pic5': arg_dict['pic5'], 'pic6': arg_dict['pic6']}
    data.update({'message': message, 'name':name, 'email': email, 'phone': phone, 'pictures': pictures})
    title = arg_dict['title']
    suburb = arg_dict['suburb']
    address = arg_dict['address']
    post_code = arg_dict['poscode']
    available_date = arg_dict['datetimes'].split(' - ')
    description = arg_dict['message']
    data.update({'title':title, 'suburb':suburb, 'address':address, 'post_code': post_code, 'date': available_date})

    data.update({'description':description})
    return data




if __name__ == '__main__':
    app.run(debug = "ON" )
