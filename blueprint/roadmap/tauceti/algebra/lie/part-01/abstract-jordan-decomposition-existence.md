---
declaration: theorem
origin: cited
lean: TauCeti.exists_isNilpotent_ad_isSemisimple_ad, TauCeti.exists_isNilpotent_ad_isSemisimple_ad_of_iSup_maxGenEigenspace_eq_top, TauCeti.isNilpotent_ad_isSemisimple_ad_unique
statement: formalized
proof: formalized
---

# Abstract Jordan decomposition, existence

In a finite-dimensional Lie algebra with
nondegenerate Killing form over an algebraically closed field, every element `x` is a sum
`n + s` of commuting elements with `ad n` nilpotent and `ad s` semisimple. Both `ad n` and
`ad s` are polynomials in `ad x`.

```lean
TauCeti.exists_isNilpotent_ad_isSemisimple_ad.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [LieAlgebra.IsKilling K L] [IsAlgClosed K]
  (x : L) :
  ∃ n s,
    (LieAlgebra.ad K L) n ∈ K[(LieAlgebra.ad K L) x] ∧
      (LieAlgebra.ad K L) s ∈ K[(LieAlgebra.ad K L) x] ∧
        IsNilpotent ((LieAlgebra.ad K L) n) ∧
          ((LieAlgebra.ad K L) s).IsSemisimple ∧ ⁅n, s⁆ = 0 ∧ x = n + s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Jordan–Chevalley decomposition of a derivation](jordan-chevalley-decomposition-of-a-derivation.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isNilpotent_ad_isSemisimple_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.html#TauCeti.exists_isNilpotent_ad_isSemisimple_ad).

## Other forms

**Abstract Jordan decomposition, existence for split elements.** Formalized in Tau Ceti as [`TauCeti.exists_isNilpotent_ad_isSemisimple_ad_of_iSup_maxGenEigenspace_eq_top`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.html#TauCeti.exists_isNilpotent_ad_isSemisimple_ad_of_iSup_maxGenEigenspace_eq_top).

```lean
TauCeti.exists_isNilpotent_ad_isSemisimple_ad_of_iSup_maxGenEigenspace_eq_top.{u_1, u_2}
  {K : Type u_1} {L : Type u_2} [Field K] [LieRing L] [LieAlgebra K L] [FiniteDimensional K L]
  [LieAlgebra.IsKilling K L] (x : L) (hx : ⨆ μ, ((LieAlgebra.ad K L) x).maxGenEigenspace μ = ⊤) :
  ∃ n s,
    (LieAlgebra.ad K L) n ∈ K[(LieAlgebra.ad K L) x] ∧
      (LieAlgebra.ad K L) s ∈ K[(LieAlgebra.ad K L) x] ∧
        IsNilpotent ((LieAlgebra.ad K L) n) ∧
          ((LieAlgebra.ad K L) s).IsSemisimple ∧ ⁅n, s⁆ = 0 ∧ x = n + s
```

**Abstract Jordan decomposition, uniqueness.** Formalized in Tau Ceti as [`TauCeti.isNilpotent_ad_isSemisimple_ad_unique`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.html#TauCeti.isNilpotent_ad_isSemisimple_ad_unique).

```lean
TauCeti.isNilpotent_ad_isSemisimple_ad_unique.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [LieRing L] [LieAlgebra K L] [FiniteDimensional K L] [LieModule.IsFaithful K L L] [PerfectField K]
  {n₁ s₁ n₂ s₂ : L} (hn₁ : IsNilpotent ((LieAlgebra.ad K L) n₁))
  (hs₁ : ((LieAlgebra.ad K L) s₁).IsSemisimple) (hn₂ : IsNilpotent ((LieAlgebra.ad K L) n₂))
  (hs₂ : ((LieAlgebra.ad K L) s₂).IsSemisimple) (hc₁ : ⁅n₁, s₁⁆ = 0) (hc₂ : ⁅n₂, s₂⁆ = 0)
  (h : n₁ + s₁ = n₂ + s₂) : n₁ = n₂ ∧ s₁ = s₂
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isNilpotent_ad_isSemisimple_ad`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.html#TauCeti.exists_isNilpotent_ad_isSemisimple_ad)
- [Source of `TauCeti.exists_isNilpotent_ad_isSemisimple_ad` in TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Killing/JordanDecomposition/Basic.lean#L80)
