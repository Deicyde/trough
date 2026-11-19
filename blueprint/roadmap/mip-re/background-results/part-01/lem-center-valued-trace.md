---
declaration: lemma
origin: cited
lean: MIPRE.Orthonormalization.vecFunctional, MIPRE.Orthonormalization.IsCenterExpectation, MIPRE.Orthonormalization.eq_of_isCentralIn_of_pairing, MIPRE.Orthonormalization.exists_isCenterExpectation, MIPRE.Orthonormalization.mvNEquiv_of_map_eq, MIPRE.Orthonormalization.IsCenterExpectation.isCenterValuedTrace, MIPRE.Orthonormalization.exists_isCenterValuedTrace
statement: formalized
proof: formalized
---

# A centre-valued trace from a vector trace

Let $\mathcal{M}$ be a von Neumann algebra on a Hilbert space $\mathcal{H}$ with a faithful tracial state of the form $\tau(x) = \sum_{k < d} \langle g_k, x g_k \rangle$ for finitely many vectors $g_k$. Then $\mathcal{M}$ has a centre-valued trace: a linear map $E$, defined on $\mathcal{B}(\mathcal{H})$ and constrained on $\mathcal{M}$ only, with values in the centre $\mathcal{Z}$ of $\mathcal{M}$, which is positive, faithful, tracial, the identity on $\mathcal{Z}$, $\mathcal{Z}$-linear, continuous along bounded weak-operator convergent nets, and admits division in the centre; and two projections of $\mathcal{M}$, or of the matrix algebra $M_n(\mathcal{M})$ compared through $\sum_i E(X_{ii})$, with the same centre-valued trace are Murray–von Neumann equivalent. These are the clauses of the centre-valued trace of the vendored structure-theory interface, at the projection $1$; no factor, type or separability hypothesis is needed.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For $x \in \mathcal{M}$, the elements $y \in \mathcal{M}$ with $\|y\| \le \|x\|$ and $\tau(yc) = \tau(xc)$ for every central $c$ form a set that is compact and convex in the weak operator topology, on which the $2$-norm $y \mapsto \sum_k \|y g_k\|^2$ is lower semicontinuous and, by the parallelogram law and faithfulness, has a unique minimizer. Conjugation by a unitary of $\mathcal{M}$ preserves the set and, by traciality, the $2$-norm, so it fixes the minimizer, which therefore commutes with every unitary of $\mathcal{M}$, hence with $\mathcal{M}$: it is central, and it is $E x$. A central element is determined by its pairings with the centre, which gives linearity and the algebraic clauses; normality and division are cluster-point arguments. For comparison, the vendored proof for factors builds a maximal partial isometry $W$ from $p$ into $q$ by a greedy chain and uses the factor hypothesis only to exclude two nonzero complements; here maximality makes the central support $c$ of $p - W^*W$ kill $q - WW^*$, and applying $E$ to $c(p - W^*W) = p - W^*W$ and $c(q - WW^*) = 0$ shows that both complements vanish. The matrix case is the same argument in $M_n(\mathcal{M})$, whose centre is the amplified centre of $\mathcal{M}$. The full proof is `reports/c6b-paper-proofs.md`, Section 2.

## Lean

Formalized as [`MIPRE.Orthonormalization.vecFunctional`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.vecFunctional), [`MIPRE.Orthonormalization.IsCenterExpectation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.IsCenterExpectation), [`MIPRE.Orthonormalization.eq_of_isCentralIn_of_pairing`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.eq_of_isCentralIn_of_pairing), [`MIPRE.Orthonormalization.exists_isCenterExpectation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isCenterExpectation), [`MIPRE.Orthonormalization.mvNEquiv_of_map_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.mvNEquiv_of_map_eq), [`MIPRE.Orthonormalization.IsCenterExpectation.isCenterValuedTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.IsCenterExpectation.isCenterValuedTrace), [`MIPRE.Orthonormalization.exists_isCenterValuedTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Orthonormalization.exists_isCenterValuedTrace).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 353](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L353)
