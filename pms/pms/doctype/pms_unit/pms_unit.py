# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class PMS_Unit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		unit_floor: DF.Int
		unit_number: DF.Data
		unit_property: DF.Link
		unit_rent_amount: DF.Currency
		unit_size: DF.Float
		unit_status: DF.Literal["", "Available", "Occupied", "Maintenance"]
	# end: auto-generated types

	pass
