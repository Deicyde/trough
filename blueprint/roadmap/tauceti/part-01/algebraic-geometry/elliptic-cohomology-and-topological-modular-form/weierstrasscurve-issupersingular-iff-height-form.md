---
declaration: theorem
origin: cited
lean: WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three
statement: formalized
proof: formalized
---

# WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three

In characteristic three, an elliptic curve is supersingular exactly when its formal group
has height two.

```lean
WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three.{u_1} {K : Type u_1}
  [Field K] [CharP K 3] (W : WeierstrassCurve K) [W.IsElliptic] :
  WeierstrassCurve.IsSupersingular 3 W ↔ W.formalGroup.height 3 = 2
```

## Depends on

- [FormalGroup.height](../../ring-theory/part-01/bordism-formal-groups-and-chromatic-operations/formalgroup-height.md)

## Proof depends on

- [The `p`-series has order a power of `p` in characteristic `p`](../../ring-theory/part-01/bordism-formal-groups-and-chromatic-operations/the-p-series-has-order-a-power-of-p-in-character.md)
- [The height-one criterion for `Ê`](the-height-one-criterion-for-e.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Char/Three.html#WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Char/Three.html#WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three)
- [Source of `WeierstrassCurve.isSupersingular_iff_height_formalGroup_eq_two_of_char_three` in TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Char/Three.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/FormalGroup/Char/Three.lean#L201)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCohomology/STATUS.md)
