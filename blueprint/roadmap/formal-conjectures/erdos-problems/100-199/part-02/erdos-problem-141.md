---
declaration: theorem
origin: cited
lean: Erdos141.erdos_141, Erdos141.erdos_141.variants.first_cases, Erdos141.erdos_141.variants.eleven, Erdos141.erdos_141.variants.infinite_three, Erdos141.erdos_141.variants.infinite_general_case
statement: formalized
---

# Erdős Problem 141

> *References:*
> - [erdosproblems.com/141](https://www.erdosproblems.com/141)
> - [Wikipedia](https://en.wikipedia.org/wiki/Primes_in_arithmetic_progression#Consecutive_primes_in_arithmetic_progression)

*Quoted from [FormalConjectures/ErdosProblems/141.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/141](https://www.erdosproblems.com/141).

The file states 5 research or textbook statements: 4 open and 1 solved. It also has 2 test statements, counted here but not shown.

## `Erdos141.erdos_141`

Open: stated without proof.

> Let $k≥3$. Are there $k$ consecutive primes in arithmetic progression?

```lean
theorem erdos_141 :
    ∀ k ≥ 3, ∃ (s : Set ℕ), s.IsAPAndPrimeProgressionOfLength k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/141.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean#L78).

## `Erdos141.erdos_141.variants.first_cases`

Solved: stated here without proof.

> The existence of such progressions has been verified for $k≤10$.

```lean
theorem erdos_141.variants.first_cases :
    (∀ k ≥ 3, k ≤ 10 → ∃ (s : Set ℕ), s.IsAPAndPrimeProgressionOfLength k)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/141.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean#L86).

## `Erdos141.erdos_141.variants.eleven`

Open: stated without proof.

> Are there $11$ consecutive primes in arithmetic progression?

```lean
theorem erdos_141.variants.eleven :
    ∃ (s : Set ℕ), s.IsAPAndPrimeProgressionOfLength 11
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/141.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean#L94).

## `Erdos141.erdos_141.variants.infinite_three`

Open: stated without proof.

> It is open, even for $k=3$, whether there are infinitely many such progressions.

```lean
theorem erdos_141.variants.infinite_three :
    (consecutivePrimeArithmeticProgressions 3).Infinite
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/141.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean#L108).

## `Erdos141.erdos_141.variants.infinite_general_case`

Open: stated without proof.

> Fix a $k \geq 3$. Is it true that there are infinitely many arithmetic prime progressions of length $k$?

```lean
theorem erdos_141.variants.infinite_general_case :
    ∀ k ≥ 3, (consecutivePrimeArithmeticProgressions k).Infinite
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/141.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean#L116).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/141.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/141.lean)
- [erdosproblems.com/141](https://www.erdosproblems.com/141)
