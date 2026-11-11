---
declaration: def
origin: cited
lean: TauCeti.Montgomery.model
statement: formalized
---

# TauCeti.Montgomery.model

The **monic model** of the Montgomery curve `B y² = x³ + A x² + x`: the Weierstrass curve
`y² = x³ + A B x² + B² x`, reached by `x' = B x`, `y' = B² y`. Its coefficients are
`(a₁, a₂, a₃, a₄, a₆) = (0, A B, 0, B², 0)`.

```lean
TauCeti.Montgomery.model.{u_1} {R : Type u_1} [CommRing R] (A B : R) : WeierstrassCurve R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Montgomery.model`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Basic.html#TauCeti.Montgomery.model).

## Sources

- [Tau Ceti documentation: `TauCeti.Montgomery.model`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Basic.html#TauCeti.Montgomery.model)
- [Source of `TauCeti.Montgomery.model` in TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Montgomery/Basic.lean#L79)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
