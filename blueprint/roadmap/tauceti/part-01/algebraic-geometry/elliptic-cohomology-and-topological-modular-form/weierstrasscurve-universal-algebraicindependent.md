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
- [Source of `WeierstrassCurve.Universal.algebraicIndependent_c₄_c₆` in TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/AlgebraicIndependent.lean#L35)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
