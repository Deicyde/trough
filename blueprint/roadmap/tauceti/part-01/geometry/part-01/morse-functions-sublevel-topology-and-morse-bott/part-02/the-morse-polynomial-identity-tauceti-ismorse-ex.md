---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff, TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul, TauCeti.IsMorse.exists_sum_range_monomial_sublevelPair_eq_add_mul, TauCeti.IsMorse.exists_sum_range_monomial_bandPair_eq_add_mul, TauCeti.IsMorse.exists_sum_range_monomial_upperBandPair_eq_add_mul, TauCeti.IsMorse.exists_relCWComplex_sum_range_monomial_sublevelPair_eq_add_mul, TauCeti.IsMorse.exists_cwComplex_criticalCount_eq_bettiNumber_add_coeff
statement: formalized
proof: formalized
---

# The Morse polynomial identity (`TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff`)

Let `f` be a Morse function on a compact boundaryless
manifold `M` of dimension `m`, with `cⱼ` critical points of index `j`, and let `bⱼ` be the Betti
numbers of `M` over a division ring `k`. Then `∑ cⱼ tʲ = ∑ bⱼ tʲ + (1 + t) Q(t)` for a polynomial
`Q` with natural number coefficients and degree below `m`. The identity is stated coefficientwise,
with the critical counts in `ℕ∞`, so that it includes the finiteness of every count.

```lean
TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ}
  (hf : TauCeti.IsMorse I f) (k : Type u) [DivisionRing k] :
  ∃ Q,
    Q.degree < ↑(Module.finrank ℝ E) ∧
      ∀ (j : ℕ),
        TauCeti.criticalCount I f j =
          ↑(TauCeti.bettiNumber k M j + ((1 + Polynomial.X) * Q).coeff j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The CW model of a compact manifold](../part-01/the-cw-model-of-a-compact-manifold.md)
- [Euler--Poincaré for cellular chains](../../../../algebraic-topology/other-results/euler-poincare-for-cellular-chains.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)
- [The Morse polynomial identity (`ChainComplex.sum_range_monomial_finrank_X_eq`)](../../../../algebra/part-02/homology/the-morse-polynomial-identity-chaincomplex-sum-r.md)
- [The Morse polynomial identity for a CW pair](../../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-morse-polynomial-identity-for-a-cw-pair.md)
- [The relative CW model of a regular band](../part-01/the-relative-cw-model-of-a-regular-band.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities for a CW pair](../../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../../algebraic-topology/algebraic-topology-of-spaces-and-manifolds/the-weak-morse-inequality-for-a-cw-pair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/BettiNumber.html#TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff).

## Other forms

**The Morse polynomial identity.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_eq_add_mul).

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

**The Morse polynomial identity for a cobordism.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sum_range_monomial_bandPair_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_bandPair_eq_add_mul).

```lean
TauCeti.IsMorse.exists_sum_range_monomial_bandPair_eq_add_mul.{u, u_1, u_2} {E : Type u_1}
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
              (Module.finrank k ↑((TauCeti.bandPair f hab).singularHomology V i)) +
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
                  ↑(Module.finrank k ↑((TauCeti.bandPair f hab).singularHomology V j))) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

**The Morse polynomial identity for a cobordism relative to its outgoing boundary.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_sum_range_monomial_upperBandPair_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.exists_sum_range_monomial_upperBandPair_eq_add_mul).

```lean
TauCeti.IsMorse.exists_sum_range_monomial_upperBandPair_eq_add_mul.{u, u_1, u_2} {E : Type u_1}
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
                  x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ico a b ∧
                    TauCeti.manifoldMorseIndex I f x + i = Module.finrank ℝ E}.ncard *
              Module.finrank k ↑V) =
        ∑ i ∈ Finset.range (n + 1),
            (Polynomial.monomial i)
              (Module.finrank k ↑((TauCeti.upperBandPair f hab).singularHomology V i)) +
          (1 + Polynomial.X) * Q ∧
      (∀ i < n,
          ↑(Q.coeff i) =
            ↑(Module.finrank k ↑V) *
                ∑ j ∈ Finset.range (i + 1),
                  (-1) ^ (i - j) *
                    ↑{x |
                          x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ico a b ∧
                            TauCeti.manifoldMorseIndex I f x + j = Module.finrank ℝ E}.ncard -
              ∑ j ∈ Finset.range (i + 1),
                (-1) ^ (i - j) *
                  ↑(Module.finrank k ↑((TauCeti.upperBandPair f hab).singularHomology V j))) ∧
        ∀ (i : ℕ), n ≤ i → Q.coeff i = 0
```

