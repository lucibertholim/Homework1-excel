Sub stockmarket():

' LOOP THROUGH ALL SHEETS

For Each ws In Worksheets

    'Assigning variables for last row and last column
    Dim LastRow As Double
    Dim LastColumn As Double
    
    'Determine LastRow and LastColumn
           
    LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    LastColumn = ws.Cells(1, Columns.Count).End(xlToLeft).Column
    
    
    'Sorting table by Ticker then by date
    With ws.Sort
     .SortFields.Add Key:=Range("A1"), Order:=xlAscending
     .SortFields.Add Key:=Range("B1"), Order:=xlAscending
     .SetRange Range(Cells(1, 1).Address(), Cells(LastRow, LastColumn).Address())
     .Header = xlYes
     .Apply
    End With
    
    ' setting names to columns
    ws.Cells(1, 9).Value = "Ticker"
    ws.Cells(1, 10).Value = "Yearly Change"
    ws.Cells(1, 11).Value = "Percent Change"
    ws.Cells(1, 12).Value = "Total Stock Volume"
    
    ' CALCULATING TOTAL VOLUME
        
        ' creating variable for total volume
    Dim totalvolume As Double
        totalvolume = 0
        
        ' Calculating volume according to the Ticker name in first column
    
    For I = 2 To LastRow
         
        
        If ws.Cells(I, 1).Value = ws.Cells(I + 1, 1).Value Then
        totalvolume = totalvolume + ws.Cells(I, 7).Value
        Else
        totalvolume = totalvolume + ws.Cells(I, 7).Value
        
        ' Creating rows in another table with ticker names, and assigning values according to the ticker volume
        
          For j = 2 To 10000
          
        ' trying to make algotithm faster with first IF
          
        If ws.Cells(j, 12).Value = "" And ws.Cells(j - 1, 12).Value = "" Then
        Exit For
        
        ElseIf ws.Cells(j, 12).Value = "" And ws.Cells(j - 1, 12).Value = "Total Stock Volume" Then
        ws.Cells(j, 12).Value = totalvolume
        ws.Cells(j, 9).Value = ws.Cells(I, 1).Value
        Exit For
                
        ElseIf ws.Cells(j, 12) = "" And ws.Cells(j - 1, 12) <> totalvolume And ws.Cells(j - 1, 12) <> "Total Stock Volume" Then
        ws.Cells(j, 12) = totalvolume
        ws.Cells(j, 9) = ws.Cells(I, 1).Value
        Exit For
                 
            
        End If
        Next j
        totalvolume = 0
        End If
        
         
        Next I

    ' CALCULATING YEARLY CHANGE
    

    ' creating variable for start and end price
    Dim startprice As Double
    Dim endprice As Double
    Dim percentchange As Double
    Dim yearlychange As Double
    
    ' Determining last row for the table just created in right side
    
     Dim LastRow2 As Double
    
     LastRow2 = ws.Cells(Rows.Count, 9).End(xlUp).Row
    
    
    ' determining start and end price according to the Ticker name in first column
    For a = 2 To LastRow
                
        If ws.Cells(a, 1).Value <> ws.Cells(a - 1, 1) Then
        startprice = ws.Cells(a, 3).Value
            
        ElseIf ws.Cells(a, 1).Value = ws.Cells(a - 1, 1) And ws.Cells(a, 1).Value <> ws.Cells(a + 1, 1) And startprice <> 0 Then
        endprice = ws.Cells(a, 6).Value
        yearlychange = endprice - startprice
        percentchange = (endprice - startprice) / startprice
      
          ' Assigning values to the other table just created according to the ticker volume
            For b = 2 To LastRow2
        
            If ws.Cells(b, 9).Value = ws.Cells(a, 1).Value Then
            ws.Cells(b, 11).Value = percentchange
            ws.Cells(b, 10).Value = yearlychange
            ws.Cells(b, 11).NumberFormat = "0.00%"
            Exit For
            
        End If
        Next b

        End If
        
        Next a
        
       
     
            
     ' FORMATING CELLS
         
        
    ' Assigning colors
        
    For I = 2 To LastRow2

          If ws.Cells(I, 10).Value > 0 Then
          ws.Cells(I, 10).Interior.ColorIndex = 4
          
          Else
          ws.Cells(I, 10).Interior.ColorIndex = 3
               
           End If
           
           Next I
           
   ' HARD PART
    
    ' setting names to columns
        ws.Cells(2, 15).Value = "Greatest % Increase"
        ws.Cells(3, 15).Value = "Greatest % Decrease"
        ws.Cells(4, 15).Value = "Greatest Total Volume"
        ws.Cells(1, 16).Value = "Ticker"
        ws.Cells(1, 17).Value = "Value"
     
    Dim rangepercent As Range
    
    Dim greatestincrease As Double
    Dim greatestdecrease As Double
    
    Dim greatestincreaseRow As Long
    Dim greatestdecreaseRow As Long
    
    Dim rangevolume As Range
    Dim greatesvolume As Double
    Dim greatestvolumeRow As Long
    
    
    'Enter range for percent change
    
    Set rangepercent = ws.Range("K1:K" & LastRow2)
    
         
    
    'Determines smallest value in percent range and assign the value to the third table just created
    
    greatestincrease = Application.WorksheetFunction.Max(rangepercent)
    
    greatestincreaseRow = Application.WorksheetFunction.Match(greatestincrease, rangepercent, 0)
    
    ws.Cells(2, 17).Value = ws.Cells(greatestincreaseRow, 11).Value
    
    ws.Cells(2, 17).NumberFormat = "0.00%"
    
    ws.Cells(2, 16).Value = ws.Cells(greatestincreaseRow, 9).Value
    
    
    'Determines greatest value in percent range and assign the value to the third table just created
    
    greatestdecrease = Application.WorksheetFunction.Min(rangepercent)
    
    greatestdecreaseRow = Application.WorksheetFunction.Match(greatestdecrease, rangepercent, 0)
    
    ws.Cells(3, 17).Value = ws.Cells(greatestdecreaseRow, 11).Value
    
    ws.Cells(3, 17).NumberFormat = "0.00%"
    
    ws.Cells(3, 16).Value = ws.Cells(greatestdecreaseRow, 9).Value
    
    
    'Enter range for total volume
    
    Set rangevolume = ws.Range("L1:L" & LastRow2)
    
    'Determines greatest total volume in total volume column and assign the value to the third table just created
    
    greatesvolume = Application.WorksheetFunction.Max(rangevolume)
    
    greatesvolumeRow = Application.WorksheetFunction.Match(greatesvolume, rangevolume, 0)
    
    ws.Cells(4, 17).Value = ws.Cells(greatesvolumeRow, 12).Value
    ws.Cells(4, 16).Value = ws.Cells(greatesvolumeRow, 9).Value

           
 ' Next sheet
 
    Next ws
           
   End Sub