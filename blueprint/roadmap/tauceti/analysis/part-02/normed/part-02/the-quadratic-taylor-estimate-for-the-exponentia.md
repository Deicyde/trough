---
declaration: theorem
origin: cited
lean: NormedSpace.isBigO_exp_sub_quadratic, NormedSpace.isBigO_exp_mul_exp_sub_one_sub_quadratic, NormedSpace.isBigO_log_one_add_sub_quadratic
statement: formalized
proof: formalized
---

# The quadratic Taylor estimate for the exponential

In a complete normed algebra,
`exp x - (1 + x + 2⁻¹ • x ^ 2)` is `O(‖x‖ ^ 3)` as `x → 0`.

```lean
NormedSpace.isBigO_exp_sub_quadratic.{u_1, u_2} (𝕂 : Type u_1) {A : Type u_2}
  [NontriviallyNormedField 𝕂] [NormedRing A] [NormedAlgebra 𝕂 A] [CharZero 𝕂] [ContinuousSMul ℚ 𝕂]
  [CompleteSpace A] :
  (fun x => NormedSpace.exp x - (1 + x + 2⁻¹ • x ^ 2)) =O[nhds 0] fun x => ‖x‖ ^ 3
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NormedSpace.isBigO_exp_sub_quadratic`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Exponential.html#NormedSpace.isBigO_exp_sub_quadratic).

## Other forms

**The quadratic Taylor estimate for `exp x * exp y - 1`.** Formalized in Tau Ceti as [`NormedSpace.isBigO_exp_mul_exp_sub_one_sub_quadratic`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/BCH/FirstOrder.html#NormedSpace.isBigO_exp_mul_exp_sub_one_sub_quadratic).

```lean
NormedSpace.isBigO_exp_mul_exp_sub_one_sub_quadratic.{u_1} (A : Type u_1) [NormedRing A]
  [NormedAlgebra ℝ A] [CompleteSpace A] :
  (fun p =>
      NormedSpace.exp p.1 * NormedSpace.exp p.2 - 1 - (p.1 + p.2) -
        (2⁻¹ • p.1 ^ 2 + p.1 * p.2 + 2⁻¹ • p.2 ^ 2)) =O[nhds (0, 0)]
    fun p => ‖p‖ ^ 3
```

**The quadratic Taylor estimate for the Banach algebra logarithm.** Formalized in Tau Ceti as [`NormedSpace.isBigO_log_one_add_sub_quadratic`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Logarithm/Basic.html#NormedSpace.isBigO_log_one_add_sub_quadratic).

```lean
NormedSpace.isBigO_log_one_add_sub_quadratic.{u_1, u_2} (𝕂 : Type u_1) (A : Type u_2)
  [NontriviallyNormedField 𝕂] [NormedRing A] [NormedAlgebra 𝕂 A] [CharZero 𝕂] [ContinuousSMul ℚ≥0 𝕂]
  [CompleteSpace A] :
  (fun u => NormedSpace.log (1 + u) - (u - 2⁻¹ • u ^ 2)) =O[nhds 0] fun u => ‖u‖ ^ 3
```

## Sources

- [Tau Ceti documentation: `NormedSpace.isBigO_exp_sub_quadratic`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Algebra/Exponential.html#NormedSpace.isBigO_exp_sub_quadratic)
- [Source of `NormedSpace.isBigO_exp_sub_quadratic` in TauCeti/Analysis/Normed/Algebra/Exponential.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Algebra/Exponential.lean#L76)
