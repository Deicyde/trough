---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero
statement: formalized
proof: formalized
---

# TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero

The local Tate pairing of the Kummer classes for an isogeny and its dual vanishes,
with no restriction on the residue characteristic.

```lean
TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero {K : Type} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [DecidableEq K]
  {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic] [W₂.IsElliptic]
  (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine) (hn : IsUnit ↑φ.degree) (Q : W₂.toAffine.Point)
  (P : W₁.toAffine.Point) :
  ((φ.localTateKerWeilPairing hn) (φ.kummerMap Q)) (φ.dual.kummerMap P) = 0
```

## Depends on

- [The local invariant](../../number-theory/part-01/class-field-theory/the-local-invariant.md)

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Orthogonality.html#TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Orthogonality.html#TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero)
- [Source of `TauCeti.Isogeny.localTateKerWeilPairing_kummerMap_kummerMap_eq_zero` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Orthogonality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Orthogonality.lean#L102)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)
