---
declaration: def
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne
statement: formalized
---

# AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne

`f : Y ⟶ U` is **tamely ramified over `X` in codimension one**: for every codimension-one point
`ξ` of `X` outside `U` and every point `y` of `Y` whose image in `X` generizes `ξ`, the residue
field `κ(y)` is tamely ramified with respect to `𝒪_{X,ξ}`, as an algebra through
`𝒪_{X,ξ} ⟶ κ(f y) ⟶ κ(y)`. For `f` finite étale and `𝒪_{X,ξ}` a discrete valuation ring, these
residue fields are the field factors of the generic fibre `L_ξ` of `Y` over `Spec 𝒪_{X,ξ}`.

```lean
AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne.{u} {X Y : AlgebraicGeometry.Scheme}
  {U : X.Opens} (f : Y ⟶ ↑U) : Prop
```

## Depends on

- [TauCeti.Algebra.IsTamelyRamifiedWRT](tauceti-algebra-istamelyramifiedwrt.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/CodimensionOne/Ramification.html#AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Morphisms/CodimensionOne/Ramification.html#AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne)
- [Source of `AlgebraicGeometry.Scheme.Hom.IsTamelyRamifiedInCodimOne` in TauCeti/AlgebraicGeometry/Morphisms/CodimensionOne/Ramification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Morphisms/CodimensionOne/Ramification.lean#L102)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
