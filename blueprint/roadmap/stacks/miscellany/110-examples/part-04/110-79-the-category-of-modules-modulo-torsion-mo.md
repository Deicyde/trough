---
declaration: section
origin: cited
lean: Stacks.Examples.localizationTorsionModuleProperty_isSerreClass, Stacks.Examples.localizedModuleFunctor_isLocalization, Stacks.Examples.fgTorsionModuleProperty_isSerreClass, Stacks.Examples.fgFractionModuleFunctor_isLocalization, Stacks.Examples.extendScalarsRat_isLocalization
statement: formalized
proof: formalized
---

# 110.79 The category of modules modulo torsion modules

Section 110.79 of the Stacks Project, [Tag 0B0J](https://stacks.math.columbia.edu/tag/0B0J). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EA5, a proposition

[Tag 0EA5](https://stacks.math.columbia.edu/tag/0EA5) in the Stacks Project.

**`Stacks.Examples.localizationTorsionModuleProperty_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean#L64). The attribute's comment: “the Serre subcategory”.

> The modules whose elements are annihilated locally by `S` form a Serre subcategory.

```lean
public instance localizationTorsionModuleProperty_isSerreClass {R : Type u} [CommRing R]
    (S : Submonoid R) :
    (localizationTorsionModuleProperty (R := R) S :
      ObjectProperty (ModuleCat.{v} R)).IsSerreClass
```

**`Stacks.Examples.localizedModuleFunctor_isLocalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean#L226). The attribute's comment: “the canonical equivalence”.

> Localizing modules at `S` presents the category of modules over `Localization S` as the Serre
> quotient by the modules whose elements are annihilated by members of `S`.
>
> In particular, `CategoryTheory.Localization.equivalenceFromModel` applied to this instance is the
> canonical equivalence from the Serre quotient to `ModuleCat (Localization S)`, and
> `CategoryTheory.Localization.qCompEquivalenceFromModelFunctorIso` identifies its composite with
> the quotient functor with `ModuleCat.localizedModuleFunctor S`.

```lean
public instance localizedModuleFunctor_isLocalization {R : Type u} [CommRing R]
    (S : Submonoid R) [Small.{v, u} R] :
    (ModuleCat.localizedModuleFunctor.{v} S).IsLocalization
      (localizationTorsionModuleProperty (R := R) S :
        ObjectProperty (ModuleCat.{v} R)).isoModSerre
```

## Tag 0B0K, a proposition

[Tag 0B0K](https://stacks.math.columbia.edu/tag/0B0K) in the Stacks Project.

**`Stacks.Examples.localizedModuleFunctor_isLocalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/ModulesModuloTorsion.lean#L226). The attribute's comment: “the case S = nonzerodivisors: Mod_A modulo torsion is equivalent to Mod_{Q(A)}”.

> Localizing modules at `S` presents the category of modules over `Localization S` as the Serre
> quotient by the modules whose elements are annihilated by members of `S`.
>
> In particular, `CategoryTheory.Localization.equivalenceFromModel` applied to this instance is the
> canonical equivalence from the Serre quotient to `ModuleCat (Localization S)`, and
> `CategoryTheory.Localization.qCompEquivalenceFromModelFunctorIso` identifies its composite with
> the quotient functor with `ModuleCat.localizedModuleFunctor S`.

```lean
public instance localizedModuleFunctor_isLocalization {R : Type u} [CommRing R]
    (S : Submonoid R) [Small.{v, u} R] :
    (ModuleCat.localizedModuleFunctor.{v} S).IsLocalization
      (localizationTorsionModuleProperty (R := R) S :
        ObjectProperty (ModuleCat.{v} R)).isoModSerre
```

## Tag 0B0L, a proposition

[Tag 0B0L](https://stacks.math.columbia.edu/tag/0B0L) in the Stacks Project.

**`Stacks.Examples.fgTorsionModuleProperty_isSerreClass`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FGModulesModuloTorsion.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FGModulesModuloTorsion.lean#L89). The attribute's comment: “the Serre subcategory”.

> Finitely generated torsion modules form a Serre subcategory.

```lean
public instance fgTorsionModuleProperty_isSerreClass (A : Type u) [CommRing A]
    [IsNoetherianRing A] :
    (fgTorsionModuleProperty A : ObjectProperty (FGModuleCat.{v} A)).IsSerreClass
```

**`Stacks.Examples.fgFractionModuleFunctor_isLocalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FGModulesModuloTorsion.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FGModulesModuloTorsion.lean#L195). The attribute's comment: “the canonical equivalence”.

> Localizing finitely generated modules at the nonzerodivisors presents the category of
> finite-dimensional fraction-field vector spaces as their Serre quotient by the torsion
> modules.

```lean
public instance fgFractionModuleFunctor_isLocalization (A : Type u) [CommRing A]
    [IsDomain A] [IsNoetherianRing A] [Small.{v, u} A] :
    (fgFractionModuleFunctor A : FGModuleCat.{v} A ⥤
      FGModuleCat.{v} (FractionRing A)).IsLocalization
      (fgTorsionModuleProperty A : ObjectProperty (FGModuleCat.{v} A)).isoModSerre
```

## Tag 0B0M, a proposition

[Tag 0B0M](https://stacks.math.columbia.edu/tag/0B0M) in the Stacks Project.

**`Stacks.Examples.extendScalarsRat_isLocalization`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/AbelianGroupsModuloTorsion.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/AbelianGroupsModuloTorsion.lean#L95).

> Rationalization presents rational vector spaces as the Serre quotient of abelian groups by
> torsion groups.

```lean
public instance extendScalarsRat_isLocalization :
    (ModuleCat.extendScalars (algebraMap ℤ ℚ) :
      ModuleCat.{v} ℤ ⥤ ModuleCat.{v} ℚ).IsLocalization
      (localizationTorsionModuleProperty (R := ℤ)
        (nonZeroDivisors ℤ) : ObjectProperty (ModuleCat.{v} ℤ)).isoModSerre
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.79, Tag 0B0J](https://stacks.math.columbia.edu/tag/0B0J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
