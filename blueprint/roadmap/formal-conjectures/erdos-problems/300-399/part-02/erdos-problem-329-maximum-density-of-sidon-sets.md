---
declaration: theorem
origin: cited
lean: Erdos329.erdos_329, Erdos329.erdos_329.variants.lower_bound, Erdos329.erdos_329.variants.kruckeberg_1961, Erdos329.erdos_329.variants.turan_1941, Erdos329.erdos_329.variants.converse_implication, Erdos329.exists_sidon_pos_density
statement: formalized
---

# Erdős Problem 329: Maximum Density of Sidon Sets

> *References:*
> - [erdosproblems.com/329](https://www.erdosproblems.com/329)
> - [AlMi25] B. Alexeev and D. G. Mixon, Forbidden Sidon subsets of perfect difference sets, featuring a human-assisted proof. [arXiv:2510.19804](https://arxiv.org/abs/2510.19804) (2025).
> - [Ha47] Hall, Jr., Marshall, Cyclic projective planes. Duke Math. J. (1947), 1079--1090.

*Quoted from [FormalConjectures/ErdosProblems/329.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/329](https://www.erdosproblems.com/329).

The file states 6 research or textbook statements: 2 open, 3 solved and 1 textbook result.

## `Erdos329.erdos_329`

Open: stated without proof.

> **Erdős Problem 329.**
> Let `A ⊆ ℕ` be a Sidon set. How large can
> `lim sup_{N → ∞} |A ∩ {1,…,N}| / N^{1/2}`
> be?

```lean
theorem erdos_329 : sSup {sidonUpperDensity A | (A : Set ℕ) (_ : IsSidon A)} =
    erdos_329.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L55).

## `Erdos329.erdos_329.variants.lower_bound`

Solved: stated here without proof.

> Erdős proved that upper density `1 / 2` can be attained; in particular,
> there exists a Sidon set whose upper density is *at least* `1 / 2`.

```lean
theorem erdos_329.variants.lower_bound : ∃ (A : Set ℕ), IsSidon A ∧ sidonUpperDensity A ≥ 1/2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L64).

## `Erdos329.erdos_329.variants.kruckeberg_1961`

Solved: stated here without proof.

> Krückeberg ([Kr61]) exhibited an infinite Sidon set `A` with
> `sidonUpperDensity A = 1 / Real.sqrt 2`, improving Erdős’ earlier
> `1 / 2` lower bound.
>
> [Kr61] Krückeberg, Fritz, $B\sb{2}$-Folgen und verwandte Zahlenfolgen. J. Reine Angew. Math. (1961), 53-60.

```lean
theorem erdos_329.variants.kruckeberg_1961 : ∃ (A : Set ℕ), IsSidon A ∧
    sidonUpperDensity A = 1 / Real.sqrt 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L75).

## `Erdos329.erdos_329.variants.turan_1941`

Solved: stated here without proof.

> Erdős and Turán [ErTu41] proved the upper bound of 1.
>
> [ErTu41] Erdős, P. and Turán, P., On a problem of Sidon in additive number theory, and on some related problems. J. London Math. Soc. (1941), 212-215.

```lean
theorem erdos_329.variants.turan_1941 : ∀ (A : Set ℕ), IsSidon A → sidonUpperDensity A ≤ 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L85).

## `Erdos329.erdos_329.variants.converse_implication`

Open: stated without proof.

> The converse: if the maximum density is 1, then any finite Sidon set
> can be embedded in a perfect difference set modulo $n > 0$.
>
> Since the consequent is false (due to the counterexamples in [Ha47] and [AlMi25]),
> this implication is logically equivalent to the statement that the maximum upper
> density of Sidon sets is NOT 1.
> Because the maximum upper density problem is still open, the truth value of this
> implication is also an open research problem.

```lean
theorem erdos_329.variants.converse_implication :
    (sSup {sidonUpperDensity A | (A : Set ℕ) (_ : IsSidon A)} = 1) →
    (∀ (A : Finset ℕ), IsSidon (A : Set ℕ) → ∃ (D : Set ℕ) (n : ℕ) (_ : n > 0),
      ↑A ⊆ D ∧ IsPerfectDifferenceSet D n)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L99).

## `Erdos329.exists_sidon_pos_density`

Textbook result, stated without proof.

> It is possible to construct a Sidon set with positive density.

```lean
theorem exists_sidon_pos_density : ∃ (A : Set ℕ), IsSidon A ∧ 0 < sidonUpperDensity A
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/329.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/329.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/329.lean)
- [erdosproblems.com/329](https://www.erdosproblems.com/329)
