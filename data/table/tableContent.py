TABLES = [
    { 
        'tableName': 'user',
        'columns': {
            'userId': 'userId',
            'roleId': 'roleId',
            'firstName': 'firstName',
            'lastName':'lastName',
            'password': 'password',
            'email': 'email',
            'profilePhoto': 'profilePhoto',
            'mobileNumber': 'mobileNumber'
        }
    },
    {
        'tableName': 'roles',
        'columns': {
            'roleId': 'roleId',
            'role': 'role'
        }
    },
    {
        'tableName': 'userSportsInterest',
        'columns': {
            'userSportsInterestId': 'userSportsInterestId',
            'userId': 'userId',
            'gameTypeId': 'gameTypeId'
        }
    },
    {
        'tableName': 'location',
        'columns': {
            'locationId': 'locationId',
            'doorNo': 'location',
            'street':'street',
            'city':'city',
            'state':'state',
            'pincode':'pincode'
        }
    },
    {
        'tableName': 'turfType',
        'columns': {
            'turfTypeId': 'turfTypeId',
            'turfType': 'turfType'
        }
    },
    {
        'tableName': 'turfDetails',
        'columns': {
            'turfId': 'turfId',
            'turfTypeId': 'turfTypeId',
            'turfAddress': 'turfAddress',
            'turfTimings': 'turfTimings',
            'description': 'description',
            'partitions': 'partitions'
        }
    },
    {
        'tableName': 'gameType',
        'columns': {
            'gameTypeId': 'gameTypeId',
            'gameType': 'gameType'
        }
    },
    {
        'tableName': 'gameDetails',
        'columns': {
            'gameId': 'gameId',
            'turfId': 'turfId',
            'gameTypeId': 'gameTypeId',
            'numberOfCourts': 'numberOfCourts',
            'noOfPersonsInvolved': 'noOfPersonsInvolved',
            'isForKids': 'isForKids',
            'pricePerHour': 'pricePerHour'
        }
    },
    {
        'tableName': 'userTurfMapping',
        'columns': {
            'mappingId': 'mappingId',
            'userId': 'userId',
            'turfId': 'turfId'
        }
    },
    {
        'tableName': 'subscription',
        'columns': {
            'subscriptionId': 'subscriptionId',
            'turfId': 'turfId',
            'subscriptionType': 'subscriptionType',
            'startDate': 'startDate',
            'endDate': 'endDate',
            'price': 'price',
            'status': 'status'
        }
    },
    {
        'tableName': 'bookings',
        'columns': {
            'bookingId': 'bookingId',
            'userId': 'userId',
            'turfId': 'turfId',
            'bookingTimings': 'bookingTimings',
            'bookingDate': 'bookingDate',
            'bookingPrice': 'bookingPrice',
            'timeSlot': 'timeSlot',
            'courtNumber': 'courtNumber',
            'gameId': 'gameId',
            'bookingStatus':'bookingStatus'
        }
    },
    {
        'tableName': 'maintenanceSchedules',
        'columns': {
            'scheduleId': 'scheduleId',
            'turfId': 'turfId',
            'userId': 'userId',
            'taskDescription': 'taskDescription',
            'scheduledDate': 'scheduledDate',
            'completionDate': 'completionDate',
            'notes': 'notes'
        }
    },
    {
        'tableName': 'equipment',
        'columns': {
            'equipmentId': 'equipmentId',
            'equipmentName': 'equipmentName',
            'equipmentType': 'equipmentType',
            'purchaseDate': 'purchaseDate',
            'maintenanceDate': 'maintenanceDate',
            'condition': 'condition',
            'turfId': 'turfId'
        }
    }
]


def get_table_info(table_name):
    for table in TABLES:
        if table['tableName'] == table_name:
            return table
    return None