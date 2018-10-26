import os, re, sys

from flask import *

import models

def search_handler(req):
    print (req)
    filtered_ids = []
    print (req)
    if req['keyword'] != '':
        data = models.select('property_id', 'suburb =\''+req['keyword']+'\'', 'location_details')
        filtered_ids.append([i[0] for i in data])

    if req['date'] != '':
        # print(req['date'])
        data = models.select('property_id', 'from_date <=\''+req['date'][0:10]+'\'and to_date >= \''+req['date'][13:]+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])
    if req['price'] != '20,20':
        data = models.select('property_id', 'cost >\''+req['price'].split(',')[0]+'\' and cost < \''+ req['price'].split(',')[1]+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])

    if req['adult'] != '0':
        g =  int(req['adult'])
        data = models.select('property_id', 'guest_num >= \''+str(g)+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])

    if 'child' in req.keys():
        if req['child'] =='Yes':
            data = models.select('property_id', "amenities_list like '%,5,%'", 'accom_amenities')
            filtered_ids.append([i[0] for i in data])
    if req['bedrooms'] != '0':
        data = models.select('property_id', 'bedrooms_num >= \''+req['bedrooms']+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])
    if req['beds'] != '0':
        data = models.select('property_id', 'bed_num >= \''+req['beds']+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])
    if req['bath'] != '0':
        data = models.select('property_id', 'bathrooms_num >= \''+req['bath']+'\'', 'room_details')
        filtered_ids.append([i[0] for i in data])

    if 'amenities' in req.keys():
        req['amenities'] = [str(i) for i in sorted(int(i) for i in request.form.getlist('amenities'))]
        print(req['amenities'] )
        l = list()
        l.append([i[0] for i in models.select('property_id', 'amenities_list like  \'%' + str(req['amenities'][0]) + ',%\'', 'accom_amenities')])
        if(len(req['amenities'])>1):
            for i in req['amenities'][1:-1] :
                data = models.select('property_id', 'amenities_list like  \'%,'+i+',%\'', 'accom_amenities')
                l.append([i[0] for i in data])
            l.append([i[0] for i in
                      models.select('property_id', 'amenities_list like  \'%,' + str(req['amenities'][-1]) + '%\'',
                                    'accom_amenities')])

        result = set(l[0])
        for s in l[1:]:
            result.intersection_update(s)
        filtered_ids.append(list(result))

    if 'facilities' in req.keys():
        req['facilities'] = sorted(request.form.getlist('facilities'))

        l = list()
        l.append([i[0] for i in models.select('property_id', 'facilities_list like  \'%' + str(req['facilities'][0]) + ',%\'', 'accom_facilities')])

        if len(req['facilities'] )>1:
            for i in req['facilities'][1:-1]:
                data = models.select('property_id', 'facilities_list like  \'%,'+i+',%\'', 'accom_facilities')
                l.append([i[0] for i in data])
            l.append([i[0] for i in
                      models.select('property_id', 'facilities_list like  \'%,' + str(req['facilities'][-1]) + '%\'',
                                    'accom_facilities')])
        result = set(l[0])
        for s in l[1:]:
            result.intersection_update(s)
        filtered_ids.append(list(result))

    if 'rule' in req.keys():
        req['rule'] = sorted(request.form.getlist('rule'))
        l = list()
        l.append([i[0] for i in models.select('property_id', 'rules like  \'%' + str(req['rule'][0]) + ',%\'', 'properties')])
        if len(req['rule'])>1:
            for i in req['rule'][1:-1] :
                data = models.select('property_id', 'rules like  \'%,'+i+',%\'', 'properties')
                l.append([i[0] for i in data])
            l.append([i[0] for i in
                  models.select('property_id', 'rules like  \'%,' + str(req['rule'][-1]) + '%\'', 'properties')])

        result = set(l[0])
        for s in l[1:]:
            result.intersection_update(s)
        filtered_ids.append(list(result))
    if len(filtered_ids):
        result = set(filtered_ids[0])
    else:
        return None
    for s in filtered_ids[1:]:
        result.intersection_update(s)

    return list(result)