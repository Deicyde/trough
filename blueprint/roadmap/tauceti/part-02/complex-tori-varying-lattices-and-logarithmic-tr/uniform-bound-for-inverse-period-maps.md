---
declaration: theorem
origin: cited
lean: TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact
statement: formalized
proof: formalized
---

# Uniform bound for inverse period maps

For a basis `b` of `Λ`, the real linear maps
`x ↦ ∑ i, x i • P y (b i)` are bounded below by one constant `c > 0` as `y` ranges over a
compact set: `c * ‖x‖ ≤ ‖∑ i, x i • P y (b i)‖`.

```lean
TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact.{u_1, u_2, u_3, u_4} {Y : Type u_1}
  [TopologicalSpace Y] {Λ : Type u_2} [AddCommGroup Λ] {E : Type u_3} [NormedAddCommGroup E]
  [NormedSpace ℝ E] (P : Y → Λ →ₗ[ℤ] E) [FiniteDimensional ℝ E]
  [∀ (y : Y), DiscreteTopology ↥(P y).range] [∀ (y : Y), IsZLattice ℝ (P y).range] {K : Set Y}
  {ι : Type u_4} [Fintype ι] (b : Module.Basis ι ℤ Λ)
  (hcont : ∀ (l : Λ), Continuous fun y => (P y) l) (hinj : ∀ (y : Y), Function.Injective ⇑(P y))
  (hK : IsCompact K) : ∃ c > 0, ∀ y ∈ K, ∀ (x : ι → ℝ), c * ‖x‖ ≤ ‖∑ i, x i • (P y) (b i)‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.periodBasis](tauceti-periodbasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Algebra/Module/ZLattice/Family/Basic.html#TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact)
- [Source of `TauCeti.exists_pos_mul_norm_le_norm_sum_smul_period_of_isCompact` in TauCeti/Algebra/Module/ZLattice/Family/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Module/ZLattice/Family/Basic.lean#L139)
- [Tau Ceti roadmap status: Complex tori: varying lattices and logarithmic transforms](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexTori/STATUS.md)
