---
declaration: theorem
origin: cited
lean: TauCeti.finrank_singularHomology_complexBasePair_le, TauCeti.finrank_singularHomology_le_of_cwComplex
statement: formalized
proof: formalized
---

# The weak Morse inequality for a CW pair

In a degree with finitely many relative cells,
the relative singular homology has dimension at most the number of cells times `dim M`.

```lean
TauCeti.finrank_singularHomology_complexBasePair_le.{w} {X : Type w} [TopologicalSpace X]
  [T2Space X] {k : Type w} [DivisionRing k] {D : Set X} (C : Set X) [Topology.RelCWComplex C D]
  (M : ModuleCat k) [Module.Finite k ↑M] (n : ℕ) [Finite (Topology.RelCWComplex.cell C n)] :
  Module.finrank k ↑((TauCeti.complexBasePair C).singularHomology M n) ≤
    Nat.card (Topology.RelCWComplex.cell C n) * Module.finrank k ↑M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [The weak Morse inequality](../../algebra/homology/the-weak-morse-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.finrank_singularHomology_complexBasePair_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.finrank_singularHomology_complexBasePair_le).

## Other forms

**The weak Morse inequality for a CW complex.** Formalized in Tau Ceti as [`TauCeti.finrank_singularHomology_le_of_cwComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.finrank_singularHomology_le_of_cwComplex).

```lean
TauCeti.finrank_singularHomology_le_of_cwComplex.{w} {X : Type w} [TopologicalSpace X] [T2Space X]
  {k : Type w} [DivisionRing k] (C : Set X) [Topology.CWComplex C] (M : ModuleCat k)
  [Module.Finite k ↑M] (n : ℕ) [Finite (Topology.RelCWComplex.cell C n)] :
  Module.finrank k ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) n).obj M).obj ↧↑C) ≤
    Nat.card (Topology.RelCWComplex.cell C n) * Module.finrank k ↑M
```

## Sources

- [Tau Ceti documentation: `TauCeti.finrank_singularHomology_complexBasePair_le`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.finrank_singularHomology_complexBasePair_le)
- [Source of `TauCeti.finrank_singularHomology_complexBasePair_le` in TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean#L61)
