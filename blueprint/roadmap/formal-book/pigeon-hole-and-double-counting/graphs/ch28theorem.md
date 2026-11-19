---
declaration: theorem
origin: cited
lean: chapter28.c4_free_edge_bound
statement: formalized
proof: formalized
---

# Reiman

If the graph $G$ on $n$ vertices contains no $4$-cycles, then

$$
|E| \leq \left\lfloor \frac{n}{4}\left(1 + \sqrt{4n - 3}\right) \right\rfloor.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Double counting](../sums/double-counting.md)
- [Handshaking](handshaking.md)

## Proof

The proof follows from the chain of inequalities above: the key combinatorial step $\sum \binom{d(u)}{2} \leq \binom{n}{2}$ is established by double counting (Theorem [Cherry counting](ch28-sum-choose.md)), and the final bound follows by Cauchy–Schwarz and the quadratic formula.

## Lean

Formalized as [`chapter28.c4_free_edge_bound`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.c4_free_edge_bound).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 276](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L276)
