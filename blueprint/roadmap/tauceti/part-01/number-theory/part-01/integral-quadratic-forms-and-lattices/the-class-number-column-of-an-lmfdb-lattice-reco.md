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

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.mass](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice-mass.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IntegralLattice.StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.html#TauCeti.IntegralLattice.StoredClassNumberCertificate).

## Sources

- [Tau Ceti documentation: `TauCeti.IntegralLattice.StoredClassNumberCertificate`](https://taucetiproject.org/docs/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.html#TauCeti.IntegralLattice.StoredClassNumberCertificate)
- [Source of `TauCeti.IntegralLattice.StoredClassNumberCertificate` in TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/IntegralLattice/LMFDB/StoredClassNumberCertificate.lean#L62)
- [Tau Ceti roadmap status: Integral quadratic forms and lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/IntegralLattices/STATUS.md)
