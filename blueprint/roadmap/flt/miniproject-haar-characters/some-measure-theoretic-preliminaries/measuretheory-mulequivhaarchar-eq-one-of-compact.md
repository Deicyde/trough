---
declaration: lemma
origin: cited
lean: MeasureTheory.mulEquivHaarChar_eq_one_of_compactSpace
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/532
---

# MeasureTheory.mulEquivHaarChar_eq_one_of_compactSpace

Say $A$ is a compact topological additive group and $\phi:A\to A$ is an additive isomorphism. Then $d_A(\phi)=1.$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have $d_A(\phi)\mu(A)=\mu(A)$ from lemma [MeasureTheory.addEquivAddHaarChar_smul_preimage](../initial-definitions/measuretheory-addequivaddhaarchar-smul-preimage.md) and $\mu(A)$ is positive and finite because $A$ is open and compact.

## Lean

Formalized as [`MeasureTheory.mulEquivHaarChar_eq_one_of_compactSpace`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.mulEquivHaarChar_eq_one_of_compactSpace).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 558](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L558)
