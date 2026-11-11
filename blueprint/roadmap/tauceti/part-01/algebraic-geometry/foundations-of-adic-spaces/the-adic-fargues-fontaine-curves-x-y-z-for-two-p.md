---
declaration: def
origin: cited
lean: TauCeti.FarguesFontaine.spaXAdicSpaceCongr
statement: formalized
---

# The adic Fargues–Fontaine curves `𝒳 = 𝒴 / φ^ℤ` for two pseudouniformisers are isomorphic

If `ϖ` and `ϖ'` define the same subset `𝒴` of `Spa(𝕎 R, 𝕎 R)`, as they do when they generate ideals
with the same radical (`spaY_eq_of_radical_eq`), and `𝒪_𝒴` is a sheaf, then the isomorphism
`spaXPreAdicSpaceCongr` of pre-adic spaces is an isomorphism in the full subcategory `(Adic)`. It is
the isomorphism induced by `spaYAdicSpaceCongr` on the quotients by Frobenius
(`quotientAdicHom_comp_spaXAdicSpaceCongr_hom`), and on points it is the homeomorphism
`spaXCongr` of orbit spaces (`spaXPreAdicSpaceCongr_hom_base`). When `R` is perfect of
characteristic `p` and is the ring of integers of a valuation `v` on a field, and `0 < v(ϖ) < 1`,
`𝒪_𝒴` is a sheaf by `isSheaf_spaYPresheaf`.

```lean
TauCeti.FarguesFontaine.spaXAdicSpaceCongr.{v} {p : ℕ} [Fact (Nat.Prime p)] {R : Type v}
  [CommRing R] {ϖ ϖ' : R} [TopologicalSpace (WittVector p R)] [CharP R p] [PerfectRing R p]
  [IsTopologicalRing (WittVector p R)] (P : TauCeti.Huber.PairOfDefinition (WittVector p R))
  (hI : IsAdic (Ideal.span {↑p, (WittVector.teichmuller p) ϖ}))
  (hI' : IsAdic (Ideal.span {↑p, (WittVector.teichmuller p) ϖ'}))
  (h : TauCeti.FarguesFontaine.spaY p ϖ = TauCeti.FarguesFontaine.spaY p ϖ')
  (hY : (TauCeti.FarguesFontaine.spaYPresheaf P ϖ).IsSheaf) :
  TauCeti.FarguesFontaine.spaXAdicSpace P hI hY ≅ TauCeti.FarguesFontaine.spaXAdicSpace P hI' ⋯
```

## Depends on

- [Adic spaces (Wedhorn, Definition 8.22)](adic-spaces-wedhorn-definition-8-22.md)

## Proof depends on

- [Ideals contained in supports](ideals-contained-in-supports.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FarguesFontaine.spaXAdicSpaceCongr`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Pseudouniformizer.html#TauCeti.FarguesFontaine.spaXAdicSpaceCongr).

## Sources

- [Tau Ceti documentation: `TauCeti.FarguesFontaine.spaXAdicSpaceCongr`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Pseudouniformizer.html#TauCeti.FarguesFontaine.spaXAdicSpaceCongr)
- [Source of `TauCeti.FarguesFontaine.spaXAdicSpaceCongr` in TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Pseudouniformizer.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Pseudouniformizer.lean#L417)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/AdicSpaces/STATUS.md)
