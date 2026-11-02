---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_smul_preimage
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/509
---

# MeasureTheory.addEquivAddHaarChar\_smul\_preimage

If $X$ is a Borel set then $\mu(X)=d_A(\phi)\mu(\phi^{-1}X)$.

## Depends on

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar\_smul\_map](measuretheory-addequivaddhaarchar-smul-map.md)

## Proof

This follows immediately from lemma [MeasureTheory.addEquivAddHaarChar\_smul\_map](measuretheory-addequivaddhaarchar-smul-map.md) and the definition of the pushforward of a measure.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_smul_preimage`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_smul_preimage).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 108](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L108)
