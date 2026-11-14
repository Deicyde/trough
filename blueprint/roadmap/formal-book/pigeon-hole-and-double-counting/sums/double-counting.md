---
declaration: theorem
origin: cited
lean: chapter28.double_counting
statement: formalized
proof: formalized
---

# Double counting

Suppose that we are given two finite sets $R$ and $C$ and a subset $S \subseteq R \times C$. Whenever $(p, q) \in S$, then we say $p$ and $q$ are incident. If $r_p$ denotes the number of elements that are incident to $p \in R$, and $c_q$ denotes the number of elements that are incident to $q \in C$, then

$$
\sum_{p \in R} r_p = |S| = \sum_{q \in C} c_q.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Again, there is nothing to prove. The first sum classifies the pairs in $S$ according to the first entry, while the second sum classifies the same pairs according to the second entry.

## Lean

Formalized as [`chapter28.double_counting`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.double_counting).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 129](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L129)
