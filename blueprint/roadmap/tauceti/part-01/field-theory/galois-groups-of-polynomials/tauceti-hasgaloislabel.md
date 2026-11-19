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
- [Source of `TauCeti.HasGaloisLabel` in TauCeti/FieldTheory/GaloisGroups/Label.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisGroups/Label.lean#L109)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
