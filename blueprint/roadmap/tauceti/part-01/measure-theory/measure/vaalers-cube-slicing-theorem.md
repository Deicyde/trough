---
declaration: theorem
origin: cited
lean: Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one
statement: formalized
proof: formalized
---

# Vaaler's cube-slicing theorem

Every central slice of the cube `[-1, 1] ^ ι` by a
subspace `V` of `EuclideanSpace ℝ ι` has volume at least `2 ^ finrank ℝ V`, computed in `V`.

```lean
Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one.{u_1} {ι : Type u_1} [Fintype ι]
  (V : Submodule ℝ (EuclideanSpace ℝ ι)) :
  2 ^ Module.finrank ℝ ↥V ≤ MeasureTheory.volume {x | ∀ (i : ι), |(↑x).ofLp i| ≤ 1}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brunn's principle, in log-concave form](../integral/part-01/brunns-principle-in-log-concave-form.md)
- [Prékopa–Leindler inequality for the minimum on `ℝ`](../integral/part-02/prekopa-leindler-inequality-for-the-minimum-on-r.md)

## Lean

Formalized in Tau Ceti as [`Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/CubeSlice.html#Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one).

## Sources

- [Tau Ceti documentation: `Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/CubeSlice.html#Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one)
- [Source of `Submodule.two_pow_finrank_le_volume_setOf_forall_abs_le_one` in TauCeti/MeasureTheory/Measure/Lebesgue/CubeSlice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/CubeSlice.lean#L331)
