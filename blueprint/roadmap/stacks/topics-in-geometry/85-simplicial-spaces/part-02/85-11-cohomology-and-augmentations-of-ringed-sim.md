---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSiteSituation.RingedAugmentation, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.totalRingedHom, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.componentRingedHom, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.transitionComponentPushforwardIso, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.componentRingedTwoIso, CategoryTheory.SimplicialSiteSituation.componentRingedAugmentation_isFlat, CategoryTheory.SimplicialSiteSituation.componentRingedAugmentation_isFlat_iff_forall, CategoryTheory.SimplicialSiteSituation.RingedAugmentation.nonempty_moduleResolution
statement: formalized
proof: formalized
---

# 85.11 Cohomology and augmentations of ringed simplicial sites

Section 85.11 of the Stacks Project, [Tag 0D9D](https://stacks.math.columbia.edu/tag/0D9D). 5 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D9D, the section

[Tag 0D9D](https://stacks.math.columbia.edu/tag/0D9D) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean#L103). The attribute's comment: “the data `O`, `O_D` and `a^♯` of a ringed augmentation”.

> **Stacks 0D9D.** The data of a ringed augmentation of a simplicial site: a sheaf of
> commutative rings `O` on the total site, a sheaf of commutative rings `O_D` on the augmentation
> site, and a map `a^♯ : O_D ⟶ a_*O` into the direct image of `O` along the total augmentation.

```lean
structure RingedAugmentation (S : SimplicialSiteSituation.{u}) (D : Cat.{u, u})
    (K : GrothendieckTopology D) (a : Augmentation S D K)
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.totalRingedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean#L128). The attribute's comment: “the morphism of ringed topoi `a : (Sh(C_total), O) ⟶ (Sh(D), O_D)`”.

> **Stacks 0D9D.** The morphism of ringed topoi
> `a : (Sh(C_total), O) ⟶ (Sh(D), O_D)` determined by the total augmentation of Stacks 0D70 and
> the structure map `a^♯`.

```lean
def totalRingedHom :
    RingedToposHom (S.totalRingedTopos A.O) A.augmentationRingedTopos
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.componentRingedHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean#L142). The attribute's comment: “the morphisms of ringed topoi `a_n = a ∘ g_n`”.

> **Stacks 0D9D.** The morphism of ringed topoi
> `a_n = a ∘ g_n : (Sh(C_n), O_n) ⟶ (Sh(D), O_D)`, the composite of the component inclusion of
> Stacks 0D72 with the ringed augmentation.

```lean
def componentRingedHom (n : SimplexCategory) :
    RingedToposHom (S.componentRingedTopos A.O n) A.augmentationRingedTopos
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.transitionComponentPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/Augmentation.lean#L166). The attribute's comment: “`a_m ∘ f_φ = a_n`, on direct images of sheaves of sets”.

> **Stacks 0D9D.** The identification `a_m ∘ f_φ = a_n` on direct images of sheaves of sets:
> the direct image of the simplicial transition followed by that of `a_m` is the direct image of
> `a_n`, for every simplex map `φ : m ⟶ n`.

```lean
def transitionComponentPushforwardIso {m n : SimplexCategory} (φ : m ⟶ n) :
    ((A.componentRingedHom m).comp (S.transitionRingedToposHom A.O φ)).toToposHom.pushforward ≅
      (A.componentRingedHom n).toToposHom.pushforward
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.componentRingedTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationRingedTwoIso.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationRingedTwoIso.lean#L90). The attribute's comment: “`a_m ∘ f_φ = a_n`, as a 2-isomorphism of the morphisms of ringed topoi”.

> **`a_m ∘ f_φ = a_n`, as a 2-isomorphism of morphisms of ringed topoi.** For every simplex map
> `φ : [m] ⟶ [n]` the canonical 2-morphism `a_n ⟶ a_m ∘ f_φ` is invertible. This is the identity
> the source's proof of Stacks 0D7H appeals to, read for morphisms of ringed topoi.
>
> It is `componentRingedTwoIsoAux` followed by the reassociation of `a ∘ (g_m ∘ f_φ)` into
> `(a ∘ g_m) ∘ f_φ = a_m ∘ f_φ`; the source `a ∘ g_n` is `a_n` on the nose.

```lean
def componentRingedTwoIso {m n : SimplexCategory} (φ : m ⟶ n) :
    AlgebraicGeometry.RingedToposHom.TwoIso.{u, u, u, u, u, u}
      (A.componentRingedHom n)
      (AlgebraicGeometry.RingedToposHom.comp (X := S.componentRingedTopos A.O n)
        (Y := S.componentRingedTopos A.O m) (Z := A.augmentationRingedTopos)
        (A.componentRingedHom m) (S.transitionRingedToposHom A.O φ))
```

## Tag 0DH3, a lemma

[Tag 0DH3](https://stacks.math.columbia.edu/tag/0DH3) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentRingedAugmentation_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationFlat.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationFlat.lean#L111). The attribute's comment: “the forward implication: flatness of a gives flatness of every a\_n”.

> If the augmentation `a` of the total ringed topos is flat, then so is the augmentation `a_n`
> of every simplicial component.

```lean
theorem componentRingedAugmentation_isFlat (ha : a.IsFlat) (n : SimplexCategory) :
    (componentRingedAugmentation S O a n).IsFlat
```

**`CategoryTheory.SimplicialSiteSituation.componentRingedAugmentation_isFlat_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationFlatConverse.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationFlatConverse.lean#L116).

> The augmentation `a` of the total ringed topos of a simplicial-site situation is flat if and
> only if the augmentation `a_n` of every simplicial component is flat.

```lean
theorem componentRingedAugmentation_isFlat_iff_forall :
    a.IsFlat ↔ ∀ n : SimplexCategory, (componentRingedAugmentation S O a n).IsFlat
```

## Tag 0D7C, a lemma

[Tag 0D7C](https://stacks.math.columbia.edu/tag/0D7C) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.nonempty_moduleResolution`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleBarResolution.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleBarResolution.lean#L105).

> With the notation of Stacks 0D9D, for a sheaf of `O_D`-modules `G` there is an exact complex
>
> `… ⟶ g_{2!}(a_2^*G) ⟶ g_{1!}(a_1^*G) ⟶ g_{0!}(a_0^*G) ⟶ a^*G ⟶ 0`
>
> of sheaves of `O`-modules on the total site, with `g_{n!}` the lower shriek of Stacks 0D72: a
> chain complex whose degree-`n` term is `g_{n!}(a_n^*G)`, whose differentials are the alternating
> sums of the face maps of a simplicial structure on its terms, augmented onto `a^*G`, exact in
> every positive degree and at the augmentation, the augmentation being an epimorphism.

```lean
alias nonempty_moduleResolution
```

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.nonempty_moduleResolution_of_iso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleResolution.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleResolution.lean#L393). The attribute's comment: “for an arbitrary coefficient module, by the simplex-coefficient resolution”.

> **Stacks 0D7C.** With the notation of Stacks 0D9D, for a sheaf of `O_D`-modules `G` the
> lower shriek images `g_{n!}(a_n^*G)` of Stacks 0D72 carry an exact complex
>
> `… ⟶ g_{2!}(a_2^*G) ⟶ g_{1!}(a_1^*G) ⟶ g_{0!}(a_0^*G) ⟶ a^*G ⟶ 0`
>
> of sheaves of `O`-modules on the total site, with differentials the alternating sums of the
> canonical face maps. The complex is `simplexModuleResolution`, the simplex-coefficient
> resolution of `a^*G`.

```lean
theorem nonempty_moduleResolution_of_iso_unit
    (G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf A.OD)) :
    Nonempty (A.ModuleResolution G)
```

## Tag 0D7D, a lemma

[Tag 0D7D](https://stacks.math.columbia.edu/tag/0D7D) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.moduleCechComplex_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleCechComplex.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleCechComplex.lean#L469).

> With the notation of Stacks 0D9D, let `F` be a sheaf of `O`-modules on the
> total site. The canonical complex of `O_D`-modules
>
> `0 ⟶ a_*F ⟶ a_{0,*}F_0 ⟶ a_{1,*}F_1 ⟶ a_{2,*}F_2 ⟶ …`
>
> (`moduleCechComplex`, with `a_*F` in degree `0` and `a_{n,*}F_n` in degree `n + 1`) is exact in
> degrees `-1` and `0` (the Lean degrees `0` and `1`). If `F` is an injective `O`-module, the
> complex is exact in all degrees and remains exact on applying `Hom_{O_D}(G, -)` for any
> `O_D`-module `G`.
>
> The complex is the source's: its differentials are the transposes, along the adjunctions
> `a^* ⊣ a_*` and `g_{n!}a_n^* ⊣ a_{n,*}g_n^*`, of the augmentation and of the differentials of the
> resolution `… ⟶ g_{1!}(a_1^*G) ⟶ g_{0!}(a_0^*G) ⟶ a^*G ⟶ 0` of Stacks 0D7C
> (`homEquiv_cechAug`, `homEquiv_cechD`), so `Hom(G, -)` of it is `Hom(-, F)` of that resolution;
> `Hom(-, F)` is left exact, and exact when `F` is injective.

```lean
theorem moduleCechComplex_spec :
    (A.moduleCechComplex F).X 0 = A.totalRingedHom.pushforwardModules.obj F ∧
    (∀ n : ℕ, (A.moduleCechComplex F).X (n + 1) =
      (A.componentRingedHom ⦋n⦌).pushforwardModules.obj
        ((S.componentModulesRestriction A.O ⦋n⦌).obj F)) ∧
    (A.moduleCechComplex F).ExactAt 0 ∧ (A.moduleCechComplex F).ExactAt 1 ∧
    (Injective F →
      (∀ k : ℕ, (A.moduleCechComplex F).ExactAt k) ∧
      ∀ (G : A.augmentationRingedTopos.Modules) (k : ℕ),
        (((preadditiveCoyoneda.obj (op G)).mapHomologicalComplex _).obj
          (A.moduleCechComplex F)).ExactAt k)
```

## Tag 0D7F, a lemma

[Tag 0D7F](https://stacks.math.columbia.edu/tag/0D7F) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.RingedAugmentation.higherDirectImageSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleSpectralSequence.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/AugmentationModuleSpectralSequence.lean#L359).

> **Stacks 0D7F.** With the notation of Stacks 0D9D (a ringed augmentation `A` of a
> simplicial-site situation towards a ringed site `(D, K, O_D)`), for `M` in `D⁺(O)` there is a
> spectral sequence `(E_r, d_r)` in `Mod(O_D)`, presented from its first page and functorial in
> `M`, with
>
> `E_1^{p,q} = R^q a_{p,*} M_p  ⇒  R^{p+q} a_* M`.
>
> Here `M_p` is the restriction of `M` to the component `C_p` (Stacks 0D72), `R^q a_{p,*}` the
> cohomology of the right derived direct image along `a_p = a ∘ g_p` and `R^n a_*` that of the
> right derived direct image along `a`. The identification of the first page is natural in `M`,
> and the first page vanishes in the negative columns.
>
> It is the spectral sequence of the double complex `A^{p,q} = a_{p,*} I^q_p` of a bounded below
> complex of injectives `I^•` representing `M`, whose horizontal maps are those of the complex of
> Stacks 0D7D, filtered by `p`.

```lean
def higherDirectImageSpectralSequence : A.HigherDirectImageSpectralSequence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.11, Tag 0D9D](https://stacks.math.columbia.edu/tag/0D9D)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
