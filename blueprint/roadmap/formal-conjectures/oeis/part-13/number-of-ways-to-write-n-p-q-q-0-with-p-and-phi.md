---
declaration: theorem
origin: cited
lean: OeisA233549.conjecture_1, OeisA233549.conjecture_2, OeisA233549.conjecture_3
statement: formalized
---

# Number of ways to write $n = p + q$ ($q > 0$) with $p$ and $(\phi(p)\phi(q))^4 + 1$ prime

> Let $\phi$ denote Euler's totient function. The sequence $a(n)$ counts the representations
> $n = p + q$ ($q > 0$) where $p$ and $(\phi(p)\phi(q))^4 + 1$ are both prime.
>
> *References:*
> - [A233549](https://oeis.org/A233549)

*Quoted from [FormalConjectures/OEIS/233549.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233549.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 open. It also has 5 test statements, counted here but not shown.

## `OeisA233549.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ for all $n > 2$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 2 < n) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233549.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233549.lean#L64).

## `OeisA233549.conjecture_2`

Open: stated without proof.

> Conjecture (ii): If $n > 2$ is not equal to $26$, then there is a prime $p < n$
> with $(\phi(p)\phi(n-p))^2 + 1$ prime.

```lean
theorem conjecture_2 (n : ℕ) (hn : 2 < n) (hne : n ≠ 26) :
    ∃ p < n, p.Prime ∧ Nat.Prime ((p.totient * (n - p).totient) ^ 2 + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233549.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233549.lean#L72).

## `OeisA233549.conjecture_3`

Open: stated without proof.

> Conjecture (iii): If $n > 3$ is different from $9$ and $16$, then there is a prime $p < n$
> with $((p+1)\phi(n-p))^2 + 1$ prime.

```lean
theorem conjecture_3 (n : ℕ) (hn : 3 < n) (hne9 : n ≠ 9) (hne16 : n ≠ 16) :
    ∃ p < n, p.Prime ∧ Nat.Prime (((p + 1) * (n - p).totient) ^ 2 + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/233549.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233549.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/233549.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/233549.lean)
- [A233549](https://oeis.org/A233549)
