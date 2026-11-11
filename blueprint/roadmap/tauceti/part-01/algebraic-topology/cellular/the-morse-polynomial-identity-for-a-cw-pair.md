---
declaration: theorem
origin: cited
lean: TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq, TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq_of_cwComplex
statement: formalized
proof: formalized
---

# The Morse polynomial identity for a CW pair

If there are finitely many relative cells
through degree `n` and none in degree `n + 1`, then in `ℕ[X]`
`∑ᵢ₌₀ⁿ cᵢ dim M · Xⁱ = ∑ᵢ₌₀ⁿ bᵢ Xⁱ + (1 + X) Q`, where `cᵢ` is the number of relative `i`-cells,
`bᵢ` the dimension of the relative singular homology, and the coefficient of `Xⁱ` in `Q` is the
rank of the cellular differential in degree `i + 1` for `i < n`, and zero otherwise.

```lean
TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq.{w} {X : Type w} [TopologicalSpace X]
  [T2Space X] {k : Type w} [DivisionRing k] {D : Set X} (C : Set X) [Topology.RelCWComplex C D]
  (M : ModuleCat k) [Module.Finite k ↑M] {n : ℕ}
  (hfinite : ∀ i ≤ n, Finite (Topology.RelCWComplex.cell C i))
  (hn : IsEmpty (Topology.RelCWComplex.cell C (n + 1))) :
  ∑ i ∈ Finset.range (n + 1),
      (Polynomial.monomial i) (Nat.card (Topology.RelCWComplex.cell C i) * Module.finrank k ↑M) =
    ∑ i ∈ Finset.range (n + 1),
        (Polynomial.monomial i)
          (Module.finrank k ↑((TauCeti.complexBasePair C).singularHomology M i)) +
      (1 + Polynomial.X) *
        ∑ i ∈ Finset.range n,
          (Polynomial.monomial i)
            (Module.finrank k
              ↥(ModuleCat.Hom.hom ((TauCeti.cellularChainComplex C M).d (i + 1) i)).range)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The Morse polynomial identity (`ChainComplex.sum_range_monomial_finrank_X_eq`)](../../algebra/part-02/homology/the-morse-polynomial-identity-chaincomplex-sum-r.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq).

## Other forms

**The Morse polynomial identity for a CW complex.** Formalized in Tau Ceti as [`TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq_of_cwComplex`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq_of_cwComplex).

```lean
TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq_of_cwComplex.{w} {X : Type w}
  [TopologicalSpace X] [T2Space X] {k : Type w} [DivisionRing k] (C : Set X) [Topology.CWComplex C]
  (M : ModuleCat k) [Module.Finite k ↑M] {n : ℕ}
  (hfinite : ∀ i ≤ n, Finite (Topology.RelCWComplex.cell C i))
  (hn : IsEmpty (Topology.RelCWComplex.cell C (n + 1))) :
  ∑ i ∈ Finset.range (n + 1),
      (Polynomial.monomial i) (Nat.card (Topology.RelCWComplex.cell C i) * Module.finrank k ↑M) =
    ∑ i ∈ Finset.range (n + 1),
        (Polynomial.monomial i)
          (Module.finrank k
            ↑(((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) i).obj M).obj ↧↑C)) +
      (1 + Polynomial.X) *
        ∑ i ∈ Finset.range n,
          (Polynomial.monomial i)
            (Module.finrank k
              ↥(ModuleCat.Hom.hom ((TauCeti.cellularChainComplex C M).d (i + 1) i)).range)
```

## Sources

- [Tau Ceti documentation: `TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.html#TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq)
- [Source of `TauCeti.sum_range_monomial_natCard_cell_mul_finrank_eq` in TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cellular/EulerCharacteristic/MorseInequalities.lean#L90)
