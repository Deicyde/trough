---
declaration: theorem
origin: cited
lean: TouchingSimplices.touchingNumber_lt
statement: formalized
proof: formalized
---

# ch16theorem2

For all $d \ge 1$, we have $f(d)< 2^{d+1}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $s$ be the number of facet hyperplanes and put $k=d+1$. Completing the zero entries of each row of the sign matrix gives $2^{s-k}$ sign vectors. These sets of completions are pairwise disjoint, and at least one of the $2^s$ possible sign vectors is missing. Thus $r2^{s-k}<2^s$, so $r<2^k=2^{d+1}$.

## Lean

Formalized as [`TouchingSimplices.touchingNumber_lt`](https://mo271.github.io/FormalBook/docs/find/#doc/TouchingSimplices.touchingNumber_lt).

## Sources

- [Formal Book blueprint: chapter/chapter16.tex, line 28](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter16.tex#L28)
