---
declaration: def
origin: cited
lean: TauCeti.Quiver.invariantForms
statement: formalized
---

# TauCeti.Quiver.invariantForms

The smooth forms on objects whose source and target pullbacks agree on total arrows.

```lean
TauCeti.Quiver.invariantForms.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {E : Type u_1} {H : Type u_2}
  {A : Type u_3} {K : Type u_4} {C : Type u_5} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] [NormedAddCommGroup A] [NormedSpace ℝ A] [TopologicalSpace K] [Quiver C]
  [TopologicalSpace C] [TopologicalSpace (Quiver.Total C)] [ChartedSpace H C]
  [ChartedSpace K (Quiver.Total C)] (I : ModelWithCorners ℝ E H) (J : ModelWithCorners ℝ A K)
  [IsManifold I (↑⊤) C] [IsManifold J (↑⊤) (Quiver.Total C)]
  (hs : ContMDiff J I (↑⊤) Quiver.Total.left) (ht : ContMDiff J I (↑⊤) Quiver.Total.right)
  (V : Type u_6) [NormedAddCommGroup V] [NormedSpace ℝ V] (k : ℕ) :
  Submodule ℝ (TauCeti.SmoothForm I C V k)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Quiver.invariantForms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Category/InvariantForm.html#TauCeti.Quiver.invariantForms).

## Sources

- [Tau Ceti documentation: `TauCeti.Quiver.invariantForms`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Category/InvariantForm.html#TauCeti.Quiver.invariantForms)
- [Source of `TauCeti.Quiver.invariantForms` in TauCeti/Geometry/Manifold/Category/InvariantForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Category/InvariantForm.lean#L52)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Orbifolds/STATUS.md)
