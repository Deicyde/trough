---
declaration: theorem
origin: cited
lean: WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero
statement: formalized
proof: formalized
---

# Global reciprocity for the Weil cup product

The finite-place local Tate pairings of
two global torsion-cohomology classes, embedded in `ℚ/ℤ` by `k ↦ k/m`, together with the
archimedean Brauer invariants of their Weil cup product, sum to zero.
The finite-place sum has finite support by
`hasFiniteSupport_localTateWeilPairing_torsionRes`. All choices of embeddings of separable
closures are allowed, independently at each place.

```lean
WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero
  {K : Type} [Field K] [NumberField K] (W : WeierstrassCurve K) [W.IsElliptic] (m : ℕ)
  (hm : IsUnit ↑m)
  (a b : TauCeti.ContCohomology.H1 (TauCeti.AbsoluteGaloisGroup K) (W.TorsionCoeff m))
  (τ :
    (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)) →
      SeparableClosure K →ₐ[K]
        SeparableClosure (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v))
  (τ' :
    (w : NumberField.InfinitePlace K) → SeparableClosure K →ₐ[K] SeparableClosure w.Completion) :
  ∑ᶠ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
        (ZMod.toRatAddCircle m)
          ((((W.baseChange
                    (IsDedekindDomain.HeightOneSpectrum.adicCompletion K v)).localTateWeilPairing
                m ⋯)
              ((W.torsionRes (τ v) m) a))
            ((W.torsionRes (τ v) m) b)) +
      ∑ w,
        (TauCeti.ClassFieldTheory.infiniteInvMap w)
          ((((W.baseChange w.Completion).torsionWeilBrauerPairing m ⋯) ((W.torsionRes (τ' w) m) a))
            ((W.torsionRes (τ' w) m) b)) =
    0
```

## Depends on

- [The local invariant](../../number-theory/part-01/class-field-theory/the-local-invariant.md)

## Proof depends on

- [Artin's theorem](../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [Dedekind's different theorem, the tame case](../../number-theory/part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../group-theory/other-results/part-01/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../number-theory/part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../../number-theory/part-01/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../number-theory/part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Restriction through Shapiro's lemma](../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../number-theory/part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's theorem](../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../../number-theory/part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../../number-theory/part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../number-theory/part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Reciprocity.html#WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Reciprocity.html#WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero)
- [Source of `WeierstrassCurve.finsum_toRatAddCircle_localTateWeilPairing_add_sum_infiniteInvMap_eq_zero` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/WeilPairing/Reciprocity.lean#L76)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EllipticCurves/STATUS.md)
