---
declaration: theorem
origin: cited
lean: OeisA185895.conjecture_1, OeisA185895.conjecture_2, OeisA185895.conjecture_3
statement: formalized
---

# Coefficients of $\prod_{k>0} (1 - x^k/k!)$

> The sequence $a(n)$ has exponential generating function
>
> $$E(x) = \prod_{k=1}^\infty \left(1 - \frac{x^k}{k!}\right),$$
>
> so that $a(n) = n! [x^n] \prod_{k=1}^n \left(1 - \frac{x^k}{k!}\right)$.
>
> Since $a(n)$ is a sum of multinomial coefficients with $\pm$ signs, it is always
> an integer.
>
> *References:*
> - [A185895](https://oeis.org/A185895)

*Quoted from [FormalConjectures/OEIS/185895.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185895.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 5 test statements, counted here but not shown.

## `OeisA185895.conjecture_1`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-sol-nk5wh4g0vh3546nm/oeis_185895_conjecture_1/Submission/Spec.lean#L4835](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-sol-nk5wh4g0vh3546nm/oeis_185895_conjecture_1/Submission/Spec.lean#L4835).

> $a(n)$ differs in sign from $a(n-1)$ if and only if $n$ is a triangular number
> (checked up to $n = 1225 = (50 \cdot 51)/2$).
> - _Peter Bala_, Mar 17 2022

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) :
    a n * a (n - 1) < 0 ↔ n.IsTriangular
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/185895.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185895.lean#L105).

## `OeisA185895.conjecture_2`

Solved: stated here; a Lean proof is at [https://github.com/kei825/oeis-a185895-conjecture2/blob/8ddd5a7d2bde415940f944440921fd760283f79d/OeisA185895Conjecture2.lean#L4959-L4961](https://github.com/kei825/oeis-a185895-conjecture2/blob/8ddd5a7d2bde415940f944440921fd760283f79d/OeisA185895Conjecture2.lean#L4959-L4961).

> The coefficients $c(n)$ of $A(x)^2 = (\sum_{n \ge 0} a(n) x^n)^2$ differ in sign from $c(n-1)$
> if and only if $n$ is a triangular number.
> - _Peter Bala_, Mar 17 2022
>
> **Proof sketch** (the kernel-checked development lives at the `formal_proof` permalink below).
> Write $a(n)/n! = \sum_j (-1)^j L_j(n)$, where $L_j(n)$ is the sum of $\prod_{s \in S} 1/s!$ over
> all sets $S$ of $j$ distinct positive integers with sum $n$. A "down map" (lowering by one the
> least element of $S$ above its first gap) gives $L_{k-1}(n) \le \frac{91}{100} L_k(n)$ for all
> $k \ge 1$ and $n \ge k(k+1)/2$. Hence the top nonzero layer $L_m(n)$ dominates, where
> $m(m+1)/2 \le n < (m+1)(m+2)/2$; this reproves `conjecture_1` and gives
> $|a(n)| \ge \frac{9}{100} n! L_m(n)$. Since $c(n) = 2a(n) + \sum_{0\lt k\lt n} a(k)a(n-k)$, the sign of
> $c(n)$ equals that of $a(n)$ whenever $\sum_{0\lt k\lt n} |a(k)a(n-k)| < 2|a(n)|$. For $n \le 2500$,
> conjecture 2 is checked in the kernel from a certified table of $a(n)$; for $n > 2500$, explicit
> estimates (rational arithmetic and elementary bounds only) bound the cross sum by
> $0.18 \cdot n! L_m(n)$, which is less than $2|a(n)|$.

```lean
theorem conjecture_2 (n : ℕ) (hn : 0 < n) :
    c n * c (n - 1) < 0 ↔ n.IsTriangular
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/185895.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185895.lean#L130).

## `OeisA185895.conjecture_3`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/oeis-a185895-conjecture3/blob/e40e3db2b47beeef22b00a481fc3a41b518168d9/lean/OeisA185895Conjecture3FC.lean#L579-L589](https://github.com/KitaKen1/oeis-a185895-conjecture3/blob/e40e3db2b47beeef22b00a481fc3a41b518168d9/lean/OeisA185895Conjecture3FC.lean#L579-L589).

> The Gauss congruences $a(n \cdot p^k) \equiv a(n \cdot p^{k-1}) \pmod{p^k}$ hold
> for all primes $p$ and positive integers $n$ and $k$.
> - _Peter Bala_, Mar 17 2022

```lean
theorem conjecture_3 (p : ℕ) (hp : p.Prime) (n k : ℕ) (hn : 0 < n) (hk : 0 < k) :
    a (n * p ^ k) ≡ a (n * p ^ (k - 1)) [ZMOD (p : ℤ) ^ k]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/185895.lean, line 143](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185895.lean#L143).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/185895.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/185895.lean)
- [A185895](https://oeis.org/A185895)
