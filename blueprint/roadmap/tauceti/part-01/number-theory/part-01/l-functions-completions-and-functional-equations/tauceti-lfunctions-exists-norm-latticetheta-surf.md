---
declaration: theorem
origin: cited
lean: TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le
statement: formalized
proof: formalized
---

# TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le

Uniform stretched-exponential decay of the theta kernel minus its constant term `1` along
the radial decomposition of any bounded subset of the norm-one surface. No fundamental-domain
or unit-invariance hypothesis is needed.

```lean
TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le.{u_1} {K : Type u_1} [Field K]
  [NumberField K] (L : Submodule ℤ (NumberField.mixedEmbedding.mixedSpace K)) [DiscreteTopology ↥L]
  {D : Set (NumberField.mixedEmbedding.realSpace K)} (hD : Bornology.IsBounded D)
  (hS : D ⊆ TauCeti.LFunctions.normOneSurface K) :
  ∃ c > 0,
    ∃ C ≥ 0,
      ∀ᶠ (u : ℝ) in Filter.atTop,
        ∀ x ∈ D,
          ‖TauCeti.LFunctions.latticeTheta L (TauCeti.LFunctions.surfaceScale x u) - 1‖ ≤
            C * Real.exp (-c * u ^ (↑(Module.finrank ℚ K))⁻¹)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Decay.html#TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le).

## Sources

- [Tau Ceti documentation: `TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LFunctions/Theta/Decay.html#TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le)
- [Source of `TauCeti.LFunctions.exists_norm_latticeTheta_surfaceScale_sub_one_le` in TauCeti/NumberTheory/LFunctions/Theta/Decay.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LFunctions/Theta/Decay.lean#L87)
- [Tau Ceti roadmap status: L-functions — completions and functional equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LFunctions/STATUS.md)
