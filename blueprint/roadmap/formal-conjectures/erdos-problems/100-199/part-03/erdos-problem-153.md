---
declaration: theorem
origin: cited
lean: Erdos153.erdos_153
statement: formalized
---

# Erdős Problem 153

> #TODO: Formalize the corresponding conjecture for infinite Sidon sets.
>
> *References:*
>  - [erdosproblems.com/153](https://www.erdosproblems.com/153)
>  - [ESS94] Erdős, P. and Sárközy, A. and Sós, T., On Sum Sets of Sidon Sets, I. Journal of Number
>     Theory (1994), 329-347.

*Quoted from [FormalConjectures/ErdosProblems/153.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/153.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/153](https://www.erdosproblems.com/153).

The file states 1 research or textbook statement: 1 open.

## `Erdos153.erdos_153`

Open: stated without proof.

> Let $A$ be a finite Sidon set and $A+A=\{s_1\lt \cdots\lt s_t\}$. Is it true that
>
> $$\frac{1}{t}\sum_{1\leq i\lt t}(s_{i+1}-s_i)^2 \to \infty$$
>
> as $\lvert A\rvert\to \infty$?

```lean
theorem erdos_153 : Tendsto f atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/153.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/153.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/153.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/153.lean)
- [erdosproblems.com/153](https://www.erdosproblems.com/153)
