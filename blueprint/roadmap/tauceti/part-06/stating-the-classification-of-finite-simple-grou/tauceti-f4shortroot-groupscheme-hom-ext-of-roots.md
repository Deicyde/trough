---
declaration: theorem
origin: cited
lean: TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup
statement: formalized
proof: formalized
---

# TauCeti.F4ShortRoot.groupScheme\_hom\_ext\_of\_rootSubgroup

**Two morphisms out of the short-root type-`F₄` carrier agree as soon as they agree on its
eight numbered root subgroups.** This drops the weight-torus hypothesis of
`TauCeti.F4ShortRoot.groupScheme_hom_ext`, which root generation of the carrier makes
redundant.

```lean
TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup {Y : CommHopfAlgCat ℤ}
  (f g : TauCeti.F4ShortRoot.groupScheme ⟶ (AlgebraicGeometry.hopfSpec ↧ℤ).obj (Opposite.op Y))
  (hroot :
    ∀ (k : Fin 4 ⊕ Fin 4),
      CategoryTheory.CategoryStruct.comp (TauCeti.F4ShortRoot.rootSubgroup k) f =
        CategoryTheory.CategoryStruct.comp (TauCeti.F4ShortRoot.rootSubgroup k) g) :
  f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/F4/ShortRoot/Generation.html#TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup).

## Sources

- [Tau Ceti documentation: `TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/F4/ShortRoot/Generation.html#TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup)
- [Source of `TauCeti.F4ShortRoot.groupScheme_hom_ext_of_rootSubgroup` in TauCeti/Algebra/Lie/F4/ShortRoot/Generation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/F4/ShortRoot/Generation.lean#L163)
- [Tau Ceti roadmap status: Stating the classification of finite simple groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CFSGStatement/STATUS.md)
