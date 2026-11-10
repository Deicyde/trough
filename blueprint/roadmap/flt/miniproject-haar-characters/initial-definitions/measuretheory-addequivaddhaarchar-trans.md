---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_trans
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/511
---

# MeasureTheory.addEquivAddHaarChar_trans

$d_A(\phi\circ\psi)=d_A(\phi)d_A(\psi).$

## Depends on

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar_smul_preimage](measuretheory-addequivaddhaarchar-smul-preimage.md)

## Proof

Here's one way: it suffices to prove that $d_A(\phi\circ\psi)(\phi\circ\psi)_*\mu=d_A(\phi)d_A(\psi)(\phi\circ\psi)_*\mu$ (because there exists a compact set with positive finite measure) and using lemma [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md) and the fact that $(\phi\circ\psi)_*\mu=\phi_*(\psi_*\mu)$ one can simplify both sides to $\mu$.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_trans`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_trans).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 178](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L178)
