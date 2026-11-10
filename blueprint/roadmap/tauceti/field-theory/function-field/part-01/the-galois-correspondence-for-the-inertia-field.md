---
declaration: theorem
origin: cited
lean: TauCeti.Place.fixingSubgroup_inertiaField, TauCeti.Place.fixingSubgroup_decompositionField
statement: formalized
proof: formalized
---

# The Galois correspondence for the inertia field

the automorphisms of `F'` fixing the
inertia field of `P` pointwise are exactly the inertia group of `P`.

```lean
TauCeti.Place.fixingSubgroup_inertiaField.{u, v, v'} {k : Type u} (F : Type v) {F' : Type v'}
  [Field k] [Field F] [Field F'] [Algebra k F'] [Algebra F F'] (P : TauCeti.Place k F')
  [FiniteDimensional F F'] :
  (TauCeti.Place.inertiaField F P).fixingSubgroup =
    Subgroup.map (ValuationSubring.decompositionSubgroup F P.integers).subtype
      (ValuationSubring.inertiaSubgroup F P.integers)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.fixingSubgroup_inertiaField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.html#TauCeti.Place.fixingSubgroup_inertiaField).

## Other forms

**The Galois correspondence for the decomposition field.** Formalized in Tau Ceti as [`TauCeti.Place.fixingSubgroup_decompositionField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Decomposition.html#TauCeti.Place.fixingSubgroup_decompositionField).

```lean
TauCeti.Place.fixingSubgroup_decompositionField.{u, v, v'} {k : Type u} (F : Type v) {F' : Type v'}
  [Field k] [Field F] [Field F'] [Algebra k F'] [Algebra F F'] [FiniteDimensional F F']
  (P : TauCeti.Place k F') :
  (TauCeti.Place.decompositionField F P).fixingSubgroup =
    ValuationSubring.decompositionSubgroup F P.integers
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.fixingSubgroup_inertiaField`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.html#TauCeti.Place.fixingSubgroup_inertiaField)
- [Source of `TauCeti.Place.fixingSubgroup_inertiaField` in TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Place/Extension/Inertia.lean#L486)
