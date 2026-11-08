---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_piCongrRight
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/521
---

# MeasureTheory.addEquivAddHaarChar_piCongrRight

If $A_i$ are a finite collection of locally compact topological abelian groups, with $\phi_i:A_i\to A_i$ additive homeomorphisms, then $d_{\prod_i A_i}(\prod_i\phi_i)=\prod_i d_{A_i}(\phi_i)$.

## Depends on

- [MeasureTheory.addEquivAddHaarChar_prodCongr](measuretheory-addequivaddhaarchar-prodcongr.md)

## Proof

Induction on the size of the finite set, using the previous lemma.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_piCongrRight`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_piCongrRight).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 487](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L487)
