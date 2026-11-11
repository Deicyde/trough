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
- [Source of `Polynomial.Gal.sign` in TauCeti/FieldTheory/GaloisGroups/Parity.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/GaloisGroups/Parity.lean#L39)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PolynomialGaloisGroups/STATUS.md)
