---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.ModuleMapSituation.isoFunctorSmallEtale, AlgebraicGeometry.Space.ModuleMapSituation.surjFunctorSmallEtale, AlgebraicGeometry.Space.ModuleMapSituation.zeroFunctorSmallEtale, AlgebraicGeometry.Space.ModuleMapSituation.IsInjAt, AlgebraicGeometry.Space.ModuleMapSituation, AlgebraicGeometry.Space.ModuleMapSituation.zeroSubfunctor, AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_surjFunctor, AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_zeroFunctor
statement: formalized
proof: formalized
---

# 77.7 Flattening functors

Section 77.7 of the Stacks Project, [Tag 083E](https://stacks.math.columbia.edu/tag/083E). 9 tags here are carried by 49 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 083F, a situation

[Tag 083F](https://stacks.math.columbia.edu/tag/083F) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctorSmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean#L126). The attribute's comment: “the functor F\_iso of Equation 77.7.1.1”.

> **Stacks 083F, Equation 77.7.1.1.**  The functor `F_iso` of a map `u : ℱ ⟶ 𝒢` of
> quasi-coherent `𝒪_X`-modules: it sends a scheme `T` over `Y` to a one-element set if the base
> change `u_T` along `X ×_Y T ⟶ X` is an isomorphism, and to the empty set otherwise.
>
> The base change is taken for the inverse image of modules of Stacks 03LU for the small étale
> ringed sites, `AlgebraicGeometry.Space.modulePullback`.

```lean
abbrev isoFunctorSmallEtale : (D.SchemesOver)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Space.ModuleMapSituation.surjFunctorSmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean#L138). The attribute's comment: “the variant F\_surj”.

> **Stacks 083F, the variant `F_surj`.**  The functor sending a scheme `T` over `Y` to a
> one-element set if the base change `u_T` is surjective, and to the empty set otherwise.
>
> Surjectivity is restriction-stable because the inverse image of modules is a left adjoint and so
> preserves epimorphisms; that is
> `AlgebraicGeometry.Space.ModuleMapSituation.isSurjectiveAt_of_hom`.

```lean
abbrev surjFunctorSmallEtale : (D.SchemesOver)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Space.ModuleMapSituation.zeroFunctorSmallEtale`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean#L146). The attribute's comment: “the variant F\_zero”.

> **Stacks 083F, the variant `F_zero`.**  The functor sending a scheme `T` over `Y` to a
> one-element set if the base change `u_T` is zero, and to the empty set otherwise.

```lean
abbrev zeroFunctorSmallEtale : (D.SchemesOver)ᵒᵖ ⥤ Type u
```

**`AlgebraicGeometry.Space.ModuleMapSituation.IsInjAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociSmallEtale.lean#L161). The attribute's comment: “the variant F\_inj: the condition that u\_T is injective”.

> **Stacks 083F, the variant `F_inj`.**  The condition the source asks of a scheme `T` over
> `Y` for its variant `F_inj`: that the base change `u_T` of `u` along `X ×_Y T ⟶ X` is injective,
> which for a map of sheaves of modules is being a monomorphism.
>
> This is a condition on test schemes and *not* a subterminal presheaf on them: it is not stable
> under restriction along a morphism of test schemes, because the inverse image of modules is only
> right exact.  The file's notes give the counterexample.  The restriction-stable condition this
> development uses in its place is
> `AlgebraicGeometry.Space.ModuleMapSituation.IsUniversallyInjectiveAt`.

```lean
def IsInjAt (T : D.SchemesOver) : Prop
```

**`AlgebraicGeometry.Space.ModuleMapSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituation.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituation.lean#L94). The attribute's comment: “standing data”.

> **Stacks 083F.** The standing data of Stacks 083F: a morphism `f : X ⟶ Y` of algebraic
> spaces over `S` and a map `u : F ⟶ G` of quasi-coherent `𝒪_X`-modules.

```lean
structure ModuleMapSituation
```

**`AlgebraicGeometry.Space.ModuleMapSituation.zeroSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapZeroLocusSubspace.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapZeroLocusSubspace.lean#L198). The attribute's comment: “the variant F\_zero, read as a subfunctor of the base”.

> **`F_zero` as a subfunctor of the base.**  Its sections over an object `U` of the big fppf
> category over `S` are the sections `x` of `Y` over `U` such that the base change of `u` along
> `X ×_Y U ⟶ X`, the base change at the test scheme `x` names, is zero.

```lean
def zeroSubfunctor (D : ModuleMapSituation.{u, u} B S hS) : Subfunctor D.Y.1
```

## Tag 083H, a lemma

[Tag 083H](https://stacks.math.columbia.edu/tag/083H) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_surjFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean#L106). The attribute's comment: “F\_surj”.

> **Stacks 083H**, surjectivity clause.  The locus of test schemes over `Y` on which the base
> change of `u` is surjective is a sheaf for the fpqc topology.
>
> The locus is subterminal, so the sheaf condition is the implication from surjectivity at every
> member of a covering sieve to surjectivity at its target.  A covering sieve contains a flat
> family which is jointly surjective after base change, and surjectivity descends along such a
> family.

```lean
theorem isSheaf_surjFunctor :
    Presheaf.IsSheaf (fpqcTopology D.Y) (D.surjFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_zeroFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean#L124). The attribute's comment: “F\_zero”.

> **Stacks 083H**, vanishing clause.  The locus of test schemes over `Y` on which the base
> change of `u` vanishes is a sheaf for the fpqc topology.
>
> The locus is subterminal, so the sheaf condition is the implication from vanishing at every
> member of a covering sieve to vanishing at its target, and vanishing descends along the flat
> jointly surjective family of base-change spaces the sieve contains.

```lean
theorem isSheaf_zeroFunctor :
    Presheaf.IsSheaf (fpqcTopology D.Y) (D.zeroFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_isoFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean#L142). The attribute's comment: “F\_iso”.

> **Stacks 083H**, isomorphism clause.  The locus of test schemes over `Y` on which the base
> change of `u` is an isomorphism is a sheaf for the fpqc topology.
>
> The locus is subterminal, so the sheaf condition is the implication from being an isomorphism at
> every member of a covering sieve to being one at its target, and being an isomorphism descends
> along the flat jointly surjective family of base-change spaces the sieve contains.

```lean
theorem isSheaf_isoFunctor :
    Presheaf.IsSheaf (fpqcTopology D.Y) (D.isoFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isSheaf_injFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFpqcSheaf.lean#L164). The attribute's comment: “F\_inj”.

> **Stacks 083H**, universal injectivity clause.  The locus of test schemes over `Y` on which
> the base change of `u` is universally injective is a sheaf for the fpqc topology.
>
> The locus is subterminal, so the sheaf condition is the implication from universal injectivity
> at every member of a covering sieve to universal injectivity at its target.  The latter asks
> for injectivity of the base change at every test scheme `T''` over `T`; the inverse image of
> the covering sieve is a covering sieve of `T''`, and injectivity at each member of that sieve
> is one instance of universal injectivity at the corresponding member of the given sieve, so
> injectivity at `T''` follows by descent along the flat jointly surjective family of base-change
> spaces.

```lean
theorem isSheaf_injFunctor :
    Presheaf.IsSheaf (fpqcTopology D.Y) (D.injFunctor (modulePullbackSystem B S hS))
```

## Tag 083I, a lemma

[Tag 083I](https://stacks.math.columbia.edu/tag/083I) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.surjFunctor_and_zeroFunctor_inverseImageSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean#L90). The attribute's comment: “part (1): F\_surj = F'\_surj and F\_zero = F'\_zero”.

> **Stacks 083I part (1).**  In Situation 083F let `g : X' ⟶ X` be a flat morphism of
> algebraic spaces and let `u' : ℱ' ⟶ 𝒢'` be the pullback of `u` to `X'`.  If `𝒢` is of finite
> type and the image of `|X'| ⟶ |X|` contains the support of `𝒢`, then `F_surj = F'_surj` and
> `F_zero = F'_zero`.

```lean
theorem surjFunctor_and_zeroFunctor_inverseImageSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hGft : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hGsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.G) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.surjFunctor (modulePullbackSystem B S hS) =
        (D.inverseImageSituation g).surjFunctor (modulePullbackSystem B S hS) ∧
      D.zeroFunctor (modulePullbackSystem B S hS) =
        (D.inverseImageSituation g).zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_and_zeroFunctor_inverseImageSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean#L105). The attribute's comment: “part (2): F\_inj = F'\_inj and F\_zero = F'\_zero”.

> **Stacks 083I part (2).**  In Situation 083F let `g : X' ⟶ X` be a flat morphism of
> algebraic spaces and let `u' : ℱ' ⟶ 𝒢'` be the pullback of `u` to `X'`.  If `ℱ` is of finite
> type and the image of `|X'| ⟶ |X|` contains the support of `ℱ`, then `F_inj = F'_inj` and
> `F_zero = F'_zero`.

```lean
theorem injFunctor_and_zeroFunctor_inverseImageSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hFsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.F) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.injFunctor (modulePullbackSystem B S hS) =
        (D.inverseImageSituation g).injFunctor (modulePullbackSystem B S hS) ∧
      D.zeroFunctor (modulePullbackSystem B S hS) =
        (D.inverseImageSituation g).zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_inverseImageSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapInverseImageLoci.lean#L120). The attribute's comment: “part (3): F\_iso = F'\_iso”.

> **Stacks 083I part (3).**  In Situation 083F let `g : X' ⟶ X` be a flat morphism of
> algebraic spaces and let `u' : ℱ' ⟶ 𝒢'` be the pullback of `u` to `X'`.  If `ℱ` and `𝒢` are of
> finite type and the image of `|X'| ⟶ |X|` contains the supports of `ℱ` and `𝒢`, then
> `F_iso = F'_iso`.

```lean
theorem isoFunctor_inverseImageSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hGft : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hFsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.F) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom))
    (hGsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.G) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.isoFunctor (modulePullbackSystem B S hS) =
      (D.inverseImageSituation g).isoFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.surjFunctor_and_zeroFunctor_pullbackSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean, line 738](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean#L738). The attribute's comment: “part (1) over `pullbackSituation`; see `inverseImageSituation`”.

> **Stacks 083I part (1).**  In the situation of Stacks 083F let `g : X' ⟶ X` be a flat
> morphism of algebraic spaces and let `u'` be the inverse image of `u` on `X'`.  If `𝒢` is of
> finite type and the image of `|X'| ⟶ |X|` contains the support of `𝒢`, then the surjectivity
> loci of `u` and `u'` agree and so do their vanishing loci.
>
> Both equalities come from the corresponding conditions at a single test scheme: the comparison
> `X' ×_Y T ⟶ X ×_Y T` of the two base changes is flat and its image contains the support of the
> base change of `𝒢`, so surjectivity and vanishing descend along it, and the loci, being
> subterminal, are determined by the conditions.
>
> The form with the quasi-coherence of `g^*ℱ` and `g^*𝒢` discharged by Stacks 03GA is
> `AlgebraicGeometry.Space.ModuleMapSituation.surjFunctor_and_zeroFunctor_inverseImageSituation_eq`.

```lean
theorem surjFunctor_and_zeroFunctor_pullbackSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hGft : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hGsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.G) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.surjFunctor (modulePullbackSystem B S hS) =
        (D.pullbackSituation g hF hG).surjFunctor (modulePullbackSystem B S hS) ∧
      D.zeroFunctor (modulePullbackSystem B S hS) =
        (D.pullbackSituation g hF hG).zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_and_zeroFunctor_pullbackSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean, line 765](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean#L765). The attribute's comment: “part (2) over `pullbackSituation`; see `inverseImageSituation`”.

> **Stacks 083I part (2).**  In the situation of Stacks 083F let `g : X' ⟶ X` be a flat
> morphism of algebraic spaces and let `u'` be the inverse image of `u` on `X'`.  If `ℱ` is of
> finite type and the image of `|X'| ⟶ |X|` contains the support of `ℱ`, then the universal
> injectivity loci of `u` and `u'` agree and so do their vanishing loci.
>
> Universal injectivity at a test scheme is injectivity of the base change over every further test
> scheme, and the two situations have the same test schemes, so the equality of the two universal
> injectivity loci follows from injectivity agreeing at every single test scheme, which is the
> descent of injectivity along the comparison of the two base changes.
>
> The form with the quasi-coherence of `g^*ℱ` and `g^*𝒢` discharged by Stacks 03GA is
> `AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_and_zeroFunctor_inverseImageSituation_eq`.

```lean
theorem injFunctor_and_zeroFunctor_pullbackSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hFsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.F) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.injFunctor (modulePullbackSystem B S hS) =
        (D.pullbackSituation g hF hG).injFunctor (modulePullbackSystem B S hS) ∧
      D.zeroFunctor (modulePullbackSystem B S hS) =
        (D.pullbackSituation g hF hG).zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_pullbackSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean, line 792](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociFlatPullback.lean#L792). The attribute's comment: “part (3) over `pullbackSituation`; see `inverseImageSituation`”.

> **Stacks 083I part (3).**  In the situation of Stacks 083F let `g : X' ⟶ X` be a flat
> morphism of algebraic spaces and let `u'` be the inverse image of `u` on `X'`.  If `ℱ` and `𝒢`
> are of finite type and the image of `|X'| ⟶ |X|` contains the supports of both, then the
> isomorphism loci of `u` and `u'` agree.
>
> The comparison `X' ×_Y T ⟶ X ×_Y T` of the two base changes is flat and its image contains the
> supports of the base changes of `ℱ` and of `𝒢`, so being an isomorphism descends along it at
> every test scheme, and the loci, being subterminal, are determined by the conditions.
>
> The form with the quasi-coherence of `g^*ℱ` and `g^*𝒢` discharged by Stacks 03GA is
> `AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_inverseImageSituation_eq`.

```lean
theorem isoFunctor_pullbackSituation_eq (hgflat : IsFlat B S hS g.hom)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hGft : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hFsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.F) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom))
    (hGsupp : supportOfSheaf B S hS D.X.1 ((SheafOfModules.toSheaf _).obj D.G) ⊆
      Set.range (pointsMap B S hS X'.1 g.hom)) :
    D.isoFunctor (modulePullbackSystem B S hS) =
      (D.pullbackSituation g hF hG).isoFunctor (modulePullbackSystem B S hS)
```

## Tag 083J, a lemma

[Tag 083J](https://stacks.math.columbia.edu/tag/083J) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_isoFunctor_of_surj_of_inj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreserving.lean, line 317](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreserving.lean#L317). The attribute's comment: “clause (3), reduced to clause (1) and limit preservation of F\_inj; both carried”.

> **Stacks 083J, clause (3), reduced.**  The isomorphism locus `F_iso` is limit preserving
> once the surjectivity locus `F_surj` and the universal injectivity locus `F_inj` are.
>
> The source deduces clause (3) from clauses (1) and (2) through the kernel of `u_{T_0}`; this is
> the balanced-category route, available because the categories of `𝒪`-modules at hand are
> abelian, hence balanced.  It needs no finiteness hypothesis at all.  What is carried is limit
> preservation of `F_surj` — clause (1) — and of `F_inj`.
>
> **`hinj` is not supplied by Stacks 083J.**  The tag's three clauses are about `F_surj`, `F_zero`
> and `F_iso`; limit preservation of `F_inj` is asserted by none of them, so this is a reduction of
> clause (3) to a statement the source does not prove.  Worse for its usefulness, by
> `AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_eq_isoFunctor_of_epi` the two functors
> `F_inj` and `F_iso` coincide as soon as `u` is an epimorphism, so on the situations the source's
> own proof of clause (3) reduces to — those where clause (1) has produced a stage with `u`
> surjective — `hinj` is verbatim this theorem's conclusion and `hsurj` holds for free.  Neither
> carry follows from the conclusion in general, so the statement is not circular; but clause (3) is
> a theorem with nothing carried,
> `AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_isoFunctor` in
> `StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean`, by the
> source's own route — `limitPreserving_isoFunctor_iff_kernelSituation` at the stage clause (1)
> provides, with Stacks 082T for finite type of the kernel there.  Prefer that.  This statement is
> kept because it asks for no finiteness at all.

```lean
theorem limitPreserving_isoFunctor_of_surj_of_inj
    (D : ModuleMapSituation.{u, u} B S hS) (P : ModulePullbackSystem.{u, u} B S hS)
    (hsurj : LimitPreserving.{u, u, w, w'} D.testScheme (D.surjFunctor P))
    (hinj : LimitPreserving.{u, u, w, w'} D.testScheme (D.injFunctor P)) :
    LimitPreserving.{u, u, w, w'} D.testScheme (D.isoFunctor P)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_surjFunctor_iff_cokernelSituation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreserving.lean, line 470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreserving.lean#L470). The attribute's comment: “clause (1), reduced to clause (2) for the cokernel situation; (2) is carried”.

> **Stacks 083J, clause (1), reduced to clause (2).**  The surjectivity locus `F_surj` of `u`
> is limit preserving exactly when the vanishing locus `F_zero` of the cokernel situation is.
>
> The hypotheses of the two clauses match on the nose: the source module of the cokernel situation
> is `𝒢` (`cokernelSituation_F`), so clause (1)'s hypothesis that `𝒢` be of finite type with
> quasi-compact scheme-theoretic support over `B` *is* clause (2)'s hypothesis on the source
> module of the cokernel situation, and the two situations have the same test category and the
> same underlying-scheme functor (`cokernelSituation_testScheme`).  What is carried is clause (2)
> itself — and clause (2) is now a theorem, so clause (1) is available outright as
> `AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_surjFunctor` in
> `StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean`.  This
> equivalence is the whole of that proof; it is stated here because it needs nothing of
> clause (2).

```lean
theorem limitPreserving_surjFunctor_iff_cokernelSituation :
    LimitPreserving.{u, u, w, w'} D.testScheme (D.surjFunctor (modulePullbackSystem B S hS)) ↔
      LimitPreserving.{u, u, w, w'} D.testScheme
        ((D.cokernelSituation).zeroFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_zeroFunctor_of_isQuasiCompact_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean#L551). The attribute's comment: “clause (2): F\_zero is limit preserving, at the source's hypotheses verbatim -- F of finite type and its scheme-theoretic support (07U1) quasi-compact over B, i.e. Z -> X -> B quasi-compact. Nothing is carried: the support hypothesis gives compactness of the support at the affine stages (hasQuasiCompactSupportOverTarget\_of\_isQuasiCompact\_schemeTheoreticSupport: 03HF on the pasted square Z x\_X X\_T = Z x\_B T, 07U0(4), 03H4), and the rest is limitPreserving\_zeroFunctor. The index universe is the universe of the schemes, and must be: the clause is FALSE one universe up, by SmallnessNecessary/Basic.lean”.

> **Stacks 083J, clause (2), at the source's hypotheses.**  In the situation of Stacks 083F,
> if `ℱ` is of finite type and the scheme-theoretic support of `ℱ` (Stacks 07U1) is quasi-compact
> over `B`, then the vanishing locus `F_zero` is limit preserving.
>
> The support hypothesis is the source's sentence verbatim: the composite of the inclusion of the
> scheme-theoretic support `Z ⟶ X` with `f : X ⟶ B` is a quasi-compact morphism.  It implies the
> compactness at the affine stages that the proof spends, by
> `hasQuasiCompactSupportOverTarget_of_isQuasiCompact_schemeTheoreticSupport`, and then this is
> `limitPreserving_zeroFunctor`.

```lean
theorem limitPreserving_zeroFunctor_of_isQuasiCompact_schemeTheoreticSupport
    (D : ModuleMapSituation.{u, u} B S hS)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hFqc : IsQuasiCompact B S hS ((schemeTheoreticSupport B S hS D.X D.F).ι ≫ D.f.hom)) :
    LimitPreserving.{u, u, u, u} D.testScheme
      (D.zeroFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_surjFunctor_of_isQuasiCompact_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean#L573). The attribute's comment: “clause (1): F\_surj is limit preserving, at the source's hypotheses verbatim -- G of finite type and its scheme-theoretic support (07U1) quasi-compact over B, i.e. Z -> X -> B quasi-compact. Nothing is carried: the support hypothesis on G is turned into compactness at the affine stages for the cokernel situation (whose source module is G) by hasQuasiCompactSupportOverTarget\_of\_isQuasiCompact\_schemeTheoreticSupport, and the rest is limitPreserving\_surjFunctor. Index universe as in clause (2)”.

> **Stacks 083J, clause (1), at the source's hypotheses.**  In the situation of Stacks 083F,
> if `𝒢` is of finite type and the scheme-theoretic support of `𝒢` (Stacks 07U1) is
> quasi-compact over `B`, then the surjectivity locus `F_surj` is limit preserving.
>
> The cokernel situation has source module `𝒢`, source space `X` and structure morphism `f`, so
> `hasQuasiCompactSupportOverTarget_of_isQuasiCompact_schemeTheoreticSupport` applied to it turns
> the source's hypothesis on `𝒢` into the one `limitPreserving_surjFunctor` asks for.

```lean
theorem limitPreserving_surjFunctor_of_isQuasiCompact_schemeTheoreticSupport
    (D : ModuleMapSituation.{u, u} B S hS)
    (hGft : SheafOfModules.IsFiniteTypeOnSite D.G)
    (hGqc : IsQuasiCompact B S hS ((schemeTheoreticSupport B S hS D.X D.G).ι ≫ D.f.hom)) :
    LimitPreserving.{u, u, u, u} D.testScheme
      (D.surjFunctor (modulePullbackSystem B S hS))
```

**`AlgebraicGeometry.Space.ModuleMapSituation.limitPreserving_isoFunctor_of_isQuasiCompact_schemeTheoreticSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapLociLimitPreservingUnconditional.lean#L600). The attribute's comment: “clause (3): F\_iso is limit preserving, at the source's hypotheses verbatim -- F of finite type, G of finite presentation, and the scheme-theoretic supports (07U1) of F and G quasi-compact over B. Nothing is carried: the two support hypotheses are turned into compactness at the affine stages by hasQuasiCompactSupportOverTarget\_of\_isQuasiCompact\_schemeTheoreticSupport (for the situation and for its cokernel situation), and the rest is limitPreserving\_isoFunctor, the source's own deduction of (3) from (1) and (2) through ker(u\_\{T\_0}) and Stacks 082T. Index universe as in clause (2)”.

> **Stacks 083J, clause (3), at the source's hypotheses.**  In the situation of Stacks 083F,
> if `ℱ` is of finite type, `𝒢` is of finite presentation, and the scheme-theoretic supports of
> `ℱ` and `𝒢` (Stacks 07U1) are quasi-compact over `B`, then the isomorphism locus `F_iso` is
> limit preserving.
>
> Both support hypotheses are the source's sentence verbatim, and
> `hasQuasiCompactSupportOverTarget_of_isQuasiCompact_schemeTheoreticSupport`, applied to the
> situation and to its cokernel situation, turns them into the ones `limitPreserving_isoFunctor`
> asks for; a module of finite presentation is of finite type.

```lean
theorem limitPreserving_isoFunctor_of_isQuasiCompact_schemeTheoreticSupport
    (D : ModuleMapSituation.{u, u} B S hS)
    (hFft : SheafOfModules.IsFiniteTypeOnSite D.F)
    (hGfp : SheafOfModules.IsFinitePresentationOnSite D.G)
    (hFqc : IsQuasiCompact B S hS ((schemeTheoreticSupport B S hS D.X D.F).ι ≫ D.f.hom))
    (hGqc : IsQuasiCompact B S hS ((schemeTheoreticSupport B S hS D.X D.G).ι ≫ D.f.hom)) :
    LimitPreserving.{u, u, u, u} D.testScheme
      (D.isoFunctor (modulePullbackSystem B S hS))
```

## Tag 0CVM, a lemma

[Tag 0CVM](https://stacks.math.columbia.edu/tag/0CVM) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isIsoAt_secondMap_iff_isZeroAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationExact.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationExact.lean#L182). The attribute's comment: “pointwise”.

> **Stacks 0CVM**, pointwise.  For an exact sequence `F ⟶ G ⟶ H ⟶ 0` of quasi-coherent
> `𝒪_X`-modules and a scheme `T` over `Y`, the base change of `v : G ⟶ H` to `X ×_Y T` is an
> isomorphism exactly when the base change of `u : F ⟶ G` is zero.

```lean
theorem isIsoAt_secondMap_iff_isZeroAt (D : ModuleMapSituation.{u, u} B S hS)
    (H : Modules.{u, u} B S hS D.X.1 D.X.2) (hH : H.IsQuasicoherentOnSite)
    (v : D.G ⟶ H) (hcomp : D.u ≫ v = 0)
    (hexact : (ShortComplex.mk D.u v hcomp).Exact) [Epi v] (T : D.SchemesOver) :
    (D.secondMap H hH v).IsIsoAt (modulePullbackSystem B S hS) T ↔
      D.IsZeroAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_secondMap_eq_zeroFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationExact.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationExact.lean#L202).

> **Stacks 0CVM.**  For an exact sequence `F ⟶ G ⟶ H ⟶ 0` of quasi-coherent `𝒪_X`-modules,
> the locus of schemes over `Y` where the base change of `v : G ⟶ H` is an isomorphism coincides
> with the locus where the base change of `u : F ⟶ G` vanishes.

```lean
theorem isoFunctor_secondMap_eq_zeroFunctor (D : ModuleMapSituation.{u, u} B S hS)
    (H : Modules.{u, u} B S hS D.X.1 D.X.2) (hH : H.IsQuasicoherentOnSite)
    (v : D.G ⟶ H) (hcomp : D.u ≫ v = 0)
    (hexact : (ShortComplex.mk D.u v hcomp).Exact) [Epi v] :
    (D.secondMap H hH v).isoFunctor (modulePullbackSystem B S hS) =
      D.zeroFunctor (modulePullbackSystem B S hS)
```

## Tag 0CW7, a lemma

[Tag 0CW7](https://stacks.math.columbia.edu/tag/0CW7) in the Stacks Project.

**`AlgebraicGeometry.Space.AffineAdjointData.isZeroAt_adjointSituation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 571](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L571). The attribute's comment: “part (1), pointwise”.

> **Stacks 0CW7, part (1)**, pointwise: the base change of `u` to a test scheme vanishes
> exactly when the base change of its adjoint `v` does.
>
> An adjunction between preadditive categories whose right adjoint is additive carries `0` to
> `0` and is a bijection, so it carries nothing else to `0`.

```lean
theorem isZeroAt_adjointSituation_iff (T : (A.sourceSituation hqcH).SchemesOver)
    (hT : A.AdjointAfterBaseChange hqcF hqcH T) :
    (A.adjointSituation hqcF).IsZeroAt (modulePullbackSystem B S hS) T ↔
      (A.sourceSituation hqcH).IsZeroAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.AffineAdjointData.zeroFunctor_adjointSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L603). The attribute's comment: “part (1)”.

> **Stacks 0CW7, part (1)**: `F_{v,zero} = F_{u,zero}`.

```lean
theorem zeroFunctor_adjointSituation_eq
    (hT : ∀ T : (A.sourceSituation hqcH).SchemesOver, A.AdjointAfterBaseChange hqcF hqcH T) :
    (A.adjointSituation hqcF).zeroFunctor (modulePullbackSystem B S hS) =
      (A.sourceSituation hqcH).zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.AffineAdjointData.isSurjectiveAt_adjointSituation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L636). The attribute's comment: “part (2), pointwise”.

> **Stacks 0CW7, part (2)**, pointwise: for a closed immersion, the base change of `u` to a
> test scheme is surjective exactly when the base change of its adjoint `v` is.
>
> Forward, the factorisation `u_T = unit ≫ i_{T,*}(v_T)` makes `i_{T,*}(v_T)` an epimorphism,
> and the direct image along a closed immersion is fully faithful
> (`AlgebraicGeometry.Space.fullyFaithfulModulePushforward`), hence faithful, hence reflects
> epimorphisms.  Backward, the unit is an epimorphism and the direct image preserves them.

```lean
theorem isSurjectiveAt_adjointSituation_iff (T : (A.sourceSituation hqcH).SchemesOver)
    (hT : ∃ iT : (A.adjointSituation hqcF).baseChangeSpace T ⟶
        (A.sourceSituation hqcH).baseChangeSpace T,
      A.IsAdjointAfterBaseChange hqcF hqcH T iT ∧
        A.ClosedImmersionSurjectivityInput hqcF hqcH T iT) :
    (A.adjointSituation hqcF).IsSurjectiveAt (modulePullbackSystem B S hS) T ↔
      (A.sourceSituation hqcH).IsSurjectiveAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.AffineAdjointData.surjFunctor_adjointSituation_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L666). The attribute's comment: “part (2)”.

> **Stacks 0CW7, part (2)**: for a closed immersion, `F_{v,surj} = F_{u,surj}`.

```lean
theorem surjFunctor_adjointSituation_eq
    (hT : ∀ T : (A.sourceSituation hqcH).SchemesOver,
      ∃ iT : (A.adjointSituation hqcF).baseChangeSpace T ⟶
          (A.sourceSituation hqcH).baseChangeSpace T,
        A.IsAdjointAfterBaseChange hqcF hqcH T iT ∧
          A.ClosedImmersionSurjectivityInput hqcF hqcH T iT) :
    (A.adjointSituation hqcF).surjFunctor (modulePullbackSystem B S hS) =
      (A.sourceSituation hqcH).surjFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.AffineAdjointData.zeroFunctor_adjointSituation_eq_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffineAdjoint.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffineAdjoint.lean#L236). The attribute's comment: “part (1)”.

> **Stacks 0CW7, part (1), unconditionally**: for an affine `i : Z ⟶ X`, a quasi-coherent
> `𝒪_Z`-module `H` and a map `u : F ⟶ i_*H` with adjoint `v : i^*F ⟶ H`,
> `F_{v,zero} = F_{u,zero}`.

```lean
theorem zeroFunctor_adjointSituation_eq_of_isAffineHom (hi : IsAffineHom B S hS A.i.hom) :
    (A.adjointSituation A.quasicoherent_modulePullback).zeroFunctor
        (modulePullbackSystem B S hS) =
      (A.sourceSituation (A.quasicoherent_modulePushforward hi)).zeroFunctor
        (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.AffineAdjointData.surjFunctor_adjointSituation_eq_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffineAdjoint.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffineAdjoint.lean#L246). The attribute's comment: “part (2)”.

> **Stacks 0CW7, part (2), unconditionally**: if moreover `i` is a closed immersion,
> `F_{v,surj} = F_{u,surj}`.

```lean
theorem surjFunctor_adjointSituation_eq_of_isClosedImmersion (hi : IsAffineHom B S hS A.i.hom)
    (hci : IsClosedImmersion B S hS A.i.hom) :
    (A.adjointSituation A.quasicoherent_modulePullback).surjFunctor
        (modulePullbackSystem B S hS) =
      (A.sourceSituation (A.quasicoherent_modulePushforward hi)).surjFunctor
        (modulePullbackSystem B S hS)
```

## Tag 0CW8, a lemma

[Tag 0CW8](https://stacks.math.columbia.edu/tag/0CW8) in the Stacks Project.

**`AlgebraicGeometry.Space.ModuleMapSituation.isIsoAt_affinePushforward_iff'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L375). The attribute's comment: “the isomorphism locus, pointwise”.

> **Stacks 0CW8**, pointwise for the isomorphism condition: the base change of `u' = g_*u`
> to a test scheme is an isomorphism exactly when the base change of `u` is.

```lean
theorem isIsoAt_affinePushforward_iff' (T : D.SchemesOver)
    (hT : D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).IsIsoAt (modulePullbackSystem B S hS) T ↔
      D.IsIsoAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isUniversallyInjectiveAt_affinePushforward_iff'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L383). The attribute's comment: “the universal-injectivity locus, pointwise”.

> **Stacks 0CW8**, pointwise for the injectivity condition.

```lean
theorem isUniversallyInjectiveAt_affinePushforward_iff' (T : D.SchemesOver)
    (hT : ∀ T' : D.SchemesOver, D.PushforwardIdentifiesBaseChange' g f' hg comm T') :
    (D.affinePushforward' g f' hg).IsUniversallyInjectiveAt
        (modulePullbackSystem B S hS) T ↔
      D.IsUniversallyInjectiveAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isSurjectiveAt_affinePushforward_iff'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L393). The attribute's comment: “the surjectivity locus, pointwise”.

> **Stacks 0CW8**, pointwise for the surjectivity condition.

```lean
theorem isSurjectiveAt_affinePushforward_iff' (T : D.SchemesOver)
    (hT : D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).IsSurjectiveAt (modulePullbackSystem B S hS) T ↔
      D.IsSurjectiveAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isZeroAt_affinePushforward_iff'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L401). The attribute's comment: “the vanishing locus, pointwise”.

> **Stacks 0CW8**, pointwise for the vanishing condition.

```lean
theorem isZeroAt_affinePushforward_iff' (T : D.SchemesOver)
    (hT : D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).IsZeroAt (modulePullbackSystem B S hS) T ↔
      D.IsZeroAt (modulePullbackSystem B S hS) T
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_affinePushforward_eq'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L409). The attribute's comment: “F\_iso”.

> **Stacks 0CW8**, `F_{u,iso} = F_{u',iso}`.

```lean
theorem isoFunctor_affinePushforward_eq'
    (hT : ∀ T : D.SchemesOver, D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).isoFunctor (modulePullbackSystem B S hS) =
      D.isoFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_affinePushforward_eq'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L421). The attribute's comment: “F\_inj”.

> **Stacks 0CW8**, `F_{u,inj} = F_{u',inj}`.

```lean
theorem injFunctor_affinePushforward_eq'
    (hT : ∀ T : D.SchemesOver, D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).injFunctor (modulePullbackSystem B S hS) =
      D.injFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.surjFunctor_affinePushforward_eq'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 433](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L433). The attribute's comment: “F\_surj”.

> **Stacks 0CW8**, `F_{u,surj} = F_{u',surj}`.

```lean
theorem surjFunctor_affinePushforward_eq'
    (hT : ∀ T : D.SchemesOver, D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).surjFunctor (modulePullbackSystem B S hS) =
      D.surjFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.zeroFunctor_affinePushforward_eq'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean, line 445](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffine.lean#L445). The attribute's comment: “F\_zero”.

> **Stacks 0CW8**, `F_{u,zero} = F_{u',zero}`.

```lean
theorem zeroFunctor_affinePushforward_eq'
    (hT : ∀ T : D.SchemesOver, D.PushforwardIdentifiesBaseChange' g f' hg comm T) :
    (D.affinePushforward' g f' hg).zeroFunctor (modulePullbackSystem B S hS) =
      D.zeroFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.isoFunctor_affinePushforward_eq_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean#L127). The attribute's comment: “F\_iso”.

> **Stacks 0CW8**, `F_{u,iso} = F_{u',iso}`: for an affine morphism `g : X ⟶ X'` over `Y`,
> the isomorphism locus of `u` is that of its direct image `u' = g_*u`.

```lean
theorem isoFunctor_affinePushforward_eq_unconditional :
    (D.affinePushforward g f' (schemeTargetAffinePushforwardQuasicoherent B S hS) hg).isoFunctor
        (modulePullbackSystem B S hS) =
      D.isoFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.injFunctor_affinePushforward_eq_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean#L137). The attribute's comment: “F\_inj”.

> **Stacks 0CW8**, `F_{u,inj} = F_{u',inj}`: for an affine morphism `g : X ⟶ X'` over `Y`,
> the universal-injectivity locus of `u` is that of its direct image `u' = g_*u`.

```lean
theorem injFunctor_affinePushforward_eq_unconditional :
    (D.affinePushforward g f' (schemeTargetAffinePushforwardQuasicoherent B S hS) hg).injFunctor
        (modulePullbackSystem B S hS) =
      D.injFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.surjFunctor_affinePushforward_eq_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean#L147). The attribute's comment: “F\_surj”.

> **Stacks 0CW8**, `F_{u,surj} = F_{u',surj}`: for an affine morphism `g : X ⟶ X'` over `Y`,
> the surjectivity locus of `u` is that of its direct image `u' = g_*u`.

```lean
theorem surjFunctor_affinePushforward_eq_unconditional :
    (D.affinePushforward g f' (schemeTargetAffinePushforwardQuasicoherent B S hS) hg).surjFunctor
        (modulePullbackSystem B S hS) =
      D.surjFunctor (modulePullbackSystem B S hS)
```

**`AlgebraicGeometry.Space.ModuleMapSituation.zeroFunctor_affinePushforward_eq_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleMapSituationAffinePushforward.lean#L157). The attribute's comment: “F\_zero”.

> **Stacks 0CW8**, `F_{u,zero} = F_{u',zero}`: for an affine morphism `g : X ⟶ X'` over `Y`,
> the vanishing locus of `u` is that of its direct image `u' = g_*u`.

```lean
theorem zeroFunctor_affinePushforward_eq_unconditional :
    (D.affinePushforward g f' (schemeTargetAffinePushforwardQuasicoherent B S hS) hg).zeroFunctor
        (modulePullbackSystem B S hS) =
      D.zeroFunctor (modulePullbackSystem B S hS)
```

## Tag 0CWX, a situation

[Tag 0CWX](https://stacks.math.columbia.edu/tag/0CWX) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatnessSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean#L126). The attribute's comment: “standing data”.

> **Stacks 0CWX.** The standing data of Stacks 0CWX: a morphism `f : X ⟶ Y` of algebraic
> spaces over `S` and a quasi-coherent `𝒪_X`-module `F`, whose base changes to the schemes over
> `Y` are tested for flatness.

```lean
structure FlatnessSituation
```

**`AlgebraicGeometry.Space.FlatnessSituation.baseChangeModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean#L145). The attribute's comment: “the base change F\_T of the module to a test scheme over the target”.

> **Stacks 0CWX.** The base change `F_T` of the module to a test scheme `T` over `Y`: the
> pullback of `F` along the projection `X_T = X ×_Y T ⟶ X`.

```lean
def baseChangeModule (D : FlatnessSituation.{u} B S hS) (T : SchemesOver D.Y) :
    Modules.{u, u} B S hS (baseChangeSpace D.f T).1 (baseChangeSpace D.f T).2
```

**`AlgebraicGeometry.Space.FlatnessSituation.flatFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctor.lean#L202). The attribute's comment: “the functor F\_flat”.

> **Stacks 0CWX.**  The flattening functor
>
> `F_flat : (Sch/Y)ᵒᵖ ⥤ Sets`, `T ↦ {*}` if `F_T` is flat over `T` and `∅` otherwise.
>
> Its value at a test scheme is a subtype of a one-element type, cut out by flatness of the base
> change there; that this is stable under a morphism of test schemes, which is what makes the
> assignment a functor, is
> `AlgebraicGeometry.Space.FlatnessSituation.isFlatAfterBaseChange_of_hom`.

```lean
def flatFunctor (D : FlatnessSituation.{u} B S hS) : (SchemesOver D.Y)ᵒᵖ ⥤ Type u
```

## Tag 0CWZ, a lemma

[Tag 0CWZ](https://stacks.math.columbia.edu/tag/0CWZ) in the Stacks Project.

**`AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_limitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorLimitPreserving.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorLimitPreserving.lean#L218). The attribute's comment: “part (2), at the tag's own hypotheses; the index universe of the cofiltered system is the universe of the schemes, which is the largest Stacks 05LY admits”. References: EGA IV (11.2.6.1), “(ii)”.

> **Stacks 0CWZ, part (2).**  Let `f : X ⟶ Y` be a quasi-compact morphism of algebraic spaces
> over `S` which is locally of finite presentation and let `F` be a quasi-coherent `𝒪_X`-module of
> finite presentation.  Then the functor `F_flat` of equation 0CWY is limit preserving in the sense
> of Stacks 049J: it carries a cofiltered inverse limit of affine test schemes over `Y` to a
> filtered colimit of sets.
>
> `F_flat` is subterminal, so limit preservation is, by
> `AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_limitPreserving_iff`, the assertion that
> flatness of `F_T` over a cofiltered limit `T` of affine test schemes already holds over one of
> the stages.  Pick a stage, read the condition over it on an affine surjective étale scheme chart
> of `X_{T_i}` of finite presentation over `T_i`
> (`AlgebraicGeometry.Space.FlatnessSituation.exists_affine_testChart`), and the condition at every
> test scheme over that stage becomes flatness of the Zariski inverse image of the chart
> restriction over the base-changed chart scheme
> (`AlgebraicGeometry.Space.FlatnessSituation.TestChart.isFlatAfterBaseChange_baseChange_iff`).
> That is the statement the scheme-level descent theorem Stacks 05LY,
> `AlgebraicGeometry.eventually_isFlatOver_modulePullback`, descends to a stage; its hypotheses on
> the chart are finite presentation of its structure morphism and finite presentation of the
> restricted module, which are the two preceding results.

```lean
theorem flatFunctor_limitPreserving (D : FlatnessSituation.{u} B S hS)
    (hqc : IsQuasiCompact B S hS D.f.hom)
    (hlfp : IsLocallyOfFinitePresentation B S hS D.f.hom)
    (hFfp : SheafOfModules.IsFinitePresentationOnSite D.F) :
    LimitPreserving.{u, u, u, u, u + 1, u} D.testScheme D.flatFunctor
```

**`AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_isSeparatedFor_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean#L230). The attribute's comment: “part (1), separatedness half only; gluing half not proved”.

> **Stacks 0CWZ, part (1), the separatedness half of the fpqc sheaf property.** Two sections
> of `F_flat` over a test scheme which agree on the members of an fpqc covering presieve of that
> test scheme are equal.
>
> Every value of `F_flat` has at most one element, so this holds for an arbitrary presieve; the
> fpqc hypothesis is carried only so that the statement is the one the source makes.  The
> existence half of the sheaf condition is fpqc descent of flatness of the base-changed module; it
> is proved separately, so that part (1) holds in full, as
> `AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_isSheafFor_fpqc` and
> `AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_isSheaf_fpqcTopology`.

```lean
theorem flatFunctor_isSeparatedFor_fpqc (D : FlatnessSituation.{u} B S hS)
    {T : SchemesOver D.Y} (R : Presieve T)
    (_hR : R ∈ D.testFpqcPrecoverage T) :
    Presieve.IsSeparatedFor D.flatFunctor R
```

**`AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_isSheaf_fpqcTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean#L367). The attribute's comment: “part (1)”.

> **Stacks 0CWZ, part (1).**  The functor `F_flat` satisfies the sheaf property for the fpqc
> topology on the test schemes over `Y`.
>
> `F_flat` is subterminal, so the sheaf condition for a covering sieve is the implication from
> flatness of the base-changed module at every member of the sieve to flatness at its target.  A
> covering sieve of the fpqc topology contains a flat family which is jointly surjective on points
> — `AlgebraicGeometry.Space.exists_isFpqcCovering_jointlySurjective_family_of_mem_fpqcTopology` —
> and flatness of the base-changed module descends along such a family by
> `AlgebraicGeometry.Space.FlatnessSituation.isFlatAfterBaseChange_of_jointlySurjective`.

```lean
theorem flatFunctor_isSheaf_fpqcTopology (D : FlatnessSituation.{u} B S hS) :
    Presheaf.IsSheaf (fpqcTopology D.Y) D.flatFunctor
```

**`AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_isSheafFor_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean#L384). The attribute's comment: “part (1), the sheaf condition for a covering presieve”.

> **Stacks 0CWZ, part (1)**, in the presieve form: `F_flat` satisfies the sheaf condition for
> every fpqc covering presieve of a test scheme over `Y`.
>
> The sieve a covering presieve generates is a covering sieve of the fpqc topology, and every
> member of that sieve factors through a member of the presieve, along which flatness of the
> base-changed module is inherited by the final assertion of Stacks 05VW.

```lean
theorem flatFunctor_isSheafFor_fpqc (D : FlatnessSituation.{u} B S hS)
    {T : SchemesOver D.Y} (R : Presieve T) (hR : R ∈ D.testFpqcPrecoverage T) :
    Presieve.IsSheafFor D.flatFunctor R
```

**`AlgebraicGeometry.Space.FlatnessSituation.subsingleton_colimitType_flatFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorSheafAndLimits.lean#L423). The attribute's comment: “part (2), injectivity half only; surjectivity not proved”.

> **Stacks 0CWZ, part (2), the uniqueness half of limit preservation.** Along a cofiltered
> system of test schemes over `Y`, the filtered colimit of the values of `F_flat` has at most one
> element.
>
> Limit preservation asserts that the canonical map from that colimit to the value of `F_flat` at
> the limit test scheme is a bijection.  This is its injectivity half: the target also has at most
> one element (`flatFunctor_obj_subsingleton`), so no two classes in the colimit can be separated.
> It needs none of the hypotheses of part (2) — not quasi-compactness or local finite presentation
> of `f`, not finite presentation of `F` — and no restriction on the index universes.  The
> surjectivity half does need them and is
> `AlgebraicGeometry.Space.FlatnessSituation.flatFunctor_limitPreserving` of
> `StacksFrontier/AlgebraicGeometry/Spaces/FlatteningFunctorLimitPreserving.lean`, which is part (2)
> in full.

```lean
theorem subsingleton_colimitType_flatFunctor (D : FlatnessSituation.{u} B S hS)
    {I : Type w} [Category.{w'} I] [IsCofiltered I]
    (E : I ⥤ SchemesOver D.Y) :
    Subsingleton ((E.op ⋙ D.flatFunctor).ColimitType)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 77.7, Tag 083E](https://stacks.math.columbia.edu/tag/083E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
