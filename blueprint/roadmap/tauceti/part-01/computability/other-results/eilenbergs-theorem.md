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

- [TauCeti.IsAutomatic](../../number-theory/part-01/classical-arithmetic-sequences-polynomials-and-r/tauceti-isautomatic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isAutomatic_iff_finite_kernel`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Kernel.html#TauCeti.isAutomatic_iff_finite_kernel).

## Sources

- [Tau Ceti documentation: `TauCeti.isAutomatic_iff_finite_kernel`](https://taucetiproject.org/docs/TauCeti/Computability/AutomaticSequence/Kernel.html#TauCeti.isAutomatic_iff_finite_kernel)
- [Source of `TauCeti.isAutomatic_iff_finite_kernel` in TauCeti/Computability/AutomaticSequence/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/AutomaticSequence/Kernel.lean#L207)
