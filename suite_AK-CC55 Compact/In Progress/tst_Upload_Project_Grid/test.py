def main():
    excel = r"C:\gitworkspace\TestAutomation-Maintenance\Test_Automation\SourceCode\suite_EKE 1C\shared\testdata\Upload_From_Controller.xls";
    #Mapping with Global scripts for Function library and key action.
    source(findFile("scripts", "Functions_AKCC.py"))
    source(findFile("scripts", "Actions.py"))
    source(findFile("scripts", "object_id.py"))
    keyAction(excel)