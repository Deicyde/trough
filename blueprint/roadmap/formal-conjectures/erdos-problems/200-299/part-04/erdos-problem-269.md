---
declaration: theorem
origin: cited
lean: Erdos269.erdos_269.variants.rational, Erdos269.erdos_269.variants.irrational, Erdos269.erdos_269.variants.infinite
statement: formalized
---

# Erdős Problem 269

> *Reference:* [erdosproblems.com/269](https://www.erdosproblems.com/269)

*Quoted from [FormalConjectures/ErdosProblems/269.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/269.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/269](https://www.erdosproblems.com/269).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos269.erdos_269.variants.rational`

Open: stated without proof.

> Let $P$ be a finite set of primes with $|P| \ge 2$ and let
> $\{a_1 < a_2 < \dots\}$ be the set of positive integers whose prime factors
> are all in $P$. Is the sum
>
> $$ \sum_{n=1}^\infty \frac{1}{[a_1,\ldots,a_n]} $$
>
> rational?

```lean
theorem erdos_269.variants.rational :
    ∀ᵉ (P : Finset ℕ) (h : ∀ p ∈ P, p.Prime) (h_card : P.card ≥ 2),
    ∃ (q : ℚ), q = (series (P : Set ℕ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/269.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/269.lean#L63).

## `Erdos269.erdos_269.variants.irrational`

Open: stated without proof.

> Let $P$ be a finite set of primes with $|P| \ge 2$ and let
> $\{a_1 < a_2 < \dots\}$ be the set of positive integers whose prime factors
> are all in $P$. Is the sum
>
> $$ \sum_{n=1}^\infty \frac{1}{[a_1,\ldots,a_n]} $$
>
> irrational?

```lean
theorem erdos_269.variants.irrational :
    ∀ᵉ (P : Finset ℕ) (h : ∀ p ∈ P, p.Prime) (h_card : P.card ≥ 2),
    Irrational (series (P : Set ℕ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/269.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/269.lean#L76).

## `Erdos269.erdos_269.variants.infinite`

Solved: stated here without proof.

> This theorem addresses the case where the set of primes $P$ is infinite. In this case the sum is
> irrational.

```lean
theorem erdos_269.variants.infinite (P : Set ℕ) (h : ∀ p ∈ P, p.Prime) (h_inf : P.Infinite) :
  Irrational (series P)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/269.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/269.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/269.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/269.lean)
- [erdosproblems.com/269](https://www.erdosproblems.com/269)
