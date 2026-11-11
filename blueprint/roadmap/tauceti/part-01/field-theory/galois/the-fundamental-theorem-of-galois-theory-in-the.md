---
declaration: def
origin: cited
lean: TauCeti.intermediateFieldEquivClosedSubgroup
statement: formalized
---

# The fundamental theorem of Galois theory in the ambient model

For a normal extension
`E/F` the closed subgroups of `Gal(E/F)` correspond, inclusion-reversingly, to the intermediate
fields of the separable closure `separableClosure F E / F`; an intermediate field of `E` outside
the separable closure has the same fixing subgroup as its separable part.

```lean
TauCeti.intermediateFieldEquivClosedSubgroup.{u_1, u_2} {F : Type u_1} {E : Type u_2} [Field F]
  [Field E] [Algebra F E] [Normal F E] :
  IntermediateField F ↥(separableClosure F E) ≃o (ClosedSubgroup Gal(E/F))ᵒᵈ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.intermediateFieldEquivClosedSubgroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Basic.html#TauCeti.intermediateFieldEquivClosedSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.intermediateFieldEquivClosedSubgroup`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Basic.html#TauCeti.intermediateFieldEquivClosedSubgroup)
- [Source of `TauCeti.intermediateFieldEquivClosedSubgroup` in TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/Galois/AbsoluteGaloisGroup/Basic.lean#L243)
