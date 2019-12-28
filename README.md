# Etekcity-Nutrition-Scale-Batch-Food-Uploader

Requires Python 3 with some dependencies:
  - requests
  - openpyxl
For easier setup can use Anaconda:
  - https://anaconda.org/nsaffie/etekcityapp

Purpose: Etekcity sells a neat nutrition scale, where you place a food on it, and tell it what the food is and it calculates detailed nutrition information. However, adding custom foods can be a tedious process, so I created this small and relatively stable program to allow you to work in a traditional excel format and then upload / edit the foods used by the app.

Complications: The one difficult aspect is that YOU need to get your accountid and token.

How?
- One solution is to MITM yourself.
For windows:
- Install Fiddler
- Follow instructions here: https://docs.telerik.com/fiddler/Configure-Fiddler/Tasks/ConfigureForiOS
- Once you are capturing traffic:
  - look for the record that has URL = '/cloud/v1/user/getUserConfig'
  - Click on this record and go to 'Inspectors'
  - Under the 'Headers' tab -> Miscellaneous
  - You want the values for: tk (token), and accountID
  
Other notes:
  - While it is resonable to expect accountID never changes, your token most likely does.
  - Token is likely something embedded in your current installation of the app. 
  - Therefore, the token may never/rarely change except for reinstalling and (hopefully not) updates
  
  How does this program actually help me?
  - Once you have the python environment setup and this project downloaded go to the directory that has Controller.py
  - Run: python Controller.py --token=<your token> --accountid=<your accountid> --save=<file path>.xlsx
    - This will save an excel spread sheet containing all your current custom foods
  - To add to or edit these: 
    - Modify the file accordingly
    - Run: python Controller.py --token=<your token> --accountid=<your accountid> --file=<file path with changes>.xlsx

Conditions:
  - CHANGING image associated with a food is not supported.
  - Don't put a foodID if you are adding a new record
  - Calories and Serving size must be nonnegative values
  - All other nutrition information should have value -1 if you are not using it (this encodes as optional)
  - First row (header) of Excel spreedsheet is ignored
  - You can not add any more columns (Etekcity base application only supports so many
