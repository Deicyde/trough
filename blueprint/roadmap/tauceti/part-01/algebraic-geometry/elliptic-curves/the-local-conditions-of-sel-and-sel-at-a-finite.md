---
declaration: theorem
origin: cited
lean: TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual
statement: formalized
proof: formalized
---

# The local conditions of `Sel_φ` and `Sel_φ̂` at a finite place

if `n = deg φ` is nonzero
in `K`, then at every finite place `v`, including those dividing `n`,

`#H¹_φ(K_v) · #H¹_φ̂(K_v) = #E₁(K_v)[φ] · #E₂(K_v)[φ̂] · #(O_v ⧸ n O_v)`.

So the product of the local factors `#H¹_φ(K_v) / #E₁(K_v)[φ]` of `φ` and of its dual is the
inverse of the normalised absolute value of `n` at `v`.

```lean
TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual.{u_1, u_2}
  (R : Type u_1) [CommRing R] [IsDedekindDomain R] {K : Type u_2} [Field K] [Algebra R K]
  [IsFractionRing R K] [∀ (v : IsDedekindDomain.HeightOneSpectrum R), Finite (R ⧸ v.asIdeal)]
  [(v : IsDedekindDomain.HeightOneSpectrum R) →
      DecidableEq (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)]
  {W₁ W₂ : WeierstrassCurve K} [W₁.IsElliptic] [W₂.IsElliptic]
  (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine)
  (τ :
    (v : IsDedekindDomain.HeightOneSpectrum R) →
      SeparableClosure K →ₐ[K]
        SeparableClosure (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v))
  (hφ : ↑φ.degree ≠ 0) (v : IsDedekindDomain.HeightOneSpectrum R) :
  Nat.card ↥((φ.selmerStructure τ).localCondition v) *
      Nat.card ↥((φ.dual.selmerStructure τ).localCondition v) =
    Nat.card
          ↥(TauCeti.Isogeny.Hom.ofIsogeny
                  (TauCeti.Isogeny.baseChange
                    (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v) φ)).pointMapHom.ker *
        Nat.card
          ↥(TauCeti.Isogeny.Hom.ofIsogeny
                  (TauCeti.Isogeny.baseChange
                    (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)
                    φ.dual)).pointMapHom.ker *
      Nat.card
        (↥(IsDedekindDomain.HeightOneSpectrum.adicCompletionIntegers K v) ⧸ Ideal.span {↑φ.degree})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem](../elliptic-curve/the-factorisation-theorem.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Hensel's lemma without monicity](../../ring-theory/part-02/other-results/part-01/hensels-lemma-without-monicity.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [The kernel form of the factorisation theorem (Silverman III.4.11)](../elliptic-curve/the-kernel-form-of-the-factorisation-theorem-sil.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Local.html#TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Local.html#TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual)
- [Source of `TauCeti.Isogeny.natCard_localCondition_selmerStructure_mul_natCard_localCondition_dual` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Local.lean#L195)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
