---
declaration: lemma
origin: cited
lean: MeasureTheory.integral_comap_eq_addEquivAddHaarChar_smul
statement: formalized
proof: formalized
---

# MeasureTheory.addEquivAddHaarChar_smul_integral_comap

If $f:A\to\mathbb{R}$ is a Borel measurable function then $d_A(\phi)\int f(x)d\mu(x)=\int f(x)d\phi^*\mu(x)$.

## Depends on

- [MeasureTheory.addEquivAddHaarChar_comap](measuretheory-addequivaddhaarchar-comap.md)

## Proof

This is immediate from corollary [MeasureTheory.addEquivAddHaarChar_comap](measuretheory-addequivaddhaarchar-comap.md).

## Lean

Formalized as [`MeasureTheory.integral_comap_eq_addEquivAddHaarChar_smul`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.integral_comap_eq_addEquivAddHaarChar_smul).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 140](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HaarCharacterProject.tex#L140)
