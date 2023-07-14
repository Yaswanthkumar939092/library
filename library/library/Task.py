import frappe
from frappe import get_doc, new_doc
@frappe.whitelist(allow_guest=True)

def check():
    # get the last available Cancelled Task
    print(frappe.get_last_doc('Proceedings'))

    # frappe.db.set_value('Proceedings','PC-00003',{
    #     'proceedings_name':'Rohith',
    # })
    # doc.save()
    # quotation = frappe.new_doc("Proceedings")

  
    # quotation.case_type = "hello"  
    # quotation.property_right = "PR-00001"  
    # quotation.jurisdiction = "JU:00001"
    # # quotation.quotation_to="Customer"
    # quotation.proceedings_name = 'Sapna Mam'

 
    # item1 = quotation.append("case_fields")
    # item1.field= "Hanuman"
    # item1.field_type='PC-00003'

    # quotation.save()
    # doc=frappe.get_doc({
    #     'doctype':'Proceedings',
    #     'case_type':'hello',
    #     'property_right':'PR-00001',
    #     'jurisdiction':'JU:00001',
    #     'proceedings_name':'Ajay Guru',
    #     'items':[
    #         {
    #             'field':'Examine',
    #         }
    #     ],
    # })
    # doc.insert()

    # print(frappe.db.get_all('Task',pluck='name'))
    # doc=get_doc('Task','TASK-2023-00002')
    # doc.add_tag('developer')

    # doc.add_comment('Comment', text='Test Comment')
    # import frappe

#     def set_multiple_field_values(doctype, docname, field_values):
#         for field, value in field_values.items():
#             frappe.db.set_value(doctype, docname, field, value)

#     field_values = {
#     "name1": "Value 123",
#     "description": "Value 2223",
#     "status": "close"
# }
#     set_multiple_field_values("YashwanthKumar", "Lava14", field_values)

    #  doc=frappe.get_last_doc('YashwanthKumar')
    #  doc.db_set('name1', 'Nithin')
    #  doc.db_set('description','Hello Sir')

    #  print(doc.get_title())
    # frappe.delete_doc('Task','TASK-2024-00009')
    # meta = frappe.get_meta('Document')
    # print(meta.has_field('status')) # True
    # (meta.get_custom_fields()) # [field1, field2, ..]

    # doc=frappe.get_doc('Task', 'TASK-2023-00002')
    # print(doc.subject)
    # frappe.rename_doc('Task', 'TASK-2023-00003', 'TASK-2024-00009')

    # frappe.delete_doc('Task', 'TASK-2023-00004')

    # doc = frappe.new_doc('Task')
    # doc.subject = 'New Task 2'
    # doc.insert()


    # task = frappe.get_last_doc('Task')
    # print(task)
#     doc = frappe.get_doc({
#     'doctype': 'Task',
#     'task_weight': 'alter_weight',
#     'subject':'Eager'
# })
#     doc.insert()

    # doc=get_doc({
    #     'doctype':'Designation',
    #     'designation_name':'Entatatainer',
    # })
    # doc.save()
#     doc = frappe.get_doc({
#     'doctype': 'Sai',
#     'name1': 'Uma'
# })
#     doc.insert()

    # doc = frappe.get_doc('Payroll Settings')
    # print(doc.max_working_hours_against_timesheet )# Asia/Kolkata
    # d=get_doc({
    #   'doctype':'Proceedings',
    #   'case_type':'hello',
    #   'property_right':'PR-00001',
    #   'jurisdiction':'JU-00001',
    #   'proceedings_name':'Yashwanth',
    #   'items':[{
    #       'field':'raj'
    #   }]
    # })
    # d.subject= "Test"

    # d.save()


    # doc.title = 'Test'
    # print(doc.title)
    # doc.save()
    # print(doc)
    # doc.title = 'Test'
    # doc.save()
    # print(doc)
    # doc.timezone
    # doc = get_doc("YashwanthKumar",'Lava14')
    # doc.db_set('name1','SaiKUmar')
       
