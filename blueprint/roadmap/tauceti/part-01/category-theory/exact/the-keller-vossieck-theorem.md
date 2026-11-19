---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity
statement: formalized
proof: formalized
---

# The Keller–Vossieck theorem

for a Frobenius exact category, the functor
`stable(E) ⥤ D_sg(E)` placing an object in degree zero is an equivalence.

```lean
TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity.{v, u} {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C]
  [CategoryTheory.Limits.HasZeroObject C] [CategoryTheory.Limits.HasBinaryBiproducts C]
  {E : TauCeti.ExactStructure C} (hF : E.IsFrobenius) : E.stableToSingularity.IsEquivalence
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Essential surjectivity in the Keller–Vossieck theorem](essential-surjectivity-in-the-keller-vossieck-th.md)
- [Faithfulness in the Keller–Vossieck theorem](faithfulness-in-the-keller-vossieck-theorem.md)
- [Fullness in the Keller–Vossieck theorem](fullness-in-the-keller-vossieck-theorem.md)
- [Neeman's lemma](neemans-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.html#TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity)
- [Source of `TauCeti.ExactStructure.IsFrobenius.isEquivalence_stableToSingularity` in TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Exact/DerivedCategory/Singularity/KellerVossieck.lean#L638)
