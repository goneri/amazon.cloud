#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2022, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by amazon_cloud_code_generator.
# See: https://github.com/ansible-collections/amazon_cloud_code_generator

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: cloudwatch_composite_alarm
short_description: Creates and manages a composite alarm
description:
- Creates and manages a composite alarm.
- When you create a composite alarm, you specify a rule expression for the alarm that
    takes into account the alarm states of other alarms that you have created.
- The composite alarm goes into ALARM state only if all conditions of the rule are
    met.
options:
    actions_enabled:
        description:
        - Indicates whether actions should be executed during any changes to the alarm
            state.
        - The default is C(True).
        type: bool
    actions_suppressor:
        description:
        - Actions will be suppressed if the suppressor alarm is in the ALARM state.
        - ActionsSuppressor can be an AlarmName or an Amazon Resource Name (ARN) from
            an existing alarm.
        type: str
    actions_suppressor_extension_period:
        description:
        - Actions will be suppressed if WaitPeriod is active.
        - The length of time that actions are suppressed is in seconds.
        type: int
    actions_suppressor_wait_period:
        description:
        - Actions will be suppressed if ExtensionPeriod is active.
        - The length of time that actions are suppressed is in seconds.
        type: int
    alarm_actions:
        description:
        - Amazon Resource Name (ARN) of the action.
        elements: str
        type: list
    alarm_description:
        description:
        - The description of the alarm.
        type: str
    alarm_name:
        description:
        - The name of the Composite Alarm.
        type: str
    alarm_rule:
        description:
        - Expression which aggregates the state of other Alarms (Metric or Composite
            Alarms).
        type: str
    force:
        default: false
        description:
        - Cancel IN_PROGRESS and PENDING resource requestes.
        - Because you can only perform a single operation on a given resource at a
            time, there might be cases where you need to cancel the current resource
            operation to make the resource available so that another operation may
            be performed on it.
        type: bool
    insufficient_data_actions:
        description:
        - Amazon Resource Name (ARN) of the action.
        elements: str
        type: list
    ok_actions:
        description:
        - Amazon Resource Name (ARN) of the action.
        elements: str
        type: list
    state:
        choices:
        - present
        - absent
        - list
        - describe
        - get
        default: present
        description:
        - Goal state for resource.
        - I(state=present) creates the resource if it doesn't exist, or updates to
            the provided state if the resource already exists.
        - I(state=absent) ensures an existing instance is deleted.
        - I(state=list) get all the existing resources.
        - I(state=describe) or I(state=get) retrieves information on an existing resource.
        type: str
    wait:
        default: false
        description:
        - Wait for operation to complete before returning.
        type: bool
    wait_timeout:
        default: 320
        description:
        - How many seconds to wait for an operation to complete before timing out.
        type: int
author: Ansible Cloud Team (@ansible-collections)
version_added: 0.2.0
extends_documentation_fragment:
- amazon.aws.aws
- amazon.aws.ec2
"""

EXAMPLES = r"""
"""

RETURN = r"""
result:
    description:
        - When I(state=list), it is a list containing dictionaries of resource information.
        - Otherwise, it is a dictionary of resource information.
        - When I(state=absent), it is an empty dictionary.
    returned: always
    type: complex
    contains:
        identifier:
            description: The unique identifier of the resource.
            type: str
        properties:
            description: The resource properties.
            type: dict
"""

import json

from ansible_collections.amazon.aws.plugins.module_utils.core import AnsibleAWSModule
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    CloudControlResource,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    snake_dict_to_camel_dict,
)
from ansible_collections.amazon.cloud.plugins.module_utils.core import (
    ansible_dict_to_boto3_tag_list,
)


def main():

    argument_spec = dict(
        state=dict(
            type="str",
            choices=["present", "absent", "list", "describe", "get"],
            default="present",
        ),
    )

    argument_spec["alarm_name"] = {"type": "str"}
    argument_spec["alarm_rule"] = {"type": "str"}
    argument_spec["alarm_description"] = {"type": "str"}
    argument_spec["actions_enabled"] = {"type": "bool"}
    argument_spec["ok_actions"] = {"type": "list", "elements": "str"}
    argument_spec["alarm_actions"] = {"type": "list", "elements": "str"}
    argument_spec["insufficient_data_actions"] = {"type": "list", "elements": "str"}
    argument_spec["actions_suppressor"] = {"type": "str"}
    argument_spec["actions_suppressor_wait_period"] = {"type": "int"}
    argument_spec["actions_suppressor_extension_period"] = {"type": "int"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["present", "absent", "list", "describe", "get"],
        "default": "present",
    }
    argument_spec["wait"] = {"type": "bool", "default": False}
    argument_spec["wait_timeout"] = {"type": "int", "default": 320}
    argument_spec["force"] = {"type": "bool", "default": False}

    required_if = [
        ["state", "present", ["alarm_name", "alarm_rule"], True],
        ["state", "absent", ["alarm_name"], True],
        ["state", "get", ["alarm_name"], True],
    ]
    mutually_exclusive = []

    module = AnsibleAWSModule(
        argument_spec=argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )
    cloud = CloudControlResource(module)

    type_name = "AWS::CloudWatch::CompositeAlarm"

    params = {}

    params["actions_enabled"] = module.params.get("actions_enabled")
    params["actions_suppressor"] = module.params.get("actions_suppressor")
    params["actions_suppressor_extension_period"] = module.params.get(
        "actions_suppressor_extension_period"
    )
    params["actions_suppressor_wait_period"] = module.params.get(
        "actions_suppressor_wait_period"
    )
    params["alarm_actions"] = module.params.get("alarm_actions")
    params["alarm_description"] = module.params.get("alarm_description")
    params["alarm_name"] = module.params.get("alarm_name")
    params["alarm_rule"] = module.params.get("alarm_rule")
    params["insufficient_data_actions"] = module.params.get("insufficient_data_actions")
    params["ok_actions"] = module.params.get("ok_actions")

    # The DesiredState we pass to AWS must be a JSONArray of non-null values
    _params_to_set = {k: v for k, v in params.items() if v is not None}

    # Only if resource is taggable
    if module.params.get("tags") is not None:
        _params_to_set["tags"] = ansible_dict_to_boto3_tag_list(module.params["tags"])

    params_to_set = snake_dict_to_camel_dict(_params_to_set, capitalize_first=True)

    # Ignore createOnlyProperties that can be set only during resource creation
    create_only_params = ["alarm_name"]

    # Necessary to handle when module does not support all the states
    handlers = ["create", "read", "update", "delete", "list"]

    state = module.params.get("state")
    identifier = ["alarm_name"]

    results = {"changed": False, "result": {}}

    if state == "list":
        if "list" not in handlers:
            module.exit_json(
                **results, msg=f"Resource type {type_name} cannot be listed."
            )
        results["result"] = cloud.list_resources(type_name, identifier)

    if state in ("describe", "get"):
        if "read" not in handlers:
            module.exit_json(
                **results, msg=f"Resource type {type_name} cannot be read."
            )
        results["result"] = cloud.get_resource(type_name, identifier)

    if state == "present":
        results = cloud.present(
            type_name, identifier, params_to_set, create_only_params
        )

    if state == "absent":
        results["changed"] |= cloud.absent(type_name, identifier)

    module.exit_json(**results)


if __name__ == "__main__":
    main()
