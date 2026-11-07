---
declaration: theorem
origin: cited
lean: TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens
statement: formalized
proof: formalized
---

# The image in `𝒳` of a wandering window is an open affinoid subspace

Let `O` be the ring of
integers of `v`, perfect of characteristic `p`, with pseudouniformiser `ϖ`, and suppose `𝒪_𝒴` is a
sheaf. If `0 < q ≤ q'` and the window `W = {v ∈ 𝒴 : q ≤ κ(v) ≤ q'}` meets none of its nontrivial
integer Frobenius translates, then `𝒳` restricted to `q(W)` is affinoid: it is isomorphic to
`Spa(B^I, B^{I,+})` for the interval `I = [v(ϖ) ^ (1 / q), v(ϖ) ^ (1 / q')]`, through the window
chart `spaXWindowChart`.

```lean
TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens.{u, u_1} {p : ℕ}
  [Fact (Nat.Prime p)] {O : Type u} [CommRing O] {ϖ : O} {q q' : ℚ≥0} {K : Type u_1} [Field K]
  [Algebra O K] {v : Valuation K NNReal} [CharP O p] [PerfectRing O p] (hv : v.Integers O)
  (hϖ : ϖ ≠ 0) (hϖ' : v ((algebraMap O K) ϖ) < 1) [TopologicalSpace (WittVector p O)]
  [IsTopologicalRing (WittVector p O)] {hI : IsAdic (Ideal.span {↑p, (WittVector.teichmuller p) ϖ})}
  {P : TauCeti.Huber.PairOfDefinition (WittVector p O)}
  (hY : (TauCeti.FarguesFontaine.spaYPresheaf P ϖ).IsSheaf) (hq : q ≠ 0) (hqq' : q ≤ q')
  (hW :
    ∀ (k : ℤ),
      k ≠ 0 →
        Disjoint
          (⇑(TauCeti.FarguesFontaine.frobeniusHomeomorph hI ^ k) ⁻¹'
            Subtype.val ⁻¹'
              {v |
                v ∈ TauCeti.FarguesFontaine.spaY p ϖ ∧
                  TauCeti.FarguesFontaine.IsRadiusLowerBound p ϖ q v ∧
                    TauCeti.FarguesFontaine.IsRadiusUpperBound p ϖ q' v})
          (Subtype.val ⁻¹'
            {v |
              v ∈ TauCeti.FarguesFontaine.spaY p ϖ ∧
                TauCeti.FarguesFontaine.IsRadiusLowerBound p ϖ q v ∧
                  TauCeti.FarguesFontaine.IsRadiusUpperBound p ϖ q' v})) :
  {
      carrier :=
        TauCeti.FarguesFontaine.quotientMap hI ''
          Subtype.val ⁻¹'
            {v |
              v ∈ TauCeti.FarguesFontaine.spaY p ϖ ∧
                TauCeti.FarguesFontaine.IsRadiusLowerBound p ϖ q v ∧
                  TauCeti.FarguesFontaine.IsRadiusUpperBound p ϖ q' v},
      is_open' := ⋯ } ∈
    (TauCeti.FarguesFontaine.spaXPreAdicSpace P hI hY).affinoidOpens
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/QuotientChart.html#TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens).

## Sources

- [Tau Ceti documentation: `TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/QuotientChart.html#TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens)
- [Source of `TauCeti.FarguesFontaine.quotientMap_image_window_mem_affinoidOpens` in TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/QuotientChart.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/QuotientChart.lean#L320)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
