---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le, TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_sublevelPair_le
statement: formalized
proof: formalized
---

# The strong Morse inequalities (`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le`)

For a Morse function `f` on a compact boundaryless manifold
`M`, write `bᵢ` for the dimension of `Hᵢ(M; V)` and `cᵢ` for the number of critical points of
index `i`. Then `bₙ - bₙ₋₁ + ⋯ ± b₀ ≤ (cₙ - cₙ₋₁ + ⋯ ± c₀) dim V`.

```lean
TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] [CompactSpace M] (hf : TauCeti.IsMorse I f) (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) *
        ↑(Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj V).obj ↧M)) ≤
    ↑(Module.finrank k ↑V) *
      ∑ i ∈ Finset.range (n + 1), (-1) ^ (n - i) * ↑(TauCeti.criticalCount I f i).toNat
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Deformation of sublevels across a band without critical points (Milnor, Theorem 3.1)](deformation-of-sublevels-across-a-band-without-c.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../manifold/part-02/milnors-cell-attachment-theorem.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities for a CW pair](../../../algebraic-topology/cellular/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../algebraic-topology/cellular/the-weak-morse-inequality-for-a-cw-pair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le).

## Other forms

**The strong Morse inequalities for a band.** Formalized in Tau Ceti as [`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_sublevelPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_sublevelPair_le).

```lean
TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_sublevelPair_le.{u, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ}
  {k : Type u} [DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f)
  {a b : ℝ} (hab : a ≤ b) (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑((TauCeti.sublevelPair f hab).singularHomology V i)) ≤
    ↑(Module.finrank k ↑V) *
      ∑ i ∈ Finset.range (n + 1),
        (-1) ^ (n - i) *
          ↑{x |
                x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                  TauCeti.manifoldMorseIndex I f x = i}.ncard
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le)
- [Source of `TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le` in TauCeti/Geometry/Manifold/Morse/Inequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Inequalities.lean#L514)
