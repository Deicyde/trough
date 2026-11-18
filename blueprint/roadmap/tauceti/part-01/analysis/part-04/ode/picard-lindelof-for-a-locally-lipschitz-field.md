---
declaration: theorem
origin: cited
lean: LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt
statement: formalized
proof: formalized
---

# Picard–Lindelöf for a locally Lipschitz field

An autonomous locally Lipschitz field
on a complete space has, from every initial point and at every initial time `t₀`, a solution on
`[t₀ - ε, t₀ + ε]`, where `ε > 0` depends only on the initial point.

The construction of the Picard–Lindelöf data follows Mathlib's
`IsPicardLindelof.of_contDiffAt_one`, whose proof uses only the local Lipschitz continuity of
the `C¹` field.

```lean
LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [CompleteSpace E] {v : E → E} (hv : LocallyLipschitz v)
  (y : E) :
  ∃ ε > 0,
    ∀ (t₀ : ℝ),
      ∃ α,
        α t₀ = y ∧
          ∀ t ∈ Set.Icc (t₀ - ε) (t₀ + ε),
            HasDerivWithinAt α (v (α t)) (Set.Icc (t₀ - ε) (t₀ + ε)) t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/UniformTime.html#LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt).

## Sources

- [Tau Ceti documentation: `LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/UniformTime.html#LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt)
- [Source of `LocallyLipschitz.exists_eq_forall_mem_Icc_hasDerivWithinAt` in TauCeti/Analysis/ODE/UniformTime.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/ODE/UniformTime.lean#L87)
