---
declaration: theorem
origin: cited
lean: OeisA234246.conjecture_1, OeisA234246.conjecture_2, OeisA234246.conjecture_3, OeisA234246.conjecture_4, OeisA234246.conjecture_5, OeisA234246.conjecture_6
statement: formalized
---

# Number of integers $0 < k < n$ such that $k \phi(n - k) + 1$ is a square

> Let $\phi$ denote Euler's totient function. The sequence $a(n)$ counts the integers $0 < k < n$
> such that $k \phi(n - k) + 1$ is a square.
>
> *References:*
> - [A234246](https://oeis.org/A234246)

*Quoted from [FormalConjectures/OEIS/234246.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 6 open. It also has 5 test statements, counted here but not shown.

## `OeisA234246.conjecture_1`

Open: stated without proof.

> Conjecture (i): $a(n) > 0$ if $n$ is not a divisor of $6$.

```lean
theorem conjecture_1 (n : ℕ) (hn : 0 < n) (hd : ¬(n ∣ 6)) : 0 < a n
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L65).

## `OeisA234246.conjecture_2`

Open: stated without proof.

> Conjecture (i): The only values of $n$ with $a(n) = 1$ are $4, 5, 8, 9, 12, 13, 24, 33, 49$.

```lean
theorem conjecture_2 (n : ℕ) :
    a n = 1 ↔ n ∈ ({4, 5, 8, 9, 12, 13, 24, 33, 49} : Finset ℕ)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L72).

## `OeisA234246.conjecture_3`

Open: stated without proof.

> Conjecture (ii): If $n \ge 60$, then $k + \phi(n - k)$ is a square for some $0 < k < n$.

```lean
theorem conjecture_3 (n : ℕ) (hn : 60 ≤ n) :
    ∃ k, 0 < k ∧ k < n ∧ IsSquare (k + (n - k).totient)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L80).

## `OeisA234246.conjecture_4`

Open: stated without proof.

> Conjecture (ii): If $n > 60$, then $\sigma(k) + \phi(n - k)$ is a square for some $0 < k < n$,
> where $\sigma(k)$ is the sum of all positive divisors of $k$.

```lean
theorem conjecture_4 (n : ℕ) (hn : 60 < n) :
    ∃ k, 0 < k ∧ k < n ∧ IsSquare (σ 1 k + (n - k).totient)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L89).

## `OeisA234246.conjecture_5`

Open: stated without proof.

> Conjecture (iii): If $n > 7$ is not equal to $10$ or $20$, then $\phi(k)\phi(n - k) + 1$
> is a square for some $0 < k < n$.

```lean
theorem conjecture_5 (n : ℕ) (hn : 7 < n) (hne10 : n ≠ 10) (hne20 : n ≠ 20) :
    ∃ k, 0 < k ∧ k < n ∧ IsSquare (k.totient * (n - k).totient + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L98).

## `OeisA234246.conjecture_6`

Open: stated without proof.

> Conjecture (iv): If $n > 7$ is not equal to $10$ or $19$, then $(\phi(k) + \phi(n - k)) / 2$
> is a triangular number for some $0 < k < n$.

```lean
theorem conjecture_6 (n : ℕ) (hn : 7 < n) (hne10 : n ≠ 10) (hne19 : n ≠ 19) :
    ∃ k, 0 < k ∧ k < n ∧ ∃ m : ℕ, k.totient + (n - k).totient = m * (m + 1)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/234246.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/234246.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/234246.lean)
- [A234246](https://oeis.org/A234246)
