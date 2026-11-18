---
declaration: theorem
origin: cited
lean: TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact
statement: formalized
proof: formalized
---

# Effective descent for schemes affine over the cover (Stacks, Tag 0245)

Let
`p : S' ⟶ S` be surjective, flat and quasi-compact, over an arbitrary base `S`. Every descent datum
relative to `p` on a scheme affine over `S'` is isomorphic to the canonical descent datum on the
base change of a scheme affine over `S`.

```lean
TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact.{u}
  {S S' : AlgebraicGeometry.Scheme} {p : S' ⟶ S} [AlgebraicGeometry.Surjective p]
  [AlgebraicGeometry.Flat p] [AlgebraicGeometry.QuasiCompact p] {X : CategoryTheory.Over S'}
  (D : TauCeti.DescentDatum p X) [AlgebraicGeometry.IsAffineHom X.hom] :
  ∃ X₀, AlgebraicGeometry.IsAffineHom X₀.hom ∧ ∃ f, CategoryTheory.IsIso f.hom
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/Fpqc.html#TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/Fpqc.html#TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact)
- [Source of `TauCeti.DescentDatum.exists_isAffineHom_baseChange_hom_isIso_of_quasiCompact` in TauCeti/AlgebraicGeometry/Descent/Fpqc.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Descent/Fpqc.lean#L86)
- [Tau Ceti roadmap status: Modular curves and the moduli of elliptic curves with level structure](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularCurves/STATUS.md)
