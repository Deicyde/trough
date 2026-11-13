---
declaration: theorem
origin: cited
lean: Erdos507.erdos_507.equivalent, Erdos507.erdos_507.lower, Erdos507.erdos_507.upper, Erdos507.erdos_507.variants.upper_trivial, Erdos507.erdos_507.variants.lower_erdos, Erdos507.erdos_507.variants.lower_kps82, Erdos507.erdos_507.variants.upper_cpz24
statement: formalized
---

# Erdős Problem 507

> *References:*
> - [erdosproblems.com/507](https://www.erdosproblems.com/507)
> - [CPZ23] Cohen, Alex, Cosmin Pohoata, and Dmitrii Zakharov. "A new upper bound for the Heilbronn
>   triangle problem." arXiv preprint arXiv:2305.18253 (2023).
> - [CPZ24] Cohen, Alex, Cosmin Pohoata, and Dmitrii Zakharov. "Lower bounds for incidences."
>   Inventiones mathematicae (2025): 1-74.
> - [KPS82] Komlós, János, János Pintz, and Endre Szemerédi. "A lower bound for Heilbronn's problem."
>   Journal of the London Mathematical Society 2.1 (1982): 13-24.
> - [KPS81] Komlós, János, János Pintz, and Endre Szemerédi. "On Heilbronn's triangle problem."
>   Journal of the London Mathematical Society 2.3 (1981): 385-396.

*Quoted from [FormalConjectures/ErdosProblems/507.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/507](https://www.erdosproblems.com/507).

The file states 7 research or textbook statements: 3 open and 4 solved.

## `Erdos507.erdos_507.equivalent`

Open: stated without proof.

> Let $\alpha(n)$ be such that every set of $n$ points in the unit disk contains three points which
> determine a triangle of area at most $\alpha(n)$. Estimate $\alpha(n)$.

```lean
theorem erdos_507.equivalent:
    α ~[atTop] erdos_507.equivalent.answer
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L75).

## `Erdos507.erdos_507.lower`

Open: stated without proof.

> Estimate a lower bound for$\alpha(n)$.

```lean
theorem erdos_507.lower:
    (lowerBest =o[atTop] erdos_507.lower.answer) ∧ (erdos_507.lower.answer ≪ α)
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L85).

## `Erdos507.erdos_507.upper`

Open: stated without proof.

> Estimate an upper bound for$\alpha(n)$.

```lean
theorem erdos_507.upper:
    (α ≪ erdos_507.upper.answer) ∧ (erdos_507.upper.answer =o[atTop] upperBarrier)
```

Category `research open`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L95).

## `Erdos507.erdos_507.variants.upper_trivial`

Solved: stated here without proof.

> It is trivial that $\alpha(n) \ll 1/n$.

```lean
theorem erdos_507.variants.upper_trivial : α ≪ (fun n ↦ 1 / (n : ℝ))
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L103).

## `Erdos507.erdos_507.variants.lower_erdos`

Solved: stated here without proof.

> Erdős observed that $\alpha(n) \gg 1/n^2$.

```lean
theorem erdos_507.variants.lower_erdos : α ≫ (fun n ↦ 1 / (n : ℝ) ^ 2)
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L110).

## `Erdos507.erdos_507.variants.lower_kps82`

Solved: stated here without proof.

> Current best lower bound [KPS82].

```lean
theorem erdos_507.variants.lower_kps82 : lowerBest ≪ α
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L117).

## `Erdos507.erdos_507.variants.upper_cpz24`

Solved: stated here without proof.

> Current best upper bound [CPZ24]: $\alpha(n) \ll n^{-7/6 + o(1)}$.

```lean
theorem erdos_507.variants.upper_cpz24 :
    ∃ (o : ℕ → ℝ), Tendsto o atTop (𝓝 0) ∧
    α ≪ (fun n ↦ upperBarrier n * (n : ℝ) ^ o n)
```

Category `research solved`; AMS [51 Geometry](../../../by-subject/part-02/51-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/507.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean#L124).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/507.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/507.lean)
- [erdosproblems.com/507](https://www.erdosproblems.com/507)
