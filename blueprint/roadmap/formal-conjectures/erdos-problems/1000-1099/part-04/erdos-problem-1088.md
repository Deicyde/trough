---
declaration: theorem
origin: cited
lean: Erdos1088.erdos_1088
statement: formalized
---

# Erdős Problem 1088

> *Reference:* [erdosproblems.com/1088](https://www.erdosproblems.com/1088)

*Quoted from [FormalConjectures/ErdosProblems/1088.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1088.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1088](https://www.erdosproblems.com/1088).

The file states 1 research or textbook statement: 1 open. It also has 1 API statement, counted here but not shown.

## `Erdos1088.erdos_1088`

Open: stated without proof.

> Let $f_d(n)$ be the minimal $m$ such that any set of $m$ points in $\mathbb{R}^d$ contains a set of
> $n$ points for which any two determined distances are distinct. Erdős Problem 1088 asks to
> estimate $f_d(n)$. In particular, is it true that, for every fixed $n \geq 3$,
>
> $$
> f_d(n) = 2^{o(d)}
> $$
>
> as $d \to \infty$?
>
> The little-$o$ condition is stated after taking the base-$2$ logarithm.

```lean
theorem erdos_1088 :
    ∀ n ≥ 3,
      (fun d : ℕ ↦ Real.logb 2 (f d n : ℝ)) =o[atTop] (fun d : ℕ ↦ (d : ℝ))
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1088.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1088.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1088.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1088.lean)
- [erdosproblems.com/1088](https://www.erdosproblems.com/1088)
