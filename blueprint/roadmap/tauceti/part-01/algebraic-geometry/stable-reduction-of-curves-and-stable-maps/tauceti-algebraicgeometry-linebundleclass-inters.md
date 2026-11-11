---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber
statement: formalized
---

# TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber

The **intersection number** `(a · C)` of a line-bundle class `a` on `X` with a scheme `C` over
the field `k` mapping to `X` by `ι`: the Euler-characteristic degree over `k` of the pullback of
`a` to `C`. For a proper curve `C` this is the degree of the restriction of `a` to `C`.

```lean
TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber.{u} (k : Type u) [Field k]
  {X C : AlgebraicGeometry.Scheme} [C.Over (AlgebraicGeometry.Spec ↧k)] (ι : C ⟶ X)
  (a : TauCeti.AlgebraicGeometry.LineBundleClass X) : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Basic.html#TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Basic.html#TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber)
- [Source of `TauCeti.AlgebraicGeometry.LineBundleClass.intersectionNumber` in TauCeti/AlgebraicGeometry/IntersectionNumber/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/IntersectionNumber/Basic.lean#L129)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StableReduction/STATUS.md)
