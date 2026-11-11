---
declaration: theorem
origin: cited
lean: Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy
statement: formalized
proof: formalized
---

# Klein's inequality for the relative entropy

For positive semidefinite `ρ` and `σ`,
`Tr ρ - Tr σ ≤ D(ρ ‖ σ)`.

```lean
Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy.{u_1, u_2} {𝕜 : Type u_1} [RCLike 𝕜]
  {n : Type u_2} [Fintype n] [DecidableEq n] {ρ σ : Matrix n n 𝕜} (hρ : ρ.PosSemidef)
  (hσ : σ.PosSemidef) : ↑(RCLike.re (ρ.trace - σ.trace)) ≤ ρ.relativeEntropy σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Entropy.html#Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy).

## Sources

- [Tau Ceti documentation: `Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/Entropy.html#Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy)
- [Source of `Matrix.PosSemidef.re_trace_sub_trace_le_relativeEntropy` in TauCeti/Analysis/Matrix/Entropy.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Matrix/Entropy.lean#L213)
