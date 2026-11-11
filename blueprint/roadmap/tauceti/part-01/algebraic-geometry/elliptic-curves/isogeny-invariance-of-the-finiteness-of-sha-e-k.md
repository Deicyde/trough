---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.Hom.finite_sha_iff
statement: formalized
proof: formalized
---

# Isogeny invariance of the finiteness of `Sha(E/K)` over a number field `K`

for a nonzero
morphism `f : W₁ → W₂` over `K`, the Shafarevich–Tate group of `W₁` is finite if and only if that
of `W₂` is, local triviality being required at every finite and infinite place.

```lean
TauCeti.Isogeny.Hom.finite_sha_iff.{u_4} {K : Type u_4} [Field K] [NumberField K]
  {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic] [W₂.IsElliptic]
  (f : TauCeti.Isogeny.Hom W₁.toAffine W₂.toAffine) (hf : f ≠ 0) : Finite ↥W₁.sha ↔ Finite ↥W₂.sha
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `m`-Selmer group of an elliptic curve over a number field is finite (Silverman X.4.2)](the-m-selmer-group-of-an-elliptic-curve-over-a-n.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.Hom.finite_sha_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Sha.html#TauCeti.Isogeny.Hom.finite_sha_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.Hom.finite_sha_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Sha.html#TauCeti.Isogeny.Hom.finite_sha_iff)
- [Source of `TauCeti.Isogeny.Hom.finite_sha_iff` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Sha.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Isogeny/Sha.lean#L210)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
