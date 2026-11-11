---
declaration: theorem
origin: cited
lean: ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume
statement: formalized
proof: formalized
---

# Minkowski's first theorem on the successive minima

For a full lattice `L` in a real normed
space `E` of positive dimension `n`, a Haar measure `μ` on `E`, and a convex body `K` symmetric
about `0`, the first successive minimum `λ₀` of `L` with respect to `K` satisfies
`λ₀ⁿ · μ.real K ≤ 2ⁿ · covolume L μ`. It follows from the upper bound of Minkowski's second
theorem, since `λ₀ ≤ λᵢ` for every `i`.

```lean
ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] (L : Submodule ℤ E) [DiscreteTopology ↥L] [IsZLattice ℝ L]
  (μ : MeasureTheory.Measure E := by volume_tac) [μ.IsAddHaarMeasure] {K : ConvexBody E}
  (hKs : ∀ x ∈ K, -x ∈ K) (hE : 0 < Module.finrank ℝ E) :
  ZLattice.successiveMin L K ⟨0, hE⟩ ^ Module.finrank ℝ E * μ.real ↑K ≤
    2 ^ Module.finrank ℝ E * ZLattice.covolume L μ
```

## Depends on

- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Proof depends on

- [Minkowski's second theorem, upper bound, in terms of the successive minima](../../part-01/heights-units-and-s-units-of-number-fields/minkowskis-second-theorem-upper-bound-in-terms-o.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume).

## Sources

- [Tau Ceti documentation: `ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.html#ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume)
- [Source of `ZLattice.successiveMin_pow_mul_measureReal_le_two_pow_mul_covolume` in TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/GeometryOfNumbers/MinkowskiSecond.lean#L674)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
