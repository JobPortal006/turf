TABLES = {
    'user': {
        'name': 'user',
        'columns': {
            'userId': 'userId',
            'roleId': 'roleId',
            'userName': 'userName',
            'password': 'password',
            'email': 'email',
            'profilePhoto': 'profilePhoto',
            'mobileNumber': 'mobileNumber'
        }
    },
    'role': {
        'name': 'role',
        'columns': {
            'roleId': 'roleId',
            'role': 'role'
        }
    },
    'turfType': {
        'name': 'turfType',
        'columns': {
            'turfTypeId': 'turfTypeId',
            'turfType': 'turfType'
        }
    },
    'turfDetails': {
        'name': 'turfDetails',
        'columns': {
            'turfId': 'turfId',
            'turfTypeId': 'turfTypeId',
            'turfAddress': 'turfAddress',
            'turfTimings': 'turfTimings',
            'description': 'description',
            'partitions': 'partitions'
        }
    },
    'gameType': {
        'name': 'gameType',
        'columns': {
            'gameTypeId': 'gameTypeId',
            'gameType': 'gameType'
        }
    },
    'gameDetails': {
        'name': 'gameDetails',
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
    'userTurfMapping': {
        'name': 'userTurfMapping',
        'columns': {
            'mappingId': 'mappingId',
            'userId': 'userId',
            'turfId': 'turfId'
        }
    },
    'subscription': {
        'name': 'subscription',
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
    'bookings': {
        'name': 'bookings',
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
    'maintenanceSchedules': {
        'name': 'maintenanceSchedules',
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
    'equipment': {
        'name': 'equipment',
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
}    
