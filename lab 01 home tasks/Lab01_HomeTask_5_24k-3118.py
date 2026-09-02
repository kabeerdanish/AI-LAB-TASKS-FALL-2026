rules={
    'IT Support':('wifi','password'),
    'Finance':('fee','scholarship'),
    'Academics':('grade','course'),
    'Library':('book','issue')
}

complaints=[
    ("wifi is not working in lab",'IT Support'),
    ("pc password required",'IT Support'),
    ("give me fee chalan",'Finance'),
    ("i need a scholarship ",'Finance'),
    ("grade sheet issue in exam",'Academics'),
    ("course registration failed",'Academics'),
    ("I need a book",'Library'),
    ("canteen food quality is bad",'General Office')
]

def route(complaint,rules,fallback='General Office'):
    comp_lower=complaint.lower()
    for dept,keywords in rules.items():
        for kw in keywords:
            if kw in comp_lower:
                return dept
    return fallback

def evaluate(*results,**info):
    correct=results.count(True)
    total=len(results)
    acc=(correct/total)*100
    print(f"\nAccuracy: {acc:.2f}%")
    print("Analyst info:",info)

dept_counts={}
res_list=[]

print("Complaint Routing Details:")
for text,true_dept in complaints:
    pred_dept=route(text,rules)
    is_correct = (pred_dept==true_dept)
    res_list.append(is_correct)
    
    dept_counts[pred_dept]=dept_counts.get(pred_dept,0)+1
    print(f"Txt: {text} | Pred: {pred_dept} | Correct: {is_correct}")

print("\nDept Counts:",dept_counts)
evaluate(*res_list,analyst='Khadeejah')