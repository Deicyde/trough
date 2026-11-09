---
declaration: theorem
origin: cited
lean: Erdos383.erdos_383
statement: formalized
---

# Erdős Problem 383

> *Reference:* [erdosproblems.com/383](https://www.erdosproblems.com/383)

*Quoted from [FormalConjectures/ErdosProblems/383.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/383.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/383](https://www.erdosproblems.com/383).

The file states 1 research or textbook statement: 1 open.

## `Erdos383.erdos_383`

Open: stated without proof.

> Is it true that for every $k$ there are infinitely many primes $p$ such that the largest prime
> divisor of
> $$
>   \prod_{i = 0}^k (p ^ 2 + i)
> $$
> is $p$?

```lean
theorem erdos_383 :
    ∀ k, {p : ℕ | p.Prime ∧ Nat.maxPrimeFac (∏ i ∈ Finset.Icc 0 k, (p ^ 2 + i)) = p}.Infinite
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/383.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/383.lean#L39).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/383.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/383.lean)
- [erdosproblems.com/383](https://www.erdosproblems.com/383)
