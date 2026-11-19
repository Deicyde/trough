---
declaration: def
origin: cited
lean: Polynomial.Gal.sign
statement: formalized
---

# Polynomial.Gal.sign

The parity character of the action of `p.Gal` on the distinct roots of `p` in its splitting
field. It takes values in `ℤˣ`, independently of the characteristic of the base field.

```lean
Polynomial.Gal.sign.{u} {F : Type u} [Field F] (p : Polynomial F) : p.Gal →* ℤˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.Gal.sign`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Parity.html#Polynomial.Gal.sign).

## Sources

- [Tau Ceti documentation: `Polynomial.Gal.sign`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Parity.html#Polynomial.Gal.sign)
- [Source of `Polynomial.Gal.sign` in TauCeti/FieldTheory/GaloisGroups/Parity.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisGroups/Parity.lean#L39)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
