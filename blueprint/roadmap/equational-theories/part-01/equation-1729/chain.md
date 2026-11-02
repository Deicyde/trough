---
declaration: lemma
origin: cited
lean: Eq1729.use_chain
statement: formalized
proof: formalized
---

# Chain of partial solutions

Suppose that one has a sequence $(L'_{0,n}, \diamond'_{n}, S'_{n}, {\mathcal I}_n)$ of partial solutions, each one an extension of the previous, such that for any $x, y \in N$, $L'_{0,n} x$, $x \diamond'_{n} y$, and $S'_n x$ are defined for some $n$. Then there exists a 1729 magma that does not satisfy 817.

## Depends on

- [Partial solution](part-sol.md)

## Proof depends on

- [Reduction to new axioms](eq1729-reduce-to-new-axioms.md)

## Proof

Take the direct limit of the chain to obtain total functions $L'_0, \diamond', S'$. The axioms (i'), (iii'), (iv”), (v”), (vi”), (vii”) of the partial solutions then easily imply that the direct limit satisfies the axioms (i'), (iii'), (iv'), (v), (vi'), (vii') (one also uses axiom (P) to note that all pending identities disappear in the direct limit). The claim now follows from [Reduction to new axioms](eq1729-reduce-to-new-axioms.md).

## Lean

Formalized as [`Eq1729.use_chain`](https://teorth.github.io/equational_theories/docs/find/#doc/Eq1729.use_chain).

## Sources

- [Equational Theories blueprint: chapter/1729.tex, line 188](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/1729.tex#L188)
