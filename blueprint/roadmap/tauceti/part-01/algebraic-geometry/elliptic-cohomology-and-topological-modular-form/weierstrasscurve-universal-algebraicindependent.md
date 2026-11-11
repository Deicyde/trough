---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆
statement: formalized
proof: formalized
---

# WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆

The two `c`-invariants of the universal Weierstrass equation satisfy no nonzero polynomial
relation with integer coefficients. In particular, the relation involving the discriminant
does not impose a relation on `c₄` and `c₆` alone.

```lean
WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆ :
  AlgebraicIndependent ℤ
    ![WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
      WeierstrassCurve.c₆ WeierstrassCurve.Universal.curve]
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.html#WeierstrassCurve.Universal.algebraicIndependent_c%E2%82%84_c%E2%82%86).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.html#WeierstrassCurve.Universal.algebraicIndependent_c%E2%82%84_c%E2%82%86)
- [Source of `WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆` in TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.lean#L35)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCohomology/STATUS.md)
