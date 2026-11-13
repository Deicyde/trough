---
declaration: theorem
origin: cited
lean: Erdos609.erdos_609
statement: formalized
---

# Erdős Problem 609

> *References:*
> - [erdosproblems.com/609](https://www.erdosproblems.com/609)
> - [ErGr75] Erdős, P. and Graham, R. L., On partition theorems for finite graphs.
>   Colloq. Math. Soc. János Bolyai (1975).
> - [Ch97] Chung, F., Open problems of Paul Erdős in graph theory. J. Graph Theory (1997), 3-36.
> - [DaJo17] Day, A. N. and Johnson, J. R., Multicolour Ramsey numbers of odd cycles.
>   J. Combin. Theory Ser. B (2017), 56-63.
> - [GiHu24] Girão, A. and Hunter, Z., Monochromatic odd cycles in edge-coloured complete graphs.
>   arXiv:2412.07708 (2024).
> - [JaYi25] Janzer, O. and Yip, F., Short monochromatic odd cycles.
>   arXiv:2506.14910 (2025).

*Quoted from [FormalConjectures/ErdosProblems/609.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/609.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/609](https://www.erdosproblems.com/609).

The file states 1 research or textbook statement: 1 open.

## `Erdos609.erdos_609`

Open: stated without proof.

> Let $f(n)$ be the minimal $m$ such that if the edges of $K_{2^n+1}$ are coloured with $n$ colours
> then there must be a monochromatic odd cycle of length at most $m$. Estimate $f(n)$.

```lean
theorem erdos_609 :
    (fun n ↦ (f n : ℝ)) =Θ[atTop] erdos_609.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/609.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/609.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/609.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/609.lean)
- [erdosproblems.com/609](https://www.erdosproblems.com/609)
