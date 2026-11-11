---
declaration: def
origin: cited
lean: TauCeti.HasGaloisLabel
statement: formalized
---

# TauCeti.HasGaloisLabel

The Galois group of `f` carries the transitive-group label `j` of degree `n`: `f` is
separable of degree `n`, and some numbering of its roots in the splitting field by `Fin n` carries
the image of the Galois action on the roots to a conjugate of the reference subgroup
`referenceSubgroup n j`. By `TauCeti.hasGaloisLabel_iff_forall`, every numbering then does.

```lean
TauCeti.HasGaloisLabel.{u} {F : Type u} [Field F] (f : Polynomial F) {n : ℕ}
  (j : TauCeti.TransitiveGroupIndex n) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasGaloisLabel`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Label.html#TauCeti.HasGaloisLabel).

## Sources

- [Tau Ceti documentation: `TauCeti.HasGaloisLabel`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Label.html#TauCeti.HasGaloisLabel)
- [Source of `TauCeti.HasGaloisLabel` in TauCeti/FieldTheory/GaloisGroups/Label.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/FieldTheory/GaloisGroups/Label.lean#L110)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/PolynomialGaloisGroups/STATUS.md)
