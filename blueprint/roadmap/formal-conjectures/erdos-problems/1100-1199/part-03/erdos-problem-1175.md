---
declaration: theorem
origin: cited
lean: Erdos1175.erdos_1175, Erdos1175.erdos_1175.variants.aleph_one, Erdos1175.erdos_1175.variants.threshold_formulation
statement: formalized
---

# Erdős Problem 1175

> *Reference:* [erdosproblems.com/1175](https://www.erdosproblems.com/1175)
>
> - [KoSh88] Komjáth, Péter and Shelah, Saharon, *Forcing constructions for uncountably chromatic
>   graphs*. J. Symbolic Logic (1988), 696--707.
>
> ## Formalization notes
>
> - **Chromatic cardinal**: `SimpleGraph.chromaticCardinal` is the cardinal-valued chromatic number
>   defined in `FormalConjecturesForMathlib`. It extends the finite `chromaticNumber` (which takes
>   values in `ℕ∞`) to a `Cardinal`, and is therefore able to distinguish between different infinite
>   chromatic numbers.
> - **Triangle-free subgraph**: a subgraph `H : G.Subgraph` is triangle-free when `H.coe.CliqueFree 3`.
>   This is the standard Mathlib formulation: `CliqueFree 3` means the graph has no `K₃` as a clique.
> - **Subgraph**: we use `G.Subgraph` (an arbitrary subgraph record) rather than an induced subgraph
>   since the problem asks for any subgraph, not just induced ones.

*Quoted from [FormalConjectures/ErdosProblems/1175.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1175.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1175](https://www.erdosproblems.com/1175).

The file states 3 research or textbook statements: 3 open. It also has 2 test statements, counted here but not shown.

## `Erdos1175.erdos_1175`

Open: stated without proof.

> Let $\kappa$ be an uncountable cardinal. Must there exist a cardinal $\lambda$ such that every
> graph with chromatic number $\lambda$ contains a triangle-free subgraph with chromatic number
> $\kappa$?
>
> Shelah proved that a negative answer is consistent when
> $\kappa = \lambda = \aleph_1$ (see `erdos_1175.variants.aleph_one`).

```lean
theorem erdos_1175 :
    ∀ (κ : Cardinal), ℵ₀ < κ →
      ∃ (μ : Cardinal),
        ∀ (V : Type*) (G : SimpleGraph V), G.chromaticCardinal = μ →
          ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1175.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1175.lean#L55).

## `Erdos1175.erdos_1175.variants.aleph_one`

Open: stated without proof.

> The case $\kappa = \lambda = \aleph_1$ of Problem 1175: does every graph with chromatic number
> $\aleph_1$ contain a triangle-free subgraph with chromatic number $\aleph_1$?
>
> Shelah proved that a negative answer is consistent with ZFC [KoSh88, Theorem 1]: there is a
> model of ZFC containing a graph with chromatic number $\aleph_1$ all of whose triangle-free
> subgraphs have countable chromatic number. Consistency results about models of ZFC are not
> directly formalizable inside Lean's fixed model, so only the underlying question is recorded
> here. Note that this concerns only the choice $\lambda = \aleph_1$; it does not rule out a
> larger $\lambda$ in `erdos_1175`.

```lean
theorem erdos_1175.variants.aleph_one :
    ∀ (V : Type*) (G : SimpleGraph V), G.chromaticCardinal = ℵ_ 1 →
      ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = ℵ_ 1
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1175.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1175.lean#L74).

## `Erdos1175.erdos_1175.variants.threshold_formulation`

Open: stated without proof.

> **Threshold reformulation variant.** Replaces `chromaticCardinal = λ` in the hypothesis
> of `erdos_1175` with `λ ≤ chromaticCardinal` (a graph of chromatic number ≥ λ has a
> triangle-free subgraph of chromatic number κ). This is a strengthening of `erdos_1175`
> (see `erdos_1175.test.threshold_implies_exact`).

```lean
theorem erdos_1175.variants.threshold_formulation :
    ∀ (κ : Cardinal), ℵ₀ < κ →
      ∃ (μ : Cardinal),
        ∀ (V : Type*) (G : SimpleGraph V), μ ≤ G.chromaticCardinal →
          ∃ (H : G.Subgraph), H.coe.CliqueFree 3 ∧ H.coe.chromaticCardinal = κ
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1175.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1175.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1175.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1175.lean)
- [erdosproblems.com/1175](https://www.erdosproblems.com/1175)
