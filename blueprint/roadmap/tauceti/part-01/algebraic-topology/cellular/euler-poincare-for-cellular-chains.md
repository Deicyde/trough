---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_finrank_cellularHomology, TauCeti.eulerChar_eq_finsum_finrank_singularHomology, TauCeti.homologyEulerChar_cellularChainComplex, TauCeti.finsum_finrank_singularHomology_of_finite_cwComplex, TauCeti.finsum_finrank_singularHomology_complexBasePair, TauCeti.eulerChar_eq_finsum_finrank_singularCohomology
statement: formalized
proof: formalized
---

# Euler--Poincaré for cellular chains

For a relative CW complex with finitely many cells
through degree `n` and a finite-dimensional coefficient module `M`, if there are no `(n + 1)`-cells,
then the alternating sum of the dimensions of the cellular homology groups in degrees at most `n`
is `dim M` times the alternating count of the cells of dimension at most `n`.

```lean
TauCeti.sum_range_finrank_cellularHomology.{w} {X : Type w} [TopologicalSpace X] {D : Set X}
  (C : Set X) [Topology.RelCWComplex C D] [T2Space X] {k : Type w} [DivisionRing k]
  (M : ModuleCat k) [Module.Finite k ↑M] {n : ℕ}
  (hfinite : ∀ i ≤ n, Finite (Topology.RelCWComplex.cell C i))
  (hn : IsEmpty (Topology.RelCWComplex.cell C (n + 1))) :
  ∑ i ∈ Finset.range (n + 1),
      (-1) ^ i *
        ↑(Module.finrank k ↑(HomologicalComplex.homology (TauCeti.cellularChainComplex C M) i)) =
    ↑(Module.finrank k ↑M) *
      ∑ i ∈ Finset.range (n + 1), (-1) ^ i * ↑(Nat.card (Topology.RelCWComplex.cell C i))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler–Poincaré for cubes](../../algebra/part-02/homology/euler-poincare-for-cubes.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The universal coefficient theorem over a field](../cohomology/the-universal-coefficient-theorem-over-a-field.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_finrank_cellularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Basic.html#TauCeti.sum_range_finrank_cellularHomology).

## Other forms

**Euler--Poincaré for a space of finite CW type.** Formalized in Tau Ceti as [`TauCeti.eulerChar_eq_finsum_finrank_singularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/FiniteCWType.html#TauCeti.eulerChar_eq_finsum_finrank_singularHomology).

```lean
TauCeti.eulerChar_eq_finsum_finrank_singularHomology.{w} (X : Type w) [TopologicalSpace X]
  [TauCeti.FiniteCWType X] (k : Type w) [DivisionRing k] :
  TauCeti.eulerChar X =
    ∑ᶠ (i : ℕ),
      (-1) ^ i *
        ↑(Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj ↧k).obj ↧X))
```

**Euler--Poincaré for a finite relative CW complex.** Formalized in Tau Ceti as [`TauCeti.homologyEulerChar_cellularChainComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Basic.html#TauCeti.homologyEulerChar_cellularChainComplex).

```lean
TauCeti.homologyEulerChar_cellularChainComplex.{w} {X : Type w} [TopologicalSpace X] {D : Set X}
  (C : Set X) [Topology.RelCWComplex C D] [T2Space X] {k : Type w} [DivisionRing k]
  (M : ModuleCat k) [Module.Finite k ↑M] [Topology.RelCWComplex.Finite C] :
  HomologicalComplex.homologyEulerChar (TauCeti.cellularChainComplex C M) =
    ↑(Module.finrank k ↑M) * TauCeti.cwEulerChar C
```

**Euler--Poincaré for ordinary singular homology.** Formalized in Tau Ceti as [`TauCeti.finsum_finrank_singularHomology_of_finite_cwComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Singular.html#TauCeti.finsum_finrank_singularHomology_of_finite_cwComplex).

```lean
TauCeti.finsum_finrank_singularHomology_of_finite_cwComplex.{w} {X : Type w} [TopologicalSpace X]
  [T2Space X] (C : Set X) [Topology.CWComplex C] {k : Type w} [DivisionRing k] (M : ModuleCat k)
  [Module.Finite k ↑M] [Topology.RelCWComplex.Finite C] :
  ∑ᶠ (i : ℕ),
      (-1) ^ i *
        ↑(Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj M).obj ↧↑C)) =
    ↑(Module.finrank k ↑M) * TauCeti.cwEulerChar C
```

**Euler--Poincaré for relative singular homology.** Formalized in Tau Ceti as [`TauCeti.finsum_finrank_singularHomology_complexBasePair`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Singular.html#TauCeti.finsum_finrank_singularHomology_complexBasePair).

```lean
TauCeti.finsum_finrank_singularHomology_complexBasePair.{w} {X : Type w} [TopologicalSpace X]
  [T2Space X] {D : Set X} (C : Set X) [Topology.RelCWComplex C D] {k : Type w} [DivisionRing k]
  (M : ModuleCat k) [Module.Finite k ↑M] [Topology.RelCWComplex.Finite C] :
  ∑ᶠ (i : ℕ), (-1) ^ i * ↑(Module.finrank k ↑((TauCeti.complexBasePair C).singularHomology M i)) =
    ↑(Module.finrank k ↑M) * TauCeti.cwEulerChar C
```

**Euler--Poincaré in cohomology for a space of finite CW type.** Formalized in Tau Ceti as [`TauCeti.eulerChar_eq_finsum_finrank_singularCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Cohomology.html#TauCeti.eulerChar_eq_finsum_finrank_singularCohomology).

```lean
TauCeti.eulerChar_eq_finsum_finrank_singularCohomology.{w} (X : Type w) [TopologicalSpace X]
  [TauCeti.FiniteCWType X] (k : Type w) [Field k] :
  TauCeti.eulerChar X =
    ∑ᶠ (i : ℕ), (-1) ^ i * ↑(Module.finrank k ↑(TopCat.singularCohomology (↧k) k (↧k) (↧X) i))
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_finrank_cellularHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Basic.html#TauCeti.sum_range_finrank_cellularHomology)
- [Source of `TauCeti.sum_range_finrank_cellularHomology` in TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/Basic.lean#L138)
