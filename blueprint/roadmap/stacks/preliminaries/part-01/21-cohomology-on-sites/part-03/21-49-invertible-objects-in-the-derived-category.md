---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.finiteFreeSummandEquivalenceFiniteProjective, AlgebraicGeometry.RingedSite.finiteFreeSummandEquivalenceFiniteProjective_iso_globalSections, AlgebraicGeometry.RingedSite.InvertibleDerived.isPerfect_of_hasInvertibleModuleDecomposition, AlgebraicGeometry.RingedSite.InvertibleDerived.IsInvertibleObject, AlgebraicGeometry.RingedSite.InvertibleDerived.HasLocalInvertibleDegree, AlgebraicGeometry.RingedSite.InvertibleDerived.isInvertibleObject_tfae
statement: formalized
proof: formalized
---

# 21.49 Invertible objects in the derived category

Section 21.49 of the Stacks Project, [Tag 0FPW](https://stacks.math.columbia.edu/tag/0FPW). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FPX, a lemma

[Tag 0FPX](https://stacks.math.columbia.edu/tag/0FPX) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.finiteFreeSummandEquivalenceFiniteProjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/SummandsOfFiniteFreeModules.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/SummandsOfFiniteFreeModules.lean#L585). The attribute's comment: “the equivalence”.

> On a ringed site `(C, O)` with `R = Γ(C, O)`, the category of `O`-modules which are summands
> of finite free modules is equivalent to the category of finite projective `R`-modules.

```lean
def finiteFreeSummandEquivalenceFiniteProjective :
    ObjectProperty.FullSubcategory X.IsDirectSummandOfFiniteFree ≌
      ObjectProperty.FullSubcategory
        (fun M : ModuleCat.{max u w}
            (Stacks.Cohomology.SiteModules.GlobalSectionRing
              (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) =>
          Module.Finite
              (Stacks.Cohomology.SiteModules.GlobalSectionRing
                (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) M ∧
            Module.Projective
              (Stacks.Cohomology.SiteModules.GlobalSectionRing
                (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) M)
```

**`AlgebraicGeometry.RingedSite.finiteFreeSummandEquivalenceFiniteProjective_iso_globalSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/SummandsOfFiniteFreeModules.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/SummandsOfFiniteFreeModules.lean#L699). The attribute's comment: “identification with global sections”.

> The equivalence `finiteFreeSummandEquivalenceFiniteProjective` is given by taking global
> sections.

```lean
def finiteFreeSummandEquivalenceFiniteProjective_iso_globalSections :
    X.finiteFreeSummandEquivalenceFiniteProjective.functor ⋙ ObjectProperty.ι _ ≅
      ObjectProperty.ι _ ⋙
        Stacks.Cohomology.SiteModules.globalSectionsFunctor
          (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
```

## Tag 0FPY, a lemma

[Tag 0FPY](https://stacks.math.columbia.edu/tag/0FPY) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.InvertibleDerived.isPerfect_of_hasInvertibleModuleDecomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjects.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjects.lean#L459). The attribute's comment: “clause (2) implies that M is a perfect object of D(O)”.

> **Stacks 0FPY, the perfectness conclusion.** Let `(C, O)` be a ringed site and let `M` be an
> object of `D(O)`. If there is a locally finite direct product decomposition
> `O = ∏_{n ∈ ℤ} O_n` of the structure sheaf and for each `n` an invertible `O_n`-module `ℋ^n`
> with `M = ⨁ ℋ^n[-n]` in `D(O)`, then `M` is a perfect object of `D(O)`.
>
> On a covering of every object only finitely many factors survive, each `ℋ^n` is there a direct
> summand of a finite free `O_n`-module and `O_n` is a direct summand of `O`, so the complex with
> `ℋ^n` in degree `n` and zero differentials — which represents `⨁ ℋ^n[-n]` — is locally
> strictly perfect.

```lean
theorem isPerfect_of_hasInvertibleModuleDecomposition (M : DerivedModules X.O)
    (hM : HasInvertibleModuleDecomposition X M) : X.IsPerfect M
```

**`AlgebraicGeometry.RingedSite.InvertibleDerived.IsInvertibleObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsClauseThree.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsClauseThree.lean#L114). The attribute's comment: “clause (1) as a condition on M: that M is invertible in D(O) in the sense of Stacks 0FFN, for the symmetric monoidal structure of Stacks 0FPT. This is the clause, not an implication between clauses”.

> **Clause (1) of Stacks 0FPY.** `M` is an invertible object of `D(O)`: there is an object `N`
> of `D(O)` with `M ⊗^L N ≅ O` and `N ⊗^L M ≅ O`, the tensor product being the derived tensor
> product of Stacks 0FPT and `O` the structure sheaf in degree zero.

```lean
def IsInvertibleObject (M : DerivedModules X.O) : Prop
```

**`AlgebraicGeometry.RingedSite.InvertibleDerived.HasLocalInvertibleDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsClauseThree.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsClauseThree.lean#L172). The attribute's comment: “clause (3) as a condition on M: that every object U of the site has a covering {U_i → U} and for each i an integer n_i with M|_{U_i} isomorphic in D(O_{U_i}) to an invertible O_{U_i}-module placed in degree n_i. This is the clause, not an implication between clauses”.

> **Clause (3) of Stacks 0FPY.** Every object `U` of the site has a covering `{U_i → U}` and
> for each `i` an integer `n_i` such that `M|_{U_i}` is represented by an invertible
> `O_{U_i}`-module placed in degree `n_i`: there are an invertible `O_{U_i}`-module `L` and an
> isomorphism `M|_{U_i} ≅ L[-n_i]` in `D(O_{U_i})`.
>
> `M|_{U_i}` is the image of `M` under the functor `D(O) ⥤ D(O_{U_i})` induced by the exact
> restriction functor `Mod(O) ⥤ Mod(O_{U_i})`, and `L[-n_i]` is `L` placed in degree `n_i`. The
> derived category `D(O_{U_i})` is read in its standard model `HasDerivedCategory.standard`; any
> two models are equivalent compatibly with their localization functors, so the condition does not
> depend on that reading.

```lean
def HasLocalInvertibleDegree (M : DerivedModules X.O) : Prop
```

**`AlgebraicGeometry.RingedSite.InvertibleDerived.isInvertibleObject_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsTFAE.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Perfect/InvertibleObjectsTFAE.lean#L165). The attribute's comment: “All of the tag: (1) ⟺ (2) on every ringed site; (1) implies that M is perfect; and (1) ⟺ (2) ⟺ (3) on a locally ringed site. The ringed site is RingedSite.{u, u, u} -- objects, morphisms and sections of O in one universe u. This is the library's one-universe convention for D(O) as a symmetric monoidal category: the derived tensor product of Stacks 0FPT on a ringed site (Stacks.SheafOfModules.DerivedMonoidal.derivedMonoidal) is built from the K-flat resolutions of Stacks 06YS, which the library constructs at that universe pattern only, so clause (1) has no meaning off it. The four HasSheafify / WEqualsLocallyBijective instance arguments are the library's standard ones, and Mathlib synthesizes all four for every RingedSite.{u, u, u}”.

> **Stacks 0FPY.** Let `(C, O)` be a ringed site and let `M` be an object of `D(O)`. The
> following are equivalent:
>
> 1. `M` is invertible in `D(O)` (`IsInvertibleObject`: Stacks 0FFN for the derived tensor product
>    of Stacks 0FPT);
> 2. there is a locally finite direct product decomposition `O = ∏_{n ∈ ℤ} O_n` and for each `n` an
>    invertible `O_n`-module `ℋ^n` (Stacks 0409) with `M = ⨁ ℋ^n[-n]` in `D(O)`
>    (`HasInvertibleModuleDecomposition`).
>
> If they hold, `M` is a perfect object of `D(O)` (`AlgebraicGeometry.RingedSite.IsPerfect`,
> Stacks 08G5). If `(C, O)` is a locally ringed site (Stacks 04EU) they are also equivalent to
>
> 3. for every object `U` of `C` there are a covering `{U_i → U}` and integers `n_i` such that
>    `M|_{U_i}` is isomorphic in `D(O_{U_i})` to an invertible `O_{U_i}`-module placed in degree
>    `n_i` (`HasLocalInvertibleDegree`).
>
> `D(O)` is any model of the derived category. The ringed site has its objects, its morphisms and
> its rings of sections in one universe; see the note of the `stacks` attribute.

```lean
theorem isInvertibleObject_tfae (M : DerivedCategory (Mod X.O)) :
    [IsInvertibleObject X M, HasInvertibleModuleDecomposition X M].TFAE ∧
      (IsInvertibleObject X M → X.IsPerfect M) ∧
      (IsLocallyRinged X →
        [IsInvertibleObject X M, HasInvertibleModuleDecomposition X M,
          HasLocalInvertibleDegree X M].TFAE)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.49, Tag 0FPW](https://stacks.math.columbia.edu/tag/0FPW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
