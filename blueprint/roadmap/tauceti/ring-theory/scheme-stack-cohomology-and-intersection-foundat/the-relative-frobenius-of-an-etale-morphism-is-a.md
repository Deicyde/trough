---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius
statement: formalized
proof: formalized
---

# The relative Frobenius of an étale morphism is an isomorphism

Stacks, Tag 0EBS.

```lean
AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius.{u} {X S : AlgebraicGeometry.Scheme}
  (π : X ⟶ S) (p : ℕ) [Fact (Nat.Prime p)] (hS : ↑p = 0) [AlgebraicGeometry.Etale π] :
  CategoryTheory.IsIso (AlgebraicGeometry.Scheme.Hom.relativeFrobenius π p hS)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Etale.html#AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Etale.html#AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius)
- [Source of `AlgebraicGeometry.Scheme.Hom.isIso_relativeFrobenius` in TauCeti/AlgebraicGeometry/Frobenius/Etale.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Frobenius/Etale.lean#L106)
