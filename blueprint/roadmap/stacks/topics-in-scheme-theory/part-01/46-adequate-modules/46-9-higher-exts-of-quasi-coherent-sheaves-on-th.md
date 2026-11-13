---
declaration: section
origin: cited
lean: AdequateFunctor.injective_iff_moduleExtension_pureInjective, Stacks.Adequate.pureExtToExt_bijective_and_natural, Stacks.Adequate.bijective_pureExtToExt_one, Stacks.Adequate.pureExtZeroAddEquivExtZero
statement: formalized
proof: formalized
---

# 46.9 Higher exts of quasi-coherent sheaves on the big site

Section 46.9 of the Stacks Project, [Tag 0707](https://stacks.math.columbia.edu/tag/0707). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0708, a lemma

[Tag 0708](https://stacks.math.columbia.edu/tag/0708) in the Stacks Project.

**`AdequateFunctor.injective_iff_moduleExtension_pureInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/InjectiveObjects.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/InjectiveObjects.lean#L244).

> **Stacks Project, Tag 0708.** An adequate module-valued functor is injective exactly when it
> is naturally isomorphic to the extension of a pure injective module.

```lean
public theorem injective_iff_moduleExtension_pureInjective {A : Type u} [CommRing A]
    (F : (adequate.{u, v, max u v w} A).FullSubcategory) :
    Injective F ↔ ∃ I : ModuleCat.{max u v w} A, Module.PureInjective A I ∧
      Nonempty (F.obj ≅ moduleExtension.{max u v w, v} A I)
```

## Tag 0709, a lemma

[Tag 0709](https://stacks.math.columbia.edu/tag/0709) in the Stacks Project.

**`Stacks.Adequate.pureExtToExt_bijective_and_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/AdequateExtComparisonAll.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/AdequateExtComparisonAll.lean#L76). The attribute's comment: “every degree i: the canonical arrow is bijective and natural in M and N”.

> Let `U = Spec A` be affine and `M`, `N` be `A`-modules. For every `i`, the canonical arrow
> `Pext^i_A(M, N) ⟶ Ext^i_{Mod(𝒪)}(M^a, N^a)` of `pureExtToExt` is bijective, and it is functorial in
> `M` and in `N`: precomposition with `g : M' ⟶ M` on `Pext` corresponds to composition with the
> class of `g^a`, and the action of `g : N ⟶ N'`, through any map of the chosen pure injective
> resolutions lying over `g`, to composition with the class of `g^a`.

```lean
public theorem pureExtToExt_bijective_and_natural :
    letI := adequate_isClosedUnderKernels.{u, u} B
    letI := adequate_isClosedUnderCokernels.{u, u} B
    letI := adequate_isClosedUnderFiniteProducts.{u, u} B
    letI : Abelian (adequate.{u, u} B).FullSubcategory := abelian_adequate B
    letI : PreservesFiniteLimits (adequate.{u, u} B).ι := (exact_ι_adequate B).1
    letI : PreservesFiniteColimits (adequate.{u, u} B).ι := (exact_ι_adequate B).2
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasDerivedCategory.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    letI : HasExt.{u + 1} (adequate.{u, u} B).FullSubcategory :=
      hasExt_of_hasDerivedCategory _
    (∀ (M N : ModuleCat.{u} A) (n : ℕ), Function.Bijective (pureExtToExt B M N n)) ∧
    (∀ {M M' : ModuleCat.{u} A} (N : ModuleCat.{u} A) (g : M' ⟶ M) (n : ℕ)
      (x : Module.pureExt (A := A) M N n),
      pureExtToExt B M' N n
          ((HomologicalComplex.homologyMap
            (Module.homComplexPrecomp g.hom (Module.pureExtResolution (A := A) N)) n).hom x) =
        (Ext.mk₀ ((associatedTilde B).map g)).comp (pureExtToExt B M N n x) (zero_add n)) ∧
    (∀ (M : ModuleCat.{u} A) {N N' : ModuleCat.{u} A} (g : N ⟶ N')
      (F : Module.pureExtResolution (A := A) N ⟶ Module.pureExtResolution (A := A) N')
      (_ : (F.f 0).hom.comp (Module.pureExtAugmentation N) =
        (Module.pureExtAugmentation N').comp g.hom)
      (n : ℕ) (x : Module.pureExt (A := A) M N n),
      pureExtToExt B M N' n
          ((HomologicalComplex.homologyMap (Module.homComplexPostcomp M F) n).hom x) =
        (pureExtToExt B M N n x).comp (Ext.mk₀ ((associatedTilde B).map g)) (add_zero n))
```

**`Stacks.Adequate.bijective_pureExtToExt_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/PureExtCanonicalArrow.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/PureExtCanonicalArrow.lean#L264). The attribute's comment: “degree 1: the canonical arrow pureExtToExt, natural in M and N by pureExtToExt\_naturality\_left/\_right, is bijective in degree 1; every degree is pureExtToExt\_bijective\_and\_natural in HigherExtsAdequate/AdequateExtComparisonAll”.

> **[Stacks, Tag 0709] in degree `1`.** For `U = Spec A` affine and `A`-modules `M`, `N`, the
> canonical arrow `Pext¹_A(M, N) ⟶ Ext¹_{Mod((Sch/U)_τ, 𝒪)}(M^a, N^a)` is bijective, with no
> hypothesis. It is the isomorphism `Pext¹_A(M, N) ≅ Ext¹_{Adeq(𝒪)}(M^a, N^a)` of
> `Stacks.Adequate.pureExtAddEquivExtAdequate` followed by the comparison of Tag 06ZW, which is
> bijective in degree `1` because the adequate modules are closed under extensions
> (`Stacks.Adequate.bijective_mapExtAddHom_ι_adequate_one`). The arrow is natural in `M` and `N`
> by `Stacks.Adequate.pureExtToExt_naturality_left` and `_naturality_right`.

```lean
public theorem bijective_pureExtToExt_one (M N : ModuleCat.{u} A) :
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    Function.Bijective (pureExtToExt B M N 1)
```

**`Stacks.Adequate.pureExtZeroAddEquivExtZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/PureExtComparison.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/PureExtComparison.lean#L179). The attribute's comment: “degree 0, where the canonical arrow is the action of M ↦ M^a on Hom composed with the computation of Pext in degree 0, and neither Tag 06ZW nor Tag 06ZG is needed; functorial in M and N by homAddEquivExtZero\_naturality\_left/\_right together with Module.homComplexZeroHom\_naturality\_left/\_right. Every degree is pureExtToExt\_bijective\_and\_natural in HigherExtsAdequate/AdequateExtComparisonAll”.

> **[Stacks, Tag 0709] in degree `0`.** For `U = Spec A` affine and `A`-modules `M`, `N`, the
> canonical arrow
>
> `Pext⁰_A(M, N) ⟶ Ext⁰_{Mod((Sch/U)_τ, 𝒪)}(M^a, N^a)`
>
> is an isomorphism, with no hypothesis. It is the composite of two identifications:
> `Pext⁰_A(M, N) = Hom_A(M, N)`, because the degree-`0` cohomology of `Hom_A(M, Iᐧ)` is the kernel
> of its first differential and that kernel is the image of the augmentation
> (`Module.pureExtZeroIsoHom`); and `Hom_A(M, N) = Ext⁰_{Mod(𝒪)}(M^a, N^a)`, because `M ↦ M^a` is
> fully faithful (`Stacks.Adequate.homAddEquivExtZero`). Neither Tag 06ZW nor Tag 06ZG enters: in
> degree `0` the comparison is a map on `Hom`, so no derived functor and no injective resolution
> in a category of functors is needed.
>
> Functoriality in `M` and `N` is the naturality of the two halves, which is
> `Stacks.Adequate.homAddEquivExtZero_naturality_left` and `_naturality_right` for the `Ext` half
> and `Module.homComplexZeroHom_naturality_left` and `Module.homComplexZeroHom_naturality_right`
> for the `Pext` half; see the module documentation for why the latter two are stated at the Hom
> complex that computes `Module.pureExt` rather than at `Module.pureExt` itself.
>
> The `letI` preamble is not a list of hypotheses: both entries are the standard derived-category
> and `Ext` choices for the sheaves of modules on the site, spelled out rather than registered
> because declaring them as `instance`s in this chapter changes instance selection for files that
> do not import this one. It matches the preamble of
> `Stacks.Adequate.bijective_mapExtAddHom_ι_adequate_zero`, the degree-`0` registration of
> Tag 06ZW, so the two share one spelling of each object.

```lean
public def pureExtZeroAddEquivExtZero (M N : ModuleCat.{u} A) :
    letI : HasDerivedCategory.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      HasDerivedCategory.standard _
    letI : HasExt.{u + 1} (SheafOfModules.{u} B.structureSheaf) :=
      hasExt_of_hasDerivedCategory _
    Module.pureExt (A := A) M N 0 ≃+
      Ext ((associatedTilde B).obj M) ((associatedTilde B).obj N) 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.9, Tag 0707](https://stacks.math.columbia.edu/tag/0707)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
