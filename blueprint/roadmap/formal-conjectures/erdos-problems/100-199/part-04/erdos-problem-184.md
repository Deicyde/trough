---
declaration: theorem
origin: cited
lean: Erdos184.erdos_184, Erdos184.erdos_184.variants.n_log_n, Erdos184.erdos_184.variants.lower_bound, Erdos184.erdos_184.variants.covering, Erdos184.erdos_184.variants.bucic_montgomery, Erdos184.erdos_184.variants.conlon_fox_sudakov
statement: formalized
---

# Erdős Problem 184

> *References:*
> - [erdosproblems.com/184](https://www.erdosproblems.com/184)
> - [BM22] Bucić, M. and Montgomery, R., Towards the Erdős-Gallai Cycle Decomposition Conjecture.
>   arXiv:2211.07689 (2022).
> - [CFS14] Conlon, David and Fox, Jacob and Sudakov, Benny, Cycle packing. Random Structures
>   Algorithms (2014), 608-626.
> - [EGP66] Erdős, Paul and Goodman, A. W. and Pósa, Lajos, The representation of a graph by set
>   intersections. Canadian J. Math. (1966), 106-112.
> - [Er71] Erdős, P., Some unsolved problems in graph theory and combinatorial analysis. Combinatorial
>   Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [OAI26a] OpenAI, *A linear cycle-and-edge decomposition of every graph*. OpenAI Math Release
>   preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-linear-cycle-and-edge-decomposition-of-every-graph-September-24-2026/main.pdf
> - [Py85] Pyber, L., An Erdős-Gallai conjecture. Combinatorica (1985), 67-79.

*Quoted from [FormalConjectures/ErdosProblems/184.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/184](https://www.erdosproblems.com/184).

The file states 6 research or textbook statements: 6 solved.

## `Erdos184.erdos_184`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/CycleDecomposition/Main.lean#L207](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Combinatorics/CycleDecomposition/Main.lean#L207).

> Any graph on $n$ vertices can be decomposed into $O(n)$ many edge-disjoint cycles and edges.
>
> This was proved by an internal OpenAI model in September 2026 [OAI26a]; see the linked Lean
> proof.

```lean
theorem erdos_184 :
    ∃ f : ℕ → ℝ,
      (f =O[atTop] fun n : ℕ ↦ (n : ℝ)) ∧
      ∀ {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      ∃ (D : Finset G.Subgraph),
        (∀ H ∈ D, IsCycleOrEdge H.coe) ∧
        IsDecomposition G D ∧
        (D.card : ℝ) ≤ f (Fintype.card V)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L62).

## `Erdos184.erdos_184.variants.n_log_n`

Solved: stated here without proof.

> Erdős and Gallai [EGP66] proved that $O(n \log n)$ many cycles and edges suffices.

```lean
theorem erdos_184.variants.n_log_n :
    ∃ f : ℕ → ℝ,
      (f =O[atTop] fun n : ℕ ↦ (n : ℝ) * Real.log (n : ℝ)) ∧
      ∀ {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      ∃ (D : Finset G.Subgraph),
        (∀ H ∈ D, IsCycleOrEdge H.coe) ∧
        IsDecomposition G D ∧
        (D.card : ℝ) ≤ f (Fintype.card V)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L77).

## `Erdos184.erdos_184.variants.lower_bound`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_Erdos184_erdos_184_variants_lower_bound.lean#L285](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/394ec1c1ff92bdf2fa10f30d62ae9d0455d3ce20/Proofs/T_Erdos184_erdos_184_variants_lower_bound.lean#L285).

> The graph $K_{3,n-3}$ shows that at least $(1+c)n$ many cycles and edges are required, for some
> constant $c>0$.

```lean
theorem erdos_184.variants.lower_bound :
    ∃ c > 0, ∀ᶠ n in atTop,
      let G : SimpleGraph (Fin n) := fromRel (fun (i j : Fin n) => (i : ℕ) < 3 ∧ 3 ≤ (j : ℕ));
      ∀ (D : Finset G.Subgraph),
        (∀ H ∈ D, IsCycleOrEdge H.coe) →
        IsDecomposition G D →
        (1 + c) * (n : ℝ) ≤ (D.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L94).

## `Erdos184.erdos_184.variants.covering`

Solved: stated here without proof.

> In [Er71] Erdős suggests that only $n-1$ many cycles and edges are required if we do not
> require them to be edge-disjoint. Pyber [Py85] proved this.

```lean
theorem erdos_184.variants.covering :
    ∀ {V : Type} [Fintype V] [DecidableEq V] [Nonempty V] (G : SimpleGraph V),
    ∃ (D : Finset G.Subgraph),
      (∀ H ∈ D, IsCycleOrEdge H.coe) ∧
      (⋃ H ∈ D, H.edgeSet) = G.edgeSet ∧
      (D.card : ℝ) ≤ (Fintype.card V : ℝ) - 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L109).

## `Erdos184.erdos_184.variants.bucic_montgomery`

Solved: stated here without proof.

> Before [OAI26a], the best bound was due to Bucić and Montgomery [BM22], who prove that
> $O(n\log^* n)$ many cycles and edges suffice, where $\log^*$ is the iterated logarithm function.

```lean
theorem erdos_184.variants.bucic_montgomery :
    ∃ f : ℕ → ℝ,
      (f =O[atTop] fun n : ℕ ↦ (n : ℝ) * (Real.iteratedLog (n : ℝ) : ℝ)) ∧
      ∀ {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      ∃ (D : Finset G.Subgraph),
        (∀ H ∈ D, IsCycleOrEdge H.coe) ∧
        IsDecomposition G D ∧
        (D.card : ℝ) ≤ f (Fintype.card V)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L123).

## `Erdos184.erdos_184.variants.conlon_fox_sudakov`

Solved: stated here without proof.

> Conlon, Fox, and Sudakov [CFS14] proved that $O_\epsilon(n)$ cycles and edges suffice if $G$ has
> minimum degree at least $\epsilon n$, for any $\epsilon>0$.

```lean
theorem erdos_184.variants.conlon_fox_sudakov :
    ∀ ε > 0, ∃ f : ℕ → ℝ,
      (f =O[atTop] fun n : ℕ ↦ (n : ℝ)) ∧
      ∀ {V : Type*} [Fintype V] [DecidableEq V] (G : SimpleGraph V),
      (G.minDegree : ℝ) ≥ ε * (Fintype.card V : ℝ) →
      ∃ (D : Finset G.Subgraph),
        (∀ H ∈ D, IsCycleOrEdge H.coe) ∧
        IsDecomposition G D ∧
        (D.card : ℝ) ≤ f (Fintype.card V)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/184.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean#L139).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/184.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/184.lean)
- [erdosproblems.com/184](https://www.erdosproblems.com/184)
