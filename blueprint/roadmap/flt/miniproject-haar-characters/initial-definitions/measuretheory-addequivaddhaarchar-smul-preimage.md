---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_smul_preimage
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/509
---

# MeasureTheory.addEquivAddHaarChar_smul_preimage

If $X$ is a Borel set then $\mu(X)=d_A(\phi)\mu(\phi^{-1}X)$.

## Depends on

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md)

## Proof

This follows immediately from lemma [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md) and the definition of the pushforward of a measure.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_smul_preimage`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_smul_preimage).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 108](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HaarCharacterProject.tex#L108)
