---
declaration: theorem
origin: cited
lean: Erdos1092.f_asymptotic_2, Erdos1092.f_asymptotic_general
statement: formalized
---

# Erdős Problem 1092

> *References:*
> - [Erdős Problem 1092](https://www.erdosproblems.com/1092)
> - [Ro82] V. Rödl, *Nearly bipartite graphs with large chromatic number*, Combinatorica **2** (1982),
>   377–383.

*Quoted from [FormalConjectures/ErdosProblems/1092.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1092.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1092](https://www.erdosproblems.com/1092).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1092.f_asymptotic_2`

Solved: stated here without proof.

> Is it true that $f_2(n) \gg n$? Disproved by Rödl, who showed $f_r(n) = o(n)$ for all fixed
> $r \geq 2$. A conjecture of Erdős, Hajnal, and Szemerédi.
>
> This seems to be closely related to, but distinct from, [744](https://www.erdosproblems.com/744).
>
> Tang notes in the comments that Rödl [Ro82] constructed, for any $\epsilon>0$ and $k$, a graph
> with chromatic number $\geq k$ such that every graph on $m$ vertices is bipartite after deleting at
> most $\epsilon m$ edges.

```lean
theorem f_asymptotic_2 :
    ¬ ∃ g : ℕ → ℕ, IsAdmissible 2 g ∧
      (fun n : ℕ => (n : ℝ)) =O[atTop] (fun n : ℕ => (g n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1092.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1092.lean#L68).

## `Erdos1092.f_asymptotic_general`

Solved: stated here without proof.

> More generally, is $f_r(n)\gg_r n$ for every $r \geq 2$? Disproved by Rödl, who showed
> $f_r(n) = o(n)$ for all fixed $r \geq 2$.

```lean
theorem f_asymptotic_general :
    ¬ ∀ r : ℕ, 2 ≤ r → ∃ g : ℕ → ℕ, IsAdmissible r g ∧
      (fun n : ℕ => (n : ℝ)) =O[atTop] (fun n : ℕ => (g n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1092.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1092.lean#L76).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1092.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1092.lean)
- [erdosproblems.com/1092](https://www.erdosproblems.com/1092)
