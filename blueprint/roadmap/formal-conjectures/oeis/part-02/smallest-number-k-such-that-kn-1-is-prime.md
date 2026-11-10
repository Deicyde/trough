---
declaration: theorem
origin: cited
lean: OeisA34693.exists_k, OeisA34693.exists_k_stronger, OeisA34693.exists_k_best_possible, OeisA34693.a_isBigO, OeisA34693.a_unbounded
statement: formalized
---

# Smallest number $k$ such that $kn + 1$ is prime

> *References:*
> - [A34693](https://oeis.org/A34693)

*Quoted from [FormalConjectures/OEIS/34693.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 4 open and 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA34693.exists_k`

Open: stated without proof.

> Conjecture: for every $n > 1$ there exists a number $k < n$ such that $nk + 1$ is a prime.

```lean
theorem exists_k {n : ℕ} (hn : 1 < n) : ∃ k < n, (n * k + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34693.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean#L61).

## `OeisA34693.exists_k_stronger`

Open: stated without proof.

> A stronger conjecture: for every n there exists a number $k < 1 + n^{0.75}$ such that
> $nk + 1$ is a prime.

```lean
theorem exists_k_stronger {n : ℕ} (hn : 0 < n) : ∃ k : ℕ,
    k < 1 + (Real.nthRoot 4 n) ^ 3 ∧ (n * k + 1).Prime
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34693.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean#L67).

## `OeisA34693.exists_k_best_possible`

Proved here.

> The expression $1 + n^{0.74}$ does not work as an upper bound.

```lean
theorem exists_k_best_possible : ∃ n > (0 : ℕ), ∀ (k : ℕ),
    k < 1 + (Real.nthRoot 100 n) ^ 74 → ¬(n * k + 1).Prime
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34693.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean#L73).

## `OeisA34693.a_isBigO`

Open: stated without proof.

> Conjecture: $a(n) = O(\log(n)\log(\log(n)))$.

```lean
theorem a_isBigO : (fun n ↦ (a n : ℝ)) =O[atTop] (fun n ↦ Real.log n * Real.log (Real.log n))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34693.lean, line 96](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean#L96).

## `OeisA34693.a_unbounded`

Open: stated without proof.

> Counter-conjecture to `a_isBigO`: $a(n) / (\log n \log \log n)$ is unbounded.

```lean
theorem a_unbounded : ¬BddAbove (Set.range fun n ↦ a n / (Real.log n * Real.log (Real.log n)))
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/34693.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean#L101).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/34693.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/34693.lean)
- [A34693](https://oeis.org/A34693)
