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
- [Source of `FDRep.trace_eq_smul` in TauCeti/RepresentationTheory/FDRep/Pivotal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/FDRep/Pivotal.lean#L60)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
