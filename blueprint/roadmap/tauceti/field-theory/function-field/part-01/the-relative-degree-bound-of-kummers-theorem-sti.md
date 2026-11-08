---
declaration: theorem
origin: cited
lean: TauCeti.Place.natDegree_map_residue_le_relativeDegree
statement: formalized
proof: formalized
---

# The relative degree bound of Kummer's theorem (Stichtenoth, Theorem 3.3.7)

a place `P'`
over `P` at which a monic `g` with irreducible reduction `γ` vanishes has relative degree at
least `deg γ`, because `γ` is the minimal polynomial of the residue of `y` at `P'`.

```lean
TauCeti.Place.natDegree_map_residue_le_relativeDegree.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] {P : TauCeti.Place k F} {P' : TauCeti.Place k' F'}
  (hres : TauCeti.Place.restrict k F P' = P) {y : F'} (hy : y ∈ P'.integers)
  {g : Polynomial ↥P.integers} (hg : g.Monic)
  (hirr : Irreducible (Polynomial.map (IsLocalRing.residue ↥P.integers) g))
  (hv : P'.valuation ((P.integersEval y) g) < 1) :
  (Polynomial.map (IsLocalRing.residue ↥P.integers) g).natDegree ≤
    TauCeti.Place.relativeDegree k F P'
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.natDegree_map_residue_le_relativeDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.natDegree_map_residue_le_relativeDegree).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.natDegree_map_residue_le_relativeDegree`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.natDegree_map_residue_le_relativeDegree)
- [Source of `TauCeti.Place.natDegree_map_residue_le_relativeDegree` in TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean#L293)
