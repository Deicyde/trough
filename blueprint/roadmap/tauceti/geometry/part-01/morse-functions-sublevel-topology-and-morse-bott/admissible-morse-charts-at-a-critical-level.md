---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_admissible_morseCharts
statement: formalized
proof: formalized
---

# Admissible Morse charts at a critical level

Let `f` be a Morse function on a Hausdorff
manifold whose band `f⁻¹[c - δ, c + δ]` is compact, for some `0 < δ`. Then there are a width
`0 < ε ≤ δ` and normalized Morse charts `ψ p`, indexed by the critical points `p` on the level
`f⁻¹(c)`, such that

* the only critical points in the band `f⁻¹[c - ε, c + ε]` are those on the level `f⁻¹(c)`;
* the chart sources are pairwise disjoint, and each lies in a prescribed neighbourhood `U p`;
* `ψ p p = 0`, and `f = c - Σ_{i < λ} (ψ p)ᵢ² + Σ_{i ≥ λ} (ψ p)ᵢ²` on the source of `ψ p`, where
  `λ` is the Morse index of `f` at `p`;
* the target of each chart contains the closed ball of radius `√(2ε)` about `0`.

The last condition places Milnor's ellipsoid `‖u‖² + 2‖v‖² ≤ 2ε` inside every chart. All of these
conditions persist when `ε` is decreased.

```lean
TauCeti.IsMorse.exists_admissible_morseCharts.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2}
  {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {f : M → ℝ} [T2Space M] (hf : TauCeti.IsMorse I f)
  {c δ : ℝ} (hδ : 0 < δ) (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) {U : M → Set M}
  (hU : ∀ x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' {c}, U x ∈ nhds x) :
  ∃ ε,
    0 < ε ∧
      ε ≤ δ ∧
        TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Icc (c - ε) (c + ε) ⊆ f ⁻¹' {c} ∧
          ∃ ψ,
            Pairwise (Function.onFun Disjoint fun p => (ψ p).source) ∧
              ∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                ↑p ∈ (ψ p).source ∧
                  (ψ p).source ⊆ U ↑p ∧
                    ↑(ψ p).toPartialEquiv ↑p = 0 ∧
                      Metric.closedBall 0 √(2 * ε) ⊆ (ψ p).target ∧
                        ∀ y ∈ (ψ p).source,
                          f y =
                            c +
                              ∑ i,
                                (if ↑i < TauCeti.manifoldMorseIndex I f ↑p then -1 else 1) *
                                  (↑(ψ p).toPartialEquiv y).ofLp i ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The normalized Morse lemma on a manifold](the-normalized-morse-lemma-on-a-manifold.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_admissible_morseCharts`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/AdmissibleCharts.html#TauCeti.IsMorse.exists_admissible_morseCharts).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_admissible_morseCharts`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/AdmissibleCharts.html#TauCeti.IsMorse.exists_admissible_morseCharts)
- [Source of `TauCeti.IsMorse.exists_admissible_morseCharts` in TauCeti/Geometry/Manifold/Morse/AdmissibleCharts.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/AdmissibleCharts.lean#L56)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
