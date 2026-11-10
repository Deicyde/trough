---
declaration: lemma
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_smul_integral_map
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/510
---

# MeasureTheory.addEquivAddHaarChar_smul_integral_map

If $f:A\to\mathbb{R}$ is a Borel measurable function then $d_A(\phi)\int f(x)d\phi_*\mu(x)=\int f(x)d\mu(x)$.

## Depends on

- [MeasureTheory.addEquivAddHaarChar](measuretheory-addequivaddhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md)

## Proof

This also follows immediately from lemma [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md).

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_smul_integral_map`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_smul_integral_map).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 123](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L123)
