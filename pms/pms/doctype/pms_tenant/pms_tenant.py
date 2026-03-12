# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PMS_Tenant(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		tenant_address: DF.SmallText
		tenant_email: DF.Data
		tenant_id_number: DF.Data
		tenant_name: DF.Data
		tenant_phone: DF.Data
	# end: auto-generated types

	pass
