---
declaration: theorem
origin: cited
lean: Erdos155.erdos_155
statement: formalized
---

# Erdős Problem 155

> *Reference:* [erdosproblems.com/155](https://www.erdosproblems.com/155)

*Quoted from [FormalConjectures/ErdosProblems/155.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/155.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/155](https://www.erdosproblems.com/155).

The file states 1 research or textbook statement: 1 open.

## `Erdos155.erdos_155`

Open: stated without proof.

> Is it true that for every $k \geq 1$ we have
>
> $$
> F(N + k) \leq F(N) + 1
> $$
>
> for all sufficiently large $N$?

```lean
theorem erdos_155 : ∀ k ≥ 1, ∀ᶠ N in atTop, F (N + k) ≤ F N + 1
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/155.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/155.lean#L45).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/155.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/155.lean)
- [erdosproblems.com/155](https://www.erdosproblems.com/155)
