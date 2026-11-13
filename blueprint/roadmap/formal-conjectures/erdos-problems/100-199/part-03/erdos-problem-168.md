---
declaration: theorem
origin: cited
lean: Erdos168.erdos_168.parts.i, Erdos168.erdos_168.parts.ii, Erdos168.erdos_168.variants.limit_exists
statement: formalized
---

# Erdős Problem 168

> *Reference:* [erdosproblems.com/168](https://www.erdosproblems.com/168)

*Quoted from [FormalConjectures/ErdosProblems/168.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/168.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/168](https://www.erdosproblems.com/168).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 6 API statements, counted here but not shown.

## `Erdos168.erdos_168.parts.i`

Open: stated without proof.

> What is the limit $F(N)/N$ as $N \to \infty$?

```lean
theorem erdos_168.parts.i :
    Filter.Tendsto (fun N => (F N / N : ℝ)) Filter.atTop (𝓝 erdos_168.parts.i.answer)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/168.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/168.lean#L94).

## `Erdos168.erdos_168.parts.ii`

Open: stated without proof.

> Is the limit $F(N)/N$ as $N \to \infty$ irrational?

```lean
theorem erdos_168.parts.ii :
    Irrational (Filter.atTop.limsup (fun N => (F N / N : ℝ)))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/168.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/168.lean#L100).

## `Erdos168.erdos_168.variants.limit_exists`

Solved: stated here without proof.

> The limit $F(N)/N$ as $N \to \infty$ exists. (proved by Graham, Spencer, and Witsenhausen)

```lean
theorem erdos_168.variants.limit_exists :
    ∃ x, Filter.Tendsto (fun N => (F N / N : ℝ)) Filter.atTop (𝓝 x)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/168.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/168.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/168.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/168.lean)
- [erdosproblems.com/168](https://www.erdosproblems.com/168)
