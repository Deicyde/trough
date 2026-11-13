---
declaration: theorem
origin: cited
lean: OeisA357513.a357513_supercongruence, OeisA357513.general_supercongruence
statement: formalized
---

# Numerator of a sum involving binomial coefficients

> $a(n)$ is the numerator of
> $\sum_{k = 1}^n \frac{1}{k^3} \binom{n}{k}^2 \binom{n+k}{k}^2$ for $n \ge 1$
> with $a(0) = 0$.
>
> *References:*
> - [A357513](https://oeis.org/A357513)

*Quoted from [FormalConjectures/OEIS/357513.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/357513.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 7 test statements, counted here but not shown.

## `OeisA357513.a357513_supercongruence`

Solved: stated here; a Lean proof is at [https://github.com/google-deepmind/formal-conjectures/blob/9c7f21e7d4445637538bc1817b058b9b3f31bd2b/FormalConjectures/OEIS/357513.lean#L232](https://github.com/google-deepmind/formal-conjectures/blob/9c7f21e7d4445637538bc1817b058b9b3f31bd2b/FormalConjectures/OEIS/357513.lean#L232).

> We have  $a(p-1) \equiv 0 \pmod{p^4}$ for all primes $p \ge 3$ except $p=7$.
>
> proved by AlphaProof

```lean
theorem a357513_supercongruence (p : ℕ) (hp : p.Prime) (h_ge3 : p ≥ 3) (h_neq7 : p ≠ 7) :
    (a (p - 1) : ℤ) ≡ 0 [ZMOD (p : ℤ) ^ 4]
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/357513.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/357513.lean#L81).

## `OeisA357513.general_supercongruence`

Open: stated without proof.

> We conjecture that $u(p-1) == 0 (mod p^4)$ for all primes $p$,
> with a finite number of exceptions that depend on $m$.

```lean
theorem general_supercongruence (m : ℕ) : ∃ (exceptions : Finset ℕ), ∀ p, p.Prime →
    p ∉ exceptions → u m (p - 1) = (0 : ZMod (p ^ 4))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/357513.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/357513.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/357513.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/357513.lean)
- [A357513](https://oeis.org/A357513)
