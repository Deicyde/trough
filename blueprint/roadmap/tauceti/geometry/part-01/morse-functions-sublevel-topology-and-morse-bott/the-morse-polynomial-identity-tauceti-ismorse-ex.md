---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul, TauCeti.IsMorse.exists_sum_range_monomial_sublevelPair_eq_add_mul
statement: formalized
proof: formalized
---

# The Morse polynomial identity (`TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul`)

For a Morse function `f` on a compact boundaryless manifold
`M`, write `bᵢ` for the dimension of `Hᵢ(M; V)` and `cᵢ` for the number of critical points of index
`i`. Then for every `n ≥ dim M`, `∑ᵢ₌₀ⁿ cᵢ dim V · tⁱ = ∑ᵢ₌₀ⁿ bᵢ tⁱ + (1 + t) Q(t)` for a polynomial
`Q` with natural number coefficients. The coefficient of `tⁱ` in `Q` is the gap
`(cᵢ - cᵢ₋₁ + ⋯ ± c₀) dim V - (bᵢ - bᵢ₋₁ + ⋯ ± b₀)` in the `i`-th strong Morse inequality for
`i < n`, and zero for `i ≥ n`.

```lean
TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] [CompactSpace M] (hf : TauCeti.IsMorse I f) {n : ℕ}
  (hn : Module.finrank ℝ E ≤ n) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i) ((TauCeti.criticalCount I f i).toNat * Module.finrank k ↑V) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k
                ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj V).obj ↧M)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          ↑(Q.coeff i) =
            ↑(Module.finrank k ↑V) *
                ∑ j ∈ Finset.range (i + 1), (-1) ^ (i - j) * ↑(TauCeti.criticalCount I f j).toNat -
              ∑ j ∈ Finset.range (i + 1),
                (-1) ^ (i - j) *
                  ↑(Module.finrank k
                      ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) j).obj V).obj
                          ↧M))) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deformation of sublevels across a band without critical points (Milnor, Theorem 3.1)](deformation-of-sublevels-across-a-band-without-c.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../manifold/part-02/milnors-cell-attachment-theorem.md)
- [The Morse polynomial identity (`ChainComplex.sum_range_monomial_finrank_X_eq`)](../../../algebra/homology/the-morse-polynomial-identity-chaincomplex-sum-r.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities for a CW pair](../../../algebraic-topology/cellular/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../algebraic-topology/cellular/the-weak-morse-inequality-for-a-cw-pair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul).

## Other forms

**The Morse polynomial identity for a band.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sum_range_monomial_sublevelPair_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_sublevelPair_eq_add_mul).

```lean
TauCeti.IsMorse.exists_sum_range_monomial_sublevelPair_eq_add_mul.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f) {a b : ℝ} (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) {n : ℕ}
  (hn : Module.finrank ℝ E ≤ n) :
  ∃ Q,
    ∑ i ∈ Finset.range (n + 1),
          (Polynomial.monomial i)
            ({x |
                  x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                    TauCeti.manifoldMorseIndex I f x = i}.ncard *
              Module.finrank k ↑V) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k ↑((TauCeti.sublevelPair f hab).singularHomology V i)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          ↑(Q.coeff i) =
            ↑(Module.finrank k ↑V) *
                ∑ j ∈ Finset.range (i + 1),
                  (-1) ^ (i - j) *
                    ↑{x |
                          x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                            TauCeti.manifoldMorseIndex I f x = j}.ncard -
              ∑ j ∈ Finset.range (i + 1),
                (-1) ^ (i - j) *
                  ↑(Module.finrank k ↑((TauCeti.sublevelPair f hab).singularHomology V j))) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul)
- [Source of `TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul` in TauCeti/Geometry/Manifold/Morse/Inequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Inequalities.lean#L543)
