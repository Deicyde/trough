---
declaration: def
origin: cited
lean: TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph
statement: formalized
---

# TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph

The orientation double cover of `E` is the quotient of the orthonormal frame bundle by the
right action of the special orthogonal group of `V`: when `card ι` is positive and equal to the
dimension of `V` and of the model fibre, transporting the orientation `o` of `V` along frames
descends to a homeomorphism from the quotient by `orientedRel` onto the orientation double cover.
It sends the class of a frame `p` to `toOrientationCover o p`
(`TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph_mk`).

```lean
TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph.{u_1, u_2, u_3, u_4, u_5} {B : Type u_1}
  {F : Type u_2} {E : B → Type u_3} [(x : B) → NormedAddCommGroup (E x)]
  [(x : B) → InnerProductSpace ℝ (E x)] {V : Type u_4} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] {ι : Type u_5} [TopologicalSpace (Bundle.TotalSpace F E)]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [TopologicalSpace B] [FiberBundle F E]
  [VectorBundle ℝ F E] [Fintype ι] [FiniteDimensional ℝ V] [IsContinuousRiemannianBundle F E]
  [Nonempty ι] [FiniteDimensional ℝ F] (hι : Fintype.card ι = Module.finrank ℝ V)
  (hF : Fintype.card ι = Module.finrank ℝ F) (o : Orientation ℝ V ι) :
  Quotient (TauCeti.OrthonormalFrameBundle.orientedRel F E V) ≃ₜ
    TauCeti.VectorBundleOrientationCover F E ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/OrthonormalFrame.html#TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/Orientation/OrthonormalFrame.html#TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph)
- [Source of `TauCeti.OrthonormalFrameBundle.orientationCoverHomeomorph` in TauCeti/Topology/VectorBundle/Orientation/OrthonormalFrame.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/VectorBundle/Orientation/OrthonormalFrame.lean#L309)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
