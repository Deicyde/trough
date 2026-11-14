---
declaration: theorem
origin: cited
lean: MIPRE.LIDT.lowIndividualDegree_soundness
statement: formalized
proof: formalized
---

# Quantum soundness of the canonical-line low individual degree test

Let

$$
\delta_{lidt}(\varepsilon, m, d, q, k)
= 10^5 \, k^2 m^4 \bigl( \varepsilon^{1/40000} + (d/q)^{1/40000}
+ e^{-k/(2560000 m^2)} \bigr).
$$

Let $\mathscr{S} = (|\psi\rangle, A, B)$ be a tensor-product strategy for the $(m,q,d)$-low individual degree test that succeeds with probability at least $1 - \varepsilon$, and let $k$ be an integer with $k \geq 400md$ and $k > 0$. Then there exist projective measurements $G^\textsc{A} = \{G^\textsc{A}_g\}$ on Alice's space and $G^\textsc{B} = \{G^\textsc{B}_g\}$ on Bob's space, both with outcomes the polynomials $g$ in $m$ variables of individual degree at most $d$, such that, writing $\delta = \delta_{lidt}(\varepsilon, m, d, q, k)$ and letting $u \sim \mathbb{F}^m$ be uniform:

1. Alice's point measurement $A^u$ and the evaluation $G^\textsc{B}_{[g(u) = \cdot]}$ are $\delta$-consistent;
2. the evaluation $G^\textsc{A}_{[g(u) = \cdot]}$ and Bob's point measurement $B^u$ are $\delta$-consistent;
3. $G^\textsc{A}$ and $G^\textsc{B}$ are $\delta$-consistent.

## Depends on

- [Canonical-line low individual degree test](def-lidt.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Inconsistency](../../foundations/part-02/def-inconsistency.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Proof

This is Theorem 1.3 of (JNVWY21qld) (`thm:main-formal` there), whose proof is the MIPStarRE formalization vendored into this repository. The Lean proof translates a strategy for our game into MIPStarRE's strategy container (the state as a density matrix; the line measurements as coarse-grainings of the measurements at the canonical line questions along the change of parametrization, which makes them covariant under rebasing), shows that MIPStarRE's failure surrogate is at most the rejection probability $1 - \mathrm{val}$ (the consistency defect of each branch is at most the rejection probability of that branch, since acceptance forces the coarse-grained answers to agree), applies their main theorem, and reads the resulting measurements back into our vocabulary.

## Lean

Formalized as [`MIPRE.LIDT.lowIndividualDegree_soundness`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.lowIndividualDegree_soundness).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 601](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L601)
