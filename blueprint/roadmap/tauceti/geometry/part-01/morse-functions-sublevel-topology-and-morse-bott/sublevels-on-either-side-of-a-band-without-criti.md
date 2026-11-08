---
declaration: theorem
origin: cited
lean: TauCeti.exists_diffeomorph_sublevel
statement: formalized
proof: formalized
---

# Sublevels on either side of a band without critical points are diffeomorphic (Milnor, Theorem 3.1)

If `f` is smooth, `a ≤ b`, and the band `f⁻¹[a, b]` is compact and contains
no critical point of `f`, then there is a diffeomorphism `Φ` of `M` carrying the sublevel
`{f ≤ b}` onto `{f ≤ a}` and the level `f⁻¹(b)` onto `f⁻¹(a)`.

```lean
TauCeti.exists_diffeomorph_sublevel.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [I.Boundaryless] [IsManifold I (↑⊤) M] {f : M → ℝ} {a b : ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (hreg : ∀ (x : M), a ≤ f x → f x ≤ b → mfderiv% f x ≠ 0) :
  ∃ Φ, ∀ (x : M), (f (Φ x) ≤ a ↔ f x ≤ b) ∧ (f (Φ x) = a ↔ f x = b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_diffeomorph_sublevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Deformation.html#TauCeti.exists_diffeomorph_sublevel).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_diffeomorph_sublevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Deformation.html#TauCeti.exists_diffeomorph_sublevel)
- [Source of `TauCeti.exists_diffeomorph_sublevel` in TauCeti/Geometry/Manifold/Morse/Deformation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Deformation.lean#L228)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
