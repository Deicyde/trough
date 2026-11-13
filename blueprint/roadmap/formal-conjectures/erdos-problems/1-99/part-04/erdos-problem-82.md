---
declaration: theorem
origin: cited
lean: Erdos82.erdos_82, Erdos82.erdos_82.variants.F_upper_bound
statement: formalized
---

# Erdős Problem 82

> *Reference:* [erdosproblems.com/82](https://www.erdosproblems.com/82)

*Quoted from [FormalConjectures/ErdosProblems/82.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/82.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/82](https://www.erdosproblems.com/82).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos82.erdos_82`

Open: stated without proof.

> $F(n) / \log n \to \infty as n \to \infty$

```lean
theorem erdos_82 : Tendsto (fun n => F n / Real.log n) atTop atTop
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/82.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/82.lean#L53).

## `Erdos82.erdos_82.variants.F_upper_bound`

Solved: stated here without proof.

> $F(n) \le O(n^{1/2} \ln ^ {3/4} n)$
>
> Theorem 1.4 from [AKS07]
>
> [AKS07] Alon, N. and Krivelevich, M. and Sudakov, B., Large nearly regular induced subgraphs. arXiv:0710.2106 (2007).

```lean
theorem erdos_82.variants.F_upper_bound :
    (fun n => (F n : ℝ)) =O[atTop] (fun n => Real.sqrt n * (Real.log n) ^ (3 / 4 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/82.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/82.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/82.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/82.lean)
- [erdosproblems.com/82](https://www.erdosproblems.com/82)
