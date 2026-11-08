---
declaration: lemma
origin: cited
lean: MeasureTheory.ringHaarChar_padic
statement: formalized
proof: formalized
---

# MeasureTheory.ringHaarChar_padic

If $R=\mathbb{Q}_p$ then $\delta_R(u)=|u|_p$, the usual $p$-adic norm.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [MeasureTheory.ringHaarChar_mul_volume](../initial-definitions/measuretheory-ringhaarchar-mul-volume.md)

## Proof

Normalise Haar measure so that $\mu(\mathbb{Z}_p)=1$. If $u$ is a $p$-adic unit then $u\mathbb{Z}_p=\mathbb{Z}_p$ so multiplication by $u$ didn't change Haar measure. If however $u=p$ then $u\mathbb{Z}_p$ has index $p$ in $\mathbb{Z}_p$ and, because $\mu(i+p\mathbb{Z}_p)=\mu(p\mathbb{Z}_p)$ we have that $\mu(\mathbb{Z}_p)=p\mu(p\mathbb{Z}_p)$ and thus $\delta(p)=p^{-1}$. These elements generate $\mathbb{Q}_p^\times$ and two characters which agree on generators of a group must agree on the group.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_padic`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_padic).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 305](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L305)
