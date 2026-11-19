---
declaration: theorem
origin: cited
lean: TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul
statement: formalized
proof: formalized
---

# Relative Gray stability

Let `α_t` be a smooth family of contact forms on a boundaryless
manifold, and let `K` be a set of points at each of which the contact hyperplane `ker α_t` is the
same for all times. Then for all times `s` and `t` there is a smooth partial diffeomorphism `φ` of
`M`, whose source and target are open neighbourhoods of `K`, which fixes every point of `K` and
pulls `α_t` back to a positive multiple of `α_s` on its source. It is Gray's partial isotopy
`TauCeti.SmoothForm.grayPartialDiffeomorph`. Neither `K` nor `M` need be compact, and `K` need not
be closed.

```lean
TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul.{u_1, u_2, u_3} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M]
  {α : TauCeti.SmoothForm ((modelWithCornersSelf ℝ ℝ).prod I) (ℝ × M) ℝ 1} [FiniteDimensional ℝ E]
  (hc : ∀ (t : ℝ), ((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α).IsContactForm) [I.Boundaryless]
  [T2Space M] {K : Set M}
  (hK :
    ∀ x ∈ K,
      ∀ (u : ℝ),
        ((TauCeti.SmoothForm.mpullback (Prod.mk u) ⋯) α).kerDistribution x =
          ((TauCeti.SmoothForm.mpullback (Prod.mk 0) ⋯) α).kerDistribution x)
  (s t : ℝ) :
  ∃ φ,
    K ⊆ φ.source ∧
      K ⊆ φ.target ∧
        (∀ x ∈ K, ↑φ.toPartialEquiv x = x) ∧
          ∀ x ∈ φ.source,
            ∃ g,
              0 < g ∧
                TauCeti.mpullback I I (↑φ.toPartialEquiv)
                    (↑((TauCeti.SmoothForm.mpullback (Prod.mk t) ⋯) α)) x =
                  g • ↑((TauCeti.SmoothForm.mpullback (Prod.mk s) ⋯) α) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [Gray's stability theorem](grays-stability-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul`](https://taucetiproject.org/docs/TauCeti/Geometry/Contact/Gray.html#TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul)
- [Source of `TauCeti.SmoothForm.exists_partialDiffeomorph_mpullback_eq_smul` in TauCeti/Geometry/Contact/Gray.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Contact/Gray.lean#L353)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
