# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import streamlit as st

st.title('Stage Property')

st.subheader('Stamp-Duty Calculator')
st.write('Reference tool for estimating stamp duty')

#st.dropdown 'language selector'

def calc_stampduty(_salePrice, _dutyType, _propertyType):
    salePrice = _salePrice
    dutyType = _dutyType
    propertyType = _propertyType
    errormsg = ''


    if dutyType == 'First Home Buyer' and propertyType == 'New or Established Home':
        if salePrice <= 430000:
            stampduty = 0
        if salePrice > 430000:
            stampduty = (salePrice - 430000) * 0.1919
        if salePrice > 530000:
            dutyType = 'General'
            
    if dutyType == 'First Home Buyer' and propertyType == 'Vacant Land':
        if salePrice <= 300000:
            stampduty = 0
        if salePrice > 300000:
            stampduty = (salePrice - 300000) * 0.1301
        if salePrice > 400000:
            dutyType = 'General'


    if dutyType == 'Concessional':
        if salePrice <= 120000:
            stampduty = salePrice * 0.015
        if salePrice > 120000:
            stampduty = (salePrice - 120000) * 0.0404 + 1800
        if salePrice >  200000:
            dutyType = 'General'
            errormsg = "Concessional rate not available on property exceeding $200,000"
   
  
    if dutyType == 'General':
        if salePrice <= 120000:
            stampduty = salePrice * 0.019
        if salePrice > 120000:
            stampduty = (salePrice - 120000) * 0.0285 + 2280
        if salePrice > 150000:
            stampduty = (salePrice - 150000) * 0.0380 + 3135
        if salePrice > 360000:
            stampduty = (salePrice - 360000) * 0.0475 + 11115
        if salePrice >  725000:
            stampduty = (salePrice - 725000) * 0.0515 + 28453

    
    return stampduty, errormsg

#Test-------
# salePrice = 465000
# dutyType = 'First Home Buyer'
# propertyType = 'New or Established Home'

# stampDuty, errormsg = calc_stampduty(salePrice, dutyType, propertyType)

#Test-------

propertyType = st.selectbox('Property Type', ['New or Established Home', 'Vacant Land'])
dutyType = st.selectbox('Duty Type', ['General', 'First Home Buyer', 'Concessional'])
salePrice = st.slider("Sale Price", 0, 2000000, 500000, 1000)

stampDuty, errormsg = calc_stampduty(salePrice, dutyType, propertyType)

st.subheader('Estimated Stamp Duty: $' + str(stampDuty))


