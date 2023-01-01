import frappe
from event_booking.utils import paginate
from frappe import _



def get_context(context):
    try:
        # frappe.msgprint(
        #  msg='This file does not exist',
        #  title='Error',
        #  raise_exception=FileNotFoundError
        #   )
        frappe.msgprint(
				_("The GL Entries will be cancelled in the background, it can take a few minutes."), alert=True
			)  
        page = frappe.form_dict.page
        # check if search request
        conditions = " "
        # type, status, city = frappe.form_dict.type, frappe.form_dict.status, frappe.form_dict.city
        # if(type and status and city):
        #     conditions = f"""WHERE property_type='{type}' AND city='{city}' AND status='{status}'"""
        #     context.type = type
        #     context.status = status
        #     context.city = city
        pagination = paginate(doctype='Manage Events', page=page, conditions=conditions) #pass to pagination
        # context.cities = frappe.db.sql("""SELECT name FROM `tabCity`;""", as_dict=True)
        # context.types = frappe.db.sql("""SELECT name FROM `tabProperty Type`;""", as_dict=True)
        context.properties = pagination.get('properties')
        context.search = pagination.get('search')
        context.prev = pagination.get('prev')
        context.next = pagination.get('next')
    
    
    except Exception as e:
            frappe.local.flags.redirect_location = '/404'
            raise frappe.Redirect

    print(frappe.session)
    return context