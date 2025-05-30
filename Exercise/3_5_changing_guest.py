#here i listed ppl who i invited and ppl who are not attending and the ppl i replaced.
ppl_invite = []
ppl_invite.append('sabitha')
ppl_invite.append('vijaya')
ppl_invite.append('shekar')
ppl_invite.append('narasama')
ppl_invite.append('venkat')
ppl_invite.append('roja')
ppl_invite.append('narasaya')
ppl_not_comming = ['narasaya','narasama']
ppl_replace =['vikas', 'mouli']
print(f"ppl that i invited at first {ppl_invite}\nthe list of ppl they are busy {ppl_not_comming}\nthe ppl that i replaced with {ppl_replace}")
#here i will use the function to achive the result
#---------------------------------------------------------------------------------------------------------------------------------------------------------
ppl_invite[3] = 'vikas'
ppl_invite[6] = 'mouli'
print(f"now the new list: \n{ppl_invite}")