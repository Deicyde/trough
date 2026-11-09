---
declaration: theorem
origin: cited
lean: FermatCatalanConjecture.fermat_catalan, FermatCatalanConjecture.fermat_catalan.variants.darmon_granville
statement: formalized
---

# Fermat-Catalan conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Fermat-Catalan_conjecture)

*Quoted from [FormalConjectures/Wikipedia/FermatCatalanConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/FermatCatalanConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `FermatCatalanConjecture.fermat_catalan`

Open: stated without proof.

> The **Fermat–Catalan conjecture** states that the equation
> $a^m + b^n = c^k$ has only finitely many solutions $(a,b,c,m,n,k)$ with distinct triplets of values
> $(a^m, b^n, c^k)$ where $a, b, c$ are positive coprime integers and $m, n, k$ are positive integers satisfying
> $\frac 1 m + \frac 1 n + \frac 1 k < 1$.

```lean
theorem fermat_catalan : fermatCatalanConjecture
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FermatCatalanConjecture.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/FermatCatalanConjecture.lean#L59).

## `FermatCatalanConjecture.fermat_catalan.variants.darmon_granville`

Solved: stated here without proof.

> By the **Darmon-Granville** theorem,
> for any fixed choice of positive integers m, n and k satisfying $\frac 1 m + \frac 1 n + \frac 1 k < 1$,
> only finitely many coprime triples $(a, b, c)$ solving $a^m + b^n = c^k$ exist.

```lean
theorem fermat_catalan.variants.darmon_granville
    (m n k : ℕ) (hm : 0 < m) (hn : 0 < n) (hk : 0 < k)
    (H : (1 / m : ℝ) + 1 / n + 1 / k < 1) :
    {(a, b, c) : ℕ × ℕ × ℕ | 0 < a ∧ 0 < b ∧ 0 < c ∧ a^m + b^n = c^k ∧
      ({a, b, c} : Set _).Pairwise Nat.Coprime}.Finite
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/FermatCatalanConjecture.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/FermatCatalanConjecture.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/FermatCatalanConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/FermatCatalanConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Fermat-Catalan_conjecture)
