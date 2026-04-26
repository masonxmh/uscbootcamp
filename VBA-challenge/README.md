# VBA Challenge

This project contains a VBA macro for analyzing stock market worksheet data across multiple years. The macro loops through each worksheet in the workbook, summarizes ticker-level performance, and highlights yearly gains and losses.

## Files

- `VBAStocks/Multiple_year_stock_data.xlsm` - main workbook for the stock analysis.
- `VBAStocks/Module1.bas` - exported VBA module containing the stock analysis macro.
- `VBAStocks/VBA stock.docx` - project document.
- `VBATests/alphabetical_testing.xlsm` - smaller workbook used for testing.
- `VBATests/Module1.bas` - exported test module placeholder.

## Macro Summary

The `alphabetical_testing` macro:

- Runs through every worksheet in the active workbook.
- Creates a summary table with ticker, yearly change, percent change, and total stock volume.
- Applies conditional formatting to yearly change values.
- Calculates the greatest percent increase, greatest percent decrease, and greatest total volume.
- Displays a completion message when the analysis is finished.

## How To Run

1. Open `VBAStocks/Multiple_year_stock_data.xlsm` in Microsoft Excel.
2. Enable macros if prompted.
3. Open the VBA editor with `Alt + F11`.
4. Confirm `Module1` is loaded, or import `VBAStocks/Module1.bas`.
5. Run the `alphabetical_testing` macro.

## Output

For each worksheet, the macro writes summary results into columns `I` through `L` and challenge summary values into columns `O` through `Q`.
