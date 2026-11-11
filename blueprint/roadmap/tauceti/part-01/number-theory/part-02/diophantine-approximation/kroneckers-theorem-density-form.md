---
declaration: theorem
origin: cited
lean: TauCeti.denseRange_mul_sub_intCast
statement: formalized
proof: formalized
---

# Kronecker's theorem, density form

If `1` and the real numbers `αᵢ` satisfy no
nontrivial integer relation, that is, if they are linearly independent over `ℚ`, then the
points `(y αᵢ - xᵢ)ᵢ`, for `y ∈ ℤ` and `x ∈ ℤ^ι`, are dense in `ℝ^ι`.

```lean
TauCeti.denseRange_mul_sub_intCast.{u_1} {ι : Type u_1} [Fintype ι] {α : ι → ℝ}
  (hα : ∀ (x : ℤ × (ι → ℤ)), ↑x.1 + ∑ i, ↑(x.2 i) * α i = 0 → x = 0) :
  DenseRange fun p i => α i * ↑p.2 - ↑(p.1 i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.denseRange_mul_sub_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.denseRange_mul_sub_intCast).

## Sources

- [Tau Ceti documentation: `TauCeti.denseRange_mul_sub_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.html#TauCeti.denseRange_mul_sub_intCast)
- [Source of `TauCeti.denseRange_mul_sub_intCast` in TauCeti/NumberTheory/DiophantineApproximation/Kronecker.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/DiophantineApproximation/Kronecker.lean#L59)
