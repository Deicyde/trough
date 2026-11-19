---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_sublevel_union_cells_deformation, TauCeti.IsMorse.exists_relCWComplex_sublevel_deformation, TauCeti.IsMorse.exists_morseCellAttachment_deformation
statement: formalized
proof: formalized
---

# Milnor's cell attachment theorem

Let `f` be a Morse function on a Hausdorff manifold whose
band `f⁻¹[c - δ, c + δ]` is compact, for some `0 < δ`. Then there are a width `0 < ε₀ ≤ δ` and
normalized Morse charts `ψ p` with pairwise disjoint sources, indexed by the critical points `p`
on the level `f⁻¹(c)`, with `ψ p p = 0`, with the closed ball of radius `√(2ε₀)` in the target of
`ψ p`, and in which `f = c - Σ_{i < λ} yᵢ² + Σ_{i ≥ λ} yᵢ²`, where `λ` is the Morse index of `f`
at `p`. For every width `0 < ε ≤ ε₀`, the cell at `p` is the disc
`{‖y‖² ≤ ε, yᵢ = 0 for i ≥ λ}` of its negative coordinates, read in `M` through `ψ p`.

The lower sublevel `{f ≤ c - ε}` with these cells attached is a strong deformation retract of
`{f ≤ c + ε}`, for every such `ε`: there is a retraction of `{f ≤ c + ε}` onto it, and a
homotopy in `{f ≤ c + ε}` from this retraction to the identity which fixes it pointwise.

