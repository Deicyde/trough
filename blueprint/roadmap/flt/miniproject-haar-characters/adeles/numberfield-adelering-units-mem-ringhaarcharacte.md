---
declaration: corollary
origin: cited
lean: NumberField.AdeleRing.units_mem_ringHaarCharacter_ker
statement: formalized
proof: formalized
---

# NumberField.AdeleRing.units\_mem\_ringHaarCharacter\_ker

If $B$ is a finite-dimensional $\mathbb{Q}$-algebra (for example a number field, or a quaternion algebra over a number field), if $B_{\mathbb{A}}$ denotes the ring $B\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}$, and if $b\in B^\times$, then $\delta_{B_{\mathbb{A}}}(b)=1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.addHaarScalarFactor\_tensor\_adeles\_eq\_one](measuretheory-addhaarscalarfactor-tensor-adeles.md)

## Proof

Follows immediately from the previous theorem.

## Lean

Formalized as [`NumberField.AdeleRing.units_mem_ringHaarCharacter_ker`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.units_mem_ringHaarCharacter_ker).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 903](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L903)
