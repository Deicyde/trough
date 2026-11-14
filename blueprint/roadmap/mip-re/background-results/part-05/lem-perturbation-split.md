---
declaration: lemma
origin: cited
lean: MIPRE.ValueApprox.dotProduct_mulVec_perturb, MIPRE.ValueApprox.kronecker_sub_kronecker, MIPRE.ValueApprox.dotProduct_kronecker_perturb
statement: formalized
proof: formalized
---

# The perturbation split

For matrices $M, N$ and vectors $\psi, \phi$,

$$
\langle\psi| M |\psi\rangle - \langle\phi| N |\phi\rangle
= \langle\psi| (M - N) |\psi\rangle + \langle\psi - \phi| N |\psi\rangle
+ \langle\phi| N |\psi - \phi\rangle,
$$

and $A \otimes B - A' \otimes B' = (A - A') \otimes B + A' \otimes (B - B')$; combining the two splits a bipartite Born expectation in which both players' operators and the state have moved into four terms, each moving exactly one of $A$, $B$ and $\psi$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Expand and cancel. Both identities are exact: no norm and no estimate occurs in either, and the analytic bounds are obtained afterwards by bounding the terms separately.

## Lean

Formalized as [`MIPRE.ValueApprox.dotProduct_mulVec_perturb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.dotProduct_mulVec_perturb), [`MIPRE.ValueApprox.kronecker_sub_kronecker`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.kronecker_sub_kronecker), [`MIPRE.ValueApprox.dotProduct_kronecker_perturb`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.dotProduct_kronecker_perturb).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7463](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7463)
