---
declaration: def
origin: cited
lean: TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate
statement: formalized
---

# The certificate of the class number column of the LMFDB record of `E₈`

It extends
`TauCeti.IntegralLattice.typeE₈StoredGenusCertificate` by the mass `1 / 696729600` of the genus
and the class number `1`.

```lean
TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate :
  TauCeti.IntegralLattice.StoredClassNumberCertificate 8
```

## Depends on

- [The class number column of an LMFDB lattice record, with the mass that certifies it](the-class-number-column-of-an-lmfdb-lattice-reco.md)
- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.mass](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-mass.md)

## Proof depends on

- [The isometry group of the E₈ lattice has order `240 · 126 · 23040 = 696729600`](the-isometry-group-of-the-e8-lattice-has-order-2.md)
- [The mass of the genus of `E₈` is `1 / 696729600`](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/the-mass-of-the-genus-of-e8-is-1-696729600.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.html#TauCeti.IntegralLattice.typeE%E2%82%88StoredClassNumberCertificate).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.html#TauCeti.IntegralLattice.typeE%E2%82%88StoredClassNumberCertificate)
- [Source of `TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate` in TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.lean#L108)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
