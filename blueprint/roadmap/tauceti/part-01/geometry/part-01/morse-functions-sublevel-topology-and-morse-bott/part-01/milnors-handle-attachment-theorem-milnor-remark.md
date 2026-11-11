---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles, TauCeti.IsMorse.exists_isPushout_sublevel_handles
statement: formalized
proof: formalized
---

# Milnor's handle attachment theorem (Milnor, Remark 3.3)

Let `f` be a Morse function on a
Hausdorff manifold of dimension `m` whose band `f⁻¹[c - δ, c + δ]` is compact, for some `0 < δ`.
Then there are a width `0 < ε ≤ δ` and normalized Morse charts `ψ p` with pairwise disjoint sources,
indexed by the critical points `p` on the level `f⁻¹(c)`, with `ψ p p = 0`, with the closed ball of
radius `√(2ε)` in the target of `ψ p`, and in which `f = c - Σ_{i < λ} yᵢ² + Σ_{i ≥ λ} yᵢ²`, where
`λ` is the Morse index of `f` at `p`.

Attaching one handle `D^λ × D^(m-λ)` at each critical point turns the lower sublevel
`{f ≤ c - ε}` into the upper one `{f ≤ c + ε}`, up to a diffeomorphism `Φ` of `M`: the conclusion
of `TauCeti.exists_diffeomorph_sublevel_eq_union_handles` holds for these charts.

```lean
TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} {c : ℝ}
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M]
  (hf : TauCeti.IsMorse I f) {δ : ℝ} (hδ : 0 < δ)
  (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    0 < ε ∧
      ε ≤ δ ∧
        ∃ ψ,
          Pairwise (Function.onFun Disjoint fun p => (ψ p).source) ∧
            (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                ↑p ∈ (ψ p).source ∧
                  ↑(ψ p).toPartialEquiv ↑p = 0 ∧
                    Metric.closedBall 0 √(2 * ε) ⊆ (ψ p).target ∧
                      ∀ y ∈ (ψ p).source,
                        f y =
                          c +
                            ∑ i,
                              (if ↑i < TauCeti.manifoldMorseIndex I f ↑p then -1 else 1) *
                                (↑(ψ p).toPartialEquiv y).ofLp i ^ 2) ∧
              ∃ H_1 e Φ,
                (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})), H_1 p ⊆ (ψ p).source) ∧
                  (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})) (x : ↑(H_1 p)), c - ε ≤ f ↑x) ∧
                    (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})) (x : ↑(H_1 p)),
                        f ↑x ≤ c - ε ↔ ‖↑((e p) x).1‖ = 1) ∧
                      (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})) (x : ↑(H_1 p)),
                          ↑((e p) x).2 = 0 ↔
                            ∀ (i : Fin (Module.finrank ℝ E)),
                              TauCeti.manifoldMorseIndex I f ↑p ≤ ↑i →
                                (↑(ψ p).toPartialEquiv ↑x).ofLp i = 0) ∧
                        (∀ (x : M), Φ x ∈ {x | f x ≤ c - ε} ∪ ⋃ p, H_1 p ↔ f x ≤ c + ε) ∧
                          ∀ (x : M),
                            f x = c + ε ↔
                              (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})) (h : Φ x ∈ H_1 p),
                                  ‖↑((e p) ⟨Φ x, h⟩).2‖ = 1) ∧
                                (Φ x ∉ ⋃ p, H_1 p → f (Φ x) = c - ε)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The normalized Morse lemma](../part-02/the-normalized-morse-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.html#TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles).

## Other forms

**Milnor's handle attachment theorem, as a pushout (Milnor, Remark 3.3).** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_isPushout_sublevel_handles`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/HandlePushout.html#TauCeti.IsMorse.exists_isPushout_sublevel_handles).

```lean
TauCeti.IsMorse.exists_isPushout_sublevel_handles.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  {M : Type u} [TopologicalSpace M] [ChartedSpace H M] {f : M → ℝ} {c : ℝ} [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] (hf : TauCeti.IsMorse I f) {δ : ℝ} (hδ : 0 < δ)
  (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    0 < ε ∧
      ε ≤ δ ∧
        ∃ α χ j,
          CategoryTheory.IsPushout (CategoryTheory.Limits.Sigma.desc α)
              (CategoryTheory.Limits.Sigma.map fun p =>
                TopCat.ofHom
                  ((TopCat.Hom.hom
                        (TopCat.diskBoundaryInclusion (TauCeti.manifoldMorseIndex I f ↑p))).prodMap
                    (ContinuousMap.id
                      ↑(TopCat.disk (Module.finrank ℝ E - TauCeti.manifoldMorseIndex I f ↑p)))))
              j (CategoryTheory.Limits.Sigma.desc χ) ∧
            (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                Topology.IsClosedEmbedding ⇑(CategoryTheory.ConcreteCategory.hom (α p))) ∧
              Pairwise
                  (Function.onFun Disjoint fun p =>
                    Set.range ⇑(CategoryTheory.ConcreteCategory.hom (α p))) ∧
                (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c}))
                    (s :
                      ↑↧(↑(TopCat.diskBoundary (TauCeti.manifoldMorseIndex I f ↑p)) ×
                            ↑(TopCat.disk
                                (Module.finrank ℝ E - TauCeti.manifoldMorseIndex I f ↑p)))),
                    f ↑((CategoryTheory.ConcreteCategory.hom (α p)) s) = c - ε) ∧
                  (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c}))
                      (w :
                        ↑↧(↑(TopCat.disk (TauCeti.manifoldMorseIndex I f ↑p)) ×
                              ↑(TopCat.disk
                                  (Module.finrank ℝ E - TauCeti.manifoldMorseIndex I f ↑p)))),
                      f ↑((CategoryTheory.ConcreteCategory.hom (χ p)) w) = c + ε ↔
                        w.2 ∈
                          Set.range
                            ⇑(CategoryTheory.ConcreteCategory.hom
                                (TopCat.diskBoundaryInclusion
                                  (Module.finrank ℝ E - TauCeti.manifoldMorseIndex I f ↑p)))) ∧
                    ∀ (x : ↑↧↑{x | f x ≤ c - ε}),
                      (∀ (p : ↑(TauCeti.criticalPoints I f ∩ f ⁻¹' {c})),
                          x ∉ Set.range ⇑(CategoryTheory.ConcreteCategory.hom (α p))) →
                        (f ↑((CategoryTheory.ConcreteCategory.hom j) x) = c + ε ↔ f ↑x = c - ε)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.html#TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles)
- [Source of `TauCeti.IsMorse.exists_diffeomorph_sublevel_eq_union_handles` in TauCeti/Geometry/Manifold/Morse/Cell/Attachment.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Cell/Attachment.lean#L696)
