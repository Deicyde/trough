---
declaration: theorem
origin: cited
lean: ModularForm.sturm_bound_finiteIndex
statement: formalized
proof: formalized
---

# Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods

A modular form of weight `k` whose `q`-expansion at the cusp `∞`
has order strictly greater than `k · [𝒮ℒ : 𝒢 ⊓ 𝒮ℒ] / 12` is identically zero.

```lean
ModularForm.sturm_bound_finiteIndex {𝒢 : Subgroup (GL (Fin 2) ℝ)}
  [𝒢.IsFiniteRelIndex (Matrix.SpecialLinearGroup.mapGL ℝ).range] {k : ℤ} (f : ModularForm 𝒢 k)
  [DiscreteTopology ↥𝒢.strictPeriods]
  (h :
    ↑((k *
              ↑(Nat.card
                  (↥(Matrix.SpecialLinearGroup.mapGL ℝ).range ⧸
                    𝒢.subgroupOf (Matrix.SpecialLinearGroup.mapGL ℝ).range))).toNat /
          12) <
      (UpperHalfPlane.qExpansion 𝒢.strictWidthInfty ⇑f).order) :
  f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ModularForm.sturm_bound_finiteIndex`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SturmBound.html#ModularForm.sturm_bound_finiteIndex).

## Sources

- [Tau Ceti documentation: `ModularForm.sturm_bound_finiteIndex`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SturmBound.html#ModularForm.sturm_bound_finiteIndex)
- [Source of `ModularForm.sturm_bound_finiteIndex` in TauCeti/NumberTheory/ModularForms/SturmBound.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SturmBound.lean#L54)
