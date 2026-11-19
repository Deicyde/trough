---
declaration: theorem
origin: cited
lean: TauCeti.Place.natDegree_map_residue_le_relativeDegree
statement: formalized
proof: formalized
---

# The relative degree bound of Kummer's theorem (Stichtenoth, Theorem 3.3.7)

let `P'` be a
place over `P` at which `y` is integral, and let `g` be a polynomial over `𝒪_P` with irreducible
reduction `γ` such that `g (y)` vanishes at `P'`. Then `P'` has relative degree at least `deg γ`,
because `γ` is associated to the minimal polynomial of the residue of `y` at `P'`, and so has the
same degree.

```lean
TauCeti.Place.natDegree_map_residue_le_relativeDegree.{u, u', v, v'} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] {P : TauCeti.Place k F} {P' : TauCeti.Place k' F'}
  (hres : TauCeti.Place.restrict k F P' = P) {y : F'} (hy : y ∈ P'.integers)
  {g : Polynomial ↥P.integers}
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
- [Source of `TauCeti.Place.natDegree_map_residue_le_relativeDegree` in TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.lean#L335)
