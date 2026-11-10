---
declaration: theorem
origin: cited
lean: Erdos857.erdos_857
statement: formalized
---

# Erdős Problem 857

> *Reference:* [erdosproblems.com/857](https://www.erdosproblems.com/857)
>
> For fixed `n, k`, let `m(n, k)` be minimal such that every family of subsets of `[n]`
> of size at least `m(n, k)` contains a `k`-sunflower.
> The problem asks to estimate `m(n, k)`, ideally asymptotically.

*Quoted from [FormalConjectures/ErdosProblems/857.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/857.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/857](https://www.erdosproblems.com/857).

The file states 1 research or textbook statement: 1 open.

## `Erdos857.erdos_857`

Open: stated without proof.

> Estimate `m(n,k)`, or better give an asymptotic formula.

```lean
theorem erdos_857 :
    ∀ k : ℕ, 3 ≤ k → Tendsto (fun n : ℕ => (m n k : ℝ) / erdos_857.answer k n) atTop (nhds 1)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/857.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/857.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/857.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/857.lean)
- [erdosproblems.com/857](https://www.erdosproblems.com/857)
