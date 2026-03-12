# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PMS_Maintenance_Request(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		maintenance_issue: DF.SmallText
		maintenance_priority: DF.Literal["", "Low", "Medium", "High"]
		maintenance_status: DF.Literal["", "Open", "In Progress", "Completed"]
		maintenance_tenant: DF.Link
		maintenance_unit: DF.Link
	# end: auto-generated types

	pass
