# Copyright (c) 2026, lloyd and contributors
# For license information, please see license.txt

# import frappe
from frappe.utils.nestedset import NestedSet


class PMS_Test_DocType_isTree(NestedSet):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_pms_test_doctype_istree: DF.Link | None
		rgt: DF.Int
	# end: auto-generated types

	pass
