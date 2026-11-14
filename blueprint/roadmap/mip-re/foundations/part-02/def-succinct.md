---
declaration: definition
origin: cited
lean: MIPRE.Cost.IsSuccinctDesc, MIPRE.Cost.bitQueryAnswer
statement: formalized
---

# Succinct description

Following (MNY), a pair $(e, n)$ of a Turing machine $e$ and integer $n$ is a *succinct description* of the string $x \in \{0,1\}^*$ if $\left\vert {x} \right\vert \leq 2^n$, the runtime of $e$ on input $m$ is at most $(n+1)(\left\vert {m} \right\vert+1)^2$, and $\phi_e(m)$ equals the $m$-th bit of $x$ for $m < \left\vert {x} \right\vert$, and $2$ for $m \geq \left\vert {x} \right\vert$. ((MNY) require runtime at most $n$ on every input; in a model that charges for reading its input this is vacuous for $\left\vert {m} \right\vert > n$, and the polynomial slack in $\left\vert {m} \right\vert$ is what the ambient model's bit-indexing program achieves. Any fixed polynomial in $n$ and $\left\vert {m} \right\vert$ would do, provided the same one is used in Theorem [Gap-preserving compression from ambient stage contracts](../../structure-of-the-proof/part-09/thm-compression.md).)

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.Cost.IsSuccinctDesc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.IsSuccinctDesc), [`MIPRE.Cost.bitQueryAnswer`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.bitQueryAnswer).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1356](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1356)
