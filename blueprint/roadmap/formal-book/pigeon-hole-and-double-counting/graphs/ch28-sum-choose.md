---
declaration: theorem
origin: cited
lean: chapter28.sum_choose_deg_le_choose_card
statement: formalized
proof: formalized
---

# Cherry counting

If the graph $G$ on $n$ vertices contains no $4$-cycles, then

$$
\sum_{v \in V} \binom{d(v)}{2} \leq \binom{n}{2}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Double counting](../sums/double-counting.md)

## Proof

Each pair $(v, \{u, w\})$ with $u, w \in N(v)$ maps to $\{u, w\}$. The $C_4$-free condition ensures this map is injective on the second component: if both $v_1$ and $v_2$ are common neighbors of $\{u, w\}$ with $v_1 \neq v_2$, then $v_1$-$u$-$v_2$-$w$ forms a $4$-cycle, a contradiction.

## Lean

Formalized as [`chapter28.sum_choose_deg_le_choose_card`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.sum_choose_deg_le_choose_card).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 293](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L293)
