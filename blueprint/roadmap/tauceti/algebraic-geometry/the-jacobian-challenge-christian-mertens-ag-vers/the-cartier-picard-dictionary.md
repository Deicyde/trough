---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass
statement: formalized
---

# The Cartier–Picard dictionary

On any integral scheme, Cartier divisors modulo
principal divisors form the Picard group of line-bundle classes under tensor product.

```lean
TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass.{u}
  (X : AlgebraicGeometry.Scheme) [AlgebraicGeometry.IsIntegral X] :
  TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.ClassGroup X ≃+
    Additive (TauCeti.AlgebraicGeometry.LineBundleClass X)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/CartierDivisor/ClassGroup.html#TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/CartierDivisor/ClassGroup.html#TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass)
- [Source of `TauCeti.AlgebraicGeometry.Scheme.CartierDivisor.classGroupAddEquivLineBundleClass` in TauCeti/AlgebraicGeometry/CartierDivisor/ClassGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/CartierDivisor/ClassGroup.lean#L121)
- [Tau Ceti roadmap status: The Jacobian challenge (Christian Merten's AG version)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/JacobianChallenge/STATUS.md)
