# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Unit(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		floor: DF.Data
		unit__building: DF.Data | None
		rent_amount: DF.Data
		size_sqm: DF.Data
		status_available__occupied__maintenance: DF.Data
		unit_number: DF.Data
	# end: auto-generated types

	pass
