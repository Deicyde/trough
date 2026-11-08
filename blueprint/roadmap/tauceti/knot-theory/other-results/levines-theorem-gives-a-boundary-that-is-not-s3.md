---
declaration: theorem
origin: cited
lean: TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere
statement: formalized
proof: formalized
---

# Levine's theorem gives a boundary that is not `S³`

Assuming Levine's theorem, some smooth
compact contractible `4`-manifold `X` has as boundary a closed `3`-manifold `Y` not diffeomorphic to
`S³`. A diffeomorphism `e : Y ≃ₘ S³` would make the knot `K` of Levine's theorem homology concordant
to the knot `e ∘ K` in `S³` (`TauCeti.SmoothEmbedding.homologyConcordant_transDiffeomorph`).

```lean
TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere
  (h : TauCeti.LevineHomologyConcordanceTheorem) :
  ∃ Y x,
    ∃ (_ : T2Space Y) (_ : CompactSpace Y),
      ∃ x_3,
        ∃ (_ : IsManifold (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 3))) (↑⊤) Y),
          ∃ X x_5,
            ∃ (_ : T2Space X) (_ : CompactSpace X) (_ : ContractibleSpace X),
              ∃ x_9,
                ∃ (_ :
                  IsManifold
                    ((modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 3))).prod
                      (modelWithCornersEuclideanHalfSpace 1))
                    (↑⊤) X),
                  ∃ κ,
                    Set.range ⇑κ = ModelWithCorners.boundary X ∧
                      IsEmpty
                        (Diffeomorph (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 3)))
                          (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin 3))) Y ↑(Metric.sphere 0 1)
                          ↑⊤)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere`](https://taucetiproject.org/docs/TauCeti/KnotTheory/HomologyConcordance.html#TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere), assuming [`TauCeti.LevineHomologyConcordanceTheorem`](https://taucetiproject.org/docs/TauCeti/KnotTheory/HomologyConcordance.html#TauCeti.LevineHomologyConcordanceTheorem), a proposition Tau Ceti defines.

## Sources

- [Tau Ceti documentation: `TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere`](https://taucetiproject.org/docs/TauCeti/KnotTheory/HomologyConcordance.html#TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere)
- [Source of `TauCeti.LevineHomologyConcordanceTheorem.exists_isEmpty_diffeomorph_sphere` in TauCeti/KnotTheory/HomologyConcordance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/HomologyConcordance.lean#L111)
