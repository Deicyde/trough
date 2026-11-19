---
declaration: definition
origin: cited
lean: MIPRE.Decider, MIPRE.Decider.Accepts, MIPRE.Decider.TimeBound
statement: formalized
---

# Decider

A *decider* is a $5$-input Turing machine $\mathcal{D}$, whose input is interpreted as $(n, x, y, a, b)$ with $n$ an integer index and $x, y, a, b$ strings. It *accepts* if it halts with output $1$, and *rejects* otherwise (output $0$, or a timeout). In the paper, $\mathsf{TIME}_\mathcal{D}(n)$ denotes the absolute supremum of its running times over all inputs with index $n$, possibly infinite. In Lean, `Decider.TimeBoundAt n T k` instead requires halting within cost $T \cdot (\left\vert {d} \right\vert + 1)^k$ on every input $(n, d)$. This relative bound implies totality at index $n$, but need not imply finite absolute $\mathsf{TIME}_\mathcal{D}(n)$, for the reasons given after Definition [Sampler](def-sampler.md).

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`MIPRE.Decider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Decider), [`MIPRE.Decider.Accepts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Decider.Accepts), [`MIPRE.Decider.TimeBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Decider.TimeBound).

## Sources

- [MIP* = RE blueprint: content/02_foundations.tex, line 1461](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/02_foundations.tex#L1461)
