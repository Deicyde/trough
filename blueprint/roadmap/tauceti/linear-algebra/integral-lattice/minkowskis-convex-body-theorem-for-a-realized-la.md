---
declaration: theorem
origin: cited
lean: TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt
statement: formalized
proof: formalized
---

# Minkowski's convex body theorem for a realized lattice

Let `φ` realize a nondegenerate
integral lattice `L` in a real inner product space `E` of dimension `n`. A convex set `K ⊆ E`,
symmetric about the origin, of volume greater than `2ⁿ · √(det L)` contains `φ y` for some
nonzero `y ∈ L`.

```lean
TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt.{u, u_1} {V : Type u}
  [AddCommGroup V] [_root_.Module ℚ V] {L : TauCeti.IntegralLattice V} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [L.IsNondegenerate] {φ : ↥L.carrier →ₗ[ℤ] E}
  (hφ : ∀ (x y : ↥L.carrier), inner ℝ (φ x) (φ y) = ↑((L.integralForm x) y))
  (hspan : Submodule.span ℝ (Set.range ⇑φ) = ⊤) {K : Set E} (hsymm : ∀ v ∈ K, -v ∈ K)
  (hconv : Convex ℝ K)
  (hK : ENNReal.ofReal (2 ^ Module.finrank ℝ E * √↑L.determinant) < MeasureTheory.volume K) :
  ∃ y, y ≠ 0 ∧ φ y ∈ K
```

## Depends on

- [TauCeti.IntegralLattice](../integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.html#TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt)
- [Source of `TauCeti.IntegralLattice.exists_ne_zero_mem_of_two_pow_mul_sqrt_determinant_lt` in TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/IntegralLattice/PosDef/Minkowski.lean#L76)
