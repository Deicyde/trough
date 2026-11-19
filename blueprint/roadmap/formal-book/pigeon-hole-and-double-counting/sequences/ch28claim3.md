---
declaration: theorem
origin: cited
lean: chapter28.claim3_erdos_szekeres
statement: formalized
proof: formalized
---

# Claim (Erdős–Szekeres)

In any sequence $a_1, a_2, \ldots, a_{mn+1}$ of $mn+1$ distinct real numbers, there exists an increasing subsequence

$$
a_{i_1} < a_{i_2} < \cdots < a_{i_{m+1}} \quad (i_1 < i_2 < \cdots < i_{m+1})
$$

of length $m+1$, or a decreasing subsequence

$$
a_{j_1} > a_{j_2} > \cdots > a_{j_{n+1}} \quad (j_1 < j_2 < \cdots < j_{n+1})
$$

of length $n+1$, or both.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Pigeon-hole principle](../pigeon-hole-principle.md)

## Proof

This time the application of the pigeon-hole principle is not immediate. Associate to each $a_i$ the number $t_i$, which is the length of a longest increasing subsequence starting at $a_i$. If $t_i \geq m+1$ for some $i$, then we have an increasing subsequence of length $m+1$. Suppose then that $t_i \leq m$ for all $i$. The function $f : a_i \mapsto t_i$ mapping $\{a_1, \dots, a_{mn+1}\}$ to $\{1, \dots, m\}$ tells us by (1) that there is some $s \in \{1, \dots, m\}$ such that $f(a_i) = s$ for $\frac{mn}{m} + 1 = n + 1$ numbers $a_i$. Let $a_{j_1}, a_{j_2}, \dots, a_{j_{n+1}}$ $(j_1 < \cdots < j_{n+1})$ be these numbers. Now look at two consecutive numbers $a_{j_i}, a_{j_{i+1}}$. If $a_{j_i} < a_{j_{i+1}}$, then we would obtain an increasing subsequence of length $s$ starting at $a_{j_{i+1}}$, and consequently an increasing subsequence of length $s+1$ starting at $a_{j_i}$, which cannot be since $f(a_{j_i}) = s$. We thus obtain a decreasing subsequence $a_{j_1} > a_{j_2} > \cdots > a_{j_{n+1}}$ of length $n+1$.

## Lean

Formalized as [`chapter28.claim3_erdos_szekeres`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.claim3_erdos_szekeres).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 68](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L68)
