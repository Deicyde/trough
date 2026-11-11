---
declaration: theorem
origin: cited
lean: TauCeti.isIntegralClosure_abhyankarModel
statement: formalized
proof: formalized
---

# The Abhyankar model is the integral closure of `B` away from `ϖ`

Let `ϖ` be a
nonzerodivisor of `B` with `B ⧸ (ϖ)` reduced, let `u` be a unit and `e` invertible in `B`, and
`d ≠ 0`. Then `(B[y]/(y ^ e − u))[x]/(x ^ d − ϖ y)` is the integral closure of `B` in its
localization away from `ϖ`. This applies to a discrete valuation ring `B` with uniformizer `ϖ`.

```lean
TauCeti.isIntegralClosure_abhyankarModel.{u, u_1} {B : Type u} [CommRing B] {ϖ u : B} {e d : ℕ}
  (Dϖ : Type u_1) [CommRing Dϖ] [Algebra (TauCeti.abhyankarModel ϖ u e d) Dϖ]
  [IsLocalization.Away ((algebraMap B (TauCeti.abhyankarModel ϖ u e d)) ϖ) Dϖ] [Algebra B Dϖ]
  [IsScalarTower B (TauCeti.abhyankarModel ϖ u e d) Dϖ] [IsReduced (B ⧸ Ideal.span {ϖ})]
  (hϖ : ϖ ∈ nonZeroDivisors B) (hu : IsUnit u) (he : IsUnit ↑e) (hd : d ≠ 0) :
  IsIntegralClosure (TauCeti.abhyankarModel ϖ u e d) B Dϖ
```

## Depends on

- [TauCeti.abhyankarModel](tauceti-abhyankarmodel.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIntegralClosure_abhyankarModel`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.html#TauCeti.isIntegralClosure_abhyankarModel).

## Sources

- [Tau Ceti documentation: `TauCeti.isIntegralClosure_abhyankarModel`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.html#TauCeti.isIntegralClosure_abhyankarModel)
- [Source of `TauCeti.isIntegralClosure_abhyankarModel` in TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean#L549)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
