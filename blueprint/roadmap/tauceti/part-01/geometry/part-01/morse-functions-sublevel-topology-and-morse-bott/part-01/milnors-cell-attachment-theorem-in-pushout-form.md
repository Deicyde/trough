---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_morseCellAttachment_deformation, TauCeti.IsMorse.exists_sublevel_union_cells_deformation, TauCeti.IsMorse.exists_relCWComplex_sublevel_deformation
statement: formalized
proof: formalized
---

# Milnor's cell attachment theorem, in pushout form

Let `f` be a Morse function and `c` a
value with a compact band `f⁻¹[c - δ, c + δ]`. Then for some `0 < ε ≤ δ` there are normalized Morse
charts `ψ p` at the critical points `p` on the level `c`, with pairwise disjoint sources, such that
the comparison map `Φ : M_{c-ε} ∪_α ⨆ₚ D^{λ p} → M_{c+ε}` from the lower sublevel with one cell of
dimension the Morse index `λ p` attached at each `p` has a left inverse `g`, and `Φ ∘ g` is
homotopic to the identity of `M_{c+ε}` relative to the image of `Φ`, which contains the lower
sublevel `M_{c-ε}`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cells of a critical level form a relative CW complex](the-cells-of-a-critical-level-form-a-relative-cw.md)
- [The normalized Morse lemma](../part-02/the-normalized-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_morseCellAttachment_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Comparison.html#TauCeti.IsMorse.exists_morseCellAttachment_deformation).

## Other forms

**Milnor's cell attachment theorem.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sublevel_union_cells_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.html#TauCeti.IsMorse.exists_sublevel_union_cells_deformation).

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

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_morseCellAttachment_deformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Comparison.html#TauCeti.IsMorse.exists_morseCellAttachment_deformation)
- [Source of `TauCeti.IsMorse.exists_morseCellAttachment_deformation` in TauCeti/Geometry/Manifold/Morse/Cell/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Cell/Comparison.lean#L587)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
