# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PMS_Lease_Agreement(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		lease_end_date: DF.Date
		lease_monthly_rent: DF.Currency
		lease_security_deposit: DF.Currency
		lease_start_date: DF.Date
		lease_status: DF.Literal["", "Active", "Expired"]
		lease_tenant: DF.Link
		lease_unit: DF.Link
	# end: auto-generated types

	pass
