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

- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](the-local-invariant.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [The local class formation](the-local-class-formation.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula)
- [Source of `TauCeti.ClassFieldTheory.hilbertProductFormula` in TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean#L63)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
