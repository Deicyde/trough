---
declaration: theorem
origin: cited
lean: Erdos563.erdos_563
statement: formalized
---

# Erdős Problem 563

> *References:*
> - [erdosproblems.com/563](https://www.erdosproblems.com/563)
> - [Er90b] Erdős, Paul, Problems and results on graphs and hypergraphs: similarities and differences.
>   Mathematics of Ramsey theory (1990), 12-28.

*Quoted from [FormalConjectures/ErdosProblems/563.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/563.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/563](https://www.erdosproblems.com/563).

The file states 1 research or textbook statement: 1 open.

## `Erdos563.erdos_563`

Open: stated without proof.

> Let $F(n,\alpha)$ denote the smallest $m$ such that there exists a $2$-colouring of the edges of
> $K_n$ so that every $X\subseteq [n]$ with $\lvert X\rvert\geq m$ contains more than
> $\alpha \binom{\lvert X\rvert}{2}$ many edges of each colour.
>
> Prove that, for every $0\leq \alpha < 1/2$,
>
> $$F(n,\alpha)\sim c_\alpha\log n$$
>
> for some constant $c_\alpha$ depending only on $\alpha$.
>
> This problem is #39 in Ramsey Theory in the graphs problem collection.

```lean
theorem erdos_563 :
    ∀ (α : ℝ), 0 ≤ α → α < 1 / 2 →
      ∃ (c : ℝ), 0 < c ∧
        Tendsto (fun n : ℕ => (F n α : ℝ) / Real.log n) atTop (nhds c)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/563.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/563.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/563.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/563.lean)
- [erdosproblems.com/563](https://www.erdosproblems.com/563)
