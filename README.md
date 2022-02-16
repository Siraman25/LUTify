# LUTify
## A convenient tool for the creation of lookup tables

This tool was created to easily create LUTs for assembly programming.

It is currently CLI-only and is controlled by the use of arguments.
Following arguments are supported:
* -h, --help --> Shows help
* -t integer, --tab=integer --> Set tab amount, standard: 1
* -p "string", --pref="string" --> Set prefix string, standard: "dc.b"
* -P "string", --posf="string" --> Set postfix string, standard: "T"
* -r integer, --rows=integer --> Amount of rows, standard: 128
* -b integer, --begin=integer --> First value of range, standard: 0
* -e integer, --end=integer --> Last value of range, standard: 100
* -a, --additional --> Additional row at the end with same value of last row, standard: null
* -o "string", --output="string" --> Output file, standard: null

#### Usage (from Linux-CLI)
`$ python3 LUTify --tab=? --pref="???" --posf="???" --rows=? --begin=? --end=? --output="???"`

Where `?` is an integer and `???` is a string.

You need to make sure that python3 is installed.

---

## Changelog

* Version 1.0: Added basic functionality and documentation