mock_group_data = {
  "results": {
    "groups": {
      "6": {
        "id": 6,
        "active": "true",
        "name": "Group 1",
        "last_modified": "2018-08-19T16:29:28+00:00",
        "created": "2018-08-19T16:29:28+00:00",
        "manager_ids": [
          "300",
          "316"
        ]
      },
      "8": {
        "id": 8,
        "active": "true",
        "name": "Group 2",
        "last_modified": "2018-08-19T16:29:35+00:00",
        "created": "2018-08-19T16:29:35+00:00",
        "manager_ids": [
          "316"
        ]
      },
      "16": {
        "id": 16,
        "active": "true",
        "name": "Group 3",
        "last_modified": "2018-08-20T23:22:13+00:00",
        "created": "2018-08-20T23:22:13+00:00",
        "manager_ids": []
      }
    }
  },
  "more": "false",
  "supplemental_data": {
    "users": {
      "300": {
        "id": 300,
        "first_name": "Joseph",
        "last_name": "",
        "group_id": 0,
        "active": "true",
      },
      "316": {
        "id": 316,
        "first_name": "Bill",
        "last_name": "Franklin",
        "group_id": 0,
        "active": "true",
      }
    }
  }
}

mock_user_data = {
  "results": {
    "users": {
      "933849": {
        "id": 933849,
        "first_name": "Mary",
        "last_name": "Samsonite",
        "group_id": 0,
        "active": "true",
        "employee_number": 0,
        "salaried": "false",
        "exempt": "false",
        "username": "admin",
        "email": "admin@example.com",
        "email_verified": "false",
        "payroll_id": "",
        "mobile_number": "2087231456",
        "hire_date": "0000-00-00",
        "term_date": "0000-00-00",
        "last_modified": "2018-03-28T17:24:20+00:00",
        "last_active": "",
        "created": "2018-03-27T16:13:34+00:00",
        "client_url": "api_sample_output",
        "company_name": "API Sample Output Company",
        "profile_image_url": "https:\/\/www.gravatar.com\/avatar\/e64c7d89f26bd1972efa854d13d7dd61",
        "display_name": "",
        "pto_balances": {
          "2624351": 0,
          "2624353": 0,
          "2624355": 0
        },
        "submitted_to": "2000-01-01",
        "approved_to": "2000-01-01",
        "manager_of_group_ids": [ ],
        "require_password_change": "false",
        "pay_rate": 0,
        "pay_interval": "hour",
        "permissions": {
          "admin": "true",
          "mobile": "true",
          "status_box": "false",
          "reports": "false",
          "manage_timesheets": "false",
          "manage_authorization": "false",
          "manage_users": "false",
          "manage_my_timesheets": "false",
          "manage_jobcodes": "false",
          "pin_login": "false",
          "approve_timesheets": "false",
          "manage_schedules": "false",
          "external_access": "false",
          "manage_my_schedule": "false",
          "manage_company_schedules": "false",
          "view_company_schedules": "false",
          "view_group_schedules": "false",
          "manage_no_schedules": "false",
          "view_my_schedules": "false",
          "time_tracking": "false"
        },
        "customfields": ""
      },
      "933845": {
        "id": 933845,
        "first_name": "Bob",
        "last_name": "Smith",
        "group_id": 64965,
        "active": "true",
        "employee_number": 0,
        "salaried": "false",
        "exempt": "false",
        "username": "bobsmith",
        "email": "",
        "email_verified": "false",
        "payroll_id": "",
        "hire_date": "0000-00-00",
        "term_date": "0000-00-00",
        "last_modified": "2018-03-27T16:13:33+00:00",
        "last_active": "2018-03-28T20:16:39+00:00",
        "created": "2018-03-27T16:13:33+00:00",
        "client_url": "api_sample_output",
        "company_name": "API Sample Output Company",
        "profile_image_url": "",
        "display_name": "",
        "mobile_number": "",
        "pto_balances": {
          "2624351": 0,
          "2624353": 0,
          "2624355": 0
        },
        "submitted_to": "2000-01-01",
        "approved_to": "2000-01-01",
        "manager_of_group_ids": [ ],
        "require_password_change": "false",
        "pay_rate": 0,
        "pay_interval": "hour",
        "permissions": {
          "admin": "false",
          "mobile": "true",
          "status_box": "false",
          "reports": "false",
          "manage_timesheets": "false",
          "manage_authorization": "false",
          "manage_users": "false",
          "manage_my_timesheets": "false",
          "manage_jobcodes": "false",
          "pin_login": "false",
          "approve_timesheets": "false",
          "manage_schedules": "false",
          "external_access": "false",
          "manage_my_schedule": "false",
          "manage_company_schedules": "false",
          "view_company_schedules": "false",
          "view_group_schedules": "false",
          "manage_no_schedules": "false",
          "view_my_schedules": "false",
          "time_tracking": "false"
        },
        "customfields": ""
      }
    }
  },
  "more": "false",
  "supplemental_data": {
    "jobcodes": {
      "2624351": {
        "id": 2624351,
        "parent_id": 0,
        "assigned_to_all": "true",
        "billable": "false",
        "active": "true",
        "type": "pto",
        "has_children": "false",
        "billable_rate": 0,
        "short_code": "",
        "name": "Sick",
        "last_modified": "2018-03-27T16:13:28+00:00",
        "created": "2018-03-27T16:13:28+00:00",
        "filtered_customfielditems": "",
        "required_customfields": [ ],
        "locations": [ ]
      },
      "2624353": {
        "id": 2624353,
        "parent_id": 0,
        "assigned_to_all": "true",
        "billable": "false",
        "active": "true",
        "type": "pto",
        "has_children": "false",
        "billable_rate": 0,
        "short_code": "",
        "name": "Vacation",
        "last_modified": "2018-03-27T16:13:28+00:00",
        "created": "2018-03-27T16:13:28+00:00",
        "filtered_customfielditems": "",
        "required_customfields": [ ],
        "locations": [ ]
      },
      "2624355": {
        "id": 2624355,
        "parent_id": 0,
        "assigned_to_all": "true",
        "billable": "false",
        "active": "true",
        "type": "pto",
        "has_children": "false",
        "billable_rate": 0,
        "short_code": "",
        "name": "Holiday",
        "last_modified": "2018-03-27T16:13:28+00:00",
        "created": "2018-03-27T16:13:28+00:00",
        "filtered_customfielditems": "",
        "required_customfields": [ ],
        "locations": [ ]
      }
    },
    "groups": {
      "64965": {
        "id": 64965,
        "active": "true",
        "name": "Construction",
        "last_modified": "2018-03-27T16:13:30+00:00",
        "created": "2018-03-27T16:13:29+00:00",
        "manager_ids": [
          "933833"
        ]
      }
    }
  }
}

