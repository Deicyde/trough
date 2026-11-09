---
declaration: theorem
origin: cited
lean: ModularForm.sturm_bound_finiteIndex_SL2Z
statement: formalized
proof: formalized
---

# Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`

```lean
ModularForm.sturm_bound_finiteIndex_SL2Z {Γ : Subgroup (Matrix.SpecialLinearGroup (Fin 2) ℤ)}
  [Γ.FiniteIndex] {k : ℤ} (f : ModularForm (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ) k)
  (h :
    ↑((k * ↑Γ.index).toNat / 12) <
      (UpperHalfPlane.qExpansion
          (Subgroup.map (Matrix.SpecialLinearGroup.mapGL ℝ) Γ).strictWidthInfty ⇑f).order) :
  f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sturm bound for subgroups of `GL(2, ℝ)` of finite relative index in `SL(2, ℤ)` with discrete strict periods](sturm-bound-for-subgroups-of-gl-2-r-of-finite-re.md)

## Lean

Formalized in Tau Ceti as [`ModularForm.sturm_bound_finiteIndex_SL2Z`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SturmBound.html#ModularForm.sturm_bound_finiteIndex_SL2Z).

## Sources

- [Tau Ceti documentation: `ModularForm.sturm_bound_finiteIndex_SL2Z`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SturmBound.html#ModularForm.sturm_bound_finiteIndex_SL2Z)
- [Source of `ModularForm.sturm_bound_finiteIndex_SL2Z` in TauCeti/NumberTheory/ModularForms/SturmBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/SturmBound.lean#L62)
