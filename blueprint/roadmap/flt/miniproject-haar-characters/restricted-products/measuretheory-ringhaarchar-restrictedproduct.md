---
declaration: corollary
origin: cited
lean: MeasureTheory.ringHaarChar_restrictedProduct
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/554
---

# MeasureTheory.ringHaarChar\_restrictedProduct

If $u=(u_i)_i\in R^\times$ then $\delta_R(u)=\prod_i\delta_{R_i}(u_i)$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](measuretheory-addequivaddhaarchar-restrictedprod.md)

## Proof

By definition of restricted product we have $u_i\in C_i$ for all but finitely many $i$. Note also that $u$ has an inverse $v=(v_i)_i$ with $v_i\in C_i$ for all but finitely many $i$. The fact that $u_iv_i=v_iu_i=1$ means that $u_i,v_i\in C_i^\times$ for all but finitely many $i$. Thus the previous theorem [MeasureTheory.addEquivAddHaarChar\_restrictedProductCongrRight](measuretheory-addequivaddhaarchar-restrictedprod.md) applies.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_restrictedProduct`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_restrictedProduct).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 699](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L699)
