---
declaration: theorem
origin: cited
lean: Erdos812.erdos_812.parts.i, Erdos812.erdos_812.parts.ii, Erdos812.erdos_812.variants.lower_bound
statement: formalized
---

# Erdős Problem 812

> *References:*
> - [erdosproblems.com/812](https://www.erdosproblems.com/812)
> - [BEFS89] Burr, S. A. and Erd\H{o}s, P. and Faudree, R. J. and Schelp, R. H., On the difference
>   between consecutive {R}amsey numbers. Utilitas Math. (1989), 115--118.

*Quoted from [FormalConjectures/ErdosProblems/812.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/812.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/812](https://www.erdosproblems.com/812).

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Erdos812.erdos_812.parts.i`

Open: stated without proof.

> Is it true that $\frac{R(n+1)}{R(n)}\geq 1+c$ for some constant $c>0$, for all large $n$?

```lean
theorem erdos_812.parts.i :
    ∃ c > 0, ∀ᶠ n in atTop, (R (n + 1) : ℝ) / (R n : ℝ) ≥ 1 + c
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/812.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/812.lean#L43).

## `Erdos812.erdos_812.parts.ii`

Open: stated without proof.

> Is it true that $R(n+1)-R(n) \gg n^2$?

```lean
theorem erdos_812.parts.ii :
    (fun n : ℕ ↦ (R (n + 1) : ℝ) - (R n : ℝ)) ≫ (fun n : ℕ ↦ (n : ℝ) ^ 2)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/812.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/812.lean#L51).

## `Erdos812.erdos_812.variants.lower_bound`

Solved: stated here without proof.

> Burr, Erdős, Faudree, and Schelp [BEFS89] proved that $R(n+1)-R(n) \geq 4n-8$ for all $n\geq 2$.

```lean
theorem erdos_812.variants.lower_bound :
    ∀ n : ℕ, n ≥ 2 → (R (n + 1) : ℤ) - (R n : ℤ) ≥ 4 * (n : ℤ) - 8
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/812.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/812.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/812.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/812.lean)
- [erdosproblems.com/812](https://www.erdosproblems.com/812)
