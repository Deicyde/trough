---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective
statement: formalized
proof: formalized
---

# Fullness in the Keller–Vossieck theorem

every morphism between objects of a Frobenius exact
category in the singularity category comes from a morphism of the category.

```lean
TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} (hF : E.IsFrobenius) (M N : C) :
  Function.Surjective E.singleToSingularity.map
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neeman's lemma](neemans-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective)
- [Source of `TauCeti.ExactStructure.IsFrobenius.singleToSingularity_map_surjective` in TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean#L425)
