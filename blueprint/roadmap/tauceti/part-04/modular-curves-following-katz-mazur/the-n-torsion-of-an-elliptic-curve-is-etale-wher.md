---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero
statement: formalized
proof: formalized
---

# The `n`-torsion of an elliptic curve is étale where `n` is invertible

(Katz–Mazur 2.3.1).
For an elliptic curve `E` over a scheme `S` and an integer `n` invertible in every residue field of
`S`, the `n`-torsion `E[n]` is étale over `S`. It is also finite over `S`
(`EllipticCurveGeom.isFinite_torsion_hom`), so `E[n]` is finite étale over `S`.

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero.{u}
  {S : AlgebraicGeometry.Scheme} (E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S) {n : ℤ}
  (hn : ∀ (s : ↥S), ↑n ≠ 0) : AlgebraicGeometry.Etale (E.torsion n).X.hom
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Torsion/Etale/Locus.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Torsion/Etale/Locus.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero)
- [Source of `TauCeti.AlgebraicGeometry.EllipticCurveGeom.etale_torsion_hom_of_forall_intCast_ne_zero` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Torsion/Etale/Locus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/Torsion/Etale/Locus.lean#L85)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
