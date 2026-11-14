---
declaration: theorem
origin: cited
lean: chapter30.erdos_ko_rado
statement: formalized
proof: formalized
---

# Erdős–Ko–Rado

Let $n \ge 2k$. The largest size of an intersecting $k$-uniform family in an $n$-set is $\binom{n - 1}{k - 1}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We follow Katona's cyclic permutation argument. Arrange $\{1,\dots,n\}$ on a circle. Among the $n$ arcs of $k$ consecutive elements, at most $k$ can be pairwise intersecting (by the arc lemma). For each of the $(n-1)!$ circular permutations, an intersecting family $\mathcal{F}$ contributes at most $k$ arcs. Each $k$-set appears as an arc in exactly $k!(n-k)!$ circular permutations. Double counting gives

$$
|\mathcal{F}| \cdot k!(n-k)! \le k \cdot (n-1)!,
$$

so $|\mathcal{F}| \le \binom{n-1}{k-1}$.

## Lean

Formalized as [`chapter30.erdos_ko_rado`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter30.erdos_ko_rado).

## Sources

- [Formal Book blueprint: chapter/chapter30.tex, line 39](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter30.tex#L39)
