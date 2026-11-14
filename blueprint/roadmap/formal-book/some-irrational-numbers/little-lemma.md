---
declaration: theorem
origin: cited
lean: book.irrational.little_lemma
statement: formalized
---

# Little Lemma

For any $n \ge 1$ the integer $n!$ contains the prime factor $2$ at most $n-1$ times — with equality if (and only if) $n$ is a power of two, $n = 2^m$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This lemma is not hard to show: $\lfloor \frac{n}{2} \rfloor$ of the factors of $n!$ are even, $\lfloor \frac{n}{4} \rfloor$ of them are divisible by $4$, and so on. So if $2^k$ is the largest power of two which satisfies $2^k \le n$, then $n!$ contains the prime factor $2$ exactly

$$
\left\lfloor \frac{n}{2} \right\rfloor + \left\lfloor \frac{n}{4} \right\rfloor + \dots + \left\lfloor \frac{n}{2^k} \right\rfloor \le \frac{n}{2} + \frac{n}{4} + \dots + \frac{n}{2^k} = n \left( 1 - \frac{1}{2^k} \right) \le n-1
$$

times, with equality in both inequalities exactly if $n = 2^k$.

## Lean

Stated as [`book.irrational.little_lemma`](https://mo271.github.io/FormalBook/docs/find/#doc/book.irrational.little_lemma); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter08.tex, line 94](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter08.tex#L94)
