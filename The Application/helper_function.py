def get_sign_description(label):
    signs = {'0': 'Maximum Speed Limit 20 MPH',
             '1': 'Maximum Speed Limit 30 MPH',
             '2': 'Maximum Speed Limit 50 MPH',
             '3': 'Maximum Speed Limit 60 MPH',
             '4': 'Maximum Speed Limit 70 MPH',
             '5': 'Maximum Speed Limit 80 MPH',
             '6': 'End Of 80 MPH Limit Speed',
             '7': 'Maximum Speed Limit 100 MPH',
             '8': 'Maximum Speed Limit 120 MPH',
             '9': 'Overtaking not allowed',
             '10': 'Overtaking is prohibited only \n for Goods vehicles having a permissible \n Maximum weight '
                   'exceeding 3.5 tons',
             '11': 'Crossroad ahead \n side roads to right and left',
             '12': 'Priority road ahead',
             '13': 'Give way to all traffic',
             '14': 'Stop and give way to all traffic',
             '15': 'Entry not allowed / forbidden',
             '16': 'Lorries - Trucks forbidden',
             '17': 'No entry (one-way traffic)',
             '18': 'Cars not allowed - prohibited',
             '19': 'Road ahead curves to the left side',
             '20': 'Road bends to the right',
             '21': 'Double curve ahead, \nto the left then to the right',
             '22': 'Poor road surface ahead',
             '23': 'Slippery road surface ahead',
             '24': 'Road gets narrow on the right side',
             '25': 'Roadworks ahead warning',
             '26': 'Traffic light ahead',
             '27': 'Warning for pedestrians',
             '28': 'Warning for children and minors',
             '29': 'Warning for bikes and cyclists',
             '30': 'snow or ice smoothness',
             '31': 'Deer crossing in area - road',
             '32': 'End of all speed and passing limits',
             '33': 'Turning right compulsory',
             '34': 'Left turn mandatory',
             '35': 'Ahead Only',
             '36': 'Driving straight ahead \n or \n turning right mandatory',
             '37': 'Driving straight ahead \n or \n turning left mandatory',
             '38': 'Pass on right only',
             '39': 'Passing left compulsory',
             '40': 'Direction of traffic on roundabout',
             '41': 'End of the overtaking prohibition',
             '42': 'End of the overtaking prohibition for trucks'
             }
    for i in signs:
        if label == int(i):
            return signs[i]
