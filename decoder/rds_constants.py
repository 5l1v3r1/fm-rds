#!/usr/bin/env python

# page 77, Annex F in the standard
pty_table=[
	"None",
	"News",
	"Current Affairs",
	"Information",
	"Sport",
	"Education",
	"Drama",
	"Cultures",
	"Science",
	"Varied Speech",
	"Pop Music",
	"Rock Music",
	"Easy Listening",
	"Light Classics M",
	"Serious Classics",
	"Other Music",
	"Weather & Metr",
	"Finance",
	"Children's Progs",
	"Social Affairs",
	"Religion",
	"Phone In",
	"Travel & Touring",
	"Leisure & Hobby",
	"Jazz Music",
	"Country Music",
	"National Music",
	"Oldies Music",
	"Folk Music",
	"Documentary",
	"Alarm Test",
	"Alarm-Alarm!"];

# page 71, Annex D, table D.1 in the standard */
pi_country_codes=[
	["DE","GR","MA","__","MD"],
	["DZ","CY","CZ","IE","EE"],
	["AD","SM","PL","TR","__"],
	["IL","CH","VA","MK","__"],
	["IT","JO","SK","__","__"],
	["BE","FI","SY","__","UA"],
	["RU","LU","TN","__","__"],
	["PS","BG","__","NL","PT"],
	["AL","DK","LI","LV","SI"],
	["AT","GI","IS","LB","__"],
	["HU","IQ","MC","__","__"],
	["MT","GB","LT","HR","__"],
	["DE","LY","YU","__","__"],
	["__","RO","ES","SE","__"],
	["EG","FR","NO","BY","BA"]];

# page 72, Annex D, table D.2 in the standard */
coverage_area_codes=[
	"Local",
	"International",
	"National",
	"Supra-regional",
	"Regional 1",
	"Regional 2",
	"Regional 3",
	"Regional 4",
	"Regional 5",
	"Regional 6",
	"Regional 7",
	"Regional 8",
	"Regional 9",
	"Regional 10",
	"Regional 11",
	"Regional 12"];

rds_group_acronyms=[
	"BASIC",
	"PIN/SL",
	"RT",
	"AID",
	"CT",
	"TDC",
	"IH",
	"RP",
	"TMC",
	"EWS",
	"___",
	"___",
	"___",
	"___",
	"EON",
	"___"];

# page 74, Annex E, table E.1 in the standard: that's the ASCII table!!! */

# see page 84, Annex J in the standard */
language_codes=[
	"Unkown/not applicable",
	"Albanian",
	"Breton",
	"Catalan",
	"Croatian",
	"Welsh",
	"Czech",
	"Danish",
	"German",
	"English",
	"Spanish",
	"Esperanto",
	"Estonian",
	"Basque",
	"Faroese",
	"French",
	"Frisian",
	"Irish",
	"Gaelic",
	"Galician",
	"Icelandic",
	"Italian",
	"Lappish",
	"Latin",
	"Latvian",
	"Luxembourgian",
	"Lithuanian",
	"Hungarian",
	"Maltese",
	"Dutch",
	"Norwegian",
	"Occitan",
	"Polish",
	"Portuguese",
	"Romanian",
	"Romansh",
	"Serbian",
	"Slovak",
	"Slovene",
	"Finnish",
	"Swedish",
	"Turkish",
	"Flemish",
	"Walloon"];

# see page 12 in ISO 14819-1 */
tmc_duration=[
	["no duration given", "no duration given"],
	["15 minutes", "next few hours"],
	["30 minutes", "rest of the day"],
	["1 hour", "until tomorrow evening"],
	["2 hours", "rest of the week"],
	["3 hours", "end of next week"],
	["4 hours", "end of the month"],
	["rest of the day", "long period"]];

# optional message content, data field lengths and labels
# see page 15 in ISO 14819-1 */
optional_content_lengths=[3,3,5,5,5,8,8,8,8,11,16,16,16,16,0,0];

label_descriptions=[
	"Duration",
	"Control code",
	"Length of route affected",
	"Speed limit advice",
	"Quantifier",
	"Quantifier",
	"Supplementary information code",
	"Explicit start time",
	"Explicit stop time",
	"Additional event",
	"Detailed diversion instructions",
	"Destination",
	"RFU (Reserved for future use)",
	"Cross linkage to source of problem, or another route",
	"Separator",
	"RFU (Reserved for future use)"];
