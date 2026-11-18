---
declaration: theorem
origin: cited
lean: WeierstrassCurve.Universal.height_span_c₄_Δ
statement: formalized
proof: formalized
---

# WeierstrassCurve.Universal.height_span_c₄_Δ

The cuspidal locus `V(c₄, Δ)` of the universal Weierstrass curve has codimension two in
`Spec ℤ[a₁, a₂, a₃, a₄, a₆]`.

```lean
WeierstrassCurve.Universal.height_span_c₄_Δ :
  (Ideal.span
        {WeierstrassCurve.c₄ WeierstrassCurve.Universal.curve,
          WeierstrassCurve.Δ WeierstrassCurve.Universal.curve}).height =
    2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.Universal.height_span_c₄_Δ`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/CuspidalLocus.html#WeierstrassCurve.Universal.height_span_c%E2%82%84_%CE%94).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.Universal.height_span_c₄_Δ`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/CuspidalLocus.html#WeierstrassCurve.Universal.height_span_c%E2%82%84_%CE%94)
- [Source of `WeierstrassCurve.Universal.height_span_c₄_Δ` in TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/CuspidalLocus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Invariants/CuspidalLocus.lean#L118)
- [Tau Ceti roadmap status: Elliptic cohomology and topological modular forms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCohomology/STATUS.md)
