---
declaration: theorem
origin: cited
lean: TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix, TauCeti.E7Minuscule.commutatorElement_rootSubgroupPoints_adjacent
statement: formalized
proof: formalized
---

# The adjacent Chevalley commutator formula in a matrix group

for one-parameter subgroups
`x` and `y` with matrices `1 + s • Eᵢ` and `1 + t • Eⱼ` at nodes joined by Cartan entries `-1`,
the commutator `⁅x(s), y(t)⁆` has matrix `1 + (s * t) • [Eᵢ, Eⱼ]`.

```lean
TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix.{u_1,
    u_2, u_3}
  {B : Type u_1} {ι : Type u_2} (T : TauCeti.MinusculeWeightTable B ι) [Fintype ι] [DecidableEq ι]
  {R : Type u_3} [CommRing R] {G : Subgroup (GL ι R)} (x y : Multiplicative R →* ↥G) {i j : B}
  (hx : ∀ (t : R), ↑↑(x (Multiplicative.ofAdd t)) = 1 + t • (T.raisingMatrix i).map Int.cast)
  (hy : ∀ (t : R), ↑↑(y (Multiplicative.ofAdd t)) = 1 + t • (T.raisingMatrix j).map Int.cast)
  (hij : T.cartanMatrix i j = -1) (hji : T.cartanMatrix j i = -1) (s t : R) :
  ↑↑⁅x (Multiplicative.ofAdd s), y (Multiplicative.ofAdd t)⁆ =
    1 + (s * t) • T.raisingCommutatorMatrix i j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Presentation/MinusculeWeightTable/Adjacent.html#TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix).

## Other forms

**The adjacent Chevalley commutator formula on the carrier points.** Formalized in Tau Ceti as [`TauCeti.E7Minuscule.commutatorElement_rootSubgroupPoints_adjacent`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/E7/Minuscule/Adjacent.html#TauCeti.E7Minuscule.commutatorElement_rootSubgroupPoints_adjacent).

```lean
TauCeti.E7Minuscule.commutatorElement_rootSubgroupPoints_adjacent.{u_1} (positive : Bool)
  (i j : Fin 7) (R : Type u_1) [CommRing R] (hij : CartanMatrix.E 7 i j = -1) (s t : R) :
  ⁅(TauCeti.E7Minuscule.rootSubgroupPoints (TauCeti.MinusculeWeightTable.signedRootIndex positive i)
          R)
        (Multiplicative.ofAdd s),
      (TauCeti.E7Minuscule.rootSubgroupPoints
          (TauCeti.MinusculeWeightTable.signedRootIndex positive j) R)
        (Multiplicative.ofAdd t)⁆ =
    TauCeti.E7Minuscule.adjacentRootCommutator positive i j R (s * t)
```

## Sources

- [Tau Ceti documentation: `TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Presentation/MinusculeWeightTable/Adjacent.html#TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix)
- [Source of `TauCeti.MinusculeWeightTable.coe_commutatorElement_eq_one_add_smul_raisingCommutatorMatrix` in TauCeti/Algebra/Lie/Presentation/MinusculeWeightTable/Adjacent.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Lie/Presentation/MinusculeWeightTable/Adjacent.lean#L371)
