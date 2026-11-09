---
declaration: theorem
origin: cited
lean: Erdos313.erdos_313, Erdos313.erdos_313.variants.primary_pseudoperfect_are_infinite, Erdos313.erdos_313.variants.exists_at_least_eight_primary_pseudoperfect
statement: formalized
---

# Erdős Problem 313

> *References:*
> - [erdosproblems.com/313](https://www.erdosproblems.com/313)
> - [A54377](https://oeis.org/A54377) (Primary pseudoperfect numbers)

*Quoted from [FormalConjectures/ErdosProblems/313.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/313.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/313](https://www.erdosproblems.com/313).

The file states 3 research or textbook statements: 2 open and 1 textbook result. It also has 2 test statements, counted here but not shown.

## `Erdos313.erdos_313`

Open: stated without proof.

> Are there infinitely many pairs `(m, P)` where `m ≥ 2` is an integer
> and `P` is a set of distinct primes such that the following equation holds:
> $\sum_{p \in P} \frac{1}{p} = 1 - \frac{1}{m}$?

```lean
theorem erdos_313 : erdos313Solutions.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/313.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/313.lean#L46).

## `Erdos313.erdos_313.variants.primary_pseudoperfect_are_infinite`

Open: stated without proof.

> It is conjectured that the set of primary pseudoperfect numbers is infinite.

```lean
theorem erdos_313.variants.primary_pseudoperfect_are_infinite :
    Set.Infinite {n | IsPrimaryPseudoperfect n}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/313.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/313.lean#L67).

## `Erdos313.erdos_313.variants.exists_at_least_eight_primary_pseudoperfect`

Textbook result, proved here.

> There are at least 8 primary pseudoperfect numbers. The first eight terms of
> [A54377](https://oeis.org/A54377) are exhibited together with their explicit
> prime decompositions.

```lean
theorem erdos_313.variants.exists_at_least_eight_primary_pseudoperfect :
    8 ≤ (Set.encard {n | IsPrimaryPseudoperfect n})
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/313.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/313.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/313.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/313.lean)
- [erdosproblems.com/313](https://www.erdosproblems.com/313)
