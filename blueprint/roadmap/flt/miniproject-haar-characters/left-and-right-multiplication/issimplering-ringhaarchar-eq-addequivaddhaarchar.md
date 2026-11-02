---
declaration: corollary
origin: cited
lean: IsSimpleRing.ringHaarChar_eq_addEquivAddHaarChar_mulRight
statement: formalized
proof: formalized
---

# IsSimpleRing.ringHaarChar\_eq\_addEquivAddHaarChar\_mulRight

If $B$ is a central simple algebra over a locally compact field $F$, and if $u\in B^\times$, then $d_B(r_u)=\delta_B(u)$ (recall that the latter is defined to mean $d_B(\ell_u)$).

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [IsSimpleRing.mulLeft\_det\_eq\_mulRight\_det](issimplering-mulleft-det-eq-mulright-det.md)

## Proof

If $\ell_u$ and $r_u$ denote left and right multiplication by $u$ on $B$, then we have seen in lemma MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det that $d_B(r_u)=\delta_F(\det(r_u))$. Lemma [IsSimpleRing.mulLeft\_det\_eq\_mulRight\_det](issimplering-mulleft-det-eq-mulright-det.md) tells us that this is $\delta_F(\det(\ell_u))$ and this is $\delta_B(u)$ again by corollary MeasureTheory.addEquivAddHaarChar\_eq\_ringHaarChar\_det.

## Lean

Formalized as [`IsSimpleRing.ringHaarChar_eq_addEquivAddHaarChar_mulRight`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsSimpleRing.ringHaarChar_eq_addEquivAddHaarChar_mulRight).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 435](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L435)
