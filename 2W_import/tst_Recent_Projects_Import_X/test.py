def main():
    excel = r"C:\gitworkspace\KoolProg-TestAutomation\Master_Functions\Test_Automation\SourceCode\suite_EETa 2W\shared\testdata\Recent_Projects_Import_X.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions.py"))
    source(findFile("scripts", "Actions.py"))
    #source(findFile("scripts", "object_id.py"))
    keyAction(excel)
    
    