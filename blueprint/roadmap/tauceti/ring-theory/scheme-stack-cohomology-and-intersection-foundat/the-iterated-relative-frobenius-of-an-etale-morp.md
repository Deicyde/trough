---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius
statement: formalized
proof: formalized
---

# The iterated relative Frobenius of an étale morphism is an isomorphism

```lean
AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius.{u} {X S : AlgebraicGeometry.Scheme}
  (π : X ⟶ S) (p : ℕ) [Fact (Nat.Prime p)] (hS : ↑p = 0) [AlgebraicGeometry.Etale π] (n : ℕ) :
  CategoryTheory.IsIso (AlgebraicGeometry.Scheme.Hom.iterateRelativeFrobenius π p hS n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Etale.html#AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Etale.html#AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius)
- [Source of `AlgebraicGeometry.Scheme.Hom.isIso_iterateRelativeFrobenius` in TauCeti/AlgebraicGeometry/Frobenius/Etale.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Frobenius/Etale.lean#L102)
