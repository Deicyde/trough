---
declaration: theorem
origin: cited
lean: InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg
statement: formalized
proof: formalized
---

# The local Harnack inequality

If `u` is harmonic and nonnegative on `ball c (4 * r)`, then
any two of its values on `ball c r` are within the factor `3 ^ n` of each other, where `n` is the
dimension of `E`.

```lean
InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {u : E → ℝ} {x y c : E}
  {r : ℝ} (hu : InnerProductSpace.HarmonicOnNhd u (Metric.ball c (4 * r)))
  (hnonneg : ∀ z ∈ Metric.ball c (4 * r), 0 ≤ u z) (hx : x ∈ Metric.ball c r)
  (hy : y ∈ Metric.ball c r) : u x ≤ 3 ^ Module.finrank ℝ E * u y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-02/distribution/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)

## Lean

Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Basic.html#InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg).

## Sources

- [Tau Ceti documentation: `InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Basic.html#InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg)
- [Source of `InnerProductSpace.HarmonicOnNhd.le_three_pow_mul_of_nonneg` in TauCeti/Analysis/PDE/Harnack/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Harnack/Basic.lean#L89)
