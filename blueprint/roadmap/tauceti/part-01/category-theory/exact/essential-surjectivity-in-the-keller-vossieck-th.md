---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity
statement: formalized
proof: formalized
---

# Essential surjectivity in the Keller–Vossieck theorem

every object of the singularity
category of a Frobenius exact category is isomorphic to an object of the category placed in degree
zero.

```lean
TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} (hF : E.IsFrobenius) : E.singleToSingularity.EssSurj
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neeman's lemma](neemans-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity)
- [Source of `TauCeti.ExactStructure.IsFrobenius.essSurj_singleToSingularity` in TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean#L610)
