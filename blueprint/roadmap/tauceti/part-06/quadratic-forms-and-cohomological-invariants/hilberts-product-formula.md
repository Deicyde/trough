---
declaration: theorem
origin: cited
lean: TauCeti.hilbertSymbol_productFormula
statement: formalized
proof: formalized
---

# Hilbert's product formula

For `a, b ∈ Kˣ` in a number field `K`, the product of the
norm-equation Hilbert symbols `(a_v, b_v)_v` over the finite places and of the real Hilbert symbols
`(a_w, b_w)_w` over the real places of `K` is `1`.

```lean
TauCeti.hilbertSymbol_productFormula.{u_1} {K : Type u_1} [Field K] [NumberField K] (a b : Kˣ) :
  (∏ᶠ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
        TauCeti.hilbertSymbol (v.unitAtFinitePlace a) (v.unitAtFinitePlace b)) *
      ∏ w, TauCeti.hilbertSymbol ((TauCeti.unitAtRealPlace w) a) ((TauCeti.unitAtRealPlace w) b) =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hilbert reciprocity](../../part-01/class-field-theory/hilbert-reciprocity.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.brauerCohomologyEquiv](tauceti-brauercohomologyequiv.md)
- [TauCeti.ClassFieldTheory.invMap](../../part-01/class-field-theory/tauceti-classfieldtheory-invmap.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)
- [TauCeti.QuaternionAlgebra.nonempty\_algEquiv\_matrix\_tfae](tauceti-quaternionalgebra-nonempty-algequiv-matr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbol_productFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#TauCeti.hilbertSymbol_productFormula).

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbol_productFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#TauCeti.hilbertSymbol_productFormula)
- [Source of `TauCeti.hilbertSymbol_productFormula` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L80)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
