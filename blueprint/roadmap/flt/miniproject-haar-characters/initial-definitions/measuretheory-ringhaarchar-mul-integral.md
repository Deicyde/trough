---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_mul_integral
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/514
---

# MeasureTheory.ringHaarChar\_mul\_integral

If $f:R\to\mathbb{R}$ is a Borel measurable function and $u\in R^\times$ then $\delta_R(u)\int f(ux)d\mu(x)=\int f(x)d\mu(x)$.

## Depends on

- [MeasureTheory.ringHaarChar](measuretheory-ringhaarchar.md)

## Proof depends on

- [MeasureTheory.addEquivAddHaarChar\_smul\_integral\_map](measuretheory-addequivaddhaarchar-smul-integral.md)

## Proof

A short calculation using lemma [Lemma MeasureTheory.addEquivAddHaarChar\_smul\_integral\_map](measuretheory-addequivaddhaarchar-smul-integral.md).

## Lean

Formalized as [`MeasureTheory.ringHaarChar_mul_integral`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_mul_integral).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 219](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L219)
