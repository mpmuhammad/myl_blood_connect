app_name = "myl_blood_connect"
app_title = "MYL Blood Connect"
app_publisher = "Zoul Technologies Pvt Ltd"
app_description = "Frappe App for collecting members blood group information"
app_email = "erp@zoul.one"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "myl_blood_connect",
# 		"logo": "/assets/myl_blood_connect/logo.png",
# 		"title": "MYL Blood Connect",
# 		"route": "/myl_blood_connect",
# 		"has_permission": "myl_blood_connect.api.permission.has_app_permission",
# 	}
# ]

# The dock, the rail down the left of the desk, is a document rather than a hook. Author it in
# Manage Dock on a developer-mode site and press Export to App, and it is written to
# `myl_blood_connect/dock/myl_blood_connect/myl_blood_connect.json` for git to carry. An app that ships none has no
# rail: its sidebar gets a switcher in the header instead.
#
# A companion app, one that extends a host app rather than standing on its own, says so with
# `mount_on` on that same record, and its entries are appended to the host's rail. Mounting keeps
# the companion off the apps screen, so it takes precedence over any add_to_apps_screen above.

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/myl_blood_connect/css/myl_blood_connect.css"
# app_include_js = "/assets/myl_blood_connect/js/myl_blood_connect.js"

# include js, css files in header of web template
# web_include_css = "/assets/myl_blood_connect/css/myl_blood_connect.css"
# web_include_js = "/assets/myl_blood_connect/js/myl_blood_connect.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "myl_blood_connect/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_kanban_js = {"doctype" : "public/js/doctype_kanban.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "myl_blood_connect/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# automatically load and sync documents of this doctype from downstream apps
# importable_doctypes = [doctype_1]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "myl_blood_connect.utils.jinja_methods",
# 	"filters": "myl_blood_connect.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "myl_blood_connect.install.before_install"
# after_install = "myl_blood_connect.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "myl_blood_connect.uninstall.before_uninstall"
# after_uninstall = "myl_blood_connect.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "myl_blood_connect.utils.before_app_install"
# after_app_install = "myl_blood_connect.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "myl_blood_connect.utils.before_app_uninstall"
# after_app_uninstall = "myl_blood_connect.utils.after_app_uninstall"

# Build
# ------------------
# To hook into the build process

# after_build = "myl_blood_connect.build.after_build"

# To hook into the build process of other apps
# The list of apps being built is passed as an argument

# after_app_build = "myl_blood_connect.build.after_app_build"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "myl_blood_connect.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["myl_blood_connect.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"myl_blood_connect.tasks.all"
# 	],
# 	"daily": [
# 		"myl_blood_connect.tasks.daily"
# 	],
# 	"hourly": [
# 		"myl_blood_connect.tasks.hourly"
# 	],
# 	"weekly": [
# 		"myl_blood_connect.tasks.weekly"
# 	],
# 	"monthly": [
# 		"myl_blood_connect.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "myl_blood_connect.install.before_tests"

# Extend DocType Class
# ------------------------------
#
# Specify custom mixins to extend the standard doctype controller.
# extend_doctype_class = {
# 	"Task": "myl_blood_connect.custom.task.CustomTaskMixin"
# }

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "myl_blood_connect.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "myl_blood_connect.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["myl_blood_connect.utils.before_request"]
# after_request = ["myl_blood_connect.utils.after_request"]

# Job Events
# ----------
# before_job = ["myl_blood_connect.utils.before_job"]
# after_job = ["myl_blood_connect.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"myl_blood_connect.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

