mock_groups_data = {
  "results": {
    "groups": {
      "6": {
        "id": 6,
        "active": "True",
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
        "active": "True",
        "name": "Group 2",
        "last_modified": "2018-08-19T16:29:35+00:00",
        "created": "2018-08-19T16:29:35+00:00",
        "manager_ids": [
          "316"
        ]
      },
      "16": {
        "id": 16,
        "active": "True",
        "name": "Group 3",
        "last_modified": "2018-08-20T23:22:13+00:00",
        "created": "2018-08-20T23:22:13+00:00",
        "manager_ids": []
      }
    }
  },
  "more": False,
  "supplemental_data": {
    "users": {
      "300": {
        "id": 300,
        "first_name": "Joseph",
        "last_name": "",
        "group_id": 0,
        "active": "True",
      },
      "316": {
        "id": 316,
        "first_name": "Bill",
        "last_name": "Franklin",
        "group_id": 0,
        "active": "True",
      }
    }
  }
}

mock_users_data = {
  "results": {
    "users": {
      "933849": {
        "id": 933849,
        "first_name": "Mary",
        "last_name": "Samsonite",
        "group_id": 0,
        "active": "True",
        "employee_number": 0,
        "salaried": "False",
        "exempt": "False",
        "username": "admin",
        "email": "admin@example.com",
        "email_verified": "False",
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
        "require_password_change": "False",
        "pay_rate": 0,
        "pay_interval": "hour",
        "permissions": {
          "admin": "True",
          "mobile": "True",
          "status_box": "False",
          "reports": "False",
          "manage_timesheets": "False",
          "manage_authorization": "False",
          "manage_users": "False",
          "manage_my_timesheets": "False",
          "manage_jobcodes": "False",
          "pin_login": "False",
          "approve_timesheets": "False",
          "manage_schedules": "False",
          "external_access": "False",
          "manage_my_schedule": "False",
          "manage_company_schedules": "False",
          "view_company_schedules": "False",
          "view_group_schedules": "False",
          "manage_no_schedules": "False",
          "view_my_schedules": "False",
          "time_tracking": "False"
        },
        "customfields": ""
      },
      "933845": {
        "id": 933845,
        "first_name": "Bob",
        "last_name": "Smith",
        "group_id": 64965,
        "active": "True",
        "employee_number": 0,
        "salaried": "False",
        "exempt": "False",
        "username": "bobsmith",
        "email": "",
        "email_verified": "False",
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
        "require_password_change": "False",
        "pay_rate": 0,
        "pay_interval": "hour",
        "permissions": {
          "admin": "False",
          "mobile": "True",
          "status_box": "False",
          "reports": "False",
          "manage_timesheets": "False",
          "manage_authorization": "False",
          "manage_users": "False",
          "manage_my_timesheets": "False",
          "manage_jobcodes": "False",
          "pin_login": "False",
          "approve_timesheets": "False",
          "manage_schedules": "False",
          "external_access": "False",
          "manage_my_schedule": "False",
          "manage_company_schedules": "False",
          "view_company_schedules": "False",
          "view_group_schedules": "False",
          "manage_no_schedules": "False",
          "view_my_schedules": "False",
          "time_tracking": "False"
        },
        "customfields": ""
      }
    }
  },
  "more": False,
  "supplemental_data": {
    "jobcodes": {
      "2624351": {
        "id": 2624351,
        "parent_id": 0,
        "assigned_to_all": "True",
        "billable": "False",
        "active": "True",
        "type": "pto",
        "has_children": "False",
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
        "assigned_to_all": "True",
        "billable": "False",
        "active": "True",
        "type": "pto",
        "has_children": "False",
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
        "assigned_to_all": "True",
        "billable": "False",
        "active": "True",
        "type": "pto",
        "has_children": "False",
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
        "active": "True",
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

mock_timesheets_data = {
  "results": {
    "timesheets": {
      "135288482": {
        "id": 135288482,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-16T09:04:00-06:00",
        "end": "2018-07-16T15:57:00-06:00",
        "duration": 24780,
        "date": "2018-07-16",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135288514": {
        "id": 135288514,
        "user_id": 1242509,
        "jobcode_id": 18080900,
        "start": "2018-07-16T13:07:00-06:00",
        "end": "2018-07-16T17:29:00-06:00",
        "duration": 15720,
        "date": "2018-07-16",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135288460": {
        "id": 135288460,
        "user_id": 1242509,
        "jobcode_id": 18080900,
        "start": "2018-07-18T08:09:00-06:00",
        "end": "2018-07-18T14:58:00-06:00",
        "duration": 24540,
        "date": "2018-07-18",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135288162": {
        "id": 135288162,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-19T12:06:00-06:00",
        "end": "2018-07-19T14:59:00-06:00",
        "duration": 10380,
        "date": "2018-07-19",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135288102": {
        "id": 135288102,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-22T13:05:00-06:00",
        "end": "2018-07-22T18:07:00-06:00",
        "duration": 18120,
        "date": "2018-07-22",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135522568": {
        "id": 135522568,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-23T08:00:00-06:00",
        "end": "2018-07-23T12:19:12-06:00",
        "duration": 15552,
        "date": "2018-07-23",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "manual",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "This is a test of a manual time entry",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135366264": {
        "id": 135366264,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-23T08:00:00-06:00",
        "end": "2018-07-23T12:19:12-06:00",
        "duration": 15552,
        "date": "2018-07-23",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "manual",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "This is a test of a manual time entry",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135288084": {
        "id": 135288084,
        "user_id": 1242509,
        "jobcode_id": 18080900,
        "start": "2018-07-23T09:07:00-06:00",
        "end": "2018-07-23T15:02:00-06:00",
        "duration": 21300,
        "date": "2018-07-23",
        "tz": -6,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135366260": {
        "id": 135366260,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-23T11:00:00-06:00",
        "end": "2018-07-23T14:10:23-06:00",
        "duration": 11423,
        "date": "2018-07-23",
        "tz": -7,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "This is a test of the emergency broadcast system",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [],
        "last_modified": "1970-01-01T00:00:00+00:00"
      },
      "135366262": {
        "id": 135366262,
        "user_id": 1242515,
        "jobcode_id": 17288283,
        "start": "2018-07-25T10:30:00-06:00",
        "end": "2018-07-25T14:10:23-06:00",
        "duration": 13223,
        "date": "2018-07-25",
        "tz": -7,
        "tz_str": "tsMT",
        "type": "regular",
        "location": "(Eagle, ID?)",
        "on_the_clock": False,
        "locked": 0,
        "notes": "This is a test",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        },
        "attached_files": [
          50692,
          44878
        ],
        "last_modified": "1970-01-01T00:00:00+00:00"
      }
    }
  },
  "more": False,
  "supplemental_data": {
    "jobcodes": {
      "17288283": {
        "id": 17288283,
        "parent_id": 0,
        "assigned_to_all": False,
        "billable": False,
        "active": True,
      },
      "18080900": {
        "id": 18080900,
        "parent_id": 17288279,
        "assigned_to_all": False,
        "billable": False,
        "active": True,
      },
      "17288279": {
        "id": 17288279,
        "parent_id": 0,
        "assigned_to_all": False,
        "billable": False,
        "active": True,
      }
    },
    "users": {
      "1242515": {
        "id": 1242515,
        "first_name": "Alexander",
        "last_name": "Luzzana",
        "group_id": 144959,
        "active": True,
      },
      "1242509": {
        "id": 1242509,
        "first_name": "Courtney",
        "last_name": "Ballenger",
        "group_id": 144961,
        "active": True,
      }
    },
    "customfields": {
      "19142": {
        "id": 19142,
        "required": False,
        "type": "timesheet",
      },
      "19144": {
        "id": 19144,
        "required": False,
        "type": "timesheet",
      }
    },
    "files": {
      "50692": {
        "id": 50692,
        "uploaded_by_user_id": 1242515,
        "file_name": "minion.jpg",
        "active": True,
      },
      "44878": {
        "id": 44878,
        "uploaded_by_user_id": 1242515,
        "file_name": "minion.jpg",
        "active": True,
      }
    }
  }
}
    
mock_jobcodes_data = {
 "results": {
  "jobcodes": {
   "17288279": {
    "id": 17288279,
    "parent_id": 0,
    "assigned_to_all": False,
    "billable": False,
    "active": True,
    "type": "regular",
    "has_children": False,
    "billable_rate": 0,
    "short_code": "asm",
    "name": "Assembly Line",
    "last_modified": "2018-07-12T21:13:14+00:00",
    "created": "2018-05-28T20:18:17+00:00",
    "filtered_customfielditems": "",
    "required_customfields": [],
    "locations": [],
    "connect_with_quickbooks": True
   },
   "17288283": {
    "id": 17288283,
    "parent_id": 0,
    "assigned_to_all": False,
    "billable": True,
    "active": True,
    "type": "regular",
    "has_children": False,
    "billable_rate": 0,
    "short_code": "dev",
    "name": "Development Team",
    "last_modified": "2018-05-28T20:19:33+00:00",
    "created": "2018-05-28T20:19:33+00:00",
    "filtered_customfielditems": "",
    "required_customfields": [],
    "locations": [],
    "connect_with_quickbooks": False
   }
  }
 },
 "more": False
}

mock_schedule_calendars_list_data = {
  "results": {
    "schedule_calendars": {
      "72595": {
        "id": 72595,
        "name": "Schedule Calendar Name",
        "last_modified": "2018-07-15T19:31:57+00:00",
        "created": "2018-07-15T19:08:33+00:00"
      },
      "72597": {
        "id": 72597,
        "name": "Schedule Calendar Name2",
        "last_modified": "2018-07-15T19:33:57+00:00",
        "created": "2018-07-15T19:08:33+00:00"
      }
    }
  }
}

mock_schedule_events_data = {
  "results": {
    "schedule_events": {
      "894562": {
        "id": 894562,
        "user_id": 1283037,
        "unassigned": False,
        "schedule_calendar_id": 72595,
        "jobcode_id": 17285791,
        "start": "2018-08-08T08:00:00-06:00",
        "end": "2018-08-08T14:00:00-06:00",
        "timezone": "tsMT",
        "notes": "Some Custom Notes",
        "last_modified": "2018-08-09T17:30:54-06:00",
        "created": "2018-07-15T19:08:33-06:00",
        "customfields": {
          "19142": "Item 1",
          "19144": "Item 2"
        }
      },
      "894588": {
        "id": 894588,
        "user_id": 1283037,
        "unassigned": True,
        "schedule_calendar_id": 72595,
        "jobcode_id": 17285791,
        "start": "2018-08-09T08:00:00-06:00",
        "end": "2018-08-09T14:00:00-06:00",
        "timezone": "tsMT",
        "notes": "Some More Custom Notes",
        "last_modified": "2018-08-09T17:31:23-06:00",
        "created": "2018-07-15T19:08:34-06:00"
      }
    },
    "more": False,
    "supplemental_data": {
      "jobcodes": {
        "17285791": {
          "id": 17285791,
          "parent_id": 0,
          "assigned_to_all": False,
          "billable": False,
          "active": False,
          "type": "regular",
        }
      },
      "users": {
        "1283037": {
          "id": 1283037,
          "first_name": "Alexander",
          "last_name": "Luzzana",
          "group_id": 144959,
          "active": True,
        },
        "customfields": {
          "19142": {
            "id": 19142,
            "required": False,
            "type": "timesheet",
          },
          "19144": {
            "id": 19144,
            "required": False,
            "type": "timesheet",
          }
        }
      }
    }
  }
}
