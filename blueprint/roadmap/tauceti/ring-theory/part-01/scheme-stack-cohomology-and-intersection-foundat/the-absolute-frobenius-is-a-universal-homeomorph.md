---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius
statement: formalized
proof: formalized
---

# The absolute Frobenius is a universal homeomorphism

every base change of `F_X` is a
homeomorphism of underlying spaces.

```lean
AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius.{u} {X : AlgebraicGeometry.Scheme}
  {p : ℕ} [Fact (Nat.Prime p)] (hX : ↑p = 0) :
  (AlgebraicGeometry.topologically @IsHomeomorph).universally (X.frobenius p hX)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/UniversalHomeomorphism.html#AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/UniversalHomeomorphism.html#AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius)
- [Source of `AlgebraicGeometry.Scheme.universally_isHomeomorph_frobenius` in TauCeti/AlgebraicGeometry/Frobenius/UniversalHomeomorphism.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Frobenius/UniversalHomeomorphism.lean#L103)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
