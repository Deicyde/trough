---
declaration: theorem
origin: cited
lean: MvPowerSeries.exists_gaussNorm_primitive_le
statement: formalized
proof: formalized
---

# The Gauss norm bound for primitives

Over a normed field of characteristic zero, for
polyradii `0 ≤ c' ≤ c` with `c'ᵢ < cᵢ`, there is `C ≥ 0` such that for every `f` with a Gauss norm
at `c`, `∫ f dXᵢ` has a Gauss norm at `c'` and `gaussNorm c' (∫ f dXᵢ) ≤ C * gaussNorm c f`.

```lean
MvPowerSeries.exists_gaussNorm_primitive_le.{u_1, u_2} {σ : Type u_1} {K : Type u_2} [NormedField K]
  [CharZero K] (c c' : σ → ℝ) (i : σ) (hc' : ∀ (j : σ), 0 ≤ c' j) (hle : ∀ (j : σ), c' j ≤ c j)
  (hlt : c' i < c i) :
  ∃ C,
    0 ≤ C ∧
      ∀ (f : MvPowerSeries σ K),
        MvPowerSeries.HasGaussNorm norm c f →
          MvPowerSeries.HasGaussNorm norm c' ((MvPowerSeries.primitive i) f) ∧
            MvPowerSeries.gaussNorm norm c' ((MvPowerSeries.primitive i) f) ≤
              C * MvPowerSeries.gaussNorm norm c f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPowerSeries.exists_gaussNorm_primitive_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/Primitive/GaussNorm.html#MvPowerSeries.exists_gaussNorm_primitive_le).

## Sources

- [Tau Ceti documentation: `MvPowerSeries.exists_gaussNorm_primitive_le`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPowerSeries/Primitive/GaussNorm.html#MvPowerSeries.exists_gaussNorm_primitive_le)
- [Source of `MvPowerSeries.exists_gaussNorm_primitive_le` in TauCeti/RingTheory/MvPowerSeries/Primitive/GaussNorm.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/MvPowerSeries/Primitive/GaussNorm.lean#L114)
