---
declaration: lemma
origin: cited
lean: MIPRE.LIDT.Co.Doubling.symmStrat_pointConsistency_unsymmetrize
statement: formalized
proof: formalized
---

# Unsymmetrization in the doubled model

Let $S$ be a projective strategy for the low individual degree test whose two players act in a finite pair $M$ with a unit state, and $S_D$ its symmetric strategy in the doubled model $D(M)$ (Theorem [Symmetrization after the bridge](thm-doubled-symmetrization.md)). Let $G$ be a measurement in the local algebra of $D(M)$ whose outcomes are the polynomials, with components $G^1$ in the first player's algebra and $G^2$ in the second's. If the point measurements of $S_D$ are $\sigma$-consistent with the evaluations of $G$ in $D(M)$, for a uniformly random point, then in $M$ the first player's point measurements are $2\sigma$-consistent with the evaluations of $G^2$, and the evaluations of $G^1$ are $2\sigma$-consistent with the second player's point measurements.

## Depends on

- [Symmetrization after the bridge](thm-doubled-symmetrization.md)

## Proof

The point measurements of $S_D$ have the point measurements of $S$ as components, and evaluation commutes with taking components. A consistency defect of $D(M)$ between two paired families is the average of the two two-space defects of $M$ (Lemma [The role average in the doubled model](lem-doubled-model-role-average.md)), both nonnegative, so each is at most twice it (`reports/c6b-paper-proofs.md`, Section 4, Theorem E). These are the constants of the vendored role-register unsymmetrization, which this replaces.

## Lean

Formalized as [`MIPRE.LIDT.Co.Doubling.symmStrat_pointConsistency_unsymmetrize`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.symmStrat_pointConsistency_unsymmetrize).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 4143](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L4143)
