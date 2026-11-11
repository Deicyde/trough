---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.bijective_comp_fromPerfection
statement: formalized
proof: formalized
---

# The universal property of the perfection

For a perfect scheme `T`, composition with the
structure morphism `X^perf ⟶ X` is a bijection from morphisms `T ⟶ X^perf` to morphisms
`T ⟶ X`. Thus the perfection is a coreflection of `X` into perfect schemes.

```lean
AlgebraicGeometry.Scheme.bijective_comp_fromPerfection.{u} {X : AlgebraicGeometry.Scheme} {p : ℕ}
  [Fact (Nat.Prime p)] {hX : ↑p = 0} {T : AlgebraicGeometry.Scheme} [T.IsPerfect p] :
  Function.Bijective fun g => CategoryTheory.CategoryStruct.comp g (X.fromPerfection p hX)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.bijective_comp_fromPerfection`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Perfection.html#AlgebraicGeometry.Scheme.bijective_comp_fromPerfection).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.bijective_comp_fromPerfection`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Frobenius/Perfection.html#AlgebraicGeometry.Scheme.bijective_comp_fromPerfection)
- [Source of `AlgebraicGeometry.Scheme.bijective_comp_fromPerfection` in TauCeti/AlgebraicGeometry/Frobenius/Perfection.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Frobenius/Perfection.lean#L416)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
