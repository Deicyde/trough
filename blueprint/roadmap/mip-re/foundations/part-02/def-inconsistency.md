---
declaration: definition
origin: cited
lean: MIPRE.inconsistency
statement: formalized
---

# Inconsistency

Let $\mu$ be a distribution on a finite set ${\mathcal{X}}$, let $|\psi\rangle \in \mathbb{C}^{d_\textsc{A}} \otimes \mathbb{C}^{d_\textsc{B}}$, and let $\{M^x_a\}$, $\{N^x_a\}$ be families of POVMs on the two factors with a common question set ${\mathcal{X}}$ and a common answer set. Their *inconsistency* on $|\psi\rangle$ is

$$
\mathop{\mathbb{E}}_{x \sim \mu} \sum_{a \neq b} \langle\psi| M^x_a \otimes N^x_b |\psi\rangle,
$$

the probability that the two measurements return different answers. We say $M$ and $N$ are *$\delta$-consistent* if their inconsistency is at most $\delta$.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.inconsistency`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.inconsistency).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1225](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1225)
