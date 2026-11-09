---
declaration: theorem
origin: cited
lean: Erdos9.erdos_9.variants.infinite, Erdos9.erdos_9
statement: formalized
---

# Erdős Problem 9

> *Reference:* [erdosproblems.com/9](https://www.erdosproblems.com/9)

*Quoted from [FormalConjectures/ErdosProblems/9.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/9.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/9](https://www.erdosproblems.com/9).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 3 test statements, counted here but not shown.

## `Erdos9.erdos_9.variants.infinite`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/de08009e59829727653bfa20b8d8f7ed1b1baf79/erdos-9/Solution.lean#L25](https://github.com/linrock/math-proofs/blob/de08009e59829727653bfa20b8d8f7ed1b1baf79/erdos-9/Solution.lean#L25).

> The set is known to be infinite. In [Er77c] Erdős credits Schinzel with proving that there are
> infinitely many odd integers not of this form, but gives no reference.
>
> [Er77c] Erdős, P., _Problems and results on combinatorial number theory. III._.

```lean
theorem erdos_9.variants.infinite : Erdos9A.Infinite
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/9.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/9.lean#L70).

## `Erdos9.erdos_9`

Open: stated without proof.

> Is the upper density of the set of odd numbers that cannot be expressed as a prime plus
> two powers of 2 positive?

```lean
theorem erdos_9 : 0 < Erdos9A.upperDensity
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/9.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/9.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/9.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/9.lean)
- [erdosproblems.com/9](https://www.erdosproblems.com/9)
