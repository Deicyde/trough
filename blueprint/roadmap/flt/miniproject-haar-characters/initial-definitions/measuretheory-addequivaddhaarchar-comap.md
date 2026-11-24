---
declaration: corollary
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_smul_eq_comap
statement: formalized
proof: formalized
---

# MeasureTheory.addEquivAddHaarChar_comap

If $\mu$ is any regular Haar measure on $A$ then $d_A(\phi)\mu = \phi^*\mu.$

## Depends on

- [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md)

## Proof

This follows from lemma [MeasureTheory.addEquivAddHaarChar_smul_map](measuretheory-addequivaddhaarchar-smul-map.md) applied to the regular Haar measure $\phi^*\mu$ and the fact that $\phi_*\phi^*\mu=\mu$.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_smul_eq_comap`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_smul_eq_comap).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 92](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HaarCharacterProject.tex#L92)
