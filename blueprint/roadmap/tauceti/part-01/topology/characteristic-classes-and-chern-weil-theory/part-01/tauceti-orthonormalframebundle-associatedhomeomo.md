---
declaration: def
origin: cited
lean: TauCeti.OrthonormalFrameBundle.associatedHomeomorph
statement: formalized
---

# TauCeti.OrthonormalFrameBundle.associatedHomeomorph

The orthonormal frame bundle reconstructs `E` as its associated bundle with fibre the
standard representation of the unitary group on `V`: when `V` has the dimension of the model
fibre, applying frames to vectors descends to a homeomorphism from the quotient of
`OrthonormalFrameBundle 𝕜 F E V × V` by `(p, g w) ∼ (p • g, w)` onto the total space of `E`. It
sends the class of `(p, v)` to `p v` in the fibre over `p.proj`
(`TauCeti.OrthonormalFrameBundle.associatedHomeomorph_mk`).

```lean
TauCeti.OrthonormalFrameBundle.associatedHomeomorph.{u_1, u_2, u_3, u_4, u_5} {𝕜 : Type u_1}
  [RCLike 𝕜] {B : Type u_2} {F : Type u_3} {E : B → Type u_4} [(x : B) → NormedAddCommGroup (E x)]
  [(x : B) → InnerProductSpace 𝕜 (E x)] {V : Type u_5} [NormedAddCommGroup V]
  [InnerProductSpace 𝕜 V] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [TopologicalSpace (Bundle.TotalSpace F E)] [TopologicalSpace B] [FiberBundle F E]
  [VectorBundle 𝕜 F E] [TauCeti.ContinuousFiberNorm F E] [CompleteSpace V] [FiniteDimensional 𝕜 F]
  [FiniteDimensional 𝕜 V] (h : Module.finrank 𝕜 V = Module.finrank 𝕜 F) :
  Quotient (TauCeti.OrthonormalFrameBundle.associatedRel 𝕜 F E V) ≃ₜ Bundle.TotalSpace F E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrthonormalFrameBundle.associatedHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/OrthonormalFrame/Basic.html#TauCeti.OrthonormalFrameBundle.associatedHomeomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.OrthonormalFrameBundle.associatedHomeomorph`](https://taucetiproject.org/docs/TauCeti/Topology/VectorBundle/OrthonormalFrame/Basic.html#TauCeti.OrthonormalFrameBundle.associatedHomeomorph)
- [Source of `TauCeti.OrthonormalFrameBundle.associatedHomeomorph` in TauCeti/Topology/VectorBundle/OrthonormalFrame/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/VectorBundle/OrthonormalFrame/Basic.lean#L649)
- [Tau Ceti roadmap status: Characteristic classes and Chern–Weil theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CharacteristicClasses/STATUS.md)
