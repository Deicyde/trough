---
declaration: theorem
origin: cited
lean: TauCeti.NormalCrystal.tensor_ε_eq_max
statement: formalized
proof: formalized
---

# TauCeti.NormalCrystal.tensor_ε_eq_max

Kashiwara's form of the raising string length of a tensor product:
`ε i (x₁ ⊗ x₂) = max (ε i x₁) (ε i x₂ - ⟨wt x₁, α_i^∨⟩)`.

```lean
TauCeti.NormalCrystal.tensor_ε_eq_max.{u, v, w, x₁, x₂} {ι : Type u} {X : Type v} {Y : Type w}
  [AddCommGroup X] [AddCommGroup Y] {P : RootDatum ι X Y} {b : RootPairing.Base P} {B₁ : Type x₁}
  {B₂ : Type x₂} {c : TauCeti.NormalCrystal P b B₁} {d : TauCeti.NormalCrystal P b B₂}
  (i : ↥b.support) (x : B₁ × B₂) :
  ↑((c.tensor d).ε i x) =
    max (↑(c.ε i x.1)) (↑(d.ε i x.2) - (P.toLinearMap (c.wt x.1)) (P.coroot ↑i))
```

## Depends on

- [TauCeti.NormalCrystal](tauceti-normalcrystal.md)
- [TauCeti.NormalCrystal.tensor](tauceti-normalcrystal-tensor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NormalCrystal.tensor_ε_eq_max`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Tensor.html#TauCeti.NormalCrystal.tensor_%CE%B5_eq_max).

## Sources

- [Tau Ceti documentation: `TauCeti.NormalCrystal.tensor_ε_eq_max`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Crystal/Tensor.html#TauCeti.NormalCrystal.tensor_%CE%B5_eq_max)
- [Source of `TauCeti.NormalCrystal.tensor_ε_eq_max` in TauCeti/RepresentationTheory/Crystal/Tensor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Crystal/Tensor.lean#L211)
- [Tau Ceti roadmap status: Schubert geometry, Demazure sections and flag K-theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchubertGeometry/STATUS.md)
