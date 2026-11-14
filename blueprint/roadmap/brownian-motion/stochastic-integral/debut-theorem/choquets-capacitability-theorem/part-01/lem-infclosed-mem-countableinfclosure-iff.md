---
declaration: lemma
origin: cited
lean: InfClosed.mem_countableInfClosure_iff_antitone
statement: formalized
proof: formalized
---

# InfClosed.mem_countableInfClosure_iff

If a paving $S$ is closed under pairwise intersection, then a set $s$ is in $S_\delta$ if and only if there exists a monotone decreasing family of sets $(A_n)_{n\in\mathbb{N}}$ in $S$ such that $s = \bigcap_{n\in\mathbb{N}} A_n$.

## Depends on

- [countableInfClosure](def-countableinfclosure.md)

## Proof

The “monotone decreasing” condition is the only non-trivial part of the statement: without it it would just be the definition of $S_\delta$. If $s \in S_\delta$ there exists a family $(B_n)$ that satisfies the condition but may not be monotone. We can then define $A_n = \bigcap_{k \le n} B_k$, and the family $(A_n)$ is monotone decreasing and satisfies $\bigcap_{n\in\mathbb{N}} A_n = \bigcap_{n\in\mathbb{N}} B_n = s$.

## Lean

Formalized as [`InfClosed.mem_countableInfClosure_iff_antitone`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/InfClosed.mem_countableInfClosure_iff_antitone).

## Sources

- [Brownian motion blueprint: chapters/debut.tex, line 49](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/debut.tex#L49)
