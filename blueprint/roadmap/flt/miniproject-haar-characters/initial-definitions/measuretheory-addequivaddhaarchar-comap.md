---
declaration: corollary
origin: cited
lean: MeasureTheory.addEquivAddHaarChar_smul_eq_comap
statement: formalized
proof: formalized
---

# MeasureTheory.addEquivAddHaarChar\_comap

If $\mu$ is any regular Haar measure on $A$ then $d_A(\phi)\mu = \phi^*\mu.$

## Depends on

- [MeasureTheory.addEquivAddHaarChar\_smul\_map](measuretheory-addequivaddhaarchar-smul-map.md)

## Proof

This follows from lemma [Lemma MeasureTheory.addEquivAddHaarChar\_smul\_map](measuretheory-addequivaddhaarchar-smul-map.md) applied to the regular Haar measure $\phi^*\mu$ and the fact that $\phi_*\phi^*\mu=\mu$.

## Lean

Formalized as [`MeasureTheory.addEquivAddHaarChar_smul_eq_comap`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.addEquivAddHaarChar_smul_eq_comap).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 92](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L92)
