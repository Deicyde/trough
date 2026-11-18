---
declaration: def
origin: cited
lean: TauCeti.weightSpaceEquiv
statement: formalized
---

# The parametrisation of the weights of `ℤ_pˣ`

For a complete ultrametric normed
commutative `ℤ_p`-algebra `R` with contractive action, a weight `κ` is determined by its finite
part `η = κ ∘ ω : (ℤ/qℤ)ˣ →* Rˣ` and its coordinate `T_κ = κ(γ) - 1`, which is topologically
nilpotent, and every such pair arises.

```lean
TauCeti.weightSpaceEquiv.{u_1} (p : ℕ) [Fact (Nat.Prime p)] (R : Type u_1) [NormedCommRing R]
  [Algebra ℤ_[p] R] [IsBoundedSMul ℤ_[p] R] [IsUltrametricDist R] [CompleteSpace R] :
  TauCeti.WeightSpace p R ≃
    ((ZMod (p ^ TauCeti.padicUnitsDepth p))ˣ →* Rˣ) ×
      { t // Filter.Tendsto (fun x => t ^ x) Filter.atTop (nhds 0) }
```

## Depends on

- [The decomposition `ℤ_pˣ ≃ₜ* (ℤ/qℤ)ˣ × ℤ_p`](the-decomposition-z-px-t-z-qz-x-z-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.weightSpaceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/WeightSpace/Basic.html#TauCeti.weightSpaceEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.weightSpaceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/WeightSpace/Basic.html#TauCeti.weightSpaceEquiv)
- [Source of `TauCeti.weightSpaceEquiv` in TauCeti/NumberTheory/Padics/WeightSpace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/WeightSpace/Basic.lean#L559)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
