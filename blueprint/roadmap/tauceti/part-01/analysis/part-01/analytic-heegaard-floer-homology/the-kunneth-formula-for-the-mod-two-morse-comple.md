---
declaration: theorem
origin: cited
lean: TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary
statement: formalized
proof: formalized
---

# The Künneth formula for the mod-two Morse complex

Under the identification of the mod-two
Morse chains of the separated sum with the tensor product of the chains of `f` and of `g`, the
Morse boundary of the separated sum is `∂ ⊗ 1 + 1 ⊗ ∂`.

```lean
TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  {f : E → ℝ} {g : F → ℝ} {K K' K'' : NNReal} [FiniteDimensional ℝ E] [FiniteDimensional ℝ F]
  (hfs : ContDiff ℝ 2 f) (hf : LipschitzWith K (gradient f))
  (hM : TauCeti.HasNondegenerateCriticalPointsOn f Set.univ)
  (hcf : ∀ (c : ℝ), IsCompact {x | f x ≤ c}) (htf : TauCeti.IsMorseSmale f hf)
  (hgs : ContDiff ℝ 2 g) (hg : LipschitzWith K' (gradient g))
  (hN : TauCeti.HasNondegenerateCriticalPointsOn g Set.univ)
  (hcg : ∀ (c : ℝ), IsCompact {y | g y ≤ c}) (htg : TauCeti.IsMorseSmale g hg)
  (hh : LipschitzWith K'' (gradient (TauCeti.separatedSum f g)))
  (hhs : ContDiff ℝ 2 (TauCeti.separatedSum f g))
  (hMh : TauCeti.HasNondegenerateCriticalPointsOn (TauCeti.separatedSum f g) Set.univ)
  (hch : ∀ (c : ℝ), IsCompact {z | TauCeti.separatedSum f g z ≤ c})
  (hth : TauCeti.IsMorseSmale (TauCeti.separatedSum f g) hh) :
  ↑(TauCeti.morseChainSeparatedSumEquiv f g) ∘ₗ TauCeti.morseBoundary hhs hh hMh hch hth =
    (LinearMap.rTensor (TauCeti.MorseChain g) (TauCeti.morseBoundary hfs hf hM hcf htf) +
        LinearMap.lTensor (TauCeti.MorseChain f) (TauCeti.morseBoundary hgs hg hN hcg htg)) ∘ₗ
      ↑(TauCeti.morseChainSeparatedSumEquiv f g)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse form of the convergence theorem](../../part-02/calculus/part-01/the-morse-form-of-the-convergence-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Boundary/Prod.html#TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary).

## Sources

- [Tau Ceti documentation: `TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Morse/Boundary/Prod.html#TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary)
- [Source of `TauCeti.morseChainSeparatedSumEquiv_comp_morseBoundary` in TauCeti/Analysis/Calculus/Morse/Boundary/Prod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Morse/Boundary/Prod.lean#L363)
- [Tau Ceti roadmap status: Analytic Heegaard Floer homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HeegaardFloer/STATUS.md)
