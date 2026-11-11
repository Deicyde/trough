---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.finrank_singularHomology_le, TauCeti.finrank_singularHomology_sphere_le_and_sum_eq_and_not_exists_isMorse, TauCeti.IsMorse.finrank_singularHomology_sublevelPair_le, TauCeti.IsMorse.finrank_singularHomology_bandPair_le, TauCeti.IsMorse.finrank_singularHomology_upperBandPair_le
statement: formalized
proof: formalized
---

# The weak Morse inequalities

For a Morse function `f` on a compact boundaryless manifold
`M`, the singular homology `Hₙ(M; V)` has dimension at most `dim V` times the number of critical
points of index `n`.

```lean
TauCeti.IsMorse.finrank_singularHomology_le.{u, u_1, u_2} {E : Type u_1} {H : Type u_2} {M : Type u}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [I.Boundaryless]
  [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k] (V : ModuleCat k)
  [Module.Finite k ↑V] [CompactSpace M] (hf : TauCeti.IsMorse I f) (n : ℕ) :
  Module.finrank k ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj V).obj ↧M) ≤
    (TauCeti.criticalCount I f n).toNat * Module.finrank k ↑V
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler--Poincaré for cellular chains](../../../../algebraic-topology/cellular/euler-poincare-for-cellular-chains.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem, in pushout form](../part-01/milnors-cell-attachment-theorem-in-pushout-form.md)
- [The relative small-chain theorem](../../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities (`TauCeti.IsMorse.sum_range_neg_one_pow_mul_finrank_singularHomology_le`)](../part-01/the-strong-morse-inequalities-tauceti-ismorse-su.md)
- [The strong Morse inequalities for a CW pair](../../../../algebraic-topology/cellular/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../../algebraic-topology/cellular/the-weak-morse-inequality-for-a-cw-pair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_le).

## Other forms

**The weak Morse inequalities and Euler's equality do not imply the strong ones.** Formalized in Tau Ceti as [`TauCeti.finrank_singularHomology_sphere_le_and_sum_eq_and_not_exists_isMorse`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Sphere/Inequalities.html#TauCeti.finrank_singularHomology_sphere_le_and_sum_eq_and_not_exists_isMorse).

```lean
TauCeti.finrank_singularHomology_sphere_le_and_sum_eq_and_not_exists_isMorse.{u} {E : Type u}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] {n : ℕ} [Fact (Module.finrank ℝ E = n + 1)]
  (hn : Odd n) (h3 : 3 ≤ n) {k : Type u} [DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] :
  (∀ (j : ℕ),
      Module.finrank k
          ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) j).obj V).obj
              ↧↑(Metric.sphere 0 1)) ≤
        (if j = 0 ∨ j = n then 2 else 0) * Module.finrank k ↑V) ∧
    (∑ j ∈ Finset.range (n + 1),
          (-1) ^ j *
            ↑(Module.finrank k
                ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) j).obj V).obj
                    ↧↑(Metric.sphere 0 1))) =
        ↑(Module.finrank k ↑V) *
          ∑ j ∈ Finset.range (n + 1), (-1) ^ j * if j = 0 ∨ j = n then 2 else 0) ∧
      ¬∃ f,
          TauCeti.IsMorse (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) f ∧
            ∀ (j : ℕ),
              TauCeti.criticalCount (modelWithCornersSelf ℝ (EuclideanSpace ℝ (Fin n))) f j =
                if j = 0 ∨ j = n then 2 else 0
```

**The weak Morse inequalities for a band.** Formalized in Tau Ceti as [`TauCeti.IsMorse.finrank_singularHomology_sublevelPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_sublevelPair_le).

```lean
TauCeti.IsMorse.finrank_singularHomology_sublevelPair_le.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f) {a b : ℝ} (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  Module.finrank k ↑((TauCeti.sublevelPair f hab).singularHomology V n) ≤
    {x |
          x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
            TauCeti.manifoldMorseIndex I f x = n}.ncard *
      Module.finrank k ↑V
```

**The weak Morse inequalities for a cobordism.** Formalized in Tau Ceti as [`TauCeti.IsMorse.finrank_singularHomology_bandPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_bandPair_le).

```lean
TauCeti.IsMorse.finrank_singularHomology_bandPair_le.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f) {a b : ℝ} (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  Module.finrank k ↑((TauCeti.bandPair f hab).singularHomology V n) ≤
    {x |
          x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
            TauCeti.manifoldMorseIndex I f x = n}.ncard *
      Module.finrank k ↑V
```

**The weak Morse inequalities for a cobordism relative to its outgoing boundary.** Formalized in Tau Ceti as [`TauCeti.IsMorse.finrank_singularHomology_upperBandPair_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_upperBandPair_le).

```lean
TauCeti.IsMorse.finrank_singularHomology_upperBandPair_le.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {k : Type u} [DivisionRing k]
  (V : ModuleCat k) [Module.Finite k ↑V] (hf : TauCeti.IsMorse I f) {a b : ℝ} (hab : a ≤ b)
  (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) (n : ℕ) :
  Module.finrank k ↑((TauCeti.upperBandPair f hab).singularHomology V n) ≤
    {x |
          x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ico a b ∧
            TauCeti.manifoldMorseIndex I f x + n = Module.finrank ℝ E}.ncard *
      Module.finrank k ↑V
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_le)
- [Source of `TauCeti.IsMorse.finrank_singularHomology_le` in TauCeti/Geometry/Manifold/Morse/Inequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Inequalities.lean#L986)
