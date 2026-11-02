---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_real
statement: formalized
proof: formalized
---

# MeasureTheory.ringHaarChar\_real

If $R=\mathbb{R}$ then $\delta_R(u)=|u|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.ringHaarChar\_mul\_volume](../initial-definitions/measuretheory-ringhaarchar-mul-volume.md)

## Proof

Take $\mu$ to be Lebesgue measure and $X=[0,1]$. We have $\delta(u)=\mu(uX)$. If $u>0$ then $u[0,1]=[0,u]$ which has measure $u=|u|$, and if $u<0$ then $u*[0,1]=[u,0]$ which has measure $-u=|u|$.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_real`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_real).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 277](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L277)
