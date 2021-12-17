# Calculating the Penetrance Functions
# def multiple():
#     output = pd.DataFrame(
#         columns=['ldlcfh1', 'ldlcnotfh1', 'txpfisfh1', 'txpfisnotfh1', 'cadpfisfh1', 'cadisnotfh1'])
#     for i, j in pinput.iterrows():
#         agei = j.values[0]
#         ldlci = j.values[1]
#         totalci = j.values[2]
#         clincalcad = j.values[4]
#         genderi = j.values[3]
#         onsetage = j.values[5]
#         txi = j.values[6]
#         ldlcfh1 = ldlcfh1(agei, ldlci, totalci)
#         txpfisfh1 = txpfisfh1(ldlci, agei, txi)
#         cadpfish1 = cadpfish1(clincalcad, genderi, onsetage, agei)
#         ldlcnotfh1 = ldlcnotfh1(ldlci, agei, totalci)
#         txpfisnotfh1 = txpfisnotfh1(txi)
#         cadisnotfh1 = cadisnotfh1(clincalcad, genderi, onsetage, agei)
#         output.loc[i] = [ldlcfh1, ldlcnotfh1, txpfisfh1, txpfisnotfh1, cadpfish1, cadisnotfh1]
#     return output
#
#
# # Founder Prior Probability 1
# def fpp1():
#     dna_dx1 = pinput.iloc[[0], [7]]
#     fh_prob = 0.002
#     trust = 0
#     output = [trust]  # list that the function will return
#     for item in binary:
#         if dna_dx1.values == 1 and item[0] == 0:
#             right_side = 0
#             trust = (1 - fh_prob) * right_side
#             output.append(trust)
#         else:
#             if item[0] > 0:
#                 right_side = 1
#                 trust = fh_prob * right_side
#                 output.append(trust)  # append to the list instead of printing
#             else:
#                 right_side = 1
#                 trust = (1 - fh_prob) * right_side
#                 output.append(trust)
#     return output  # return list of values
#
#
# # Founder Prior Probability 2
# def fpp2():
#     dna_dx2 = pinput.iloc[[1], [7]]
#     fh_prob = 0.002
#     trust = 0
#     output = [trust]  # list that the function will return
#     for item in binary:
#         if dna_dx2.values == 1 and item[1] == 0:
#             right_side = 0
#             trust = (1 - fh_prob) * right_side
#             output.append(trust)
#         else:
#             if item[1] > 0:
#                 right_side = 1
#                 trust = fh_prob * right_side
#                 output.append(trust)  # append to the list instead of printing
#             else:
#                 right_side = 1
#                 trust = (1 - fh_prob) * right_side
#                 output.append(trust)
#     return output  # return list of values
#
#
# # Founder Prior Probability 3
# def fpp3():
#     dna_dx3 = pinput.iloc[[2], [7]]
#     fh_prob = 0.002
#     trust = 0
#     output = [trust]  # list that the function will return
#     for item in binary:
#         if dna_dx3.values == 1 and item[2] == 0:
#             right_side = 0
#             trust = (1 - fh_prob) * right_side
#             output.append(trust)
#         else:
#             if item[2] > 0:
#                 right_side = 1
#                 trust = fh_prob * right_side
#                 output.append(trust)  # append to the list instead of printing
#             else:
#                 right_side = 1
#                 trust = (1 - fh_prob) * right_side
#                 output.append(trust)
#     return output  # return list of values
#
#
# # Transmission Probability 4
# def tp4():
#     transdna4 = pinput.iloc[[3], [7]]
#     left_side = 0
#     transprob4 = [left_side]
#     for item in binary:
#         if item[3] == 0 and transdna4.values == 1:
#             left_side = 0
#             transprob4.append(left_side)
#         else:
#             if item[0] > 0 and item[1] > 0 and item[3] > 0:
#                 multiply = 1
#                 left_side = 0.75 * multiply
#                 transprob4.append(left_side)
#             elif item[0] > 0 and item[1] > 0 and item[3] == 0:
#                 multiply = 1
#                 left_side = 0.25 * multiply
#                 transprob4.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[3] > 0:
#                 multiply = 1
#                 left_side = 0.5 * multiply
#                 transprob4.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[3] == 0:
#                 multiply = 1
#                 left_side = 0.5 * multiply
#                 transprob4.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[3] > 0:
#                 multiply = 1
#                 left_side = 0.5 * multiply
#                 transprob4.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[3] == 0:
#                 multiply = 1
#                 left_side = 0.5 * multiply
#                 transprob4.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[3] > 0:
#                 multiply = 1
#                 left_side = 0 * multiply
#                 transprob4.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[3] == 0:
#                 multiply = 1
#                 left_side = 1 * multiply
#                 transprob4.append(left_side)
#     return transprob4
#
#
# # Transmission Probability 5
# def tp5():
#     transdna5 = pinput.iloc[[4], [7]]
#     multiply = 1
#     left_side = 0
#     transprob5 = [left_side]
#     for item in binary:
#         if item[4] == 0 and transdna5.values == 1:
#             left_side = 0
#             transprob5.append(left_side)
#         else:
#             if item[0] > 0 and item[1] > 0 and item[4] > 0:
#                 left_side = 0.75 * multiply
#                 transprob5.append(left_side)
#             elif item[0] > 0 and item[1] > 0 and item[4] == 0:
#                 left_side = 0.25 * multiply
#                 transprob5.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[4] > 0:
#                 left_side = 0.5 * multiply
#                 transprob5.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[4] == 0:
#                 left_side = 0.5 * multiply
#                 transprob5.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[4] > 0:
#                 left_side = 0.5 * multiply
#                 transprob5.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[4] == 0:
#                 left_side = 0.5 * multiply
#                 transprob5.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[4] > 0:
#                 left_side = 0 * multiply
#                 transprob5.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[4] == 0:
#                 left_side = 1 * multiply
#                 transprob5.append(left_side)
#     return transprob5
#
#
# # Transmission Probability 6
# def tp6():
#     transdna6 = pinput.iloc[[5], [7]]
#     multiply = 1
#     left_side = 0
#     transprob6 = [left_side]
#     for item in binary:
#         if item[5] == 0 and transdna6.values == 1:
#             left_side = 0
#             transprob6.append(left_side)
#         else:
#             if item[0] > 0 and item[1] > 0 and item[5] > 0:
#                 left_side = 0.75 * multiply
#                 transprob6.append(left_side)
#             elif item[0] > 0 and item[1] > 0 and item[5] == 0:
#                 left_side = 0.25 * multiply
#                 transprob6.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[5] > 0:
#                 left_side = 0.5 * multiply
#                 transprob6.append(left_side)
#             elif item[0] > 0 and item[1] == 0 and item[5] == 0:
#                 left_side = 0.5 * multiply
#                 transprob6.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[5] > 0:
#                 left_side = 0.5 * multiply
#                 transprob6.append(left_side)
#             elif item[0] == 0 and item[1] > 0 and item[5] == 0:
#                 left_side = 0.5 * multiply
#                 transprob6.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[5] > 0:
#                 left_side = 0 * multiply
#                 transprob6.append(left_side)
#             elif item[0] == 0 and item[1] == 0 and item[5] == 0:
#                 left_side = 1 * multiply
#                 transprob6.append(left_side)
#     return transprob6
#
#
# # Transmission Probability 7
# def tp7():
#     transdna7 = pinput.iloc[[6], [7]]
#     multiply = 1
#     left_side = 0
#     transprob7 = [left_side]
#     for item in binary:
#         if item[6] == 0 and transdna7.values == 1:
#             left_side = 0
#             transprob7.append(left_side)
#         else:
#             if item[2] > 0 and item[5] > 0 and item[6] > 0:
#                 left_side = 0.75 * multiply
#                 transprob7.append(left_side)
#             elif item[2] > 0 and item[5] > 0 and item[6] == 0:
#                 left_side = 0.25 * multiply
#                 transprob7.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[6] > 0:
#                 left_side = 0.5 * multiply
#                 transprob7.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[6] == 0:
#                 left_side = 0.5 * multiply
#                 transprob7.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[6] > 0:
#                 left_side = 0.5 * multiply
#                 transprob7.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[6] == 0:
#                 left_side = 0.5 * multiply
#                 transprob7.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[6] > 0:
#                 left_side = 0 * multiply
#                 transprob7.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[6] == 0:
#                 left_side = 1 * multiply
#                 transprob7.append(left_side)
#
#     return transprob7
#
#
# # Transmission Probability 8
# def tp8():
#     transdna8 = pinput.iloc[[7], [7]]
#     multiply = 1
#     left_side = 0
#     transprob8 = [left_side]
#     for item in binary:
#         if item[7] == 0 and transdna8.values == 1:
#             left_side = 0
#             transprob8.append(left_side)
#         else:
#             if item[2] > 0 and item[5] > 0 and item[7] > 0:
#                 left_side = 0.75 * multiply
#                 transprob8.append(left_side)
#             elif item[2] > 0 and item[5] > 0 and item[7] == 0:
#                 left_side = 0.25 * multiply
#                 transprob8.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[7] > 0:
#                 left_side = 0.5 * multiply
#                 transprob8.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[7] == 0:
#                 left_side = 0.5 * multiply
#                 transprob8.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[7] > 0:
#                 left_side = 0.5 * multiply
#                 transprob8.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[7] == 0:
#                 left_side = 0.5 * multiply
#                 transprob8.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[7] > 0:
#                 left_side = 0 * multiply
#                 transprob8.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[7] == 0:
#                 left_side = 1 * multiply
#                 transprob8.append(left_side)
#
#     return transprob8
#
#
# # Transmission Probability 9
# def tp9():
#     transdna9 = pinput.iloc[[8], [7]]
#     multiply = 1
#     left_side = 0
#     transprob9 = [left_side]
#     for item in binary:
#         if item[8] == 0 and transdna9.values == 1:
#             left_side = 0
#             transprob9.append(left_side)
#         else:
#             if item[2] > 0 and item[5] > 0 and item[8] > 0:
#                 left_side = 0.75 * multiply
#                 transprob9.append(left_side)
#             elif item[2] > 0 and item[5] > 0 and item[8] == 0:
#                 left_side = 0.25 * multiply
#                 transprob9.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[8] > 0:
#                 left_side = 0.5 * multiply
#                 transprob9.append(left_side)
#             elif item[2] > 0 and item[5] == 0 and item[8] == 0:
#                 left_side = 0.5 * multiply
#                 transprob9.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[8] > 0:
#                 left_side = 0.5 * multiply
#                 transprob9.append(left_side)
#             elif item[2] == 0 and item[5] > 0 and item[8] == 0:
#                 left_side = 0.5 * multiply
#                 transprob9.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[8] > 0:
#                 left_side = 0 * multiply
#                 transprob9.append(left_side)
#             elif item[2] == 0 and item[5] == 0 and item[8] == 0:
#                 left_side = 1 * multiply
#                 transprob9.append(left_side)
#
#     return transprob9
#
#
# # LDL Cholesterol Penetrance Val 1
# def ldlc1():
#     ldlcage1 = pinput.iloc[0, 0]
#     ldlccheck1 = pinput.iloc[0, 1]
#     ldlctotalc1 = pinput.iloc[0, 2]
#     isfh = ldlcfh(ldlcage1, ldlccheck1, ldlctotalc1)
#     notfh = ldlcnotfh(ldlccheck1, ldlcage1, ldlctotalc1)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[0] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 2
# def ldlc2():
#     ldlcage2 = pinput.iloc[1, 0]
#     ldlccheck2 = pinput.iloc[1, 1]
#     ldlctotalc2 = pinput.iloc[1, 2]
#     isfh = ldlcfh(ldlcage2, ldlccheck2, ldlctotalc2)
#     notfh = ldlcnotfh(ldlccheck2, ldlcage2, ldlctotalc2)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[1] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 3
# def ldlc3():
#     ldlcage3 = pinput.iloc[2, 0]
#     ldlccheck3 = pinput.iloc[2, 1]
#     ldlctotalc3 = pinput.iloc[2, 2]
#     isfh = ldlcfh(ldlcage3, ldlccheck3, ldlctotalc3)
#     notfh = ldlcnotfh(ldlccheck3, ldlcage3, ldlctotalc3)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[2] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 4
# def ldlc4():
#     ldlcage4 = pinput.iloc[3, 0]
#     ldlccheck4 = pinput.iloc[3, 1]
#     ldlctotalc4 = pinput.iloc[3, 2]
#     isfh = ldlcfh(ldlcage4, ldlccheck4, ldlctotalc4)
#     notfh = ldlcnotfh(ldlccheck4, ldlcage4, ldlctotalc4)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[3] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 5
# def ldlc5():
#     ldlcage5 = pinput.iloc[4, 0]
#     ldlccheck5 = pinput.iloc[4, 1]
#     ldlctotalc5 = pinput.iloc[4, 2]
#     isfh = ldlcfh(ldlcage5, ldlccheck5, ldlctotalc5)
#     notfh = ldlcnotfh(ldlccheck5, ldlcage5, ldlctotalc5)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[4] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 6
# def ldlc6():
#     ldlcage6 = pinput.iloc[5, 0]
#     ldlccheck6 = pinput.iloc[5, 1]
#     ldlctotalc6 = pinput.iloc[5, 2]
#     isfh = ldlcfh(ldlcage6, ldlccheck6, ldlctotalc6)
#     notfh = ldlcnotfh(ldlccheck6, ldlcage6, ldlctotalc6)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[5] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 7
# def ldlc7():
#     ldlcage7 = pinput.iloc[6, 0]
#     ldlccheck7 = pinput.iloc[6, 1]
#     ldlctotalc7 = pinput.iloc[6, 2]
#     isfh = ldlcfh(ldlcage7, ldlccheck7, ldlctotalc7)
#     notfh = ldlcnotfh(ldlccheck7, ldlcage7, ldlctotalc7)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[6] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 8
# def ldlc8():
#     ldlcage8 = pinput.iloc[7, 0]
#     ldlccheck8 = pinput.iloc[7, 1]
#     ldlctotalc8 = pinput.iloc[7, 2]
#     isfh = ldlcfh(ldlcage8, ldlccheck8, ldlctotalc8)
#     notfh = ldlcnotfh(ldlccheck8, ldlcage8, ldlctotalc8)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[7] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # LDL Cholesterol Penetrance Val 9
# def ldlc9():
#     ldlcage9 = pinput.iloc[8, 0]
#     ldlccheck9 = pinput.iloc[8, 1]
#     ldlctotalc9 = pinput.iloc[8, 2]
#     isfh = ldlcfh(ldlcage9, ldlccheck9, ldlctotalc9)
#     notfh = ldlcnotfh(ldlccheck9, ldlcage9, ldlctotalc9)
#     ldlcprob = 0
#     ldlcoutput = [ldlcprob]
#     for item in binary:
#         if item[8] == 0:
#             ldlcprob = notfh
#             ldlcoutput.append(ldlcprob)
#         else:
#             ldlcprob = isfh
#             ldlcoutput.append(ldlcprob)
#     return ldlcoutput
#
#
# # TX Penetrance Val 1
# def tx1():
#     tx1 = pinput.iloc[0, 6]
#     txldlc1 = pinput.iloc[0, 1]
#     txage1 = pinput.iloc[0, 0]
#     istx = txfh(txldlc1, txage1, tx1)
#     nottx = txnotfh(tx1)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[0] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 2
# def tx2():
#     tx2 = pinput.iloc[1, 6]
#     txldlc2 = pinput.iloc[1, 1]
#     txage2 = pinput.iloc[1, 0]
#     istx = txfh(txldlc2, txage2, tx2)
#     nottx = txnotfh(tx2)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[1] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 3
# def tx3():
#     tx3 = pinput.iloc[2, 6]
#     txldlc3 = pinput.iloc[2, 1]
#     txage3 = pinput.iloc[2, 0]
#     istx = txfh(txldlc3, txage3, tx3)
#     nottx = txnotfh(tx3)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[2] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 4
# def tx4():
#     tx4 = pinput.iloc[3, 6]
#     txldlc4 = pinput.iloc[3, 1]
#     txage4 = pinput.iloc[3, 0]
#     istx = txfh(txldlc4, txage4, tx4)
#     nottx = txnotfh(tx4)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[3] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 5
# def tx5():
#     tx5 = pinput.iloc[4, 6]
#     txldlc5 = pinput.iloc[4, 1]
#     txage5 = pinput.iloc[4, 0]
#     istx = txfh(txldlc5, txage5, tx5)
#     nottx = txnotfh(tx5)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[4] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 6
# def tx6():
#     tx6 = pinput.iloc[5, 6]
#     txldlc6 = pinput.iloc[5, 1]
#     txage6 = pinput.iloc[5, 0]
#     istx = txfh(txldlc6, txage6, tx6)
#     nottx = txnotfh(tx6)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[5] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 7
# def tx7():
#     tx7 = pinput.iloc[6, 6]
#     txldlc7 = pinput.iloc[6, 1]
#     txage7 = pinput.iloc[6, 0]
#     istx = txfh(txldlc7, txage7, tx7)
#     nottx = txnotfh(tx7)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[6] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 8
# def tx8():
#     tx8 = pinput.iloc[7, 6]
#     txldlc8 = pinput.iloc[7, 1]
#     txage8 = pinput.iloc[7, 0]
#     istx = txfh(txldlc8, txage8, tx8)
#     nottx = txnotfh(tx8)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[7] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # TX Penetrance Val 9
# def tx9():
#     tx9 = pinput.iloc[8, 6]
#     txldlc9 = pinput.iloc[8, 1]
#     txage9 = pinput.iloc[8, 0]
#     istx = txfh(txldlc9, txage9, tx9)
#     nottx = txnotfh(tx9)
#     txprob = 0
#     txoutput = [txprob]
#     for item in binary:
#         if item[8] == 1:
#             txprob = istx
#             txoutput.append(txprob)
#         else:
#             txprob = nottx
#             txoutput.append(txprob)
#     return txoutput
#
#
# # CAD Penetrance Val 1
# def cad1():
#     cadclinical1 = pinput.iloc[0, 4]
#     cadgender1 = pinput.iloc[0, 3]
#     cadonsetage1 = pinput.iloc[0, 5]
#     cadage1 = pinput.iloc[0, 0]
#     iscad1 = cadfh(cadclinical1, cadgender1, cadonsetage1, cadage1)
#     isnotcad1 = cadnotfh(cadclinical1, cadgender1, cadonsetage1, cadage1)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[0] == 1:
#             cadprob = iscad1
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad1
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 2
# def cad2():
#     cadclinical2 = pinput.iloc[1, 4]
#     cadgender2 = pinput.iloc[1, 3]
#     cadonsetage2 = pinput.iloc[1, 5]
#     cadage2 = pinput.iloc[1, 0]
#     iscad2 = cadfh(cadclinical2, cadgender2, cadonsetage2, cadage2)
#     isnotcad2 = cadnotfh(cadclinical2, cadgender2, cadonsetage2, cadage2)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[1] == 1:
#             cadprob = iscad2
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad2
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 3
# def cad3():
#     cadclinical3 = pinput.iloc[2, 4]
#     cadgender3 = pinput.iloc[2, 3]
#     cadonsetage3 = pinput.iloc[2, 5]
#     cadage3 = pinput.iloc[2, 0]
#     iscad3 = cadfh(cadclinical3, cadgender3, cadonsetage3, cadage3)
#     isnotcad3 = cadnotfh(cadclinical3, cadgender3, cadonsetage3, cadage3)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[2] == 1:
#             cadprob = iscad3
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad3
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 4
# def cad4():
#     cadclinical4 = pinput.iloc[3, 4]
#     cadgender4 = pinput.iloc[3, 3]
#     cadonsetage4 = pinput.iloc[3, 5]
#     cadage4 = pinput.iloc[3, 0]
#     iscad4 = cadfh(cadclinical4, cadgender4, cadonsetage4, cadage4)
#     isnotcad4 = cadnotfh(cadclinical4, cadgender4, cadonsetage4, cadage4)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[3] == 1:
#             cadprob = iscad4
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad4
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 5
# def cad5():
#     cadclinical5 = pinput.iloc[4, 4]
#     cadgender5 = pinput.iloc[4, 3]
#     cadonsetage5 = pinput.iloc[4, 5]
#     cadage5 = pinput.iloc[4, 0]
#     iscad5 = cadfh(cadclinical5, cadgender5, cadonsetage5, cadage5)
#     isnotcad5 = cadnotfh(cadclinical5, cadgender5, cadonsetage5, cadage5)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[4] == 1:
#             cadprob = iscad5
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad5
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 6
# def cad6():
#     cadclinical6 = pinput.iloc[5, 4]
#     cadgender6 = pinput.iloc[5, 3]
#     cadonsetage6 = pinput.iloc[5, 5]
#     cadage6 = pinput.iloc[5, 0]
#     iscad6 = cadfh(cadclinical6, cadgender6, cadonsetage6, cadage6)
#     isnotcad6 = cadnotfh(cadclinical6, cadgender6, cadonsetage6, cadage6)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[5] == 1:
#             cadprob = iscad6
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad6
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 7
# def cad7():
#     cadclinical7 = pinput.iloc[6, 4]
#     cadgender7 = pinput.iloc[6, 3]
#     cadonsetage7 = pinput.iloc[6, 5]
#     cadage7 = pinput.iloc[6, 0]
#     iscad7 = cadfh(cadclinical7, cadgender7, cadonsetage7, cadage7)
#     isnotcad7 = cadnotfh(cadclinical7, cadgender7, cadonsetage7, cadage7)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[6] == 1:
#             cadprob = iscad7
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad7
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 8
# def cad8():
#     cadclinical8 = pinput.iloc[7, 4]
#     cadgender8 = pinput.iloc[7, 3]
#     cadonsetage8 = pinput.iloc[7, 5]
#     cadage8 = pinput.iloc[7, 0]
#     iscad8 = cadfh(cadclinical8, cadgender8, cadonsetage8, cadage8)
#     isnotcad8 = cadnotfh(cadclinical8, cadgender8, cadonsetage8, cadage8)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[7] == 1:
#             cadprob = iscad8
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad8
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # CAD Penetrance Val 9
# def cad9():
#     cadclinical9 = pinput.iloc[8, 4]
#     cadgender9 = pinput.iloc[8, 3]
#     cadonsetage9 = pinput.iloc[8, 5]
#     cadage9 = pinput.iloc[8, 0]
#     iscad9 = cadfh(cadclinical9, cadgender9, cadonsetage9, cadage9)
#     isnotcad9 = cadnotfh(cadclinical9, cadgender9, cadonsetage9, cadage9)
#     cadprob = 0
#     cadoutput = [cadprob]
#     for item in binary:
#         if item[8] == 1:
#             cadprob = iscad9
#             cadoutput.append(cadprob)
#         else:
#             cadprob = isnotcad9
#             cadoutput.append(cadprob)
#     return cadoutput
#
#
# # Calculating Family Probability
# def family():
#     value = 0
#     output = [value]
#     for row in binary:
#         if row.any() == 1:
#             value = 1
#             output.append(value)
#         elif row.any() == 0:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 1 Likelihood
# def person1():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[0] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 2 Likelihood
# def person2():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[1] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 3 Likelihood
# def person3():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[2] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 4 Likelihood
# def person4():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[3] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 5 Likelihood
# def person5():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[4] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 6 Likelihood
# def person6():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[5] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 7 Likelihood
# def person7():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[6] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 8 Likelihood
# def person8():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[7] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Person 9 Likelihood
# def person9():
#     value = 0
#     output = [value]
#     for item in binary:
#         if item[8] == 1:
#             value = 1
#             output.append(value)
#         else:
#             value = 0
#             output.append(value)
#     return output
#
#
# # Pedigree Likelihood String
# def stringlikestuff():
#     founder = pd.DataFrame([fpp1(), fpp2(), fpp3()]).transpose()
#     founderprob = founder.iloc[1:, :]
#
#     transmission = pd.DataFrame([tp4(), tp5(), tp6(), tp7(), tp8(), tp9()]).transpose()
#     transmissionprob = transmission.iloc[1:, :]
#     ldldf = pd.DataFrame([ldlc1(), ldlc2(), ldlc3(), ldlc4(), ldlc5(), ldlc6(), ldlc7(), ldlc8(), ldlc9()]
#                          ).transpose()
#     ldlarray = ldldf.iloc[1:, :]
#
#     txdf = pd.DataFrame([tx1(), tx2(), tx3(), tx4(), tx5(), tx6(), tx7(), tx8(), tx9()]).transpose()
#     txarray = txdf.iloc[1:, :]
#
#     caddf = pd.DataFrame([cad1(), cad2(), cad3(), cad4(), cad5(), cad6(), cad7(), cad8(), cad9()]).transpose()
#     cadarray = caddf.iloc[1:, :]
#
#     # Creating the table by Calculating the String Probabilities
#     probs = pd.DataFrame([
#         fpp1(), fpp2(), fpp3(), tp4(), tp5(), tp6(), tp7(), tp8(), tp9()
#         , ldlc1(), ldlc2(), ldlc3(), ldlc4(), ldlc5(), ldlc6(), ldlc7(), ldlc8(), ldlc9()
#         , tx1(), tx2(), tx3(), tx4(), tx5(), tx6(), tx7(), tx8(), tx9()
#         , cad1(), cad2(), cad3(), cad4(), cad5(), cad6(), cad7(), cad8(), cad9()
#     ]).transpose()
#
#     # Creating 4 sections
#     section1 = pd.DataFrame([fpp1(), fpp2(), fpp3(), tp4(), tp5(), tp6(), tp7(), tp8(), tp9()]
#                             ).transpose()
#     section2 = pd.DataFrame([ldlc1(), ldlc2(), ldlc3(), ldlc4(), ldlc5(), ldlc6(), ldlc7(), ldlc8(), ldlc9()]
#                             ).transpose()
#     section3 = pd.DataFrame([tx1(), tx2(), tx3(), tx4(), tx5(), tx6(), tx7(), tx8(), tx9()]
#                             ).transpose()
#     section4 = pd.DataFrame([cad1(), cad2(), cad3(), cad4(), cad5(), cad6(), cad7(), cad8(), cad9()]
#                             ).transpose()
#     section1prod = section1.prod(axis=1)
#     section2prod = section2.prod(axis=1)
#     section3prod = section3.prod(axis=1)
#     section4prod = section4.prod(axis=1)
#
#     # Creating 1 dataframe with the products of 4 sections
#     ultimateprod = pd.DataFrame([section1prod, section2prod, section3prod, section4prod]).transpose()
#     probs["String Likelihood"] = ultimateprod.prod(axis=1)
#     string = probs.iloc[1:, :]
#     stringlike = pd.DataFrame([string["String Likelihood"]]).transpose()
#
#     return stringlike
#
#
# # Pedigree Sum Likelihood String
# def stringsumstuff():
#     probs = pd.DataFrame(
#         [fpp1(), fpp2(), fpp3(), tp4(), tp5(), tp6(), tp7(), tp8(), tp9()
#             , ldlc1(), ldlc2(), ldlc3(), ldlc4(), ldlc5(), ldlc6(), ldlc7(), ldlc8(), ldlc9()
#             , tx1(), tx2(), tx3(), tx4(), tx5(), tx6(), tx7(), tx8(), tx9()
#             , cad1(), cad2(), cad3(), cad4(), cad5(), cad6(), cad7(), cad8(), cad9()]).transpose()
#     # Creating 4 sections
#     section1 = pd.DataFrame([fpp1(), fpp2(), fpp3(), tp4(), tp5(), tp6(), tp7(), tp8(), tp9()]
#                             ).transpose()
#     section2 = pd.DataFrame([ldlc1(), ldlc2(), ldlc3(), ldlc4(), ldlc5(), ldlc6(), ldlc7(), ldlc8(), ldlc9()]
#                             ).transpose()
#     section3 = pd.DataFrame([tx1(), tx2(), tx3(), tx4(), tx5(), tx6(), tx7(), tx8(), tx9()]
#                             ).transpose()
#     section4 = pd.DataFrame([cad1(), cad2(), cad3(), cad4(), cad5(), cad6(), cad7(), cad8(), cad9()]
#                             ).transpose()
#     # Cut off the first row
#     # Creating products of 4 sections
#     section1prod = section1.prod(axis=1)
#     section2prod = section2.prod(axis=1)
#     section3prod = section3.prod(axis=1)
#     section4prod = section4.prod(axis=1)
#
#     # Creating 1 dataframe with the products of 4 sections
#     ultimateprod = pd.DataFrame([section1prod, section2prod, section3prod, section4prod]).transpose()
#     probs["String Likelihood"] = ultimateprod.prod(axis=1)
#     string = probs.iloc[1:, :]
#     stringsum = pd.DataFrame([string["String Likelihood"].sum()])
#     return stringsum
#
#
# # Pedigree Family Info
# def famsumstuff():
#     stringlike = stringlikestuff()
#     fam1 = pd.DataFrame([family()]).transpose()
#     fam = fam1.iloc[1:, :]
#     familylikelihood = fam.mul(stringlike.values)
#     familylikelihood.columns = ["Family Likelihood"]
#     famsum = pd.DataFrame([familylikelihood["Family Likelihood"].sum()])
#
#     return famsum
#
#
# # Person 1 in Pedigree
# def person1stuff():
#     stringlike = stringlikestuff()
#     person1f = pd.DataFrame([person1()]).transpose()
#     person1df = person1f.iloc[1:, :]
#     person1likely = person1df.mul(stringlike.values)
#     person1likely.columns = ["Person 1 Likelihood"]
#     person1sum = pd.DataFrame([person1likely["Person 1 Likelihood"].sum()])
#
#     return person1sum
#
#
# # Person 2 in Pedigree
# def person2stuff():
#     stringlike = stringlikestuff()
#     person2f = pd.DataFrame([person2()]).transpose()
#     person2df = person2f.iloc[1:, :]
#     person2likely = person2df.mul(stringlike.values)
#     person2likely.columns = ["Person 2 Likelihood"]
#     person2sum = pd.DataFrame([person2likely["Person 2 Likelihood"].sum()])
#
#     return person2sum
#
#
# # Person 3 in Pedigree
# def person3stuff():
#     stringlike = stringlikestuff()
#     person3f = pd.DataFrame([person3()]).transpose()
#     person3df = person3f.iloc[1:, :]
#     person3likely = person3df.mul(stringlike.values)
#     person3likely.columns = ["Person 3 Likelihood"]
#     person3sum = pd.DataFrame([person3likely["Person 3 Likelihood"].sum()])
#
#     return person3sum
#
#
# # Person 4 in Pedigree
# def person4stuff():
#     stringlike = stringlikestuff()
#     person4f = pd.DataFrame([person4()]).transpose()
#     person4df = person4f.iloc[1:, :]
#     person4likely = person4df.mul(stringlike.values)
#     person4likely.columns = ["Person 4 Likelihood"]
#     person4sum = pd.DataFrame([person4likely["Person 4 Likelihood"].sum()])
#
#     return person4sum
#
#
# # Person 5 in Pedigree
# def person5stuff():
#     stringlike = stringlikestuff()
#     person5f = pd.DataFrame([person5()]).transpose()
#     person5df = person5f.iloc[1:, :]
#     person5likely = person5df.mul(stringlike.values)
#     person5likely.columns = ["Person 5 Likelihood"]
#     person5sum = pd.DataFrame([person5likely["Person 5 Likelihood"].sum()])
#
#     return person5sum
#
#
# # Person 6 in Pedigree
# def person6stuff():
#     stringlike = stringlikestuff()
#     person6f = pd.DataFrame([person6()]).transpose()
#     person6df = person6f.iloc[1:, :]
#     person6likely = person6df.mul(stringlike.values)
#     person6likely.columns = ["Person 6 Likelihood"]
#     person6sum = pd.DataFrame([person6likely["Person 6 Likelihood"].sum()])
#
#     return person6sum
#
#
# # Person 7 in Pedigree
# def person7stuff():
#     stringlike = stringlikestuff()
#     person7f = pd.DataFrame([person7()]).transpose()
#     person7df = person7f.iloc[1:, :]
#     person7likely = person7df.mul(stringlike.values)
#     person7likely.columns = ["Person 7 Likelihood"]
#     person7sum = pd.DataFrame([person7likely["Person 7 Likelihood"].sum()])
#
#     return person7sum
#
#
# # Person 8 in Pedigree
# def person8stuff():
#     stringlike = stringlikestuff()
#     person8f = pd.DataFrame([person8()]).transpose()
#     person8df = person8f.iloc[1:, :]
#     person8likely = person8df.mul(stringlike.values)
#     person8likely.columns = ["Person 8 Likelihood"]
#     person8sum = pd.DataFrame([person8likely["Person 8 Likelihood"].sum()])
#
#     return person8sum
#
#
# # Person 9 in Pedigree
# def person9stuff():
#     stringlike = stringlikestuff()
#     person9f = pd.DataFrame([person9()]).transpose()
#     person9df = person9f.iloc[1:, :]
#     person9likely = person9df.mul(stringlike.values)
#     person9likely.columns = ["Person 9 Likelihood"]
#     person9sum = pd.DataFrame([person9likely["Person 9 Likelihood"].sum()])
#
#     return person9sum
#
#
# stringsum = stringsumstuff()
# famsum = famsumstuff()
# person1sum = person1stuff()
# person2sum = person2stuff()
# person3sum = person3stuff()
# person4sum = person4stuff()
# person5sum = person5stuff()
# person6sum = person6stuff()
# person7sum = person7stuff()
# person8sum = person8stuff()
# person9sum = person9stuff()
#
# ped1fhprob = person1sum.div(stringsum) * 100
# fh1prob = ped1fhprob.iloc[0, 0]
#
# ped2fhprob = person2sum.div(stringsum) * 100
# fh2prob = ped2fhprob.iloc[0, 0]
#
# ped3fhprob = person3sum.div(stringsum) * 100
# fh3prob = ped3fhprob.iloc[0, 0]
#
# ped4fhprob = person4sum.div(stringsum) * 100
# fh4prob = ped4fhprob.iloc[0, 0]
#
# ped5fhprob = person5sum.div(stringsum) * 100
# fh5prob = ped5fhprob.iloc[0, 0]
#
# ped6fhprob = person6sum.div(stringsum) * 100
# fh6prob = ped6fhprob.iloc[0, 0]
#
# ped7fhprob = person7sum.div(stringsum) * 100
# fh7prob = ped7fhprob.iloc[0, 0]
#
# ped8fhprob = person8sum.div(stringsum) * 100
# fh8prob = ped8fhprob.iloc[0, 0]
#
# ped9fhprob = person9sum.div(stringsum) * 100
# fh9prob = ped9fhprob.iloc[0, 0]
#
# familyprob = famsum.div(stringsum) * 100
# fhfamprob = familyprob.iloc[0, 0]
