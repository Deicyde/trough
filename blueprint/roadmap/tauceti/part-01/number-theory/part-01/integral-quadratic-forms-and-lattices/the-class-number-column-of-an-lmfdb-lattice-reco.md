---
declaration: structure
origin: cited
lean: TauCeti.IntegralLattice.StoredClassNumberCertificate
statement: formalized
---

# The class number column of an LMFDB lattice record, with the mass that certifies it

It
extends the certificate of the stored columns by the stored class number, which is the number of
stored representatives, and by a rational number `mass` together with

* the imported hypothesis `mass_eq` that `mass` is the mass of the genus of the stored lattice,
  and
* the finite check `sum_inv_natCard_isometry_reps_eq_mass` that the stored representatives
  already carry the whole mass.

Completeness of the list of representatives is not a field: it is the theorem
`TauCeti.IntegralLattice.StoredClassNumberCertificate.classNumber_eq_classNumber_lattice`.

```lean
TauCeti.IntegralLattice.StoredClassNumberCertificate (n : ℕ) : Type
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.mass](../../../linear-algebra/part-01/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-mass.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.html#TauCeti.IntegralLattice.StoredClassNumberCertificate).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.html#TauCeti.IntegralLattice.StoredClassNumberCertificate)
- [Source of `TauCeti.IntegralLattice.StoredClassNumberCertificate` in TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.lean#L62)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/IntegralLattices/STATUS.md)
