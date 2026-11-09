---
declaration: theorem
origin: cited
lean: TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum, TauCeti.PairColorSystem.card_mul_sq_pairColorDensity_sub_le_sum
statement: formalized
proof: formalized
---

# Cauchy–Schwarz on a resolved witness

The squared deviation of its density from any
real number `a`, multiplied by its size, is bounded by the sum of the squared deviations of
the fine densities from `a`. The empty witness is allowed.

```lean
TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum.{u_1, u_3, u_4} {κ : Type u_1}
  {κ₂' : Type u_3} {V : Type u_4} [Fintype V] [DecidableEq V] [DecidableEq κ]
  (H : TauCeti.Colored3Graph κ V) {T : TauCeti.PairSkeleton3 κ₂' V} (c : κ)
  (U : Finset { x // Function.Injective x })
  (hU :
    ∀ (x y : { x // Function.Injective x }),
      TauCeti.Polyad3.ofTriple T x = TauCeti.Polyad3.ofTriple T y → (x ∈ U ↔ y ∈ U))
  (a : ℝ) :
  ↑U.card * (↑(H.relDensityOn c U) - a) ^ 2 ≤
    ∑ x ∈ U, (↑(H.relativeDensity c (TauCeti.Polyad3.ofTriple T x)) - a) ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/Increment.html#TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum).

## Other forms

**Cauchy–Schwarz on a resolved rectangle.** Formalized in Tau Ceti as [`TauCeti.PairColorSystem.card_mul_sq_pairColorDensity_sub_le_sum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/PairColor/Energy.html#TauCeti.PairColorSystem.card_mul_sq_pairColorDensity_sub_le_sum).

```lean
TauCeti.PairColorSystem.card_mul_sq_pairColorDensity_sub_le_sum.{u_1, u_2} {κ : Type u_1}
  {V : Type u_2} [Fintype V] [DecidableEq V] (S : TauCeti.PairColorSystem κ V)
  {Q : Finpartition Finset.univ} {X Y : Finset V} (hX : ∀ C ∈ Q.parts, C ⊆ X ∨ Disjoint C X)
  (hY : ∀ C ∈ Q.parts, C ⊆ Y ∨ Disjoint C Y) (c : κ) (a : ℝ) :
  ↑{p ∈ X ×ˢ Y | p.1 ≠ p.2}.card * (↑(TauCeti.pairColorDensity S c X Y) - a) ^ 2 ≤
    ∑ p ∈ X ×ˢ Y with p.1 ≠ p.2, (↑(TauCeti.pairColorDensity S c (Q.part p.1) (Q.part p.2)) - a) ^ 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Polyad/Increment.html#TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum)
- [Source of `TauCeti.Colored3Graph.card_mul_sq_relDensityOn_sub_le_sum` in TauCeti/Combinatorics/Hypergraph/Polyad/Increment.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Hypergraph/Polyad/Increment.lean#L73)
