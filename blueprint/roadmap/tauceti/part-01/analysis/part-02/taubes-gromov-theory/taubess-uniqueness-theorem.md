---
declaration: theorem
origin: cited
lean: TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff
statement: formalized
proof: formalized
---

# Taubes's uniqueness theorem

Two smooth framed degree-`m` vortices have the same divisor
exactly when they differ by a smooth framed gauge.

```lean
TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff {m : ℕ}
  {x y : ↥(TauCeti.Vortex.framedVortexSubMulAction m)} :
  TauCeti.Vortex.framedVortexDivisor x = TauCeti.Vortex.framedVortexDivisor y ↔ ∃ u, u • y = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula with a cutoff](../../part-03/complex/part-01/the-cauchy-pompeiu-formula-with-a-cutoff.md)
- [Liouville's theorem (`InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded`)](../../part-03/inner-product-space/part-02/liouvilles-theorem-innerproductspace-harmoniconn.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Vortex/Existence.html#TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff)
- [Source of `TauCeti.Vortex.framedVortexDivisor_eq_framedVortexDivisor_iff` in TauCeti/Analysis/PDE/Vortex/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Vortex/Existence.lean#L294)
