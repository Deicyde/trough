---
declaration: theorem
origin: cited
lean: Erdos1177.erdos_1177.parts.i, Erdos1177.erdos_1177.parts.ii, Erdos1177.erdos_1177.parts.iii
statement: formalized
---

# Erdős Problem 1177

> *References:*
> - [erdosproblems.com/1177](https://www.erdosproblems.com/1177)
> - [Li26] Li, E., *A Resolution of Erdős Problems 593 and 1177: Obligatory Triple Systems
>   and Exact Spectra*. [arXiv:2606.24882v2](https://arxiv.org/abs/2606.24882v2) (2026),
>   Corollary 1.4.

*Quoted from [FormalConjectures/ErdosProblems/1177.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1177.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1177](https://www.erdosproblems.com/1177).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1177.erdos_1177.parts.i`

Solved: stated here without proof.

> Let $G$ be a finite $3$-uniform hypergraph, and let $F_G(\kappa)$ denote the collection of
> $3$-uniform hypergraphs with chromatic number $\kappa$ not containing $G$. If
> $F_G(\aleph_1)$ is non-empty, then it contains a hypergraph on at most
> $2^{2^{\aleph_0}}$ vertices. Li [Li26, Corollary 1.4(1)] proved this.

```lean
theorem erdos_1177.parts.i :
    ∀ (W : Type) [Fintype W] (G : UniformHypergraph W 3),
    G.HasAvoidingChromaticCardinal ℵ₁ →
      ∃ (V : Type) (_ : DecidableEq V) (X : UniformHypergraph V 3),
        X.chromaticCardinal = ℵ₁ ∧ ¬ G.Appears X ∧
          Cardinal.mk V ≤ (2 : Cardinal) ^ ((2 : Cardinal) ^ ℵ₀)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1177.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1177.lean#L43).

## `Erdos1177.erdos_1177.parts.ii`

Solved: stated here without proof.

> The assertion that two non-empty avoidance families $F_G(\aleph_1)$ and $F_H(\aleph_1)$
> always have non-empty intersection is false. Li [Li26, Corollary 1.4(2)] gives a
> counterexample using two triples sharing a pair and the loose seven-cycle.

```lean
theorem erdos_1177.parts.ii :
    ¬ ∀ (W U : Type) [Fintype W] [Fintype U]
    (G : UniformHypergraph W 3) (H : UniformHypergraph U 3),
    G.HasAvoidingChromaticCardinal ℵ₁ → H.HasAvoidingChromaticCardinal ℵ₁ →
      ∃ (V : Type) (_ : DecidableEq V) (X : UniformHypergraph V 3),
        X.chromaticCardinal = ℵ₁ ∧ ¬ G.Appears X ∧ ¬ H.Appears X
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1177.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1177.lean#L57).

## `Erdos1177.erdos_1177.parts.iii`

Solved: stated here without proof.

> If $\kappa,\lambda$ are uncountable cardinals and $F_G(\kappa)$ is non-empty then
> $F_G(\lambda)$ is non-empty. Li [Li26, Corollary 1.4(3)] proved this.

```lean
theorem erdos_1177.parts.iii :
    ∀ (W : Type) [Fintype W] (G : UniformHypergraph W 3)
    (κ μ : Cardinal), ℵ₀ < κ → ℵ₀ < μ →
      G.HasAvoidingChromaticCardinal κ → G.HasAvoidingChromaticCardinal μ
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1177.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1177.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1177.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1177.lean)
- [erdosproblems.com/1177](https://www.erdosproblems.com/1177)
