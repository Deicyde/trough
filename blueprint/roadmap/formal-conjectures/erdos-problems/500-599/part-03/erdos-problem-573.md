---
declaration: theorem
origin: cited
lean: Erdos573.erdos_573, Erdos573.erdos_573.variants.c4_c5, Erdos573.erdos_573.variants.kst
statement: formalized
---

# Erdős Problem 573

> *References:*
> - [erdosproblems.com/573](https://www.erdosproblems.com/573)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Er75] Erdős, P., *Some recent progress on extremal problems in graph theory*. Congr. Numer.
>   (1975), 3-14.
> - [ErSi82] Erdős, P. and Simonovits, M., *Compactness results in extremal graph theory*.
>   Combinatorica (1982), 275-288.
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.
> - [KST54] Kővári, T. and Sós, V. T. and Turán, P., *On a problem of K. Zarankiewicz*.
>   Colloq. Math. (1954), 50-57.

*Quoted from [FormalConjectures/ErdosProblems/573.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/573.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/573](https://www.erdosproblems.com/573).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos573.erdos_573`

Open: stated without proof.

> Is it true that
>
> $$\mathrm{ex}(n;\{C_3,C_4\})\sim (n/2)^{3/2}?$$
>
> A problem of Erdős and Simonovits. This problem is asking whether the threshold is the same as
> for forbidding $C_4$ and all odd cycles (see `erdos_573.variants.kst`) if one only forbids the odd
> cycle of length $3$. See also [574] for the general case, and [765] for $\mathrm{ex}(n;C_4)$.
>
> This problem is #48 in Extremal Graph Theory in the graphs problem collection.

```lean
theorem erdos_573 :
    (fun n : ℕ ↦ (cycleExtremalNumber {3, 4} n : ℝ)) ~[atTop]
      fun n : ℕ ↦ ((n : ℝ) / 2) ^ (3 / 2 : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/573.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/573.lean#L65).

## `Erdos573.erdos_573.variants.c4_c5`

Solved: stated here without proof.

> Erdős and Simonovits [ErSi82] proved that
>
> $$\mathrm{ex}(n;\{C_4,C_5\})=(n/2)^{3/2}+O(n).$$
>
> The source writes an equality; only the upper bound is stated here.

```lean
theorem erdos_573.variants.c4_c5 :
    ∃ C : ℝ, ∀ᶠ n : ℕ in atTop,
      (cycleExtremalNumber {4, 5} n : ℝ) ≤ ((n : ℝ) / 2) ^ (3 / 2 : ℝ) + C * n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/573.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/573.lean#L77).

## `Erdos573.erdos_573.variants.kst`

Solved: stated here without proof.

> Kővári, Sós, and Turán [KST54] proved that the extremal number of edges for containing either
> $C_4$ or an odd cycle of any length is $\sim (n/2)^{3/2}$, that is,
>
> $$\mathrm{ex}(n;\{C_4, C_3, C_5, C_7, \ldots\})\sim (n/2)^{3/2}.$$
>
> Equivalently, the maximum number of edges of a bipartite $C_4$-free graph on $n$ vertices is
> $\sim (n/2)^{3/2}$. The attribution follows erdosproblems.com; the matching lower bound comes from
> finite-geometry constructions.

```lean
theorem erdos_573.variants.kst :
    (fun n : ℕ ↦ (cycleExtremalNumber ({4} ∪ {k | Odd k ∧ 3 ≤ k}) n : ℝ)) ~[atTop]
      fun n : ℕ ↦ ((n : ℝ) / 2) ^ (3 / 2 : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/573.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/573.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/573.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/573.lean)
- [erdosproblems.com/573](https://www.erdosproblems.com/573)
