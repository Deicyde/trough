---
declaration: theorem
origin: cited
lean: ZLattice.prod_successiveMin_mul_measureReal_crosspolytope
statement: formalized
proof: formalized
---

# Equality in the lower bound of Minkowski's second theorem

Let `b` be a basis of `E`, `a`
positive nondecreasing weights and `μ` an additive Haar measure on `E`. The weighted
cross-polytope `K = {x | ∑ j, a j * |b.repr x j| ≤ 1}` satisfies
`(∏ i, λ_i) * μ K = 2 ^ d / d! * covolume L μ` for the lattice `L = span ℤ (range b)`, so the
constant `2 ^ d / d!` of
`ZLattice.two_pow_div_factorial_mul_covolume_le_prod_successiveMin_mul_measureReal` is
attained.

```lean
ZLattice.prod_successiveMin_mul_measureReal_crosspolytope.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {b : Module.Basis (Fin (Module.finrank ℝ E)) ℝ E}
  {a : Fin (Module.finrank ℝ E) → ℝ} {K : ConvexBody E} [MeasurableSpace E] [BorelSpace E]
  (ha : ∀ (j : Fin (Module.finrank ℝ E)), 0 < a j) (hmono : Monotone a)
  (hK : ↑K = {x | ∑ j, a j * |(b.repr x) j| ≤ 1}) (μ : MeasureTheory.Measure E := by volume_tac)
  [μ.IsAddHaarMeasure] :
  (∏ i, ZLattice.successiveMin (Submodule.span ℤ (Set.range ⇑b)) K i) * μ.real ↑K =
    2 ^ Module.finrank ℝ E / ↑(Module.finrank ℝ E).factorial *
      ZLattice.covolume (Submodule.span ℤ (Set.range ⇑b)) μ
```

## Depends on

- [ZLattice.successiveMin](../../part-01/heights-units-and-s-units-of-number-fields/zlattice-successivemin.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.prod_successiveMin_mul_measureReal_crosspolytope`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/BoxMinima.html#ZLattice.prod_successiveMin_mul_measureReal_crosspolytope).

## Sources

- [Tau Ceti documentation: `ZLattice.prod_successiveMin_mul_measureReal_crosspolytope`](https://taucetiproject.org/docs/TauCeti/NumberTheory/GeometryOfNumbers/BoxMinima.html#ZLattice.prod_successiveMin_mul_measureReal_crosspolytope)
- [Source of `ZLattice.prod_successiveMin_mul_measureReal_crosspolytope` in TauCeti/NumberTheory/GeometryOfNumbers/BoxMinima.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/GeometryOfNumbers/BoxMinima.lean#L223)
- [Tau Ceti roadmap status: Successive minima and Minkowski's theorems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SuccessiveMinima/STATUS.md)
