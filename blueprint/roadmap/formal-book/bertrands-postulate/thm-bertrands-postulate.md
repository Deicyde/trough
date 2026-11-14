---
declaration: theorem
origin: cited
lean: chapter2.exists_prime_lt_and_le_two_mul
statement: formalized
proof: formalized
---

# Bertrand's postulate

For any positive natural number, there is a prime which is greater than it, but no more than twice as large.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We will estimate the size of the binomial coefficient $\binom{2n}{n}$ carefully enough to see that if it didn't have any prime factors in the range $n < p \le 2n$, then it would be “too small.” Our argument is in five steps.

1. We first prove Bertrand's postulate for $n \le 511$. For this one does not need to check 511 cases: it suffices (this is “Landau's trick”) to check that

    $$
    2,3,5,7,13,23,43,83,163,317,521
    $$

    is a sequence of prime numbers, where each is smaller than twice the previous one. Hence every interval $\{y : n < y \le 2n\}$, with $n \le 511$, contains one of these 11 primes.

2. Next we prove that

    $$
    \prod_{p \le x} p \le 4^{x-1} \quad \text{for all real } x \ge 2,\qquad\text{(1)}
    $$

    where our notation — here and in the following — is meant to imply that the product is taken over all prime numbers $p \le x$. The proof that we present for this fact uses induction on the number of these primes. It is not from Erdős' original paper, but it is also due to Erdős, and it is a true Book Proof. First we note that if $q$ is the largest prime with $q \le x$, then

    $$
    \prod_{p \le x} p = \prod_{p \le q} p \quad \text{and} \quad 4^{q-1} \le 4^{x-1}.
    $$

    Thus it suffices to check (1) for the case where $x=q$ is a prime number. For $q=2$ we get “$2 \le 4$,” so we proceed to consider odd primes $q = 2m + 1$. (Here we may assume, by induction, that (1) is valid for all integers $x$ in the set $\{2, 3, \dots, 2m\}$.) For $q = 2m + 1$ we split the product and compute

    $$
    \prod_{p \le 2m + 1} p = \prod_{p \le m + 1} p \cdot \prod_{m + 1 < p \le 2m + 1} p \le 4^m \binom{2m + 1}{m} \le 4^m 2^{2m} = 4^{2m}.
    $$

    All the pieces of this “one-line computation” are easy to see. In fact,

    $$
    \prod_{p \le m + 1} p \le 4^m
    $$

    holds by induction. The inequality

    $$
    \prod_{m + 1 < p \le 2m + 1} p \le \binom{2m + 1}{m}
    $$

    follows from the observation that $\binom{2m + 1}{m} = \frac{(2m + 1)!}{m! (m + 1)!}$ is an integer, where the primes that we consider all are factors of the numerator $(2m + 1)!$, but not of the denominator $m! (m + 1)!$. Finally

    $$
    \binom{2m + 1}{m} \le 2^{2m}
    $$

    holds since

    $$
    \binom{2m + 1}{m} \quad \text{and} \quad \binom{2m + 1}{m + 1}
    $$

    are two (equal!) summands that appear in

    $$
    \sum_{k = 0}^{2m + 1} \binom{2m + 1}{k} = 2^{2m + 1}.
    $$

3. From Legendre's theorem we get that $\binom{2n}{n} = \frac{(2n)!}{n! n!}$ contains the prime factor $p$ exactly

    $$
    \sum_{k \geq 1} \left( \left\lfloor  \frac{2n}{p^k} \right\rfloor - 2 \left\lfloor \frac{n}{p^k} \right\rfloor \right)
    $$

    times. Here each summand is at most 1, since it satisfies

    $$
    \left\lfloor \frac{2n}{p^k} \right\rfloor - 2 \left\lfloor  \frac{n}{p^k}  \right\rfloor < \frac{2n}{p^k} - 2 \left( \frac{n}{p^k} - 1 \right) = 2,
    $$

    and it is an integer. Furthermore the summands vanish whenever $p^k > 2n$. Thus $\binom{2n}{n}$ contains $p$ exactly

    $$
    \sum_{k \geq 1} \left( \left\lfloor  \frac{2n}{p^k} \right\rfloor - 2 \left\lfloor \frac{n}{p^k} \right\rfloor \right) \le \max\{r : p^r \le 2n\}
    $$

    times. Hence the largest power of $p$ that divides $\binom{2n}{n}$ is not larger than $2n$. In particular, primes $p > \sqrt{2n}$ appear at most once in $\binom{2n}{n}$.

    Furthermore — and this, according to Erdős, is the key fact for his proof — primes $p$ that satisfy $\frac{2}{3} n < p < n$ do not divide $\binom{2n}{n}$ at all! Indeed, $3p > 2n$ implies (for $n \geq 3$, and hence $p \geq 3$) that $p$ and $2p$ are the only multiples of $p$ that appear as factors in the numerator of $\frac{(2n)!}{n! n!}$, while we get two $p$-factors in the denominator.

4. Now we are ready to estimate $\binom{2n}{n}$, benefitting from a suggestion by Raimund Seidel, which nicely improves Erdős' original argument. For $n \ge 3$, using an estimate for the lower bound, we get

    $$
    \frac{4^n}{2n} \le \binom{2n}{n} \le \prod_{p \le \sqrt{2n}} 2n \cdot \prod_{\sqrt{2n} < p \le \frac{2}{3}n} p \cdot \prod_{n < p \le 2n} p.
    $$

    Now, there are no more than $\sqrt{2n}$ primes in the first factor; hence using (1) for the second factor and letting $P(n)$ denote the number of primes between $n$ and $2n$ we get

    $$
    \frac{4^n}{2n} < ((2n)^{\sqrt{2n}}) \cdot (4^{\frac{2}{3}n}) \cdot (2n)^{P(n)},
    $$

    that is,

    $$
    4^{\frac{n}{3}} < (2n)^{\sqrt{2n}+1+P(n)}. \quad \text{(2)}
    $$

5. Taking the logarithm to base 2, the last inequality is turned into

    $$
    P(n) > \frac{2n}{3 \log_2(2n)} - (\sqrt{2n} + 1). \quad \text{(3)}
    $$

    It remains to verify that the right-hand side of (3) is positive for $n$ large enough. We show that this is the case for $n = 2^9 = 512$ (actually, it holds for $n = 468$ onward). By writing $2n - 1 = (\sqrt{2n} - 1)(\sqrt{2n} + 1)$ and cancelling the $(\sqrt{2n} + 1)$-factor it suffices to show

    $$
    \sqrt{2n}-1 > 3 \log_2(2n) \quad \text{for } n \ge 2^9. \quad \text{(4)}
    $$

    For $n = 2^9$, (4) becomes $31 > 30$, and comparing the derivatives $(\sqrt{x}-1)' = \frac{1}{2} \frac{1}{\sqrt{x}}$ and $(3 \log_2 x)' = \frac{3}{\log 2} \frac{1}{x}$ we see that $\sqrt{x} - 1$ grows faster than $3 \log_2 x$ for $x > (\frac{6}{\log 2})^2 \approx 75$ and thus certainly for $x \ge 2^{10} = 1024.$

## Lean

Formalized as [`chapter2.exists_prime_lt_and_le_two_mul`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter2.exists_prime_lt_and_le_two_mul).

## Sources

- [Formal Book blueprint: chapter/chapter02.tex, line 3](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter02.tex#L3)
