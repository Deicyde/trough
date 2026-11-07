---
declaration: theorem
origin: cited
lean: LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd
statement: formalized
proof: formalized
---

# Classification of odd unimodular forms over `ℤ_[2]`

Let `B` and `C` be symmetric forms
over `ℤ_[2]` with unit Gram determinants in bases of the same size, each representing a unit, and
let `w` and `w'` be characteristic vectors for `B` and `C`. Then `B` and `C` are isometric exactly
when the product of their Gram determinants is a square and `B w w ≡ C w' w'` modulo `8`.

The second condition says that the oddities of `B` and `C` agree.

```lean
LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd.{u_1, u_2}
  {M : Type u_1} {N : Type u_2} [AddCommGroup M] [_root_.Module ℤ_[2] M] [AddCommGroup N]
  [_root_.Module ℤ_[2] N] {B : LinearMap.BilinForm ℤ_[2] M} {C : LinearMap.BilinForm ℤ_[2] N}
  (hB : B.IsSymm) (hC : C.IsSymm) {n : ℕ} (b : Module.Basis (Fin n) ℤ_[2] M)
  (c : Module.Basis (Fin n) ℤ_[2] N) (hBdet : IsUnit ((LinearMap.BilinForm.toMatrix b) B).det)
  (hCdet : IsUnit ((LinearMap.BilinForm.toMatrix c) C).det) (hBodd : ∃ x, IsUnit ((B x) x))
  (hCodd : ∃ y, IsUnit ((C y) y)) {w : M} {w' : N} (hw : B.IsCharacteristic w)
  (hw' : C.IsCharacteristic w') :
  B.Equivalent C ↔
    IsSquare (((LinearMap.BilinForm.toMatrix b) B).det * ((LinearMap.BilinForm.toMatrix c) C).det) ∧
      8 ∣ (C w') w' - (B w) w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/BilinearForm/OddUnimodular.html#LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd).

## Sources

- [Tau Ceti documentation: `LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/BilinearForm/OddUnimodular.html#LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd)
- [Source of `LinearMap.BilinForm.IsSymm.equivalent_iff_isSquare_det_mul_det_and_eight_dvd_of_odd` in TauCeti/NumberTheory/Padics/BilinearForm/OddUnimodular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/BilinearForm/OddUnimodular.lean#L399)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/IntegralLattices/STATUS.md)