```lean
TauCeti.IsMorse.exists_sublevel_union_cells_deformation.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} {c : ℝ}
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M]
  (hf : TauCeti.IsMorse I f) {δ : ℝ} (hδ : 0 < δ)
  (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε₀,
    0 < ε₀ ∧
      ε₀ ≤ δ ∧
        ∃ ψ,
          Pairwise (Function.onFun Disjoint fun p => (ψ p).source) ∧
            (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                ↑p ∈ (ψ p).source ∧
                  ↑(ψ p).toPartialEquiv ↑p = 0 ∧
                    Metric.closedBall 0 √(2 * ε₀) ⊆ (ψ p).target ∧
                      ∀ y ∈ (ψ p).source,
                        f y =
                          c +
                            ∑ i,
                              (if ↑i < TauCeti.manifoldMorseIndex I f ↑p then -1 else 1) *
                                (↑(ψ p).toPartialEquiv y).ofLp i ^ 2) ∧
              ∀ (ε : ℝ),
                0 < ε →
                  ε ≤ ε₀ →
                    ∃ r,
                      (∀
                          (x :
                            ↑({x | f x ≤ c + ε} ∩
                                ({x | f x ≤ c - ε} ∪
                                  ⋃ p,
                                    (ψ p).source ∩
                                      ↑(ψ p).toPartialEquiv ⁻¹'
                                        {y |
                                          ‖y‖ ^ 2 ≤ ε ∧
                                            ∀ (i : Fin (Module.finrank ℝ E)),
                                              TauCeti.manifoldMorseIndex I f ↑p ≤ ↑i →
                                                y.ofLp i = 0}))),
                          r ((ContinuousMap.inclusion ⋯) x) = x) ∧
                        Nonempty
                          (((ContinuousMap.inclusion ⋯).comp r).HomotopyRel
                            (ContinuousMap.id ↑{x | f x ≤ c + ε})
                            {x |
                              ↑x ∈
                                {x | f x ≤ c - ε} ∪
                                  ⋃ p,
                                    (ψ p).source ∩
                                      ↑(ψ p).toPartialEquiv ⁻¹'
                                        {y |
                                          ‖y‖ ^ 2 ≤ ε ∧
                                            ∀ (i : Fin (Module.finrank ℝ E)),
                                              TauCeti.manifoldMorseIndex I f ↑p ≤ ↑i →
                                                y.ofLp i = 0}})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The cells of a critical level form a relative CW complex](../../../part-01/morse-functions-sublevel-topology-and-morse-bott/part-01/the-cells-of-a-critical-level-form-a-relative-cw.md)
- [The normalized Morse lemma](../../../part-01/morse-functions-sublevel-topology-and-morse-bott/part-02/the-normalized-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sublevel_union_cells_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.html#TauCeti.IsMorse.exists_sublevel_union_cells_deformation).

## Other forms

**Milnor's cell attachment theorem in CW form.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_relCWComplex_sublevel_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/RelCWComplex.html#TauCeti.IsMorse.exists_relCWComplex_sublevel_deformation).

```lean
TauCeti.IsMorse.exists_relCWComplex_sublevel_deformation.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {c δ : ℝ}
  (hf : TauCeti.IsMorse I f) (hδ : 0 < δ) (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    0 < ε ∧
      ε ≤ δ ∧
        ∃ C x,
          ∃ (_ : Topology.RelCWComplex.Finite C) (hC : C ⊆ {x | f x ≤ c + ε}),
            (∀ (m : ℕ),
                Nonempty
                  (Topology.RelCWComplex.cell C m ≃
                    { p // TauCeti.manifoldMorseIndex I f ↑p = m })) ∧
              (∀ (m : ℕ) (j : Topology.RelCWComplex.cell C m),
                  Topology.RelCWComplex.cellFrontier m j ⊆ {x | f x ≤ c - ε}) ∧
                ∃ r,
                  (∀ (x : ↑C), r ((ContinuousMap.inclusion hC) x) = x) ∧
                    Nonempty
                      (((ContinuousMap.inclusion hC).comp r).HomotopyRel
                        (ContinuousMap.id ↑{x | f x ≤ c + ε}) {x | ↑x ∈ C})
```

**Milnor's cell attachment theorem, in pushout form.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_morseCellAttachment_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Comparison.html#TauCeti.IsMorse.exists_morseCellAttachment_deformation).

```lean
TauCeti.IsMorse.exists_morseCellAttachment_deformation.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {c : ℝ} (hf : TauCeti.IsMorse I f)
  {δ : ℝ} (hδ : 0 < δ) (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    ∃ (hε : 0 < ε),
      ε ≤ δ ∧
        ∃ ψ,
          Pairwise (Function.onFun Disjoint fun p => (ψ p).source) ∧
            (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                ↑p ∈ (ψ p).source ∧ ↑(ψ p).toPartialEquiv ↑p = 0) ∧
              ∃ (hball :
                ∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                  Metric.closedBall 0 √ε ⊆ (ψ p).target)
                (hψ :
                ∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                  ∀ y ∈ (ψ p).source,
                    f y =
                      c +
                        ∑ i,
                          (if ↑i < TauCeti.manifoldMorseIndex I f ↑p then -1 else 1) *
                            (↑(ψ p).toPartialEquiv y).ofLp i ^ 2),
                ∃ g,
                  Function.LeftInverse ⇑g
                      ⇑(CategoryTheory.ConcreteCategory.hom
                          (TauCeti.morseCellComparison (fun p => (ψ p).toOpenPartialHomeomorph)
                            (fun x => TauCeti.manifoldMorseIndex I f ↑x) ⋯ ⋯ hball hψ)) ∧
                    (ContinuousMap.id ↑↧↑{x | f x ≤ c + ε}).HomotopicRel
                      ((TopCat.Hom.hom
                            (TauCeti.morseCellComparison (fun p => (ψ p).toOpenPartialHomeomorph)
                              (fun x => TauCeti.manifoldMorseIndex I f ↑x) ⋯ ⋯ hball hψ)).comp
                        g)
                      (Set.range
                        ⇑(CategoryTheory.ConcreteCategory.hom
                            (TauCeti.morseCellComparison (fun p => (ψ p).toOpenPartialHomeomorph)
                              (fun x => TauCeti.manifoldMorseIndex I f ↑x) ⋯ ⋯ hball hψ)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_sublevel_union_cells_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.html#TauCeti.IsMorse.exists_sublevel_union_cells_deformation)
- [Source of `TauCeti.IsMorse.exists_sublevel_union_cells_deformation` in TauCeti/Geometry/Manifold/Morse/Cell/Attachment.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.lean#L664)
