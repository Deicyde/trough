---
declaration: theorem
origin: cited
lean: OeisA228425.conjecture_1, OeisA228425.conjecture_2, OeisA228425.conjecture_3, OeisA228425.conjecture_4, OeisA228425.conjecture_5
statement: formalized
---

# Partitions of $n$ into $x + y$ with $x(x+1)/2 + y^2$ prime

> Number of ways to write $n = x + y$ ($x, y > 0$) with $x(x+1)/2 + y^2$ prime.
>
> *References:*
> - [A228425](https://oeis.org/A228425)

*Quoted from [FormalConjectures/OEIS/228425.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 5 open. It also has 5 test statements, counted here but not shown.

## `OeisA228425.conjecture_1`

Open: stated without proof.

> Conjecture: $a(n) > 0$ for all $n > 1$.

```lean
theorem conjecture_1 (n : ℕ) (hn : n > 1) : a n > 0
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228425.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean#L59).

## `OeisA228425.conjecture_2`

Open: stated without proof.

> We also conjecture that any integer $n > 1$ can be written as $x + y$ ($x, y > 0$) with
> $p_k(x) + p_{k+1}(y)$ prime, if and only if $k$ is among $3, 39, 99$.

```lean
theorem conjecture_2 (k : ℕ) (hk : 3 ≤ k) :
    (∀ n : ℕ, 1 < n → ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      Nat.Prime (Nat.polygonalNumber k x + Nat.polygonalNumber (k + 1) y)) ↔
    k = 3 ∨ k = 39 ∨ k = 99
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228425.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean#L67).

## `OeisA228425.conjecture_3`

Open: stated without proof.

> The pair $(k, m)$ works if $k$ is among $3, 4, 6$, and $m > k$ is not congruent to $k$ modulo $2$,
> in the sense that all sufficiently large integers $n$ can be written as $x + y$ ($x, y > 0$) with
> $p_k(x) + p_m(y)$ prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_3 (k m : ℕ) (hk : k = 3 ∨ k = 4 ∨ k = 6) (hm : k < m)
    (hmod : ¬ m ≡ k [MOD 2]) :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      Nat.Prime (Nat.polygonalNumber k x + Nat.polygonalNumber m y)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228425.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean#L80).

## `OeisA228425.conjecture_4`

Open: stated without proof.

> For $k = 5$, the pair $(5, m)$ works (with $m > 5$) if $m$ is congruent to $0$ or $4$ modulo $6$,
> in the sense that all sufficiently large integers $n$ can be written as $x + y$ ($x, y > 0$) with
> $p_5(x) + p_m(y)$ prime.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_4 (m : ℕ) (hm : 5 < m) (hmod : m ≡ 0 [MOD 6] ∨ m ≡ 4 [MOD 6]) :
    ∀ᶠ (n : ℕ) in Filter.atTop, ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      Nat.Prime (Nat.polygonalNumber 5 x + Nat.polygonalNumber m y)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228425.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean#L93).

## `OeisA228425.conjecture_5`

Open: stated without proof.

> The only pairs $(k, m)$ with $2 < k \le 10$ and $k < m \le 100$ such that any integer $n > 1$ can
> be written as $x + y$ ($x, y > 0$) with $p_k(x) + p_m(y)$ prime, are the $31$ pairs in
> `sunPolygonalPairs`.
> - _Zhi-Wei Sun_

```lean
theorem conjecture_5 (k m : ℕ) (hk : 2 < k) (hk10 : k ≤ 10) (hm : k < m) (hm100 : m ≤ 100) :
    (∀ n : ℕ, 1 < n → ∃ x y : ℕ, 0 < x ∧ 0 < y ∧ x + y = n ∧
      Nat.Prime (Nat.polygonalNumber k x + Nat.polygonalNumber m y)) ↔
    (k, m) ∈ sunPolygonalPairs
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/228425.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean#L115).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/228425.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/228425.lean)
- [A228425](https://oeis.org/A228425)
