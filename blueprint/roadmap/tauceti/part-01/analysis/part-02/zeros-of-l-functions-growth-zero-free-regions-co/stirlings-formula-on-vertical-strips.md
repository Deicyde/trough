---
declaration: theorem
origin: cited
lean: TauCeti.isBigO_log_norm_Gamma_vertical_sub, TauCeti.abs_log_norm_Gamma_vertical_sub_le, TauCeti.isBigO_log_norm_Gamma_vertical_strip_sub
statement: formalized
proof: formalized
---

# Stirling's formula on vertical strips

**Stirling's formula on vertical strips** ([DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9)):
`log ‖Γ(σ + i t)‖ = (σ - 1/2) log |t| - π |t| / 2 + log (2π) / 2 + O(1 / |t|)` uniformly for
`σ ∈ [a, b]` as `|t| → ∞`.

```lean
TauCeti.isBigO_log_norm_Gamma_vertical_sub (a b : ℝ) :
  (fun p =>
      Real.log ‖Complex.Gamma (↑p.1 + ↑p.2 * Complex.I)‖ -
        ((p.1 - 1 / 2) * Real.log |p.2| - Real.pi * |p.2| / 2 +
          Real.log (2 * Real.pi) / 2)) =O[Filter.principal (Set.Icc a b) ×ˢ Filter.cocompact ℝ]
    fun p => |p.2|⁻¹
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Stirling's formula on a sector, with an explicit constant](stirlings-formula-on-a-sector-with-an-explicit-c.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isBigO_log_norm_Gamma_vertical_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.html#TauCeti.isBigO_log_norm_Gamma_vertical_sub).

## Other forms

**Stirling's formula on vertical strips, explicit form.** Formalized in Tau Ceti as [`TauCeti.abs_log_norm_Gamma_vertical_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.html#TauCeti.abs_log_norm_Gamma_vertical_sub_le).

```lean
TauCeti.abs_log_norm_Gamma_vertical_sub_le {s : ℂ} (hs : s.im ≠ 0) (hre : |s.re| ≤ |s.im|) :
  |Real.log ‖Complex.Gamma s‖ -
        ((s.re - 1 / 2) * Real.log |s.im| - Real.pi * |s.im| / 2 + Real.log (2 * Real.pi) / 2)| ≤
    (2 / (1 - Real.cos (Real.pi / 4)) ^ 3 + |s.re - 1 / 2| * |s.re| + s.re ^ 2) / |s.im|
```

**Stirling's formula on vertical strips as a function of `s = σ + i t`.** Formalized in Tau Ceti as [`TauCeti.isBigO_log_norm_Gamma_vertical_strip_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.html#TauCeti.isBigO_log_norm_Gamma_vertical_strip_sub).

```lean
TauCeti.isBigO_log_norm_Gamma_vertical_strip_sub (a b : ℝ) :
  (fun s =>
      Real.log ‖Complex.Gamma s‖ -
        ((s.re - 1 / 2) * Real.log |s.im| - Real.pi * |s.im| / 2 +
          Real.log (2 * Real.pi) /
            2)) =O[Filter.cocompact ℂ ⊓ Filter.principal (Complex.re ⁻¹' Set.Icc a b)]
    fun s => |s.im|⁻¹
```

## Sources

- [Tau Ceti documentation: `TauCeti.isBigO_log_norm_Gamma_vertical_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.html#TauCeti.isBigO_log_norm_Gamma_vertical_sub)
- [Source of `TauCeti.isBigO_log_norm_Gamma_vertical_sub` in TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Gamma/Stirling/Vertical.lean#L182)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
