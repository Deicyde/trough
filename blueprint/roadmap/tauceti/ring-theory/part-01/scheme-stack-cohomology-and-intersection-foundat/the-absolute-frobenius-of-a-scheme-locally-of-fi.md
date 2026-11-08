---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.isFinite_frobenius
statement: formalized
proof: formalized
---

# The absolute Frobenius of a scheme locally of finite type over a perfect ring is finite

For a scheme `X` locally of finite type over `Spec R`, with `R` a perfect ring of characteristic
`p`, the absolute Frobenius `F_X : X ⟶ X` is a finite morphism.

```lean
AlgebraicGeometry.Scheme.isFinite_frobenius.{u} {X : AlgebraicGeometry.Scheme} {p : ℕ}
  [Fact (Nat.Prime p)] {R : Type u} [CommRing R] [ExpChar R p] [PerfectRing R p]
  (f : X ⟶ AlgebraicGeometry.Spec ↧R) [AlgebraicGeometry.LocallyOfFiniteType f] (hX : ↑p = 0) :
  AlgebraicGeometry.IsFinite (X.frobenius p hX)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.isFinite_frobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Finite.html#AlgebraicGeometry.Scheme.isFinite_frobenius).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.isFinite_frobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Finite.html#AlgebraicGeometry.Scheme.isFinite_frobenius)
- [Source of `AlgebraicGeometry.Scheme.isFinite_frobenius` in TauCeti/AlgebraicGeometry/Frobenius/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Frobenius/Finite.lean#L41)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
