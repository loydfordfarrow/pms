# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		address: DF.Data
		contact_number: DF.Data
		email: DF.Data
		id_proof: DF.AttachImage
		move_in_date: DF.Date
		move_out_date: DF.Date
		tenant_name: DF.Data
	# end: auto-generated types

	pass
