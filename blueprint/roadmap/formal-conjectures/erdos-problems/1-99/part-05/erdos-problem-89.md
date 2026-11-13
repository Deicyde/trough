---
declaration: theorem
origin: cited
lean: Erdos89.erdos_89, Erdos89.erdos_89.variants.n_dvd_log_n, Erdos89.erdos_89.variants.grid_upper_bound
statement: formalized
---

# Erdős Problem 89

> *References:*
> - [erdosproblems.com/89](https://www.erdosproblems.com/89)
> - [Er46] Erdős, Paul. On sets of distances of $n$ points. Amer. Math. Monthly
>   53 (1946), 248--250.
> - [GuKa15] Guth, Larry and Katz, Nets Hawk. On the Erdős distinct distances
>   problem in the plane. Ann. of Math. (2) 181 (2015), 155--190.
> - [Mo52] Moser, Leo. On the different distances determined by $n$ points.
>   Amer. Math. Monthly 59 (1952), 85--91.
>
> ### AI disclosure
>
> Lean 4 code in this file was drafted with assistance from OpenAI Codex.
> The mathematical content and references are the author's own work.

*Quoted from [FormalConjectures/ErdosProblems/89.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/89.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/89](https://www.erdosproblems.com/89).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos89.erdos_89`

Open: stated without proof.

> Erdős [Er46] asked whether every set of $n$ distinct points in $\mathbb{R}^2$
> determines $\gg \frac{n}{\sqrt{\log n}}$ many distinct distances.

```lean
theorem erdos_89 :
    (fun (n : ℕ) => n/(n : ℝ).log.sqrt) =O[atTop]
      (fun n => (minimalDistinctDistances ℝ² n : ℝ))
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/89.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/89.lean#L50).

## `Erdos89.erdos_89.variants.n_dvd_log_n`

Solved: stated here without proof.

> Guth and Katz [GuKa15] proved that there are always $\gg \frac{n}{\log n}$
> many distinct distances.

```lean
theorem erdos_89.variants.n_dvd_log_n :
    (fun (n : ℕ) => n/(n : ℝ).log) =O[atTop]
      (fun n => (minimalDistinctDistances ℝ² n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/89.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/89.lean#L60).

## `Erdos89.erdos_89.variants.grid_upper_bound`

Solved: stated here without proof.

> The square grid construction, going back to Erdős and Moser, shows that
> $\frac{n}{\sqrt{\log n}}$ is the correct order if the conjecture is true:
> there are configurations whose number of distinct distances is
> $O(\frac{n}{\sqrt{\log n}})$.

```lean
theorem erdos_89.variants.grid_upper_bound :
    (fun n => (minimalDistinctDistances ℝ² n : ℝ)) =O[atTop]
      (fun (n : ℕ) => n/(n : ℝ).log.sqrt)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/89.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/89.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/89.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/89.lean)
- [erdosproblems.com/89](https://www.erdosproblems.com/89)
