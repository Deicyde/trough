---
declaration: theorem
origin: cited
lean: Erdos642.erdos_642, Erdos642.erdos_642.variants.upper_bound_n_pow_three_halves, Erdos642.erdos_642.variants.upper_bound_n_log_pow_eight
statement: formalized
---

# Erdős Problem 642

> *References:*
> - [erdosproblems.com/642](https://www.erdosproblems.com/642)
> - [CES96] Chen, Guantao and Erdős, Paul and Staton, William, *Proof of a conjecture of Bollobás
>   on nested cycles*. J. Combin. Theory Ser. B (1996), 38--43.
> - [DMMS24] Draganić, Nemanja and Methuku, Abhishek and Munhá Correia, David and Sudakov,
>   Benny, *Cycles with many chords*. Random Structures Algorithms (2024), 3--16.
> - [Er97d] Erdős, Paul, *Some recent problems and results in graph theory*. Discrete Math.
>   (1997), 81-85.

*Quoted from [FormalConjectures/ErdosProblems/642.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/642.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/642](https://www.erdosproblems.com/642).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 2 test statements and 4 API statements, counted here but not shown.

## `Erdos642.erdos_642`

Open: stated without proof.

> Let $f(n)$ be the maximal number of edges in a graph on $n$ vertices such that all cycles have more
> vertices than chords. Is it true that $f(n)\ll n$?
>
> A problem of Hamburger and Szegedy. A chord is an edge between two vertices of the cycle which are
> not consecutive in the cycle.

```lean
theorem erdos_642 :
    (fun n : ℕ => (maxEdges n : ℝ)) =O[atTop] (fun n : ℕ => (n : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/642.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/642.lean#L62).

## `Erdos642.erdos_642.variants.upper_bound_n_pow_three_halves`

Solved: stated here without proof.

> Chen, Erdős, and Staton [CES96] proved $f(n) \ll n^{3/2}$.

```lean
theorem erdos_642.variants.upper_bound_n_pow_three_halves :
    (fun n : ℕ => (maxEdges n : ℝ)) =O[atTop] (fun n : ℕ => (n : ℝ) ^ (3 / 2 : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/642.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/642.lean#L68).

## `Erdos642.erdos_642.variants.upper_bound_n_log_pow_eight`

Solved: stated here without proof.

> Draganić, Methuku, Munhá Correia, and Sudakov [DMMS24] have improved this to
>
> $$f(n) \ll n(\log n)^8.$$

```lean
theorem erdos_642.variants.upper_bound_n_log_pow_eight :
    (fun n : ℕ => (maxEdges n : ℝ)) =O[atTop] (fun n : ℕ => (n : ℝ) * Real.log n ^ 8)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/642.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/642.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/642.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/642.lean)
- [erdosproblems.com/642](https://www.erdosproblems.com/642)
