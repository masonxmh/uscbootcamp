Attribute VB_Name = "Module1"
Sub alphabetical_testing()

    
    Dim ticker As String
    
    Dim WorkSheetName As String

    Dim SummaryTableRow As Double
    
    Dim YearlyChange As Double
    
    Dim openValue As Double
    
    Dim closeValue As Double
        
    Dim tickerCount As Double
    
    Dim percentChange As Double
    
    Dim totalVolume As Double
    
    
    'Dim lastrow As Double
    
    
    'Dim ws As Worksheet
    

' Action on sheet

    For Each ws In Worksheets
    
    ws.Activate
    
    Range("I1: R100000").ClearContents
    Range("I1: R100000").ClearFormats
    

    lastrow = ws.Cells(Rows.Count, 1).End(xlUp).Row
    
    SummaryTableRow = 2
    tickerCount = 0
    totalVolume = 0
    
' Define header

    Range("I1").Value = "Ticker"
    Range("J1").Value = "Yearly Change"
    Range("K1").Value = "Percent Change"
    Range("L1").Value = "Total Stock Volume"
    
' loop start point


    For i = 2 To lastrow

        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then
        
        ticker = ws.Cells(i, 1).Value
        Range("I" & SummaryTableRow).Value = ticker
       
        'Define open & close Value
       
        openValue = Cells(i - tickerCount, 3).Value
        closeValue = Cells(i, 6).Value
        
       
        'yearly change calculation
        YearlyChange = closeValue - openValue
        Range("J" & SummaryTableRow).Value = YearlyChange
        
            
    

        'percent change
            If openValue = 0 And closeValue <> 0 Then
            percentChange = 1
            ElseIf openValue = 0 And closeValue = 0 Then
            percentChange = 0
            Else: percentChange = YearlyChange / openValue
            Range("K" & SummaryTableRow).Value = percentChange
            Range("k" & SummaryTableRow).NumberFormat = "0.00%"
            End If
        
        
        'Volume Calculation
        totalVolume = Cells(i, 7).Value + totalVolume
        Range("L" & SummaryTableRow).Value = totalVolume
       
        'reset
        
        'openValue = 0
        'closeValue = 0
        'YearlyChange = 0
        'percentChange = 0
        
        'summary table counter
        
        SummaryTableRow = SummaryTableRow + 1
        tickerCount = 0
        totalVolume = 0
        Else
       
        tickerCount = tickerCount + 1
        totalVolume = Cells(i, 7).Value + totalVolume
        
        End If
Next i
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    'Conditional Formating
  
        For j = 2 To SummaryTableRow - 1
  
            If Cells(j, 10) > 0 Or ws.Cells(j, 10) = 0 Then
            Cells(j, 10).Interior.ColorIndex = 4
            Else
            Cells(j, 10).Interior.ColorIndex = 3
            End If
  
        Next j


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'define challege part
    Dim maxPercent As Double
    Dim miniPercent As Double
    Dim maxVolume As Double

    
Range("O2").Value = "Greatest % Increase"
Range("O3").Value = "Greatest % Decrease"
Range("O4").Value = "Greatest Total Volume"
Range("P1").Value = "Ticker"
Range("Q1").Value = "Value"

maxPercent = Application.WorksheetFunction.Max(Columns("K"))
minPercent = Application.WorksheetFunction.Min(Columns("K"))
maxVolume = Application.WorksheetFunction.Max(Columns("L"))


For k = 2 To SummaryTableRow

    If Cells(k, 11).Value = maxPercent Then

    Range("Q2").Value = maxPercent
    Range("Q2").NumberFormat = "0.00%"
    Range("P2").Value = Cells(k, 9).Value
    
    ElseIf Cells(k, 11).Value = minPercent Then

    Range("Q3").Value = minPercent
    Range("Q3").NumberFormat = "0.00%"
    Range("P3").Value = Cells(k, 9).Value
    
    ElseIf Cells(k, 12).Value = maxVolume Then
    Range("Q4").Value = maxVolume
    Range("P4").Value = Cells(k, 9).Value
    End If

Next k
Next ws
    
 MsgBox (" Complete ")

End Sub

