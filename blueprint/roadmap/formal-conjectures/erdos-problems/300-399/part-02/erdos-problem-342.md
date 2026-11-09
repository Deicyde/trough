---
declaration: theorem
origin: cited
lean: Erdos342.erdos_342.parts.i, Erdos342.erdos_342.parts.ii, Erdos342.erdos_342.parts.iii
statement: formalized
---

# Erdős Problem 342

> *References:*
> - [erdosproblems.com/342](https://www.erdosproblems.com/342)
> - [Ben Green's Open Problem 7](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.7)
> - [OEIS A002858](https://oeis.org/A002858)
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory* (2004), xviii+437.

*Quoted from [FormalConjectures/ErdosProblems/342.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/342.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/342](https://www.erdosproblems.com/342).

The file states 3 research or textbook statements: 3 open. It also has 4 test statements, counted here but not shown.

## `Erdos342.erdos_342.parts.i`

Open: stated without proof.

> Do infinitely many pairs $(a, a+2)$ occur in Ulam's sequence?

```lean
theorem erdos_342.parts.i :
    ∀ a : ℕ → ℕ, IsUlamSequence a →
      Set.Infinite {n : ℕ | ∃ m, a m = a n + 2}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/342.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/342.lean#L115).

## `Erdos342.erdos_342.parts.ii`

Open: stated without proof.

> Does Ulam's sequence eventually have periodic differences? That is, is $a(n+1) - a(n)$ eventually periodic?

```lean
theorem erdos_342.parts.ii :
    ∀ a : ℕ → ℕ, IsUlamSequence a →
      let d (n : ℕ) : ℤ := a (n + 1) - a n
      ∃ p > 0, ∀ᶠ m in atTop, d (m + p) = d m
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/342.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/342.lean#L124).

## `Erdos342.erdos_342.parts.iii`

Open: stated without proof.

> Part (iii), is the density of the sequence 0?

```lean
theorem erdos_342.parts.iii :
    ∀ a : ℕ → ℕ, IsUlamSequence a →
      Set.upperDensity (Set.range a) = 0
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [40 Sequences, series, summability](../../../by-subject/part-02/40-sequences-series-summability/README.md). Declared in [FormalConjectures/ErdosProblems/342.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/342.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/342.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/342.lean)
- [erdosproblems.com/342](https://www.erdosproblems.com/342)
