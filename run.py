from flask_app import app
import gspread

if __name__ == '__main__':
    app.run(debug=True,port=6969)
    # account=gspread.service_account('/home/abodi-massarwa/website_final_project/secret_files/credentials.json')
    # sheet=account.open_by_url('https://docs.google.com/spreadsheets/d/1fs_FeivOv-LXOQ89OIug1PVZw1X3LqE7Dul0t8JsaDw/edit?gid=0#gid=0')
    # print(sheet.worksheet('Players&Valuations').get_all_records())# TODO success !!
    # print(sheet.worksheet('Categories').get_values()[1])# TODO success !!!