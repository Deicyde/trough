---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.finrank_singularHomology_le, TauCeti.IsMorse.exists_isZero_and_finrank_le_singularHomology_sublevelPair, TauCeti.IsMorse.finrank_singularHomology_sublevelPair_le
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

- [Deformation of sublevels across a band without critical points (Milnor, Theorem 3.1)](deformation-of-sublevels-across-a-band-without-c.md)
- [The Mayer–Vietoris isomorphism of a sphere](../../../algebraic-topology/singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [Milnor's cell attachment theorem](../manifold/part-02/milnors-cell-attachment-theorem.md)
- [The relative small-chain theorem](../../../algebraic-topology/singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities for a CW pair](../../../algebraic-topology/cellular/the-strong-morse-inequalities-for-a-cw-pair.md)
- [The weak Morse inequality for a CW pair](../../../algebraic-topology/cellular/the-weak-morse-inequality-for-a-cw-pair.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_le).

## Other forms

**The weak Morse inequalities across a critical level.** Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_isZero_and_finrank_le_singularHomology_sublevelPair`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Cell/Homology.html#TauCeti.IsMorse.exists_isZero_and_finrank_le_singularHomology_sublevelPair).

```lean
TauCeti.IsMorse.exists_isZero_and_finrank_le_singularHomology_sublevelPair.{u, v, w, u_1, u_2}
  {E : Type u_1} {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} {c δ : ℝ}
  (hf : TauCeti.IsMorse I f) (hδ : 0 < δ) (hcompact : IsCompact (f ⁻¹' Set.Icc (c - δ) (c + δ))) :
  ∃ ε,
    ∃ (hε : 0 < ε),
      ε ≤ δ ∧
        (∀ {A : Type v} [inst : CategoryTheory.Category.{w, v} A]
            [inst_1 : CategoryTheory.Abelian A] [inst_2 : CategoryTheory.Limits.HasCoproducts A]
            (R : A) (n : ℕ),
            (∀ p ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' {c}, TauCeti.manifoldMorseIndex I f p ≠ n) →
              CategoryTheory.Limits.IsZero ((TauCeti.sublevelPair f ⋯).singularHomology R n)) ∧
          ∀ (k : Type u) [inst : DivisionRing k] (V : ModuleCat k) [Module.Finite k ↑V] (n : ℕ),
            Module.Finite k ↑((TauCeti.sublevelPair f ⋯).singularHomology V n) ∧
              Module.finrank k ↑((TauCeti.sublevelPair f ⋯).singularHomology V n) ≤
                Nat.card { p // TauCeti.manifoldMorseIndex I f ↑p = n } * Module.finrank k ↑V
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

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.finrank_singularHomology_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Inequalities.html#TauCeti.IsMorse.finrank_singularHomology_le)
- [Source of `TauCeti.IsMorse.finrank_singularHomology_le` in TauCeti/Geometry/Manifold/Morse/Inequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Morse/Inequalities.lean#L503)
