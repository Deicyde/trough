---
declaration: theorem
origin: cited
lean: TauCeti.Place.residueAut_residue
statement: formalized
proof: formalized
---

# The residue action, on residues (Stichtenoth, Theorem 3.8.2)

the automorphism of `F'_P`
induced by `g` sends the residue of an element `x` of `𝒪_P` to the residue of `g x`.

```lean
TauCeti.Place.residueAut_residue.{u, v, v'} {k : Type u} (F : Type v) {F' : Type v'} [Field k]
  [Field F] [Field F'] [Algebra k F'] [Algebra F F'] (P : TauCeti.Place k F') [Algebra k F]
  [IsScalarTower k F F'] [Algebra.IsIntegral F F']
  (g : ↥(ValuationSubring.decompositionSubgroup F P.integers)) (x : ↥P.integers) :
  ((TauCeti.Place.residueAut F P) g) ((IsLocalRing.residue ↥P.integers) x) =
    (IsLocalRing.residue ↥P.integers) (g • x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.residueAut_residue`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.html#TauCeti.Place.residueAut_residue).

## Sources

- [Tau Ceti documentation: `TauCeti.Place.residueAut_residue`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.html#TauCeti.Place.residueAut_residue)
- [Source of `TauCeti.Place.residueAut_residue` in TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.lean#L168)
