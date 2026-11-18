---
declaration: theorem
origin: cited
lean: TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt
statement: formalized
proof: formalized
---

# Nonconstant pseudoholomorphic horizontal curves cover their orbit torus

Let `u` be a smooth
pseudoholomorphic map from a compact connected boundaryless surface `C`, oriented so that the
frames `(e, j e)` are positive, into `X_φ` with an almost complex structure satisfying `J ∂_s = T`
along the image of `u`, and let every tangent image of `u` lie in the horizontal plane
`span(∂_s, T)`. Suppose the differential of `u` is nonzero somewhere, and let `(s, [t, x])` be a
value of `u`, where `x` has least period `d`. Then `u = τ ∘ v` for the orbit torus
`τ : (ℝ / ℤ) × (ℝ / dℤ) → X_φ`, `(s, θ) ↦ (s, [θ, x])`, and a smooth map `v` that is
pseudoholomorphic for the standard structure of the torus and onto. Unlike
`exists_isLocalDiffeomorph_orbitTorus_comp_eq_of_mfderiv_mem_suspensionHorizontalSubspace`, `u`
may have critical points, and then `v` need not be a local diffeomorphism.

```lean
TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt.{u_1, u_2,
    u_3, u_4, u_5, u_6}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (↑⊤) M] [T2Space M] [LocallyCompactSpace M] {φ : Diffeomorph I I M M ↑⊤}
  {E' : Type u_4} [NormedAddCommGroup E'] [NormedSpace ℝ E'] {H' : Type u_5} [TopologicalSpace H']
  {I' : ModelWithCorners ℝ E' H'} {C : Type u_6} [TopologicalSpace C] [ChartedSpace H' C]
  {u : C → UnitAddCircle × TauCeti.SmoothMappingTorus φ} [IsManifold I' (↑⊤) C]
  [FiniteDimensional ℝ E']
  {J :
    TauCeti.SmoothAlmostComplexStructure
      ((modelWithCornersSelf ℝ ℝ).prod ((modelWithCornersSelf ℝ ℝ).prod I))
      (UnitAddCircle × TauCeti.SmoothMappingTorus φ)}
  {j : TauCeti.SmoothAlmostComplexStructure I' C} {o : TauCeti.Manifold.Orientation I' C (Fin 2)}
  [I.Boundaryless] [FiniteDimensional ℝ E] [I'.Boundaryless] [T2Space C] [CompactSpace C]
  [PreconnectedSpace C]
  (hu : ContMDiff I' ((modelWithCornersSelf ℝ ℝ).prod ((modelWithCornersSelf ℝ ℝ).prod I)) (↑⊤) u)
  (ho :
    ∀ (c : C) (b : Module.Basis (Fin 2) ℝ (TangentSpace I' c)),
      b 1 = (fun x => ⇑(j.toEndomorphism x)) c (b 0) → b.orientation = o.orientationAt c)
  (hhol : ∀ (c : C), TauCeti.IsPseudoholomorphicAt j J u c)
  (hS :
    ∀ (c : C),
      (fun x => ⇑(J.toEndomorphism x)) (u c)
          ((TauCeti.Manifold.tangentSpaceProdEquiv (u c)).symm (1, 0)) =
        (TauCeti.Manifold.tangentSpaceProdEquiv (u c)).symm
          (0, TauCeti.SmoothMappingTorus.timeVectorField φ (u c).2))
  (hH :
    ∀ (c : C) (e : TangentSpace I' c),
      (mfderiv% u c) e ∈ TauCeti.SmoothMappingTorus.suspensionHorizontalSubspace φ (u c))
  {c₀ : C} (hne : mfderiv% u c₀ ≠ 0) {c : C} {t : ℝ} {x : M}
  (hc : (u c).2 = TauCeti.SmoothMappingTorus.mk φ t x) {d : ℕ} [Fact (0 < ↑d)]
  (h : Function.IsPeriodicPt (⇑φ) d x) (hd : Function.minimalPeriod (⇑φ) x = d) :
  ∃ v,
    ContMDiff I' ((modelWithCornersSelf ℝ ℝ).prod (modelWithCornersSelf ℝ ℝ)) (↑⊤) v ∧
      (∀ (c : C),
          TauCeti.IsPseudoholomorphicAt j (TauCeti.SmoothAlmostComplexStructure.addCircleProd 1 ↑d)
            v c) ∧
        Function.Surjective v ∧ TauCeti.SmoothMappingTorus.orbitTorus φ h ∘ v = u
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The compactly supported Poincaré lemma on the line](../../../geometry/part-02/manifold/part-01/the-compactly-supported-poincare-lemma-on-the-li.md)
- [The inverse function theorem for a converging family](../../part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Suspension/Leaf.html#TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/Suspension/Leaf.html#TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt)
- [Source of `TauCeti.SmoothMappingTorus.exists_surjective_orbitTorus_comp_eq_of_isPseudoholomorphicAt` in TauCeti/Geometry/Symplectic/Manifold/Suspension/Leaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/Suspension/Leaf.lean#L468)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
