---
declaration: def
origin: cited
lean: TauCeti.Isogeny.selmerGroup
statement: formalized
---

# The `φ`-Selmer group

**The `φ`-Selmer group** of the isogeny `φ : W₁ → W₂` relative to the family of extensions
`L i` with embeddings `τ i`: the Selmer group of `selmerStructure φ τ`, that is, the classes in
`H¹(G_K, E₁(Kˢ)[φ])` whose image in `H¹(G_K, E₁(Kˢ))` lies in the Shafarevich–Tate group of `W₁`
(`TauCeti.Isogeny.mem_selmerGroup_iff`). For a number field and the family of its completions at
all places this is `Sel_φ(E₁/K)` (Silverman X.4).

```lean
TauCeti.Isogeny.selmerGroup.{u_1, u_2, u_3} {K : Type u_1} [Field K] {W₁ W₂ : WeierstrassCurve K}
  [W₁.IsElliptic] [W₂.IsElliptic] {ι : Type u_2} {L : ι → Type u_3} [(i : ι) → Field (L i)]
  [(i : ι) → Algebra K (L i)] (φ : TauCeti.Isogeny W₁.toAffine W₂.toAffine)
  (τ : (i : ι) → SeparableClosure K →ₐ[K] SeparableClosure (L i)) :
  AddSubgroup
    (TauCeti.ContCohomology.H1 (TauCeti.AbsoluteGaloisGroup K)
      (TauCeti.Isogeny.Hom.ofIsogeny φ).KerCoeff)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Dedekind's different theorem, first part (Stichtenoth, Theorem 3.5.1(a))](../../field-theory/function-field/part-01/dedekinds-different-theorem-first-part-stichteno.md)
- [The factorisation theorem for isogenies (Silverman II.2.12)](../elliptic-curve/the-factorisation-theorem-for-isogenies-silverma.md)
- [The fundamental identity](../../field-theory/function-field/part-01/the-fundamental-identity.md)
- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../../field-theory/function-field/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [The Hurwitz genus formula (Stichtenoth, Theorem 3.4.13)](../algebraic-curves-function-fields-divisors-and-ri/the-hurwitz-genus-formula-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [Vieta's formula at a pair of parameters, cleared of the inverse of the cubic's leading coefficient](../elliptic-curve/vietas-formula-at-a-pair-of-parameters-cleared-o.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Isogeny.selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Basic.html#TauCeti.Isogeny.selmerGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.Isogeny.selmerGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Basic.html#TauCeti.Isogeny.selmerGroup)
- [Source of `TauCeti.Isogeny.selmerGroup` in TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/EllipticCurve/GaloisCohomology/Selmer/Isogeny/Basic.lean#L148)
- [Tau Ceti roadmap status: Elliptic curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticCurves/STATUS.md)
