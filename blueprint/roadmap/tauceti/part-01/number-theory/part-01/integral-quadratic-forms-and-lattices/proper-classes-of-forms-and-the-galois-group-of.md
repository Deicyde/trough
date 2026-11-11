---
declaration: def
origin: cited
lean: TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal
statement: formalized
---

# Proper classes of forms and the Galois group of the ring class field

The proper classes
of primitive positive definite forms of discriminant `-n` are in bijection with the Galois group
of the ring class field of the quadratic order of discriminant `-n` over `ℚ(√(-n))`: the
bijection with the Picard group of the order, followed by ring-class reciprocity.

```lean
TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal (n : ℕ) [NeZero n]
  (hn : -↑n % 4 = 0 ∨ -↑n % 4 = 1) :
  TauCeti.BinaryQuadraticForm.PosDefProperClass n ≃
    Gal(↥(TauCeti.ClassFieldTheory.ringClassField
          (TauCeti.QuadraticOrder.numberFieldOrder (-↑n) hn))/QuadraticAlgebra ℚ (↑(-↑n)) 0)
```

## Depends on

- [The global class formation](../class-field-theory/the-global-class-formation.md)
- [The ring class field of an order `O` of a number field `K`](../class-field-theory/the-ring-class-field-of-an-order-o-of-a-number-f.md)
- [Tate's theorem for a class formation, in every integer degree](../class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.BinaryQuadraticForm.posDefProperClassEquivPic](tauceti-binaryquadraticform-posdefproperclassequ.md)

## Proof depends on

- [Global existence (Milne VII, Theorem 9.5)](../class-field-theory/global-existence-milne-vii-theorem-9-5.md)
- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](../global-number-fields-ray-classes-adeles-and-heck/isdedekinddomain-finiteadelering-sintegraladeles.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal).

## Sources

- [Tau Ceti documentation: `TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal`](https://taucetiproject.org/docs/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.html#TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal)
- [Source of `TauCeti.BinaryQuadraticForm.posDefProperClassEquivGal` in TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/BinaryQuadraticForm/Ideal/RingClassField.lean#L79)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
