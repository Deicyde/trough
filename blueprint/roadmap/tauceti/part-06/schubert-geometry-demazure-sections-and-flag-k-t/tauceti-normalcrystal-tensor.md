---
declaration: def
origin: cited
lean: TauCeti.NormalCrystal.tensor
statement: formalized
---

# TauCeti.NormalCrystal.tensor

The **tensor product** `B₁ ⊗ B₂` of two normal crystals, on the product type, with
Kashiwara's tie convention: on a tie `φ i x₁ = ε i x₂` the raising operator acts on the left
factor and the lowering operator on the right factor.

```lean
TauCeti.NormalCrystal.tensor.{u, v, w, x₁, x₂} {ι : Type u} {X : Type v} {Y : Type w}
  [AddCommGroup X] [AddCommGroup Y] {P : RootDatum ι X Y} {b : RootPairing.Base P} {B₁ : Type x₁}
  {B₂ : Type x₂} (c : TauCeti.NormalCrystal P b B₁) (d : TauCeti.NormalCrystal P b B₂) :
  TauCeti.NormalCrystal P b (B₁ × B₂)
```

## Depends on

- [TauCeti.NormalCrystal](tauceti-normalcrystal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NormalCrystal.tensor`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Tensor.html#TauCeti.NormalCrystal.tensor).

## Sources

- [Tau Ceti documentation: `TauCeti.NormalCrystal.tensor`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Tensor.html#TauCeti.NormalCrystal.tensor)
- [Source of `TauCeti.NormalCrystal.tensor` in TauCeti/RepresentationTheory/Crystal/Tensor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Crystal/Tensor.lean#L86)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
