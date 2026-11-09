---
declaration: theorem
origin: cited
lean: WeierstrassCurve.localTateWeilPairing_bijective, TauCeti.Isogeny.localTateKerWeilPairing_bijective
statement: formalized
proof: formalized
---

# Perfect local Tate duality for `E[m]`

Pairing with a class gives a bijection from
`H¹(K, E[m])` to its additive characters with values in `ℤ/m`.

```lean
WeierstrassCurve.localTateWeilPairing_bijective {K : Type} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] (W : WeierstrassCurve K) [W.IsElliptic]
  (m : ℕ) (hm : IsUnit ↑m) : Function.Bijective ⇑(W.localTateWeilPairing m hm)
```

## Depends on

- [The local invariant](../../../number-theory/part-01/class-field-theory/the-local-invariant.md)

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../../ring-theory/part-02/other-results/part-01/krull-akizuki-for-mathlibs-integralclosure.md)
- [Local Tate duality in degree one](../../../number-theory/part-02/class-field-theory/local-tate-duality-in-degree-one.md)
- [Riemann's theorem](../../../field-theory/algebraic-curves-function-fields-divisors-and-ri/riemanns-theorem.md)
- [TauCeti.Ring.IsJapanese](../../../ring-theory/part-01/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.localTateWeilPairing_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Local.html#WeierstrassCurve.localTateWeilPairing_bijective).

## Other forms

**Perfect local Tate duality for the kernels of an isogeny and of its dual.** Formalized in Tau Ceti as [`TauCeti.Isogeny.localTateKerWeilPairing_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Local.html#TauCeti.Isogeny.localTateKerWeilPairing_bijective).

```lean
TauCeti.Isogeny.localTateKerWeilPairing_bijective {K : Type} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic]
  [W₂.IsElliptic] (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine) (hn : IsUnit ↑φ.degree) :
  Function.Bijective ⇑(φ.localTateKerWeilPairing hn)
```

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.localTateWeilPairing_bijective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Local.html#WeierstrassCurve.localTateWeilPairing_bijective)
- [Source of `WeierstrassCurve.localTateWeilPairing_bijective` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Local.lean#L70)
