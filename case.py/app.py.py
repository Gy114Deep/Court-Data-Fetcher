from flask import Flask,render_template,request
from court_scraper import fetch_case
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def interface():
    if request.method=='GET':
        return render_template('case.html')
    if request.method=='POST':
        case_type=request.form.get('case_type')
        case_number=request.form.get('case_number')
        filing_year=request.form.get('filing_year')
        result=fetch_case(case_type,case_number,filing_year)
        return f"""
        <h2>Case Details:</h2>
        <li>Case Type: {case_type}</li>
        <li>Case Number: {case_number}</li>
        <li>Filing Year: {filing_year}</li>
        <li>Parties: {result['Parties']}</li>
        <li>Filing Date:{result['Filing Date']}</li>
        <li>Next Hearing:{result['Next Hearing']}</li>
        You Submitted SUCCESSFULLY ✔️ <br>
        <botton><a name="go_back" href="/"> Go Back </a></botton>"""
    if "error" in  result:
        return f"""<h2>Error:</h2>
        <button onclick="location.href='/'"> Go Back</button>"""
    return render_template('case.html')
if __name__=="__main__":
    app.run(debug=True,port=224)
