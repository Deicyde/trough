---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.hilbertProductFormula
statement: formalized
proof: formalized
---

# Hilbert reciprocity

For `a, b ∈ Kˣ`, the Hilbert invariants of `a` and `b` at all the
finite and infinite places of the number field `K` sum to zero.

```lean
TauCeti.ClassFieldTheory.hilbertProductFormula {K : Type} [Field K] [NumberField K] (a b : Kˣ) :
  ∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport K a b,
        TauCeti.ClassFieldTheory.finiteHilbertInvariantAt K v a b +
      ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt K w a b =
    0
```

## Depends on

- [The Kummer isomorphism](../../part-02/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](the-local-invariant.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../../part-04/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [The semi-local decomposition](../../part-05/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition.md)
- [Tate's theorem for a class formation](tates-theorem-for-a-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula)
- [Source of `TauCeti.ClassFieldTheory.hilbertProductFormula` in TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean#L63)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
