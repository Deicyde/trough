---
declaration: theorem
origin: cited
lean: Erdos1037.erdos_1037, Erdos1037.erdos_1037.variants.cambie_chan_hunter
statement: formalized
---

# Erdős Problem 1037

> *References:*
> - [erdosproblems.com/1037](https://www.erdosproblems.com/1037)
> - [Er93] Erdős, Paul, *Some of my favorite solved and unsolved problems in graph theory*.
>   Quaestiones Math. (1993), 333-350.

*Quoted from [FormalConjectures/ErdosProblems/1037.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1037.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1037](https://www.erdosproblems.com/1037).

The file states 2 research or textbook statements: 2 solved.

## `Erdos1037.erdos_1037`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1037.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1037.lean).

> Let $G$ be a graph on $n$ vertices in which every degree occurs at most twice, and the number of
> distinct degrees is $>(\frac{1}{2}+\epsilon)n$. Must $G$ contain a trivial (empty or complete)
> subgraph of size 'much larger' than $\log n$?
>
> A question of Chen and Erdős.
>
> The answer is no - Cambie, Chan, and Hunter have in the comment section given a simple
> construction of a graph on $n$ vertices with at least $\frac{3}{4}n$ distinct degrees, every
> degree appears at most twice, and the largest trivial subgraph has size $O(\log n)$.

```lean
theorem erdos_1037 :
    ¬ ∀ ε : ℝ, 0 < ε → ∀ C : ℝ, ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n),
      (∀ d : ℕ, {v : Fin n | (G.neighborSet v).ncard = d}.ncard ≤ 2) →
      ((1 / 2 + ε) * (n : ℝ) <
        ((Set.range fun v : Fin n => (G.neighborSet v).ncard).ncard : ℝ)) →
      ∃ s : Set (Fin n), G.IsHomogeneous s ∧ (C * Real.log (n : ℝ) < (s.ncard : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1037.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1037.lean#L48).

## `Erdos1037.erdos_1037.variants.cambie_chan_hunter`

Solved: stated here without proof.

> Cambie, Chan, and Hunter have in the comment section given a simple construction of a graph on
> $n$ vertices with at least $\frac{3}{4}n$ distinct degrees, every degree appears at most twice,
> and the largest trivial subgraph has size $O(\log n)$.

```lean
theorem erdos_1037.variants.cambie_chan_hunter :
    ∃ C : ℝ, ∀ᶠ n : ℕ in atTop, ∃ G : SimpleGraph (Fin n),
      (∀ d : ℕ, {v : Fin n | (G.neighborSet v).ncard = d}.ncard ≤ 2) ∧
      (3 / 4 * (n : ℝ) ≤
        ((Set.range fun v : Fin n => (G.neighborSet v).ncard).ncard : ℝ)) ∧
      ∀ s : Set (Fin n), G.IsHomogeneous s → ((s.ncard : ℝ) ≤ C * Real.log (n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1037.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1037.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1037.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1037.lean)
- [erdosproblems.com/1037](https://www.erdosproblems.com/1037)
