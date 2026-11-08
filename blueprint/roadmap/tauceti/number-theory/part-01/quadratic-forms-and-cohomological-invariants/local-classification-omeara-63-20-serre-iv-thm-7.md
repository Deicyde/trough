---
declaration: theorem
origin: cited
lean: TauCeti.RegularFormClass.localInvariants_injective
statement: formalized
proof: formalized
---

# Local classification (O'Meara 63:20, Serre IV Thm 7)

A regular-form class over a
nonarchimedean local field is determined by its rank, discriminant and local Hasse invariant.

```lean
TauCeti.RegularFormClass.localInvariants_injective.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] :
  Function.Injective TauCeti.RegularFormClass.localInvariants
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RegularFormClass.localInvariants_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariants_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.RegularFormClass.localInvariants_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.html#TauCeti.RegularFormClass.localInvariants_injective)
- [Source of `TauCeti.RegularFormClass.localInvariants_injective` in TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Invariants.lean#L140)
