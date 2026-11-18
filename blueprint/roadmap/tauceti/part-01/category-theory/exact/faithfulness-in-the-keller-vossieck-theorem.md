---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero
statement: formalized
proof: formalized
---

# Faithfulness in the Keller–Vossieck theorem

a morphism of a Frobenius exact category which
vanishes in the singularity category factors through a projective object.

```lean
TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero.{v,
    u}
  {C : Type u} [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} (hF : E.IsFrobenius) {M N : C} (f : M ⟶ N)
  (hf : E.singleToSingularity.map f = 0) : f ∈ E.projectiveStableIdeal.hom M N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Neeman's lemma](neemans-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero)
- [Source of `TauCeti.ExactStructure.IsFrobenius.mem_projectiveStableIdeal_of_singleToSingularity_map_eq_zero` in TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean#L211)
