---
declaration: theorem
origin: cited
lean: Erdos218.erdos_218.variants.le, Erdos218.erdos_218.variants.ge, Erdos218.erdos_218.variants.infinite_equal_prime_gap
statement: formalized
---

# Erdős Problem 218

> *Reference:* [erdosproblems.com/218](https://www.erdosproblems.com/218)

*Quoted from [FormalConjectures/ErdosProblems/218.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/218.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/218](https://www.erdosproblems.com/218).

The file states 3 research or textbook statements: 3 open.

## `Erdos218.erdos_218.variants.le`

Open: stated without proof.

> The set of indices $n$ for which a prime gap is followed by a larger or equal prime gap has a
> natural density of $\frac 1 2$.

```lean
theorem erdos_218.variants.le : {n | primeGap n ≤ primeGap (n + 1)}.HasDensity <| 1 / 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/218.lean, line 35](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/218.lean#L35).

## `Erdos218.erdos_218.variants.ge`

Open: stated without proof.

> The set of indices $n$ for which a prime gap is preceded by a larger or equal prime gap has a
> natural density of $\frac 1 2$.

```lean
theorem erdos_218.variants.ge : {n | primeGap (n + 1) ≤ primeGap n}.HasDensity <| 1 / 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/218.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/218.lean#L43).

## `Erdos218.erdos_218.variants.infinite_equal_prime_gap`

Open: stated without proof.

> There are infinitely many indices $n$ such that the prime gap at $n$ is equal to the prime gap
> at $n+1$. This is equivalent to the existence of infinitely many arithmetic progressions of
> length $3$, see `erdos_141.variants.infinite_three`.

```lean
theorem erdos_218.variants.infinite_equal_prime_gap : {n | primeGap n = primeGap (n + 1)}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/218.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/218.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/218.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/218.lean)
- [erdosproblems.com/218](https://www.erdosproblems.com/218)
