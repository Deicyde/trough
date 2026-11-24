---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_complex
statement: formalized
proof: formalized
---

# MeasureTheory.ringHaarChar_complex

If $R=\mathbb{C}$ then $\delta_R(u)=|u|^2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.ringHaarChar_mul_volume](../initial-definitions/measuretheory-ringhaarchar-mul-volume.md)

## Proof

Multiplication by a positive real $r$ sends a unit square to a square of area $r^2=|r|^2$. Multiplication by $e^{i\theta}$ is a rotation and thus does not change area. The general case follows.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_complex`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_complex).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 291](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/HaarCharacterProject.tex#L291)
