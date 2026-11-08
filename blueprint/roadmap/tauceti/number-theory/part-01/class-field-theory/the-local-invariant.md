---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.invMap
statement: formalized
---

# The local invariant

**The local invariant** `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized
by arithmetic Frobenius: on the classes inflated from an unramified extension `E/K` inside `Kˢ`
it is the invariant `TauCeti.ClassFieldTheory.unramifiedInv K E` of the layer
(`invMap_relBrInfl`).

```lean
TauCeti.ClassFieldTheory.invMap (K : Type) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] : TauCeti.ClassFieldTheory.Br K ≃+ AddCircle 1
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.invMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Brauer/Invariant.html#TauCeti.ClassFieldTheory.invMap).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.invMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Brauer/Invariant.html#TauCeti.ClassFieldTheory.invMap)
- [Source of `TauCeti.ClassFieldTheory.invMap` in TauCeti/NumberTheory/ClassFieldTheory/Brauer/Invariant.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Brauer/Invariant.lean#L196)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
