---
declaration: theorem
origin: cited
lean: TauCeti.FarguesFontaine.isSheaf_spaYPresheaf
statement: formalized
proof: formalized
---

# `𝒪_𝒴` is a sheaf

let `R` be the ring of integers of a valuation `v` on a field `K`,
perfect of characteristic `p`, and `ϖ ∈ R` with `0 < v(ϖ) < 1`; for `R = 𝒪_F` this is the
Fargues–Fontaine space `𝒴 ⊆ Spa(A_inf, A_inf)`. Then the structure presheaf `𝒪_𝒴` is a sheaf, so
`𝒴` and `𝒳 = 𝒴 / φ^ℤ` are adic spaces (`isAdic_spaYPreAdicSpace_iff`, `isAdic_spaXPreAdicSpace`).
The window `W_n = {p ^ (-n) ≤ κ ≤ p ^ n}` is `Spa(B^I, B^{I,+})` for
`I = [v(ϖ) ^ (p ^ n), v(ϖ) ^ (p ^ (-n))]` (`TauCeti.FarguesFontaine.windowPreAdicSpaceIso`), and
this pair is sheafy because `B^I` is strongly noetherian (Kedlaya's Theorem 4.10), so `𝒪_𝒴` is
sheafy on each window (`isSheafy_spaYPreAdicSpace_restrict`), and hence a sheaf
(`isSheaf_spaYPresheaf_of_isSheafy_restrict`).

```lean
TauCeti.FarguesFontaine.isSheaf_spaYPresheaf.{v, u_1} {p : ℕ} [Fact (Nat.Prime p)] {R : Type v}
  [CommRing R] [TopologicalSpace (WittVector p R)] [IsTopologicalRing (WittVector p R)] {ϖ : R}
  {P : TauCeti.Huber.PairOfDefinition (WittVector p R)}
  (hI : IsAdic (Ideal.span {↑p, (WittVector.teichmuller p) ϖ})) [CharP R p] [PerfectRing R p]
  {K : Type u_1} [Field K] [Algebra R K] {v : Valuation K NNReal} (hv : v.Integers R) (hϖ : ϖ ≠ 0)
  (hϖ' : v ((algebraMap R K) ϖ) < 1) : (TauCeti.FarguesFontaine.spaYPresheaf P ϖ).IsSheaf
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.PreAdicSpace.isAdic](tauceti-preadicspace-isadic.md)
- [TauCeti.WittVector.isStronglyNoetherian\_intervalRing](tauceti-wittvector-isstronglynoetherian-interval.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FarguesFontaine.isSheaf_spaYPresheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Adic.html#TauCeti.FarguesFontaine.isSheaf_spaYPresheaf).

## Sources

- [Tau Ceti documentation: `TauCeti.FarguesFontaine.isSheaf_spaYPresheaf`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Adic.html#TauCeti.FarguesFontaine.isSheaf_spaYPresheaf)
- [Source of `TauCeti.FarguesFontaine.isSheaf_spaYPresheaf` in TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Adic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/AdicSpace/FarguesFontaine/Adic.lean#L149)
- [Tau Ceti roadmap status: Foundations of adic spaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/AdicSpaces/STATUS.md)
