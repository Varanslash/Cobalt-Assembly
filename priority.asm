; EXPERIMENT PRIORITY CHECK SCRIPT 

; Initialization

str aa
str bb 
str cc
sav aa print by hand
sav bb print by rout
sav cc print by loop

; Routine Print

sar rout
sro rout prt bb

; Loop Print

lop loop
lro loop prt cc

; Priority Checker (Note that the loop is run first, then routine, then isolated)

lup loop 3
run rout
prt aa

; Output:
; print by hand
; print by loop
; print by loop
; print by loop
; print by rout

; Conclusion: All isolated lines are compiled and run first
; Then, loop is run
; Then, routines are run
; This means the only way you can run code outside of loops after them is to use a routine
; It doesn't make the language unusable (real assembly is harder anyways), but should be addressed in the guide or fixed