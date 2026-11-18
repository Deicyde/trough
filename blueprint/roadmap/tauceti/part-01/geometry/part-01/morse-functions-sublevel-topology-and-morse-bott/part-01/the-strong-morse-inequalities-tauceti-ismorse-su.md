---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le, TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_sublevelPair_le, TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_bandPair_le, TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_upperBandPair_le, TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.sum_range_neg_one_pow_mul_finrank_homology_morseComplex_le, TauCeti.morse_inequalities
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

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Euler--Poincaré for cellular chains](../../../../algebraic-topology/other-results/euler-poincare-for-cellular-chains.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)
- [The mod-two Morse boundary squares to zero](../../../../analysis/part-01/analytic-heegaard-floer-homology/the-mod-two-morse-boundary-squares-to-zero.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities (`ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le`)](../../../../algebra/part-02/homology/the-strong-morse-inequalities-chaincomplex-sum-r.md)
- [The strong Morse inequalities for a CW pair](../../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-weak-morse-inequality-for-a-cw-pair.md)

## Informally uses

- [The coefficientwise Morse polynomial identity with module coefficients](the-coefficientwise-morse-polynomial-identity-wi.md)

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

**The strong Morse inequalities for a cobordism.** Formalized in Tau Ceti as [`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_bandPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_bandPair_le).

```lean
TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_bandPair_le.{u, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ}
  {k : Type u} [DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f)
  {a b : ℝ} (hab : a ≤ b) (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑((TauCeti.bandPair f hab).singularHomology V i)) ≤
    ↑(Module.finrank k ↑V) *
      ∑ i ∈ Finset.range (n + 1),
        (-1) ^ (n - i) *
          ↑{x |
                x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                  TauCeti.manifoldMorseIndex I f x = i}.ncard
```

**The strong Morse inequalities for a cobordism relative to its outgoing boundary.** Formalized in Tau Ceti as [`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_upperBandPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_upperBandPair_le).

```lean
TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_upperBandPair_le.{u, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ}
  {k : Type u} [DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f)
  {a b : ℝ} (hab : a ≤ b) (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑((TauCeti.upperBandPair f hab).singularHomology V i)) ≤
    ↑(Module.finrank k ↑V) *
      ∑ i ∈ Finset.range (n + 1),
        (-1) ^ (n - i) *
          ↑{x |
                x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ico a b ∧
                  TauCeti.manifoldMorseIndex I f x + i = Module.finrank ℝ E}.ncard
```

**The strong Morse inequalities for Morse homology.** Formalized in Tau Ceti as [`TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.sum_range_neg_one_pow_mul_finrank_homology_morseComplex_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Boundary/ChainComplex.html#TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.sum_range_neg_one_pow_mul_finrank_homology_morseComplex_le).

```lean
TauCeti.IsAdaptedPseudoGradient.IsMorseSmale.sum_range_neg_one_pow_mul_finrank_homology_morseComplex_le.{u_1,
    u_2}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {M : Type u_2}
  [TopologicalSpace M] [ChartedSpace E M] [IsManifold (modelWithCornersSelf ℝ E) (↑⊤) M]
  [CompactSpace M] [T2Space M] {f : M → ℝ} {X : (x : M) → TangentSpace (modelWithCornersSelf ℝ E) x}
  {hX : TauCeti.IsAdaptedPseudoGradient f X} (h : hX.IsMorseSmale)
  (hf : TauCeti.IsMorse (modelWithCornersSelf ℝ E) f) (n : ℕ) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) *
        ↑(Module.finrank (ZMod 2) ↑(HomologicalComplex.homology (h.morseComplex hf) i)) ≤
    ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(TauCeti.criticalCount (modelWithCornersSelf ℝ E) f i).toNat
```

**The strong Morse inequalities in polynomial form.** Formalized in Tau Ceti as [`TauCeti.morse_inequalities`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Polynomial.html#TauCeti.morse_inequalities).

```lean
TauCeti.morse_inequalities.{u, u_1, u_2} {E : Type u_1} {H : Type u_2} {M : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ} (hf : TauCeti.IsMorse I f)
  (k : Type u) [DivisionRing k] :
  ∃ Q,
    ∀ (j : ℕ),
      TauCeti.criticalCount I f j = ↑(TauCeti.bettiNumber k M j + ((1 + Polynomial.X) * Q).coeff j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le)
- [Source of `TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le` in TauCeti/Geometry/Manifold/Morse/Inequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Inequalities.lean#L1002)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
