#!/usr/bin/env python
# coding: utf-8

# In[2]:


property_transfer_xml = """

<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';

//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';

//urn:multiCall/sessionId['?']</con:targetPath>

"""
splited_row=property_transfer_xml.split("con:targetType>")
print(splited_row[1])

splited_row=property_transfer_xml.split("con:targetType>")
print(splited_row[1])
result=splited_row[1].strip("/")
result=result[:-1]
print(result)


# In[ ]:





# In[ ]:




