---
declaration: theorem
origin: cited
lean: TauCeti.ExactStructure.acyclic_mappingCone
statement: formalized
proof: formalized
---

# Neeman's lemma

the mapping cone of a chain map between acyclic complexes is acyclic
(Bühler, Lemma 10.3).

```lean
TauCeti.ExactStructure.acyclic_mappingCone.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.Preadditive C] [CategoryTheory.Limits.HasZeroObject C]
  [CategoryTheory.Limits.HasBinaryBiproducts C] (E : TauCeti.ExactStructure C)
  {K L : CochainComplex C ℤ} (φ : K ⟶ L) (hK : E.acyclic K) (hL : E.acyclic L) :
  E.acyclic (CochainComplex.mappingCone φ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ExactStructure.acyclic_mappingCone`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Acyclic.html#TauCeti.ExactStructure.acyclic_mappingCone).

## Sources

- [Tau Ceti documentation: `TauCeti.ExactStructure.acyclic_mappingCone`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Exact/Acyclic.html#TauCeti.ExactStructure.acyclic_mappingCone)
- [Source of `TauCeti.ExactStructure.acyclic_mappingCone` in TauCeti/CategoryTheory/Exact/Acyclic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Exact/Acyclic.lean#L337)
