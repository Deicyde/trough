---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le, TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_of_cwComplex
statement: formalized
proof: formalized
---

# The strong Morse inequalities for a CW pair

If there are finitely many relative cells
through degree `n`, then `bₙ - bₙ₋₁ + ⋯ ± b₀ ≤ (cₙ - cₙ₋₁ + ⋯ ± c₀) · dim M`, where `bᵢ` is the
dimension of the relative singular homology and `cᵢ` the number of relative `i`-cells.

```lean
TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le.{w} {X : Type w}
  [TopologicalSpace X] [T2Space X] {k : Type w} [DivisionRing k] {D : Set X} (C : Set X)
  [Topology.RelCWComplex C D] (M : ModuleCat k) [Module.Finite k ↑M] {n : ℕ}
  (hfinite : ∀ i ≤ n, Finite (Topology.RelCWComplex.cell C i)) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) * ↑(Module.finrank k ↑((TauCeti.complexBasePair C).singularHomology M i)) ≤
    ↑(Module.finrank k ↑M) *
      ∑ i ∈ Finset.range (n + 1), (-1) ^ (n - i) * ↑(Nat.card (Topology.RelCWComplex.cell C i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The strong Morse inequalities (`ChainComplex.sum_range_neg_one_pow_mul_finrank_homology_le`)](../../algebra/homology/the-strong-morse-inequalities-chaincomplex-sum-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le).

## Other forms

**The strong Morse inequalities for a CW complex.** Formalized in Tau Ceti as [`TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_of_cwComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_of_cwComplex).

```lean
TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_le_of_cwComplex.{w} {X : Type w}
  [TopologicalSpace X] [T2Space X] {k : Type w} [DivisionRing k] (C : Set X) [Topology.CWComplex C]
  (M : ModuleCat k) [Module.Finite k ↑M] {n : ℕ}
  (hfinite : ∀ i ≤ n, Finite (Topology.RelCWComplex.cell C i)) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ (n - i) *
        ↑(Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj M).obj ↧↑C)) ≤
    ↑(Module.finrank k ↑M) *
      ∑ i ∈ Finset.range (n + 1), (-1) ^ (n - i) * ↑(Nat.card (Topology.RelCWComplex.cell C i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le)
- [Source of `TauCeti.sum_range_neg_one_pow_mul_finrank_singularHomology_complexBasePair_le` in TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean#L71)
