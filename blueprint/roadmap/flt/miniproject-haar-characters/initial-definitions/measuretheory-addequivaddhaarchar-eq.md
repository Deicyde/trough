---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_eq
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/508
---

# MeasureTheory.addEquivAddHaarChar_eq

$d_A(\phi)$ is independent of choice of regular Haar measure.

## Depends on

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

## Proof

If $\mu'$ is a second choice then $\mu'=\lambda\mu$ for some positive real $\lambda$, and the $\lambda$s on each side of $\mu'(X)=d_A(\phi)(\phi_*\mu')(X)$ cancel.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_eq`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_eq).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 61](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L61)
