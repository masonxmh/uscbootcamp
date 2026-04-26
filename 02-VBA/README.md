# VBA Homework: The VBA of Wall Street

This project uses VBA scripting to analyze stock market data across multiple Excel worksheets. The macro summarizes each ticker's yearly performance, applies conditional formatting, and identifies the greatest stock performance metrics for each worksheet.

## Background

The assignment asks for a VBA script that can process stock data for each year, summarize ticker-level results, and run across every worksheet in the workbook with one macro execution.

## Files

- `VBAStocks/Multiple_year_stock_data.xlsm` - main macro-enabled workbook for the final stock analysis.
- `VBAStocks/Module1.bas` - exported VBA module containing the completed stock analysis macro.
- `VBAStocks/VBA stock.docx` - project document for the VBA stock challenge.
- `VBATests/alphabetical_testing.xlsm` - smaller test workbook used while developing and validating the macro.
- `VBATests/Module1.bas` - exported test module placeholder.
- `HW guideline/README.md` - original homework instructions used as the project guideline.

## Macro Summary

The `alphabetical_testing` macro in `VBAStocks/Module1.bas`:

- Loops through every worksheet in the active workbook.
- Clears previous output from columns `I` through `R`.
- Creates a summary table with ticker, yearly change, percent change, and total stock volume.
- Calculates yearly change from opening price to closing price.
- Calculates percent change and formats the result as a percentage.
- Totals stock volume for each ticker.
- Applies green formatting to positive or zero yearly change values and red formatting to negative values.
- Finds the ticker with the greatest percent increase.
- Finds the ticker with the greatest percent decrease.
- Finds the ticker with the greatest total stock volume.
- Displays a completion message when the macro finishes.

## Output

For each worksheet, the macro writes:

- Ticker summary results in columns `I` through `L`.
- Challenge summary labels, tickers, and values in columns `O` through `Q`.

## How To Run

1. Open `VBAStocks/Multiple_year_stock_data.xlsm` in Microsoft Excel.
2. Enable macros if prompted.
3. Open the VBA editor with `Alt + F11`.
4. Confirm `Module1` is available, or import `VBAStocks/Module1.bas`.
5. Run the `alphabetical_testing` macro.

## Development Notes

- Use `VBATests/alphabetical_testing.xlsm` for faster testing on the smaller dataset.
- Run the final macro on `VBAStocks/Multiple_year_stock_data.xlsm`.
- The script is designed to handle every worksheet in the active workbook in a single run.
