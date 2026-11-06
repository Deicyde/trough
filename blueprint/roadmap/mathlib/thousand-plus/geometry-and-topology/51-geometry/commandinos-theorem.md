---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: Affine.Simplex.point_vsub_centroid_eq_smul_vsub
mathlib_file: Mathlib/LinearAlgebra/AffineSpace/Simplex/Centroid.lean
---

# Commandino's theorem

*Commandino's theorem* : For n-simplex, the vector from a vertex to the `centroid`
equals `n` times the vector from the `centroid` to the corresponding `faceOppositeCentroid`.

```lean
Affine.Simplex.point_vsub_centroid_eq_smul_vsub.{u_1, u_2, u_3} {k : Type u_1} {V : Type u_2}
  {P : Type u_3} [DivisionRing k] [AddCommGroup V] [_root_.Module k V] [AddTorsor V P] {n : ℕ}
  [NeZero n] [CharZero k] (s : Affine.Simplex k P n) (i : Fin (n + 1)) :
  s.points i -ᵥ s.centroid = ↑n • (s.centroid -ᵥ s.faceOppositeCentroid i)
```

## Depends on

- [Barycenter](../../../overview/geometry/affine-and-euclidean-geometry/barycenter.md)
- [Characteristic zero](../../../overview/general-algebra/field-theory/characteristic-zero.md)
- [Rational number](../../../overview/general-algebra/numbers/rational-number.md)

## Sources

- [Mathlib documentation: `Affine.Simplex.point_vsub_centroid_eq_smul_vsub`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/AffineSpace/Simplex/Centroid.html#Affine.Simplex.point_vsub_centroid_eq_smul_vsub)
- [Source of `Affine.Simplex.point_vsub_centroid_eq_smul_vsub` in Mathlib/LinearAlgebra/AffineSpace/Simplex/Centroid.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/AffineSpace/Simplex/Centroid.lean#L345)
- [1000+ theorems list: Q2226625](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/1000.yaml#L2049)
- [1000+ theorems project: Q2226625](https://1000-plus.github.io/all.html?length=-1#Q2226625)
- [Wikipedia: Commandino's theorem](https://en.wikipedia.org/wiki/Commandino's_theorem)
- [Wikidata: Q2226625](https://www.wikidata.org/wiki/Q2226625)
