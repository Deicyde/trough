---
declaration: def
origin: cited
lean: TauCeti.normResidueSymbol
statement: formalized
---

# TauCeti.normResidueSymbol

The **degree-`n` norm-residue symbol**, normalized by arithmetic Frobenius.
The first argument enters the absolute local Artin map, and the second supplies an `n`-th root.
No primitive root of unity is chosen as a coordinate.

```lean
TauCeti.normResidueSymbol (K : Type) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] (n : ℕ) [NeZero n] [HasEnoughRootsOfUnity K n] (a b : Kˣ) :
  ↥(rootsOfUnity n K)
```

## Depends on

- [The local invariant](../class-field-theory/the-local-invariant.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../class-field-theory/tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.normResidueSymbol`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/NormResidueSymbol/Basic.html#TauCeti.normResidueSymbol).

## Sources

- [Tau Ceti documentation: `TauCeti.normResidueSymbol`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/NormResidueSymbol/Basic.html#TauCeti.normResidueSymbol)
- [Source of `TauCeti.normResidueSymbol` in TauCeti/NumberTheory/LocalField/NormResidueSymbol/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/LocalField/NormResidueSymbol/Basic.lean#L112)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
