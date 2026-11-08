---
declaration: theorem
origin: cited
lean: TauCeti.cup_kummerClass_eq_hilbertSymbol_smul
statement: formalized
proof: formalized
---

# A Kummer cup over a local field is its Hilbert symbol times a fixed nonzero cup

if
`(c, e)_K = -1`, then `(a) ∪ (b) = ε • ((c) ∪ (e))`, where `ε ∈ ZMod 2` is `0` if `(a, b)_K = 1`
and `1` if `(a, b)_K = -1`.

```lean
TauCeti.cup_kummerClass_eq_hilbertSymbol_smul.{u} {K : Type u} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Invertible 2] {c e : Kˣ}
  (hce : TauCeti.hilbertSymbol c e = -1) (a b : Kˣ) :
  (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1) (TauCeti.kummerClass a))
      (TauCeti.kummerClass b) =
    TauCeti.additiveIntUnitsAddEquiv (Additive.ofMul (TauCeti.hilbertSymbol a b)) •
      (((TauCeti.trivialF2TopPairing (TauCeti.AbsoluteGaloisGroup K)).cup 1 1)
          (TauCeti.kummerClass c))
        (TauCeti.kummerClass e)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The comparison isomorphism `Br(K) ≃ H²_cont(G_K, (Kˢ)ˣ)` with Mathlib's continuous cohomology, for `K` in any universe](the-comparison-isomorphism-br-k-h2-cont-g-k-ks-x.md)
- [The cup-norm theorem](../../../field-theory/other-results/the-cup-norm-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The Skolem-Noether theorem](../../../algebra/central-simple/the-skolem-noether-theorem.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [Witt decomposition](../../../linear-algebra/quadratic-form/witt-decomposition.md)
- [Witt's chain theorem in its nontrivial range](../../../linear-algebra/quadratic-form/witts-chain-theorem-in-its-nontrivial-range.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cup_kummerClass_eq_hilbertSymbol_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/Basic.html#TauCeti.cup_kummerClass_eq_hilbertSymbol_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.cup_kummerClass_eq_hilbertSymbol_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/Basic.html#TauCeti.cup_kummerClass_eq_hilbertSymbol_smul)
- [Source of `TauCeti.cup_kummerClass_eq_hilbertSymbol_smul` in TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/Cup/Basic.lean#L57)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
