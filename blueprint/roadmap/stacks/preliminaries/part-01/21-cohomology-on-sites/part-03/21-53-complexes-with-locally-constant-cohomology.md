---
declaration: section
origin: cited
lean: Stacks.ConstantSheaf.exists_cover_isRepresentedByLocallyConstantComplex, Stacks.ConstantSheaf.exists_cover_isRepresentedByLocallyConstantComplex_of_isGE_of_isLE, AlgebraicGeometry.RingedSite.exists_coveringSieve_complexMap_constant, Stacks.SheafOfModules.Constant.isStrictlyPerfect_constantModuleSheafFunctor, AlgebraicGeometry.RingedSite.exists_coveringSieve_complexMap_of_finite_projective, Stacks.ConstantSheaf.exists_cover_overPullback_eq_constantSheaf_mapHomologicalComplex, Stacks.ConstantDerivedMap.exists_cover_overPullback_map_eq_overConstantSheaf_map, Stacks.ConstantRingModules.isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor
statement: formalized
proof: formalized
---

# 21.53 Complexes with locally constant cohomology sheaves

Section 21.53 of the Stacks Project, [Tag 094F](https://stacks.math.columbia.edu/tag/094F). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 094G, a lemma

[Tag 094G](https://stacks.math.columbia.edu/tag/094G) in the Stacks Project.

**`Stacks.ConstantSheaf.exists_cover_isRepresentedByLocallyConstantComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/BoundedComplexes.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/BoundedComplexes.lean#L195). The attribute's comment: “the case of at most one nonzero cohomology sheaf”.

> **Stacks Tag 094G, the case of at most one nonzero cohomology sheaf.** Let `K` be an object of
> the derived category of sheaves of `Λ`-modules whose cohomology is concentrated in a single
> degree `n` and whose cohomology sheaves are locally constant of finite type. Then every object
> `U` of the site has a covering family `V i ⟶ U` such that the restriction of `K` to each slice
> site `C/V i` is represented by a complex of locally constant sheaves of `Λ`-modules of finite
> type, concentrated in degree `n`.

```lean
theorem exists_cover_isRepresentedByLocallyConstantComplex (n : ℤ) (U : C)
    (K : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)))
    [K.IsGE n] [K.IsLE n]
    (hK : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj K)) :
    ∃ (I : Type (max u v)) (V : I → C) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ J U ∧ ∀ i : I,
        IsRepresentedByLocallyConstantComplex.{v, max u v, w} (J.over (V i)) Λ n n
          ((J.overPullback (ModuleCat.{max u v w} Λ) (V i)).mapDerivedCategory.obj K)
