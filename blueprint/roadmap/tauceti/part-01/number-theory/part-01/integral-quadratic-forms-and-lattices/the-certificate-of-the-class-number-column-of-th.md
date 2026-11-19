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
- [TauCeti.IntegralLattice](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.mass](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-mass.md)

## Proof depends on

- [The `E₈` root lattice is isometric to the spinor glue lattice `D₈⁺`](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/the-e8-root-lattice-is-isometric-to-the-spinor-g.md)
- [Hermite's inequality for the minimum](../../../linear-algebra/part-01/integral-lattice/hermites-inequality-for-the-minimum.md)
- [The isometry group of the E₈ lattice has order `240 · 126 · 23040 = 696729600`](the-isometry-group-of-the-e8-lattice-has-order-2.md)
- [TauCeti.FiniteQuadraticModule](tauceti-finitequadraticmodule.md)
- [TauCeti.IntegralLattice.discriminantQuadraticModule](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-discriminantquadraticmod.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.html#TauCeti.IntegralLattice.typeE%E2%82%88StoredClassNumberCertificate).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.html#TauCeti.IntegralLattice.typeE%E2%82%88StoredClassNumberCertificate)
- [Source of `TauCeti.IntegralLattice.typeE₈StoredClassNumberCertificate` in TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/IntegralLattice/LMFDB/E8.lean#L108)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
