---
declaration: theorem
origin: cited
lean: TauCeti.isAutomatic_iff_finite_kernel
statement: formalized
proof: formalized
---

# Eilenberg's theorem

for `2 ≤ k`, a sequence is `k`-automatic if and only if its
`k`-kernel is finite.

```lean
TauCeti.isAutomatic_iff_finite_kernel.{u} {k : ℕ} {Δ : Type u} {a : ℕ → Δ} [NeZero k] (hk : 2 ≤ k) :
  TauCeti.IsAutomatic k a ↔ (TauCeti.kernel k a).Finite
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isAutomatic_iff_finite_kernel`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Kernel.html#TauCeti.isAutomatic_iff_finite_kernel).

## Sources

- [Tau Ceti documentation: `TauCeti.isAutomatic_iff_finite_kernel`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Kernel.html#TauCeti.isAutomatic_iff_finite_kernel)
- [Source of `TauCeti.isAutomatic_iff_finite_kernel` in TauCeti/Computability/AutomaticSequence/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Computability/AutomaticSequence/Kernel.lean#L207)