```

**`Stacks.ConstantSheaf.exists_cover_isRepresentedByLocallyConstantComplex_of_isGE_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/BoundedComplexInduction.lean, line 707](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/BoundedComplexInduction.lean#L707). The attribute's comment: “the general case: the induction on the number of nonzero cohomology sheaves”.

> **Stacks Tag 094G, the general case.** Let `K` be an object of the derived category of
> sheaves of `Λ`-modules over a Noetherian ring whose cohomology is concentrated in the degrees
> `[a, b]` and all of whose cohomology sheaves are locally constant of finite type. Then every
> object `U` of the site has a covering family `V i ⟶ U` such that the restriction of `K` to each
> slice site `C / V i` is represented by a complex of locally constant sheaves of `Λ`-modules of
> finite type, concentrated in the degrees `[a, b]`.
>
> This is the statement of the source for an arbitrary number of nonzero cohomology sheaves,
> proved by the source's induction on `b - a`;
> `Stacks.ConstantSheaf.exists_cover_isRepresentedByLocallyConstantComplex` is the base case
> `a = b` of that induction. The complex produced here is in fact degreewise *constant* on each
> member of the covering family, which is more than the conclusion records.

```lean
public theorem exists_cover_isRepresentedByLocallyConstantComplex_of_isGE_of_isLE
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    (Λ : Type w) [CommRing Λ] [IsNoetherianRing Λ]
    [∀ V : C, HasWeakSheafify (J.over V) (ModuleCat.{max u v w} Λ)]
    (a b : ℤ) (hab : a ≤ b) (U : C)
    (K : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)))
    [K.IsGE a] [K.IsLE b]
    (hK : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj K)) :
    ∃ (I : Type (max u v)) (V : I → C) (f : ∀ i, V i ⟶ U),
      Sieve.ofArrows V f ∈ J U ∧ ∀ i : I,
        IsRepresentedByLocallyConstantComplex.{v, max u v, w} (J.over (V i)) Λ a b
          ((J.overPullback (ModuleCat.{max u v w} Λ) (V i)).mapDerivedCategory.obj K)
```

## Tag 09BD, a lemma

[Tag 09BD](https://stacks.math.columbia.edu/tag/09BD) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_complexMap_constant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfAConstantComplex.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfAConstantComplex.lean#L395). The attribute's comment: “local_representation_for_the_constant_complex”.

> **Maps out of the complex of constant sheaves of modules.** Let `Λ` be a commutative ring, let
> `K^•` be a bounded complex of finite projective `Λ`-modules, and let `L^•` be a complex of sheaves
> of modules over the restriction to `U` of the structure sheaf `Λ̲` of the constant ringed site.
> Any morphism `K̲^• ⟶ L^•` of `D(Λ̲|_U)` is, after restriction along the arrows of a covering sieve
> of `U`, the image under the localisation functor of a morphism of complexes.

```lean
theorem exists_coveringSieve_complexMap_constant
    [∀ W : C, HasSheafify (J.over W) AddCommGrpCat.{0}]
    [∀ W : C, (J.over W).WEqualsLocallyBijective AddCommGrpCat.{0}]
    [HasDerivedCategory.{d}
      (_root_.SheafOfModules.{0}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (constantRingedSite J Λ).O).over U))]
    {P : CochainComplex (ModuleCat.{0} Λ) ℤ} (a b : ℤ)
    [P.IsStrictlyGE a] [P.IsStrictlyLE b]
    (hfin : ∀ i : ℤ, Module.Finite Λ (P.X i)) (hproj : ∀ i : ℤ, Module.Projective Λ (P.X i))
    {F : CochainComplex
      (_root_.SheafOfModules.{0}
        ((Stacks.SheafOfModules.Tensor.ringSheaf (constantRingedSite J Λ).O).over U)) ℤ}
    (α : DerivedCategory.Q.obj
        (((constantFunctorOver J Λ U).mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ⟶
      DerivedCategory.Q.obj F) :
    ∃ S : Sieve U, S ∈ J U ∧
      ∀ {V : C} (f : V ⟶ U), S f →
        let H := _root_.SheafOfModules.overMap
          (Stacks.SheafOfModules.Tensor.ringSheaf (constantRingedSite J Λ).O) f
        ∃ (hsheaf : HasSheafify (J.over V) AddCommGrpCat)
          (hlocal : (J.over V).WEqualsLocallyBijective AddCommGrpCat),
          letI := hsheaf
          letI := hlocal
          letI : HasDerivedCategory
              (_root_.SheafOfModules
                ((Stacks.SheafOfModules.Tensor.ringSheaf (constantRingedSite J Λ).O).over V)) :=
            HasDerivedCategory.standard _
          ∃ (hadd : H.Additive)
            (hlim : PreservesFiniteLimits H)
            (hcolim : PreservesFiniteColimits H),
            letI := hadd
            letI := hlim
            letI := hcolim
            ∃ β : (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj
                (((constantFunctorOver J Λ U).mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ⟶
                (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj F,
              H.mapDerivedCategory.map α ≫ H.mapDerivedCategoryFactors.hom.app F =
                H.mapDerivedCategoryFactors.hom.app
                    (((constantFunctorOver J Λ U).mapHomologicalComplex
                      (ComplexShape.up ℤ)).obj P) ≫
                  DerivedCategory.Q.map β
```

**`Stacks.SheafOfModules.Constant.isStrictlyPerfect_constantModuleSheafFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfALocallyConstantComplex.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfALocallyConstantComplex.lean#L158). The attribute's comment: “strict_perfectness_of_the_constant_complex”.

> The complex of constant sheaves of modules on a bounded complex of finite projective
> `Λ`-modules is strictly perfect over the constant sheaf of rings `Λ̲`.

```lean
theorem isStrictlyPerfect_constantModuleSheafFunctor
    {P : CochainComplex (ModuleCat.{w} Λ) ℤ} (a b : ℤ)
    [P.IsStrictlyGE a] [P.IsStrictlyLE b]
    (hfin : ∀ i : ℤ, Module.Finite Λ (P.X i)) (hproj : ∀ i : ℤ, Module.Projective Λ (P.X i)) :
    IsStrictlyPerfect ((constantSheaf J RingCat.{w}).obj (RingCat.of Λ))
      (((constantModuleSheafFunctor J (R := Λ)).mapHomologicalComplex
        (ComplexShape.up ℤ)).obj P)
```

**`AlgebraicGeometry.RingedSite.exists_coveringSieve_complexMap_of_finite_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfALocallyConstantComplex.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/MapOutOfALocallyConstantComplex.lean#L258). The attribute's comment: “local_representation_for_a_transported_finite_projective_complex”.

> Let `Φ` be an additive right exact functor from `Λ`-modules to sheaves of `O|_U`-modules
> taking `Λ` to the unit object. Let `K^•` be a bounded complex of finite projective `Λ`-modules
> and `L^•` a complex of sheaves of `O|_U`-modules. Any morphism `Φ(K^•) ⟶ L^•` of `D(O|_U)` is,
> after restriction along the arrows of a covering sieve of `U`, the image under the localisation
> functor of a morphism of complexes.

```lean
theorem exists_coveringSieve_complexMap_of_finite_projective
    {Λ : Type} [Ring Λ]
    (Φ : ModuleCat.{0} Λ ⥤ SheafOfModules.{0} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    [Φ.Additive]
    [PreservesFiniteColimits Φ]
    (e : Φ.obj (ModuleCat.of Λ Λ) ≅
      SheafOfModules.unit ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    {P : CochainComplex (ModuleCat.{0} Λ) ℤ} (a b : ℤ)
    [P.IsStrictlyGE a] [P.IsStrictlyLE b]
    (hfin : ∀ i : ℤ, Module.Finite Λ (P.X i)) (hproj : ∀ i : ℤ, Module.Projective Λ (P.X i))
    {F : CochainComplex
      (SheafOfModules.{0} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U)) ℤ}
    (α : DerivedCategory.Q.obj ((Φ.mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ⟶
      DerivedCategory.Q.obj F) :
    ∃ S : Sieve U, S ∈ X.J U ∧
      ∀ {V : X.C} (f : V ⟶ U), S f →
        let H := SheafOfModules.overMap (Stacks.SheafOfModules.Tensor.ringSheaf X.O) f
        ∃ (hsheaf : HasSheafify (X.J.over V) AddCommGrpCat)
          (hlocal : (X.J.over V).WEqualsLocallyBijective AddCommGrpCat),
          letI := hsheaf
          letI := hlocal
          letI : HasDerivedCategory
              (SheafOfModules ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over V)) :=
            HasDerivedCategory.standard _
          ∃ (hadd : H.Additive)
            (hlim : PreservesFiniteLimits H)
            (hcolim : PreservesFiniteColimits H),
            letI := hadd
            letI := hlim
            letI := hcolim
            ∃ β : (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj
                ((Φ.mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ⟶
                (H.mapHomologicalComplex (ComplexShape.up ℤ)).obj F,
              H.mapDerivedCategory.map α ≫ H.mapDerivedCategoryFactors.hom.app F =
                H.mapDerivedCategoryFactors.hom.app
                    ((Φ.mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ≫
                  DerivedCategory.Q.map β
```

## Tag 09BE, a lemma

[Tag 09BE](https://stacks.math.columbia.edu/tag/09BE) in the Stacks Project.

**`Stacks.ConstantSheaf.exists_cover_overPullback_eq_constantSheaf_mapHomologicalComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafComplexLocalHom.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafComplexLocalHom.lean#L278). The attribute's comment: “local_constancy_of_a_map_of_constant_complexes”.

> **The local constancy of a map of complexes of constant sheaves of modules.** Let `P` be a
> complex of finite projective `Λ`-modules which is nonzero in only finitely many degrees, let `T`
> be any complex of `Λ`-modules, and write `P̲`, `T̲` for the associated complexes of constant
> sheaves of `Λ`-modules. A map of complexes `β : P̲|_U ⟶ T̲|_U` on a slice site is, after
> restriction along the arrows of a covering sieve of `U`, the image of an honest map of complexes
> `P ⟶ T` of `Λ`-modules.
>
> This is the content Stacks 09BE adds to Stacks 09BD at the level of complexes, i.e. the
> application of Stacks 093S (3) made in the source's proof.

```lean
theorem exists_cover_overPullback_eq_constantSheaf_mapHomologicalComplex
    [J.WEqualsLocallyBijective (ModuleCat.{w} Λ)]
    [∀ V : C, HasWeakSheafify (J.over V) (ModuleCat.{w} Λ)]
    [∀ V : C, (J.over V).WEqualsLocallyBijective (ModuleCat.{w} Λ)]
    (P T : CochainComplex (ModuleCat.{w} Λ) ℤ)
    (hs : {n : ℤ | ¬ IsZero (P.X n)}.Finite)
    (hfin : ∀ n : ℤ, Module.Finite Λ (P.X n))
    (hproj : ∀ n : ℤ, Module.Projective Λ (P.X n)) (U : C)
    (β : ((J.overPullback (ModuleCat.{w} Λ) U).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (((constantSheaf J (ModuleCat.{w} Λ)).mapHomologicalComplex (ComplexShape.up ℤ)).obj P) ⟶
      ((J.overPullback (ModuleCat.{w} Λ) U).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (((constantSheaf J (ModuleCat.{w} Λ)).mapHomologicalComplex (ComplexShape.up ℤ)).obj T)) :
    ∃ S : Sieve U, S ∈ J U ∧ ∀ {V : C} (f : V ⟶ U), S f →
      ∃ g : P ⟶ T, ∀ n,
        (J.overMapPullback (ModuleCat.{w} Λ) f).map (β.f n) =
          (J.overPullback (ModuleCat.{w} Λ) V).map
            ((constantSheaf J (ModuleCat.{w} Λ)).map (g.f n))
```

**`Stacks.ConstantDerivedMap.exists_cover_overPullback_map_eq_overConstantSheaf_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/DerivedMapOfConstantComplexes.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/StrictlyPerfect/DerivedMapOfConstantComplexes.lean#L515).

> **Stacks 09BE.** Let `(C, J)` be a site, `X` an object of `C` (in the source, its final
> object), `Λ` a ring, and `K`, `L` objects of `D(Λ)` with `K` perfect. Let `φ : K̲ ⟶ L̲` be a
> map in `D(C, Λ)`. There exists a covering `{U_i ⟶ X}` such that `φ|_{U_i}` is equal to
> `α̲_i` for some map `α_i : K ⟶ L` in `D(Λ)`.
>
> Here `φ|_{U_i}` is the image of `φ` under the functor `D(C, Λ) ⥤ D(C/U_i, Λ)` induced by
> restriction, and `α̲_i` is the map `K̲ ⟶ L̲` of `D(C/U_i, Λ)` induced by the constant sheaf
> functor of the slice site `C/U_i`; the two objects `(K̲)|_{U_i}` and `K̲` of `D(C/U_i, Λ)` are
> identified by the canonical isomorphism
> `Stacks.ConstantDerivedMap.overConstantSheafMapDerivedCategoryIso` (and likewise for `L`), which
> is the first conjunct. The second conjunct records the equivalent form `φ|_{U_i} = (α̲_i)|_{U_i}`,
> with `α̲_i` the constant map on `C`.
>
> The derived categories `D(Λ)`, `D(C, Λ)` and `D(C/V, Λ)` are taken with arbitrary models
> (`HasDerivedCategory` instances, which always exist: `HasDerivedCategory.standard`). The site is
> small and the modules live in its universe `u`, the library's standard one-universe convention
> for sheaves of modules on a site; the ring is commutative, as are all rings of the Stacks
> Project; and the final object `X` of the source is generalized to an arbitrary object.

```lean
theorem exists_cover_overPullback_map_eq_overConstantSheaf_map
    [HasDerivedCategory.{d} (ModuleCat.{u} Λ)]
    (X : C) {K L : DerivedCategory (ModuleCat.{u} Λ)} (hK : StacksDraft.Perfect.IsPerfect K)
    (φ : (constantSheaf J (ModuleCat.{u} Λ)).mapDerivedCategory.obj K ⟶
      (constantSheaf J (ModuleCat.{u} Λ)).mapDerivedCategory.obj L) :
    ∃ (ι : Type u) (U : ι → C) (f : ∀ i, U i ⟶ X), Sieve.ofArrows U f ∈ J X ∧
      ∀ i, ∃ α : K ⟶ L,
        (J.overPullback (ModuleCat.{u} Λ) (U i)).mapDerivedCategory.map φ =
          (overConstantSheafMapDerivedCategoryIso J Λ (U i)).inv.app K ≫
            (constantSheaf (J.over (U i)) (ModuleCat.{u} Λ)).mapDerivedCategory.map α ≫
              (overConstantSheafMapDerivedCategoryIso J Λ (U i)).hom.app L ∧
        (J.overPullback (ModuleCat.{u} Λ) (U i)).mapDerivedCategory.map φ =
          (J.overPullback (ModuleCat.{u} Λ) (U i)).mapDerivedCategory.map
            ((constantSheaf J (ModuleCat.{u} Λ)).mapDerivedCategory.map α)
```

## Tag 094H, a lemma

[Tag 094H](https://stacks.math.columbia.edu/tag/094H) in the Stacks Project.

**`Stacks.ConstantRingModules.isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/ConstantDerivedTensorLocallyConstant.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/ConstantDerivedTensorLocallyConstant.lean#L302). The attribute's comment: “the full statement for the derived tensor product over the constant sheaf of commutative rings on Λ: for K and L in D^- of the sheaves of Λ-modules whose cohomology sheaves are locally constant of finite type, so are those of K ⊗^L_Λ L. The site is small and every universe is one, which is the configuration in which the derived tensor product of Stacks 06YU is available; apart from that nothing is assumed, and in particular the bounded case of the tag is proved here and not supposed”.

> Let `(C, J)` be a small site, `Λ` a Noetherian commutative ring, and let `K` and `L` be
> objects of `D^-` of the sheaves of `Λ`-modules whose cohomology sheaves are locally constant of
> finite type. Then the cohomology sheaves of `K ⊗^L_Λ L` are locally constant of finite type, where
> the derived tensor product is `Stacks.ConstantRingModules.constantDerivedTensor`, taken over the
> constant sheaf of commutative rings on `Λ`.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor
    (K L : DerivedCategory.Minus (Sheaf J (ModuleCat.{u} Λ)))
    (hK : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj K.obj))
    (hL : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj L.obj)) (i : ℤ) :
    IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (((constantDerivedTensor J Λ).obj K.obj).obj L.obj))
```

**`Stacks.ConstantSheaf.isFiniteTypeLocallyConstantModuleSheaf_mapBifunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorBoundedAbove.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorBoundedAbove.lean#L367). The attribute's comment: “the termwise conclusion: every term of the total complex of an additive bifunctor applied to two bounded above complexes of locally constant sheaves of finite type is locally constant of finite type”.

> **Stacks Tag 094H, the termwise conclusion.** Let `P` and `Q` be cochain complexes of
> sheaves of `Λ`-modules, bounded strictly above, all of whose terms are locally constant of
> finite type, and let `T` be a bifunctor on sheaves of `Λ`-modules, additive in each variable,
> whose values on those terms are locally constant of finite type — for the sheafified tensor
> product this is
> `Stacks.ConstantSheaf.isFiniteTypeLocallyConstantModuleSheaf_tensor`. Then every term of the
> total complex of `T` applied to `P` and `Q` is locally constant of finite type.
>
> This is what the bounded case of Tag 094H consumes once Tag 094G and a finite free model have
> produced the two complexes: the derived tensor product of two such complexes is the class of
> their total tensor complex, so its cohomology sheaves are subquotients of these terms, and the
> weak Serre property of Tag 093U finishes the argument.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_mapBifunctor
    (T : Sheaf J (ModuleCat.{max u v w} Λ) ⥤ Sheaf J (ModuleCat.{max u v w} Λ) ⥤
      Sheaf J (ModuleCat.{max u v w} Λ)) [T.Additive] [∀ X, (T.obj X).Additive]
    (P Q : CochainComplex (Sheaf J (ModuleCat.{max u v w} Λ)) ℤ)
    [HomologicalComplex.HasMapBifunctor P Q T (ComplexShape.up ℤ)] (a b : ℤ)
    [P.IsStrictlyLE a] [Q.IsStrictlyLE b]
    (hT : ∀ p q, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((T.obj (P.X p)).obj (Q.X q))) (n : ℤ) :
    IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((HomologicalComplex.mapBifunctor P Q T (ComplexShape.up ℤ)).X n)
```

**`Stacks.ConstantSheaf.isFiniteTypeLocallyConstantModuleSheaf_homology_of_bounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorBoundedAbove.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorBoundedAbove.lean#L392). The attribute's comment: “the reduction of the bounded above case to the bounded case, for a bifunctor exact in each variable which carries bounds above to their sum; the bounded case is a hypothesis”.

> **Stacks Tag 094H, the reduction of the bounded above case to the bounded case.** Let `T` be
> a bifunctor on the derived category of sheaves of `Λ`-modules which is exact in each variable
> and carries objects in degrees `≤ a` and `≤ b` to objects in degrees `≤ a + b` — both are
> properties of the derived tensor product of Tag 06YU. If the conclusion of Tag 094H holds for
> bounded `K` and `L`, then it holds for `K` and `L` in `D^-`.
>
> The proof is the first half of the source's: `H^i((T.obj K).obj L)` is computed by the bounded
> truncations `τ^{> i-b-1}K` and `τ^{> i-a-1}L`.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_homology_of_bounded
    (T : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)) ⥤
      DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)) ⥤
      DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)))
    [∀ K, (T.obj K).CommShift ℤ] [∀ K, (T.obj K).IsTriangulated]
    [∀ L, (T.flip.obj L).CommShift ℤ] [∀ L, (T.flip.obj L).IsTriangulated]
    (hbound : ∀ (K L : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ))) (a b : ℤ),
      K.IsLE a → L.IsLE b → ((T.obj K).obj L).IsLE (a + b))
    (hbounded : ∀ (K L : DerivedCategory.Bounded (Sheaf J (ModuleCat.{max u v w} Λ))),
      (∀ i, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
        ((DerivedCategory.homologyFunctor _ i).obj K.obj)) →
      (∀ i, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
        ((DerivedCategory.homologyFunctor _ i).obj L.obj)) →
      ∀ i, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
        ((DerivedCategory.homologyFunctor _ i).obj ((T.obj K.obj).obj L.obj)))
    (K L : DerivedCategory.Minus (Sheaf J (ModuleCat.{max u v w} Λ)))
    (hK : ∀ i, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj K.obj))
    (hL : ∀ i, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj L.obj)) (i : ℤ) :
    IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj ((T.obj K.obj).obj L.obj))
```

## Tag 094I, a lemma

[Tag 094I](https://stacks.math.columbia.edu/tag/094I) in the Stacks Project.

**`Stacks.ConstantRingModules.isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor_quotientIdealPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/ConstantRingDerivedTensor.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/ConstantRingDerivedTensor.lean#L300). The attribute's comment: “for a site whose objects, morphisms and coefficient ring lie in one universe, which is where the library's derived tensor product over a sheaf of commutative rings is available; the derived tensor product is constructed, not a parameter. Beyond the source's own hypotheses the binders hold only `SmallCategory C`, `CommRing Λ` and `IsNoetherianRing Λ`: the sheafification conditions this file's construction uses — `HasSheafify`, `WEqualsLocallyBijective` and `HasSheafCompose` for the forgetful functor to abelian groups — are synthesized at such a site, not assumed”.

> **Stacks Tag 094I.** Let `(C, J)` be a site, `Λ` a Noetherian commutative ring, `I ⊆ Λ` an
> ideal and `K` an object of `D^-` of the sheaves of `Λ`-modules. If the cohomology sheaves of
> `K ⊗^L_Λ Λ/I` are locally constant of finite type, then so are those of `K ⊗^L_Λ Λ/Iⁿ` for every
> `n ≥ 1`.
>
> The derived tensor product is `Stacks.ConstantRingModules.constantDerivedTensor`, the derived
> tensor product of Stacks 06YU over the constant sheaf of commutative rings on `Λ` read through
> the identification of sheaves of modules over it with sheaves of `Λ`-modules. The proof is
> `isFiniteTypeLocallyConstantModuleSheaf_homology_tensor_quotientIdealPow_of_isLE`, in the
> namespace `Stacks.ConstantSheaf`, whose bifunctor parameter is instantiated here and whose two
> properties of it,
> exactness in the second variable and the degree bound, are
> `Stacks.ConstantRingModules.derivedTensor_isTriangulated` and
> `Stacks.ConstantRingModules.isLE_constantDerivedTensor`.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor_quotientIdealPow
    [IsNoetherianRing Λ] (I : Ideal Λ) (b : ℤ)
    (K : DerivedCategory (Sheaf J (ModuleCat.{u} Λ))) [K.IsLE b]
    (hbase : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ (constantDerivedTensor J Λ) K
          (ModuleCat.of Λ (Λ ⧸ I)))))
    (n : ℕ) (hn : 1 ≤ n) (i : ℤ) :
    IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ (constantDerivedTensor J Λ) K
          (ModuleCat.of Λ (Λ ⧸ I ^ n))))
```

**`Stacks.ConstantSheaf.isFiniteTypeLocallyConstantModuleSheaf_homology_derivedTensorConstant_quotientIdealPow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorConstructed.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorConstructed.lean#L345). The attribute's comment: “the derived tensor product is constructed, not assumed: it is Tag 06YU for the constant ringed site read through the equivalence Sheaf J (ModuleCat Λ) ≌ SheafOfModules Λ̲; the source's own hypotheses only”.

> **Stacks Tag 094I.** Let `(C, J)` be a site, let `Λ` be a Noetherian commutative ring, let
> `I ⊆ Λ` be an ideal and let `K` be an object of `D^-(C, Λ)`. If the cohomology sheaves of
> `K ⊗^L_Λ Λ/I` are locally constant sheaves of finite type, then so are those of
> `K ⊗^L_Λ Λ/Iⁿ` for every `n ≥ 1`.
>
> The derived tensor product is `Stacks.ConstantSheaf.constantDerivedTensor`, the derived tensor
> product of Tag 06YU for the constant ringed site read through the equivalence of Tag 03ET.
> Nothing about it is assumed: its exactness in the second variable and its bound above are the
> instances and the theorem of this file, and the mathematics of the tag is
> `isFiniteTypeLocallyConstantModuleSheaf_homology_tensor_quotientIdealPow_of_isLE`.
>
> The hypothesis `K.IsLE b` is the source's `K ∈ D^-(C, Λ)`. Local constancy of finite type is
> stated over `Λ` rather than over `Λ/Iⁿ`, which is equivalent: a `Λ`-module killed by `Iⁿ` is of
> finite type over `Λ` exactly when it is over `Λ/Iⁿ`, by
> `Stacks.ConstantSheaf.module_finite_iff_finite_quotient`, and constant for one ring exactly when
> constant for the other.
>
> `HasSheafify J (ModuleCat.{u} Λ)` is deliberately **not** a binder here: the namespace is
> reopened above with a `variable` line that does not carry it, so that the binder list is the
> source's own hypotheses and nothing else. At these universes instance search finds it, through
> Mathlib's sheafification instance for small sites.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_homology_derivedTensorConstant_quotientIdealPow
    (I : Ideal Λ) (b : ℤ) (K : DerivedCategory (Sheaf J (ModuleCat.{u} Λ))) [K.IsLE b]
    (hbase : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ (constantDerivedTensor J Λ) K (ModuleCat.of Λ (Λ ⧸ I)))))
    (n : ℕ) (hn : 1 ≤ n) :
    ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{u, u, u} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ (constantDerivedTensor J Λ) K
          (ModuleCat.of Λ (Λ ⧸ I ^ n))))
```

**`Stacks.ConstantSheaf.isFiniteTypeLocallyConstantModuleSheaf_homology_tensor_quotientIdealPow_of_isLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorGradedPieces.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/LocallyConstant/DerivedTensorGradedPieces.lean#L459). The attribute's comment: “the induction on n from Λ/I to Λ/Iⁿ, with the source's distinguished triangles and its base change to Λ/I both proved rather than assumed. The derived tensor product enters as a bifunctor parameter, and two of its properties are hypotheses: exactness in the second variable, and that it takes objects in degrees ≤ a and ≤ b to objects in degrees ≤ a + b. The parameter is instantiated, and this tag registered with nothing assumed of the derived tensor product, on Stacks.ConstantRingModules.isFiniteTypeLocallyConstantModuleSheaf_homology_constantDerivedTensor_quotientIdealPow”.

> **Stacks Tag 094I.** Let `(C, J)` be a site, let `Λ` be a Noetherian ring, let `I ⊆ Λ` be an
> ideal and let `K` be an object of `D^-` of the sheaves of `Λ`-modules. Let `T` stand for the
> derived tensor product over `Λ`: a bifunctor on that derived category which is exact in its
> second variable and carries objects in degrees `≤ a` and `≤ b` to objects in degrees `≤ a + b`.
> If the cohomology sheaves of `K ⊗^L_Λ Λ/I` are locally constant of finite type, then so are
> those of `K ⊗^L_Λ Λ/Iⁿ` for every `n ≥ 1`.
>
> For the **constructed** derived tensor product `Stacks.ConstantSheaf.constantDerivedTensor` —
> Tag 06YU for the constant ringed site, read through the equivalence of Tag 03ET — the bifunctor
> `T`, its two exactness instances and `hbound` are discharged in
> `isFiniteTypeLocallyConstantModuleSheaf_homology_derivedTensorConstant_quotientIdealPow`, which
> applies this theorem; the generality `Λ : Type (max u v w)` here is one the construction cannot
> be given.
>
> The proof is the source's induction on `n` along the distinguished triangles
>
> `K ⊗^L_Λ Iⁿ/Iⁿ⁺¹ ⟶ K ⊗^L_Λ Λ/Iⁿ⁺¹ ⟶ K ⊗^L_Λ Λ/Iⁿ ⟶ (K ⊗^L_Λ Iⁿ/Iⁿ⁺¹)[1]`,
>
> supplied by `Stacks.ConstantSheaf.exists_distTriang_derivedTensorConstant`, with the locally
> constant sheaves of finite type absorbing the middle vertex because they form a weak Serre
> subcategory (Tag 093U, through Tag 06UQ). Its remaining input, the local constancy of the graded
> pieces `K ⊗^L_Λ Iⁿ/Iⁿ⁺¹`, is
> `isFiniteTypeLocallyConstantModuleSheaf_homology_derivedTensorConstant_of_annihilated`:
> `Iⁿ/Iⁿ⁺¹` is a finitely generated `Λ`-module killed by `I`, hence has a resolution by finite
> free `Λ/I`-modules, which computes each cohomology sheaf of `K ⊗^L_Λ Iⁿ/Iⁿ⁺¹` out of finitely
> many copies of `K ⊗^L_Λ Λ/I`. That replaces the source's base change identification
> `K ⊗^L_Λ Iⁿ/Iⁿ⁺¹ = (K ⊗^L_Λ Λ/I) ⊗^L_{Λ/I} Iⁿ/Iⁿ⁺¹` together with Tag 094H, and needs neither a
> derived tensor product over `Λ/I` nor Tag 094H.
>
> **The conclusion is stated over `Λ`, not over `Λ/Iⁿ`**: a `Λ`-module killed by `Iⁿ` is of
> finite type over `Λ` exactly when it is over `Λ/Iⁿ`
> (`Stacks.ConstantSheaf.module_finite_iff_finite_quotient`), and constant for one ring exactly
> when constant for the other.
>
> Besides the source's own hypotheses — `Λ` Noetherian, `I ⊆ Λ` an ideal, `K` in `D^-`, and the
> local constancy of `K ⊗^L_Λ Λ/I` — the binders hold only the bifunctor `T` with the two
> properties of a derived tensor product that the argument consumes: exactness in the second
> variable, and the bound above.

```lean
theorem isFiniteTypeLocallyConstantModuleSheaf_homology_tensor_quotientIdealPow_of_isLE
    (T : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)) ⥤
      DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)) ⥤
      DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ)))
    [∀ K, (T.obj K).CommShift ℤ] [∀ K, (T.obj K).IsTriangulated]
    (hbound : ∀ (K L : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ))) (a b : ℤ),
      K.IsLE a → L.IsLE b → ((T.obj K).obj L).IsLE (a + b))
    (b : ℤ) (K : DerivedCategory (Sheaf J (ModuleCat.{max u v w} Λ))) [K.IsLE b]
    (hbase : ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ T K (ModuleCat.of Λ (Λ ⧸ I)))))
    (n : ℕ) (hn : 1 ≤ n) :
    ∀ i : ℤ, IsFiniteTypeLocallyConstantModuleSheaf.{v, u, w} J Λ
      ((DerivedCategory.homologyFunctor _ i).obj
        (derivedTensorConstant J Λ T K (ModuleCat.of Λ (Λ ⧸ I ^ n))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.53, Tag 094F](https://stacks.math.columbia.edu/tag/094F)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
