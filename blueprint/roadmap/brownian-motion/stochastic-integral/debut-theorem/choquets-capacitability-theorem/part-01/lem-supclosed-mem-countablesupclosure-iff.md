---
declaration: lemma
origin: cited
lean: SupClosed.mem_countableSupClosure_iff_monotone
statement: formalized
proof: formalized
---

# SupClosed.mem_countableSupClosure_iff

If a paving $S$ is closed under pairwise union, then a set $s$ is in $S_\sigma$ if and only if there exists a monotone increasing family of sets $(A_n)_{n\in\mathbb{N}}$ in $S$ such that $s = \bigcup_{n\in\mathbb{N}} A_n$.

## Depends on

- [countableSupClosure](def-countablesupclosure.md)

## Proof

Similar to the proof of Lemma [InfClosed.mem_countableInfClosure_iff](lem-infclosed-mem-countableinfclosure-iff.md).

## Lean

Formalized as [`SupClosed.mem_countableSupClosure_iff_monotone`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/SupClosed.mem_countableSupClosure_iff_monotone).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 62](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L62)
