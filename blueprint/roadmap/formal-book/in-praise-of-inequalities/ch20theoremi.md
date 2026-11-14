---
declaration: theorem
origin: cited
lean: cauchy_schwarz_inequality
statement: formalized
proof: formalized
---

# ch20theoremI

Let $\langle a, b \rangle$ be an inner product on a real vector space $V$ (with the norm $|a|^2 := \langle a, a \rangle$). Then

$$
\langle a, b \rangle^2 \leq |a|^2 |b|^2
$$

holds for all vectors $a, b \in V$, with equality if and only if $a$ and $b$ are linearly dependent.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The following (folklore) proof is probably the shortest. Consider the quadratic function

$$
|x a + b|^2 = x^2 |a|^2 + 2x \langle a, b \rangle + |b|^2
$$

in the variable $x$. We may assume $a \neq 0$. If $b = \lambda a$, then clearly

$$
\langle a, b \rangle^2 = |a|^2 |b|^2.
$$

If, on the other hand, $a$ and $b$ are linearly independent, then $|x a + b|^2 > 0$ for all $x$, and thus the discriminant $\langle a, b \rangle^2 - |a|^2 |b|^2$ is less than 0.

## Lean

Formalized as [`cauchy_schwarz_inequality`](https://mo271.github.io/FormalBook/docs/find/#doc/cauchy_schwarz_inequality).

## Sources

- [Formal Book blueprint: chapter/chapter20.tex, line 3](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter20.tex#L3)
