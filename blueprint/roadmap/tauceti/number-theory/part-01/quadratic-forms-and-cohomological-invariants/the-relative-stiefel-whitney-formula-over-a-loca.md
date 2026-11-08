---
declaration: theorem
origin: cited
lean: TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq
statement: formalized
proof: formalized
---

# The relative Stiefel–Whitney formula over a local field

for a quadratic extension `L` of a
local field `K` and `a ∈ Lˣ`, the Evens norm `N^{Ev}((a)) ∈ H²(G_K, 𝔽₂)`, taken along any
`K`-embedding `σ` of `L` into a separable closure of `K`, vanishes exactly when the twisted trace
form `Tr_*⟨a⟩` and the trace form `Tr_*⟨1⟩` have the same local Hasse invariant.

```lean
TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq.{u} {K L : Type u} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] [Field L]
  [Algebra K L] [FiniteDimensional K L] [Invertible 2] (σ : L →ₐ[K] SeparableClosure K)
  (hfin : Module.finrank K L = 2) (a : Lˣ) (ha : QuadraticMap.Nondegenerate)
  (h1 : QuadraticMap.Nondegenerate) :
  TauCeti.galoisEvens K L σ hfin (TauCeti.kummerClass a) = 0 ↔
    (TauCeti.formClass (QuadraticMap.traceTransfer K (↑a • QuadraticMap.sq)) ha).localHasse =
      (TauCeti.formClass (QuadraticMap.traceTransfer K QuadraticMap.sq) h1).localHasse
```

## Depends on

- [The index-two degree-one Evens norm](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-index-two-degree-one-evens-norm.md)

## Proof depends on

- [Artin--Wedderburn over a separably closed field](../../../algebra/central-simple/artin-wedderburn-over-a-separably-closed-field.md)
- [The comparison isomorphism](the-comparison-isomorphism.md)
- [The cup-norm theorem](../../../field-theory/other-results/the-cup-norm-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [Serre's formula for the Evens norm of a Kummer class (Serre, Théorème 1′ at `n = 2`)](../../../field-theory/other-results/serres-formula-for-the-evens-norm-of-a-kummer-cl.md)
- [The Skolem-Noether theorem](../../../algebra/central-simple/the-skolem-noether-theorem.md)
- [The splitting criterion for quaternion algebras](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Wedderburn-Artin for central simple algebras](../../../algebra/central-simple/wedderburn-artin-for-central-simple-algebras.md)
- [Witt decomposition](../../../linear-algebra/quadratic-form/witt-decomposition.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.html#TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq)
- [Source of `TauCeti.galoisEvens_kummerClass_eq_zero_iff_localHasse_eq` in TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/StiefelWhitney/Transfer.lean#L127)
