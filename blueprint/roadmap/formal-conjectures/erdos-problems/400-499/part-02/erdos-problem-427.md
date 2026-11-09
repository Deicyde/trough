---
declaration: theorem
origin: cited
lean: Erdos427.erdos_427.variants.shiu, Erdos427.erdos_427, Erdos427.erdos_427.variants.of_shiu
statement: formalized
---

# Erdős Problem 427

> *Reference:* [erdosproblems.com/427](https://www.erdosproblems.com/427)

*Quoted from [FormalConjectures/ErdosProblems/427.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/427.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/427](https://www.erdosproblems.com/427).

The file states 3 research or textbook statements: 3 solved.

## `Erdos427.erdos_427.variants.shiu`

Solved: stated here without proof.

> **Shiu's theorem**: for any $k \geq 1$ and $(a, q) = 1$ there exist infinitely many $k$-tuples of consecutive primes
> $p_m, \dots, p_{m + k - 1}$ all of which are congruent to $a$ modulo $q$.
>
> This is stated ahead of `erdos_427` because the formal proof linked there assumes it, and the
> `assuming` clause must name a declaration that already exists.
>
> [Sh00] Shiu, D. K. L., _Strings of congruent primes_. J. London Math. Soc. (2) (2000), 359-373.

```lean
theorem erdos_427.variants.shiu : ShiuTheorem
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/427.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/427.lean#L64).

## `Erdos427.erdos_427`

Solved: stated here; a Lean proof is at [https://github.com/Jayyhk/erdos-lean/blob/main/problems/427/Erdos427.lean](https://github.com/Jayyhk/erdos-lean/blob/main/problems/427/Erdos427.lean).

> **Erdős Problem 427**: is it true that, for every $n$ and $d$, there exists $k$ such that
>
> $$
>   d \mid p_{n + 1} + \cdots + p_{n + k},
> $$
>
> where $p_r$ denotes the $r$th prime?

```lean
theorem erdos_427 : erdos427
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/427.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/427.lean#L79).

## `Erdos427.erdos_427.variants.of_shiu`

Solved: stated here without proof.

> Cedric Pilatte has observed that a positive solution to Erdős Problem 427 follows from Shiu's theorem.

```lean
theorem erdos_427.variants.of_shiu (H : ShiuTheorem) : erdos427
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/427.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/427.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/427.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/427.lean)
- [erdosproblems.com/427](https://www.erdosproblems.com/427)
