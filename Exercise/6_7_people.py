
ppl1={'name':'nagu',
      'num':'7993503614'
      }
ppl2={'name':'mouli',
      'num':'2930012323'
      }
ppl=[ppl2,ppl1]
for p in ppl:
    for key,value in p.items():
        print(f"{key}:{value}")