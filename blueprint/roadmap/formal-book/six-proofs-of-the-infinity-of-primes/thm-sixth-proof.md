---
declaration: theorem
origin: cited
lean: infinity_of_primes₆
statement: formalized
---

# Sixth Proof

The series $\sum_{p\in\mathbb{P}}\frac 1 p$ diverges.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Our final proof goes a considerable step further and demonstrates not only that there are infinitely many primes, but also that the series $\sum_{p \in \mathbb{P}} \frac{1}{p}$ diverges. The first proof of this important result was given by Euler (and is interesting in its own right), but our proof, devised by Erdős, is of compelling beauty.

Let $p_1, p_2, p_3, \dots$ be the sequence of primes in increasing order, and assume that $\sum_{p \in \mathbb{P}} \frac{1}{p}$ converges. Then there must be a natural number $k$ such that $\sum_{i \geq k+1} \frac{1}{p_i} < \frac{1}{2}$. Let us call $p_1, \dots, p_k$ the small primes, and $p_{k+1}, p_{k+2}, \dots$ the big primes. For an arbitrary natural number $N$, we therefore find

$$
\sum_{i \geq k+1} \frac{N}{p_i} < \frac{N}{2}.
$$

Let $N_b$ be the number of positive integers $n \leq N$ which are divisible by at least one big prime, and $N_s$ the number of positive integers $n \leq N$ which have only small prime divisors. We are going to show that for a suitable $N$

$$
N_b + N_s < N,
$$

which will be our desired contradiction, since by definition $N_b + N_s$ would have to be equal to $N$.

To estimate $N_b$, note that $\left\lfloor \frac{N}{p_i} \right\rfloor$ counts the positive integers $n \leq N$ which are multiples of $p_i$. Hence by (1) we obtain

$$
N_b \leq \sum_{i \geq k+1} \left\lfloor \frac{N}{p_i} \right\rfloor < \frac{N}{2}.
$$

Let us now look at $N_s$. We write every $n \leq N$ which has only small prime divisors in the form $n = a_n b_n^2$, where $a_n$ is the square-free part. Every $a_n$ is thus a product of *different* small primes, and we conclude that there are precisely $2^k$ different square-free parts. Furthermore, as $b_n^2 \leq n \leq N$, we find that there are at most $\sqrt{N}$ different square parts, and so

$$
N_s \leq 2^k \sqrt{N}.
$$

Since (2) holds for any $N$, it remains to find a number $N$ with $2^k \sqrt{N} < \frac{N}{2}$, or $2^{k+1} < \sqrt{N}$, and for this $N = 2^{2k+2}$ will do.

## Lean

Stated as [`infinity_of_primes₆`](https://mo271.github.io/FormalBook/docs/find/#doc/infinity_of_primes₆); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter01.tex, line 147](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter01.tex#L147)
