---
declaration: theorem
origin: cited
lean: Asymptotics.infinitely_many_more_proofs
statement: formalized
---

# infty_proof

If the sequence $S = (s_1, s_2, s_3, \dots)$ is almost injective and of subexponential growth, then the set $\mathbb{P}_S$ of primes that divide some member of $S$ is infinite.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We may assume that $f(n)$ is monotonely increasing. Otherwise, replace $f(n)$ by $F(n) = \max_{i \leq n} f(i)$; you can easily check that with this $F(n)$ the sequence $S$ again satisfies the subexponential growth condition.

Let us suppose for a contradiction that $\mathbb{P}_S = \{p_1, \dots, p_k\}$ is finite. For $n \in \mathbb{N}$, let

$$
s_n = \varepsilon_n p_1^{\alpha_1} \cdots p_k^{\alpha_k}, \quad \text{with } \varepsilon_n \in \{1, 0, -1\}, \alpha_i \ge 0,
$$

where the $\alpha_i = \alpha_i(n)$ depend on $n$. (For $s_n = 0$ we can put $\alpha_i = 0$ for all $i$.) Then

$$
2^{\alpha_1 + \dots + \alpha_k} \leq |s_n| \leq 2^{2^{f(n)}} \quad \text{for } s_n \ne 0,
$$

and thus by taking the binary logarithm

$$
0 \leq \alpha_i \leq \alpha_1 + \dots + \alpha_k \leq 2^{f(n)} \quad \text{for } 1 \leq i \leq k.
$$

Hence there are not more than $2^{f(n)} + 1$ different possible values for each $\alpha_i = \alpha_i(n)$. Since $f$ is monotone, this gives a first estimate

$$
\#\{\text{distinct } |s_n| \ne 0 \text{ for } n \leq N\} \leq (2^{f(N)} + 1)^k \leq 2^{(f(N)+1)k}.
$$

On the other hand, since $S$ is almost injective only $c$ terms in the sequence can be equal to 0, and each nonzero absolute value can occur at most $2c$ times, so we get the lower estimate

$$
\#\{\text{distinct } |s_n| \ne 0 \text{ for } n \leq N\} \ge \frac{N-c}{2c}.
$$

Altogether, this gives

$$
\frac{N-c}{2c} \leq 2^{k(f(N)+1)}.
$$

Taking again the logarithm with base 2 on both sides, we obtain

$$
\log_2(N-c) - \log_2(2c) \leq k(f(N)+1) \quad \text{for all } N.
$$

This, however, is plainly false for large $N$, as $k$ and $c$ are constants, so $\frac{\log_2(N-c)}{\log_2 N}$ goes to 1 for $N \to \infty$, while $\frac{f(N)}{\log_2 N}$ goes to 0.

## Lean

Stated as [`Asymptotics.infinitely_many_more_proofs`](https://mo271.github.io/FormalBook/docs/find/#doc/Asymptotics.infinitely_many_more_proofs); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 192](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L192)
