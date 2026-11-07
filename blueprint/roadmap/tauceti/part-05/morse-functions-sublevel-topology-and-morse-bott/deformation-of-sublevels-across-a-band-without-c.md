---
declaration: theorem
origin: cited
lean: TauCeti.exists_sublevelDeformation
statement: formalized
proof: formalized
---

# Deformation of sublevels across a band without critical points

(Milnor, Theorem 3.1). If
`f` is smooth, `a ≤ b`, and the band `f⁻¹[a, b]` is compact and contains no critical point of `f`,
then the sublevel `{f ≤ a}` is a strong deformation retract of `{f ≤ b}`: there is a retraction
`r` of `{f ≤ b}` onto `{f ≤ a}` and a homotopy from the inclusion of `r` to the identity fixing
`{f ≤ a}` pointwise.

```lean
TauCeti.exists_sublevelDeformation.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [I.Boundaryless] [IsManifold I (↑⊤) M] {f : M → ℝ} {a b : ℝ}
  (hf : ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) f) (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (hreg : ∀ (x : M), a ≤ f x → f x ≤ b → mfderiv% f x ≠ 0) :
  ∃ r,
    (∀ (x : ↑{x | f x ≤ a}), r ((TauCeti.sublevelInclusion f a b hab) x) = x) ∧
      Nonempty
        (((TauCeti.sublevelInclusion f a b hab).comp r).HomotopyRel
          (ContinuousMap.id ↑{x | f x ≤ b}) {x | f ↑x ≤ a})
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_sublevelDeformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Deformation.html#TauCeti.exists_sublevelDeformation).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_sublevelDeformation`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Deformation.html#TauCeti.exists_sublevelDeformation)
- [Source of `TauCeti.exists_sublevelDeformation` in TauCeti/Geometry/Manifold/Morse/Deformation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Deformation.lean#L194)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MorseTheory/STATUS.md)
