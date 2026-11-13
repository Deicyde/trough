---
declaration: theorem
origin: cited
lean: Erdos688.erdos_688.parts.i, Erdos688.erdos_688.parts.ii, Erdos688.erdos_688.variants.lglglg_over_lglg_is_big_o
statement: formalized
---

# Erdős Problem 688

> *Reference:*
> - [erdosproblems.com/688](https://www.erdosproblems.com/688)
> - [Er80] Erdős, Paul, _A survey of problems in combinatorial number theory_. Ann. Discrete Math. (1980), 89-115.

*Quoted from [FormalConjectures/ErdosProblems/688.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/688.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/688](https://www.erdosproblems.com/688).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos688.erdos_688.parts.i`

Open: stated without proof.

> Estimate $\epsilon_n$.

```lean
theorem erdos_688.parts.i :
    epsilonFunction =Θ[atTop] erdos_688.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/688.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/688.lean#L51).

## `Erdos688.erdos_688.parts.ii`

Open: stated without proof.

> In particular, is it true that $\epsilon_n = o(1)$?

```lean
theorem erdos_688.parts.ii :
    epsilonFunction =o[atTop] (fun (n : ℕ) ↦ (1 : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/688.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/688.lean#L59).

## `Erdos688.erdos_688.variants.lglglg_over_lglg_is_big_o`

Solved: stated here without proof.

> Erdős claims in [Er80] (p. 106) that it is not difficult to prove
> $\epsilon_n \gg \frac{\log\log\log n}{\log\log n}$.

```lean
theorem erdos_688.variants.lglglg_over_lglg_is_big_o :
    (fun (n : ℕ) ↦ (log (log (log (n : ℝ)))) / (log (log (n : ℝ))))
      =O[atTop] epsilonFunction
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/688.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/688.lean#L68).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/688.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/688.lean)
- [erdosproblems.com/688](https://www.erdosproblems.com/688)
