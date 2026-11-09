---
declaration: theorem
origin: cited
lean: FDRep.trace_eq_smul
statement: formalized
proof: formalized
---

# FDRep.trace_eq_smul

The categorical trace of an equivariant endomorphism of a finite-dimensional representation
is its linear trace, acting on the trivial representation by scalar multiplication.

```lean
FDRep.trace_eq_smul.{u, v} {k : Type u} {G : Type v} [Field k] [Group G] {V : FDRep k G}
  (f : V ⟶ V) :
  TauCeti.trace f =
    (LinearMap.trace k ↑V.V) (ModuleCat.Hom.hom f.hom.hom) •
      CategoryTheory.CategoryStruct.id
        (CategoryTheory.MonoidalCategoryStruct.tensorUnit (FDRep k G))
```

## Depends on

- [TauCeti.symmetricSphericalCategory](tauceti-symmetricsphericalcategory.md)

## Lean

Formalized in Tau Ceti as [`FDRep.trace_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FDRep/Pivotal.html#FDRep.trace_eq_smul).

## Sources

- [Tau Ceti documentation: `FDRep.trace_eq_smul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FDRep/Pivotal.html#FDRep.trace_eq_smul)
- [Source of `FDRep.trace_eq_smul` in TauCeti/RepresentationTheory/FDRep/Pivotal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/FDRep/Pivotal.lean#L60)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
