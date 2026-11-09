---
declaration: theorem
origin: cited
lean: Kurepa.kurepa_conjecture, Kurepa.kurepa_conjecture.variants.prime, Kurepa.kurepa_conjecture.prime_reduction, Kurepa.kurepa_conjecture.variants.gcd, Kurepa.kurepa_conjecture.gcd_reduction
statement: formalized
---

# Kurepa's conjecture

> *Reference:* [On the left factorial function !N](https://oeis.org/A3422), by *Đuro Kurepa* Math. Balkanica 1, p. 147-153, 1971

*Quoted from [FormalConjectures/Paper/Kurepa.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 textbook results. It also has 2 test statements, counted here but not shown.

## `Kurepa.kurepa_conjecture`

Open: stated without proof.

> ## Kurepa's conjecture
>
> For all $n$,
>
> $$!n\not\equiv 0 \mod n$$
>
> This appears as B44 "Sums of factorials."
> in [Unsolved Problems in Number Theory](https://doi.org/10.1007/978-0-387-26677-0)
> by *Richard K. Guy*

```lean
theorem kurepa_conjecture (n : ℕ) (h_n : 2 < n) : (!n : ℕ) % n ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Kurepa.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean#L50).

## `Kurepa.kurepa_conjecture.variants.prime`

Open: stated without proof.

> This statement can be reduced to the prime case only.

```lean
theorem kurepa_conjecture.variants.prime (p : ℕ) (h_p : 2 < p) :
    p.Prime → (!p : ℕ) % p ≠ 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Kurepa.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean#L57).

## `Kurepa.kurepa_conjecture.prime_reduction`

Textbook result, proved here.

> Kurepa's conjecture for all integers greater than 2 is equivalent to the conjecture restricted to primes greater than 2.

```lean
theorem kurepa_conjecture.prime_reduction : (∀ n, 2 < n → (!n : ℕ) % n ≠ 0)
    ↔ (∀ p, 2 < p → p.Prime → (!p : ℕ) % p ≠ 0)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Kurepa.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean#L65).

## `Kurepa.kurepa_conjecture.variants.gcd`

Open: stated without proof.

> An equivalent formulation in terms of the gcd of $n!$ and $!n$.

```lean
theorem kurepa_conjecture.variants.gcd (n : ℕ) : 2 < n → (n !).gcd (! n) = 2
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Kurepa.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean#L96).

## `Kurepa.kurepa_conjecture.gcd_reduction`

Textbook result, proved here.

> Kurepa's conjecture for all integers greater than 2 is equivalent to the statement that $\gcd(n!, !n) = 2$ for all integers greater than 2.

```lean
theorem kurepa_conjecture.gcd_reduction : (∀ n, 2 < n → (!n : ℕ) % n ≠ 0)
    ↔ (∀ n, 2 < n → (n)!.gcd (!n) = 2)
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Paper/Kurepa.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/Kurepa.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Paper/Kurepa.lean)
- [On the left factorial function !N](https://oeis.org/A3422)
