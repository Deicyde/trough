---
declaration: lemma
origin: cited
lean: Erdos170.erdos170, Erdos170.erdos170.existing_bounds
statement: formalized
---

# Erdős Problem 170

> *Reference:* [erdosproblems.com/170](https://www.erdosproblems.com/170)

*Quoted from [FormalConjectures/ErdosProblems/170.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/170.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/170](https://www.erdosproblems.com/170).

The file states 2 research or textbook statements: 1 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos170.erdos170`

Open: stated without proof.

> The problem is to determine the limit of the sequence $\frac{F(N)}{\sqrt{N}}$ as $N \to \infty$.

```lean
lemma erdos170 : Filter.Tendsto (fun N => F N / √N) Filter.atTop (𝓝 erdos170.answer)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/170.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/170.lean#L63).

## `Erdos170.erdos170.existing_bounds`

Solved: stated here without proof.

> The existence of the limit has been proved by Erdős and Gál [ErGa48].
> The lower bound has been proven by Leech [Le56], who refined an argument of Rédei and Rényi.
> The upper bound is due to Wichmann [Wi63].

```lean
lemma erdos170.existing_bounds :
  ∃ x ∈ Set.Icc lower_bound upper_bound,
    Filter.Tendsto (fun N => F N / √N) Filter.atTop (𝓝 x)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/170.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/170.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/170.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/170.lean)
- [erdosproblems.com/170](https://www.erdosproblems.com/170)
