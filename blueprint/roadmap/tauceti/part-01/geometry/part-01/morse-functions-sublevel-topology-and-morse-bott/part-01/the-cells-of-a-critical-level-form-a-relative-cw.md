---
declaration: def
origin: cited
lean: TauCeti.morseRelCWComplex
statement: formalized
---

# The cells of a critical level form a relative CW complex

Let `φ i` be charts of `M` into
`ℝⁿ` with pairwise disjoint sources, each containing the closed ball of radius `√ε` in its target,
in which a continuous `f` has the normal form `c - Σ_{j < k i} yⱼ² + Σ_{j ≥ k i} yⱼ²`. Then the
lower sublevel `{f ≤ c - ε}` with the discs `{‖y‖² ≤ ε, yⱼ = 0 for j ≥ k i}` of the charts
attached is a finite CW complex relative to `{f ≤ c - ε}`, with one `k i`-cell for each `i`
(`TauCeti.morseRelCWComplexCellEquiv`), whose characteristic map is
`OpenPartialHomeomorph.morseCellMap` (`TauCeti.coe_map_morseRelCWComplex`).

```lean
TauCeti.morseRelCWComplex.{u} {M : Type u} [TopologicalSpace M] {n : ℕ} {ι : Type u} [Finite ι]
  {f : M → ℝ} {c ε : ℝ} (hfc : Continuous f)
  (φ : ι → OpenPartialHomeomorph M (EuclideanSpace ℝ (Fin n)))
  (hφ : Pairwise (Function.onFun Disjoint fun i => (φ i).source)) (k : ι → ℕ)
  (hk : ∀ (i : ι), k i ≤ n) (hε : 0 < ε) (hball : ∀ (i : ι), Metric.closedBall 0 √ε ⊆ (φ i).target)
  (hf :
    ∀ (i : ι),
      ∀ y ∈ (φ i).source, f y = c + ∑ j, (if ↑j < k i then -1 else 1) * (↑(φ i) y).ofLp j ^ 2) :
  Topology.RelCWComplex
    ({x | f x ≤ c - ε} ∪
      ⋃ i, (φ i).source ∩ ↑(φ i) ⁻¹' {y | ‖y‖ ^ 2 ≤ ε ∧ ∀ (j : Fin n), k i ≤ ↑j → y.ofLp j = 0})
    {x | f x ≤ c - ε}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.morseRelCWComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/RelCWComplex.html#TauCeti.morseRelCWComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.morseRelCWComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/RelCWComplex.html#TauCeti.morseRelCWComplex)
- [Source of `TauCeti.morseRelCWComplex` in TauCeti/Geometry/Manifold/Morse/RelCWComplex.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/RelCWComplex.lean#L194)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
