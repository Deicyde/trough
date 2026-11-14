---
declaration: theorem
origin: cited
lean: chapter28.claim4_contiguous_sum
statement: formalized
proof: formalized
---

# Claim

Suppose we are given $n$ integers $a_1, \dots, a_n$, which need not be distinct. Then there is always a set of consecutive numbers $a_{k+1}, a_{k+2}, \dots, a_{\ell}$ whose sum $\sum_{i=k+1}^{\ell} a_i$ is a multiple of $n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Pigeon-hole principle](../pigeon-hole-principle.md)

## Proof

For the proof we set $N = \{0, 1, \dots, n\}$ and $R = \{0, 1, \dots, n-1\}$. Consider the map $f : N \to R$, where $f(m)$ is the remainder of $a_1 + \cdots + a_m$ upon division by $n$. Since $|N| = n+1 > n = |R|$, it follows that there are two sums $a_1 + \cdots + a_k, a_1 + \cdots + a_{\ell}$ $(k < \ell)$ with the same remainder, where the first sum may be the empty sum denoted by $0$. It follows that

$$
\sum_{i=k+1}^{\ell} a_i = \sum_{i=1}^{\ell} a_i - \sum_{i=1}^{k} a_i
$$

has remainder $0$ — end of proof.

## Lean

Formalized as [`chapter28.claim4_contiguous_sum`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.claim4_contiguous_sum).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 103](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L103)
