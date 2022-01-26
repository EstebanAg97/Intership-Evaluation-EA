import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


stocks = pd.read_excel('CarSalesDataForReports.xlsx', sheet_name='Stock')
invoices = pd.read_excel('CarSalesDataForReports.xlsx', sheet_name='Invoices')
invoiceLines = pd.read_excel('CarSalesDataForReports.xlsx', sheet_name='InvoiceLines')
colors = pd.read_excel('CarSalesDataForReports.xlsx', sheet_name='Colors')
#Exercise 3 - Queries
#print("Reversed sorted List C based on index 1: % s" % (sorted(C, key=itemgetter(1), reverse=True)))

def firstQuery():
    #First Quarter Query
    brandSales = []
    print("------------Top 3 Most Sold Brands during the Q1 2015--------------")
    #Filling The list used to Show the info afterwards
    for car in stocks.index:
           if [stocks["Make"][car],0] not in brandSales:
               brandSales.append([stocks["Make"][car],0])

    for i in invoices.index:
        aux = invoices['InvoiceDateKey'][i]
        if aux >= 20150100 and aux <= 20150330:
            for j in invoiceLines.index:
                aux_1 = invoiceLines['InvoiceID'][j]
                if aux_1 == (invoices['InvoiceID'][i]):
                    carBrand = stocks['Make'][(invoiceLines['StockID'][j])+1]
                    for x in brandSales:
                        #Adding to the existant car registered in the list
                        if x[0] == carBrand:
                            x[1]+=1
                    #print("Invoice ID:",(invoices['InvoiceID'][i]),"-",aux," Stock Id:",invoiceLines['StockID'][j]," Brand: ",carBrand)

    # Sorting The List
    brandSales.sort(key=lambda x: x[1],reverse=True)
    index = 0
    while index <= 2:
        print("Brand:",brandSales[index][0],"- Units:",brandSales[index][1])
        index+=1

    #Third Quarter Query
    brandSalesQ3 = []
    print("------------Top 3 Most Sold Brands during the Q3 2015--------------")
    # Filling The list used to Show the info afterwards
    for car in stocks.index:
        if [stocks["Make"][car], 0] not in brandSalesQ3:
            brandSalesQ3.append([stocks["Make"][car], 0])

    for i in invoices.index:
        aux = invoices['InvoiceDateKey'][i]
        if aux >= 20150700 and aux <= 20150930:
            for j in invoiceLines.index:
                aux_1 = invoiceLines['InvoiceID'][j]
                if aux_1 == (invoices['InvoiceID'][i]):
                    carBrand = stocks['Make'][(invoiceLines['StockID'][j]) + 1]
                    for x in brandSalesQ3:
                        #Adding to the existant car registered in the list
                        if x[0] == carBrand:
                            x[1] += 1
                    # print("Invoice ID:",(invoices['InvoiceID'][i]),"-",aux," Stock Id:",invoiceLines['StockID'][j]," Brand: ",carBrand)

    # Sorting The List
    brandSalesQ3.sort(key=lambda x: x[1], reverse=True)
    index = 0
    while index <= 2:
        print("Brand:", brandSalesQ3[index][0], "- Units:", brandSalesQ3[index][1])
        index += 1


def secondQuery(year):
    var1 = 1
    var2 = 3
    #These Variables are used to set the Quarters Dynamically
    for x in range(1,5):
        start = str(year) + "0" + str(var1) + "00"
        end = str(year) + "0" + str(var2) + "30"
        #Exception when in the last quarter to avoid failures because of concanting the months 10, 11 and 12
        if x == 4:
            start = str(year) + str(var1) + "00"
            end = str(year) +  str(var2) + "30"

        ColorSales = []
        print("------------Most Sold Colors During Quarter",x,"Year",year,"--------------")

        #Filling The list used to Show the info afterwards
        for color in colors.index:
            if [colors["ColorID"][color],colors["Color"][color], 0] not in ColorSales:
                ColorSales.append([colors["ColorID"][color],colors["Color"][color], 0])

        #Loop for searching every Sale
        for i in invoices.index:
            aux = invoices['InvoiceDateKey'][i]
            if aux >= int(start) and aux <= int(end):
                for j in invoiceLines.index:
                    aux_1 = invoiceLines['InvoiceID'][j]
                    if aux_1 == (invoices['InvoiceID'][i]):
                        for y in stocks.index:
                            if stocks["StockID"][y] == (invoiceLines['StockID'][j]):
                                colorId = stocks['ColorID'][y]
                                for x in ColorSales:
                                    # Adding to the existant car registered in the list
                                    if x[0] == colorId:
                                        x[2] += 1

        #Skipping to next Quarter by adding 3 months to each variable
        var1 += 3
        var2 += 3

        # Sorting The List
        ColorSales.sort(key=lambda x: x[2], reverse=True)
        index = 0
        while index <= 2:
            print("Color:", ColorSales[index][1], "- Units:", ColorSales[index][2])
            index += 1
print("================ Third Excercise ===============\n")
print("\n================ First Query ===============\n")
firstQuery()
print("\n================ Second Query ===============\n")
secondQuery(2012)
secondQuery(2013)
secondQuery(2014)
secondQuery(2015)