**The Morse polynomial identity of a sublevel pair, with cellular coefficients.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_relCWComplex_sum_range_monomial_sublevelPair_eq_add_mul`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CWModel/Relative.html#TauCeti.IsMorse.exists_relCWComplex_sum_range_monomial_sublevelPair_eq_add_mul).

```lean
TauCeti.IsMorse.exists_relCWComplex_sum_range_monomial_sublevelPair_eq_add_mul.{u, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ}
  (hf : TauCeti.IsMorse I f) {a b : ℝ} (hab : a ≤ b) (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) :
  ∃ W x,
    ∃ (x_1 : T2Space W),
      ∃ B x_2,
        Topology.RelCWComplex.Finite Set.univ ∧
          (∀ (m : ℕ),
              Nonempty
                (Topology.RelCWComplex.cell Set.univ m ≃
                  ↑{x |
                      x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                        TauCeti.manifoldMorseIndex I f x = m})) ∧
            ∀ {k : Type u} [inst : DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] {n : ℕ},
              Module.finrank ℝ E ≤ n →
                ∑ i ∈ Finset.range (n + 1),
                    (Polynomial.monomial i)
                      ({x |
                            x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                              TauCeti.manifoldMorseIndex I f x = i}.ncard *
                        Module.finrank k ↑V) =
                  ∑ i ∈ Finset.range (n + 1),
                      (Polynomial.monomial i)
                        (Module.finrank k ↑((TauCeti.sublevelPair f hab).singularHomology V i)) +
                    (1 + Polynomial.X) *
                      ∑ i ∈ Finset.range n,
                        (Polynomial.monomial i)
                          (Module.finrank k
                            ↥(ModuleCat.Hom.hom
                                  ((TauCeti.cellularChainComplex Set.univ V).d (i + 1) i)).range)
```

**The Morse polynomial identity, with the cellular coefficients.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_cwComplex_criticalCount_eq_bettiNumber_add_coeff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/BettiNumber.html#TauCeti.IsMorse.exists_cwComplex_criticalCount_eq_bettiNumber_add_coeff).

```lean
TauCeti.IsMorse.exists_cwComplex_criticalCount_eq_bettiNumber_add_coeff.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] [CompactSpace M] {f : M → ℝ}
  (hf : TauCeti.IsMorse I f) :
  ∃ W x,
    ∃ (x_1 : T2Space W),
      ∃ x_2,
        Topology.RelCWComplex.Finite Set.univ ∧
          Nonempty (ContinuousMap.HomotopyEquiv W M) ∧
            (∀ (m : ℕ),
                ENat.card (Topology.RelCWComplex.cell Set.univ m) = TauCeti.criticalCount I f m) ∧
              ∀ (k : Type u) [inst : DivisionRing k] (j : ℕ),
                TauCeti.criticalCount I f j =
                  ↑(TauCeti.bettiNumber k M j +
                      ((1 + Polynomial.X) *
                            ∑ i ∈ Finset.range (Module.finrank ℝ E),
                              (Polynomial.monomial i)
                                (Module.finrank k
                                  ↥(ModuleCat.Hom.hom
                                        ((TauCeti.cellularChainComplex Set.univ ↧k).d (i + 1)
                                          i)).range)).coeff
                        j)
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/BettiNumber.html#TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff)
- [Source of `TauCeti.IsMorse.exists_criticalCount_eq_bettiNumber_add_coeff` in TauCeti/Geometry/Manifold/Morse/BettiNumber.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/BettiNumber.lean#L119)
