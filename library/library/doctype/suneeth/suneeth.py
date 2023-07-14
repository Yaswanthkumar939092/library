# Copyright (c) 2023, Yashwanth kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class suneeth(Document):
	pass
    # def onload(self):
    #     frappe.throw('suneeth')


# frappe.whitelist(allow_guest=True)
# def aa(D=None):
#     frappe.db.change_column_type('suni','name1', 'Text')





    # print(frappe.db.describe('Banana'))







def zz():	
	print(frappe.db.sql("""
		SELECT
			gl.name1,
			gl.age,
			acc.like
		FROM `tabsuni` gl
		LEFT JOIN `tabvini` acc
		ON gl.name1 = acc.name1
		WHERE gl.age > 19;
	"""))
		




def main():
	# frappe.db.truncate('Thirupathi')
	# frappe.db.delete('suneeth','suni06')
	# print(frappe.db.count('suneeth'))
	# print(frappe.db.exists({"doctype": "suni", "name1": "Ramdisk"}))
	timezone = frappe.db.get_single_value('suni', 'name1')
	print(timezone)




	# frappe.db.set_value('suneeth','suni06','d','new subject')
	# frappe.db.set_value('suneeth','suni06',{
	# 	'd':'Dumpeti',
	# 	'a':'Sai',
	# 	'b':'Kumar'

	# })






	# print(frappe.db.get_single_value('Proceedings','proceedings_name'))
	# doc=frappe.db.get_all('Proceedings',filters={
	# 	'proceedings_name': ['like', 'Ra%']
	# })
	# print(doc)




def eeS():
	doc=frappe.db.get_value('Proceedings','PC-00008','proceedings_name')
	print(doc)






	# doc=frappe.db.get_all('Proceedings',filters={
	# 	'proceedings_name': ['like', 'Ra%']
	# })
	# print(doc)




# 	print(frappe.db.get_list('Task', filters={
#     'subject': ['like', '%New%']
# }))




# 	print(frappe.db.get_list('suneeth', filters=[[
#     'date', 'between', ['2023-07-07', '2023-07-20']
# ]]))




	# doc=frappe.get_all('Proceedings','PC-00008')
	# doc.proceedings_name="Teja"
	# doc.insert(ignore_permissions=True)




	# doc=frappe.new_doc('Proceedings')
	# doc.case_type="hello"
	# doc.property_right="PR-00001"
	# doc.jurisdiction="JU-00001"
	# doc.proceedings_name="LavaRaju"
	# ls=doc.append("case_fields")
	# ls.field="Or"
	# doc.insert(ignore_mandatory=True)





	# doc=frappe.get_doc('suneeth','suni03')
	# doc.add_comment('Comment',text="Hi Suneeth How Do You Want")
	# new_items = frappe.get_doc({
    # "doctype": "Proceedings",
    # "case_type": "hello",
    # "property_right": "PR-00001",
    # "jurisdiction": "JU-00001",
    # "proceedings_name": "Ramesh",
    # "items": [
    #     {
    #         "field": "Or",
    #     }
    # ]
	# })
	# new_items.insert(ignore_permissions=True)






# frappe.insert(new_items)

	# print(frappe.db.get_list('suneeth',
    # fields=['count(d) as count']
    # ))



	# print(frappe.db.get_list('suneeth',pluck='d'))


def dd():
	doc=frappe.get_doc('suni','823df2ac90')
	doc.db_update('age',23)
	
	# doc.insert()

	
	# meta=frappe.get_meta('suneeth')
	# for x in meta.fields:
    #         if x.fieldname=='name':
    #             pass
    #         else:
    #             print(frappe.db.set_value('suneeth','suni03','d','Teja'))



	# for x in meta.fields:
	# 	c=x
	# 	print(c.name)
            # if x.fieldname=='d':
            #     return "Yashwanth Kumar"
            # else:
            #     return 'KAMAL SINGH'




	# frappe.rename_doc('suneeth','suni01','yash01')



	# frappe.delete_doc('suneeth','suni02')

def cc():
	doc=frappe.new_doc('suni')
	doc.name1='Ramdisk'
	doc.save()


# def bb():
# 	task=frappe.get_last_doc('suni')
# 	print(task.name1)



	# doc=frappe.get_doc({
	# 	'doctype': 'suneeth',
	# 	'd': 'aa',
    # })
	# doc.insert()



	# doc.timezone
	# doc.b='hooka'
	# doc.a='Saineth'
	# doc.d="gadda"
	# doc.save()

# def aa():
# 	return frappe.db.sql("""SELECT * FROM `tabsuni`;""",as_dict=True)
	# return doc






    # ##### WE CAN ADD FIELD BY USING THIS FIELD #####
def vv():
    doc=frappe.get_doc("DocType","suni")
    doc.append("fields",{
        "label":'ff',
        "fieldname":'d',
        "fieldtype":'Data',
        
        "reqd":0
	})
    doc.save()

