---
declaration: theorem
origin: cited
lean: Erdos143.erdos_143.parts.i, Erdos143.erdos_143.parts.ii
statement: formalized
---

# Erdős Problem 143

> *Reference:* [erdosproblems.com/143](https://www.erdosproblems.com/143)

*Quoted from [FormalConjectures/ErdosProblems/143.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/143.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/143](https://www.erdosproblems.com/143).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos143.erdos_143.parts.i`

Solved: stated here without proof.

> Does this imply that
>
> $$
> \liminf \frac{|A \cap [1,x]|}{x} = 0?
> $$
>
> The answer is yes: Koukoulopoulos, Lamzouri and Lichtman proved that every such $A$ satisfies
> $\sum_{x \in A,\, x < n} \frac{1}{x} = o(\log n)$
> ([arXiv:2502.09539](https://arxiv.org/abs/2502.09539), Theorem 1), and this implies
> $\liminf \frac{|A \cap [1,x]|}{x} = 0$ by partial summation.

```lean
theorem erdos_143.parts.i : ∀ (A : Set ℝ), WellSeparatedSet A →
    liminf (fun x => (A ∩ (Set.Icc 1 x)).ncard / x) atTop = 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/143.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/143.lean#L53).

## `Erdos143.erdos_143.parts.ii`

Open: stated without proof.

> Or
>
> $$
> \sum_{x \in A} \frac{1}{x \log x} < \infty,
> $$

```lean
theorem erdos_143.parts.ii (A : Set ℝ) (h : WellSeparatedSet A) :
    Summable fun (x : A) ↦ 1 / (x * Real.log x)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/143.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/143.lean#L64).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/143.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/143.lean)
- [erdosproblems.com/143](https://www.erdosproblems.com/143)
