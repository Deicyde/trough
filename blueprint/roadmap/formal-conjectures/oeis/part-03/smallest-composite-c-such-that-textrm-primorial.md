---
declaration: theorem
origin: cited
lean: OeisA38771.a_n_exists, OeisA38771.conjecture1, OeisA38771.conjecture2
statement: formalized
---

# Smallest composite $c$ such that $\textrm{primorial}(n) + c$ is prime

> *References:*
> - [A038771](https://oeis.org/A038771)

*Quoted from [FormalConjectures/OEIS/38771.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38771.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 4 test statements, counted here but not shown.

## `OeisA38771.a_n_exists`

Textbook result, proved here.

> $a(n) \ne 0$ for all $n$ (i.e., a suitable composite $c$ always exists).
> The following more general statement follows from Dirichlet's theorem
> on primes in arithmetic progressions:
>   there doesn't exist a > 0 natural number such that p - a is prime for every prime p > a.
>
> Choose q prime such that q is coprime with a, and p > a + q prime such that q | p - a
> (such a p exists from Dirichlet's theorem). Then p - a is composite, a contradiction.

```lean
theorem a_n_exists (n : ℕ) : a n ≠ 0
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38771.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38771.lean#L111).

## `OeisA38771.conjecture1`

Open: stated without proof.

> Conjecture:
> $\liminf_{n \to \infty} \frac{a(n)}{p_{n+1}^2} = 1 <$
> $\limsup_{n \to \infty} \frac{a(n)}{p_{n+1}^2} = 2$.
> - Charles R Greathouse IV and Thomas Ordowski, Apr 24 2015

```lean
theorem conjecture1 :
    let p_next_sq (n : ℕ) : ℝ := ((Nat.nth Nat.Prime n : ℝ)) ^ 2
    let seq (n : ℕ) : ℝ := (a n : ℝ) / p_next_sq n
    (liminf seq atTop = 1) ∧ (limsup seq atTop = 2)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38771.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38771.lean#L139).

## `OeisA38771.conjecture2`

Open: stated without proof.

> All the terms in this sequence have exactly two prime factors.
> This conjecture is true for the first 133 terms.
> - [Dmitry Kamenetsky](https://oeis.org/wiki/User:Dmitry_Kamenetsky), Jan 06 2019

```lean
theorem conjecture2 (n : ℕ) : (a n).IsSemiprime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/38771.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38771.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/38771.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/38771.lean)
- [A038771](https://oeis.org/A038771)
