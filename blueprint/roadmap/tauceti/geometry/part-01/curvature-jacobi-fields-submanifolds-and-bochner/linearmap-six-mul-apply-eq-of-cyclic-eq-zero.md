---
declaration: theorem
origin: cited
lean: LinearMap.six_mul_apply_eq_of_cyclic_eq_zero
statement: formalized
proof: formalized
---

# LinearMap.six_mul_apply_eq_of_cyclic_eq_zero

The polarization identity for curvature-type tensors: for a quadrilinear form `T`
antisymmetric in its first and in its last pair of arguments and satisfying the first Bianchi
identity, `6 T(x, y, z, w)` is an explicit combination of values `T(a, b, b, a)`. This recovers
`T` itself only when multiplication by `6` is injective, see `LinearMap.eq_of_cyclic_eq_zero`.

```lean
LinearMap.six_mul_apply_eq_of_cyclic_eq_zero.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommRing R]
  [AddCommGroup M] [_root_.Module R M] {T : M →ₗ[R] M →ₗ[R] M →ₗ[R] M →ₗ[R] R}
  (h₁ : ∀ (x y z w : M), (((T x) y) z) w = -(((T y) x) z) w)
  (h₂ : ∀ (x y z w : M), (((T x) y) z) w = -(((T x) y) w) z)
  (h₃ : ∀ (x y z w : M), (((T x) y) z) w + (((T y) z) x) w + (((T z) x) y) w = 0) (x y z w : M) :
  6 * (((T x) y) z) w =
    (((T (x + w)) (y + z)) (y + z)) (x + w) - (((T (x + z)) (y + w)) (y + w)) (x + z) -
                            (((T x) (y + z)) (y + z)) x -
                          (((T w) (y + z)) (y + z)) w +
                        (((T x) (y + w)) (y + w)) x +
                      (((T z) (y + w)) (y + w)) z -
                    (((T (x + w)) y) y) (x + w) +
                  (((T (x + z)) y) y) (x + z) -
                (((T (x + w)) z) z) (x + w) +
              (((T (x + z)) w) w) (x + z) +
            (((T w) y) y) w -
          (((T z) y) y) z +
        (((T x) z) z) x -
      (((T x) w) w) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.six_mul_apply_eq_of_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Multilinear/SectionalPolarization.html#LinearMap.six_mul_apply_eq_of_cyclic_eq_zero).

## Sources

- [Tau Ceti documentation: `LinearMap.six_mul_apply_eq_of_cyclic_eq_zero`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Multilinear/SectionalPolarization.html#LinearMap.six_mul_apply_eq_of_cyclic_eq_zero)
- [Source of `LinearMap.six_mul_apply_eq_of_cyclic_eq_zero` in TauCeti/LinearAlgebra/Multilinear/SectionalPolarization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/Multilinear/SectionalPolarization.lean#L58)
- [Tau Ceti roadmap status: Curvature, Jacobi fields, submanifolds, and Bochner geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RiemannianGeometry/STATUS.md)
