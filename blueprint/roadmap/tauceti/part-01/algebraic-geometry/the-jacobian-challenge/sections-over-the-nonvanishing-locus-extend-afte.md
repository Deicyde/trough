---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection
statement: formalized
proof: formalized
---

# Sections over the nonvanishing locus extend after tensoring with a power of the section (Hartshorne, Lemma II.5.14(b))

Let `F` be quasi-coherent and `L` invertible, and let `s` be a
section of `L` over a quasi-compact quasi-separated open `U`. For every section `t` of `F` over the
nonvanishing locus `X_s`, there are `n` and a section of `F ⊗ Lⁿ` over `U` whose restriction to
`X_s` is `t ⊗ sⁿ`.

```lean
AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection.{u}
  {X : AlgebraicGeometry.Scheme} (F : X.Modules) {L : X.Modules}
  [TauCeti.AlgebraicGeometry.SheafOfModules.isInvertible X L] [SheafOfModules.IsQuasicoherent F]
  {U : X.Opens} (hU : IsCompact ↑U) (hU' : IsQuasiSeparated ↑U)
  (s : ↑(L.presheaf.obj (Opposite.op U)))
  (t : ↑(F.presheaf.obj (Opposite.op (L.nonvanishingLocus s)))) :
  ∃ n t',
    (CategoryTheory.ConcreteCategory.hom
          ((CategoryTheory.MonoidalCategoryStruct.tensorObj F (TauCeti.tensorPow L n)).presheaf.map
            (CategoryTheory.homOfLE ⋯).op))
        t' =
      (F.tmulRight
          (AlgebraicGeometry.Scheme.Modules.tensorPowSection
            ((CategoryTheory.ConcreteCategory.hom (L.presheaf.map (CategoryTheory.homOfLE ⋯).op)) s)
            n))
        t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/TwistedSections.html#AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/LineBundle/TwistedSections.html#AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection)
- [Source of `AlgebraicGeometry.Scheme.Modules.exists_map_eq_tmulRight_tensorPowSection` in TauCeti/AlgebraicGeometry/LineBundle/TwistedSections.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/LineBundle/TwistedSections.lean#L144)
- [Tau Ceti roadmap status: The Jacobian challenge](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/JacobianChallenge/STATUS.md)
