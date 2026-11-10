---
declaration: section
origin: cited
lean: AlgebraicGeometry.StandardPHCovering, AlgebraicGeometry.StandardPHCovering.pullback, AlgebraicGeometry.exists_standardPHCovering_refinement_bind, AlgebraicGeometry.exists_standardPHCovering_refinement_of_openCover, AlgebraicGeometry.IsPHCovering, AlgebraicGeometry.IsPHCovering.of_openCover, AlgebraicGeometry.surjective_proper_isPHCovering, AlgebraicGeometry.isPHCovering_tfae
statement: formalized
proof: formalized
---

# 34.8 The ph topology

Section 34.8 of the Stacks Project, [Tag 0DBC](https://stacks.math.columbia.edu/tag/0DBC). 17 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DBD, a definition

[Tag 0DBD](https://stacks.math.columbia.edu/tag/0DBD) in the Stacks Project.

**`AlgebraicGeometry.StandardPHCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardCoverings.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardCoverings.lean#L54).

> A family `fᵢ : Xᵢ ⟶ T` is a standard ph covering if its index type is finite, every
> `Xᵢ` is affine, and the family is obtained from a finite affine open cover of the source of
> a proper surjective morphism to the affine scheme `T`.

```lean
def StandardPHCovering {ι : Type v} {T : Scheme.{u}} [IsAffine T] {X : ι → Scheme.{u}}
    (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0DBE, a lemma

[Tag 0DBE](https://stacks.math.columbia.edu/tag/0DBE) in the Stacks Project.

**`AlgebraicGeometry.StandardPHCovering.pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardCoverings.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardCoverings.lean#L104).

> **Stacks 0DBE.** A standard ph covering remains standard after pullback along a
> morphism of affine schemes.

```lean
theorem StandardPHCovering.pullback {ι : Type v} {T T' : Scheme.{u}}
    [IsAffine T] [IsAffine T'] {X : ι → Scheme.{u}} {f : ∀ i, X i ⟶ T}
    (hf : StandardPHCovering f) (g : T' ⟶ T) :
    StandardPHCovering (fun i ↦ pullback.snd (f i) g)
```

## Tag 0DBF, a lemma

[Tag 0DBF](https://stacks.math.columbia.edu/tag/0DBF) in the Stacks Project.

**`AlgebraicGeometry.exists_standardPHCovering_refinement_bind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardRefinementParts0DBF.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/StandardRefinementParts0DBF.lean#L156). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 0DBF, part (2).** Let `T` be an affine scheme, let `E` be a standard
> ph covering of `T`, and for each member `E.X i` let `F i` be a standard ph covering of it. Then
> the composite family `E.bind F`, whose members are the `(F i).X j ⟶ E.X i ⟶ T`, has a
> refinement by a standard ph covering of `T`.
>
> This consumes Chow's lemma (Stacks 0202) through `AlgebraicGeometry.chowLemmaStatement`.

```lean
theorem exists_standardPHCovering_refinement_bind {T : Scheme.{u}} [IsAffine T]
    (E : PreZeroHypercover.{v} T) (hE : StandardPHCovering E.f)
    (F : ∀ i, PreZeroHypercover.{w} (E.X i))
    (hF : ∀ i, @StandardPHCovering (F i).I₀ (E.X i) (hE.isAffine i) (F i).X (F i).f) :
    ∃ G : PreZeroHypercover.{max v w} T,
      StandardPHCovering G.f ∧ Nonempty (G.Hom (E.bind F))
```

**`AlgebraicGeometry.exists_standardPHCovering_refinement_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardPhRefinement.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardPhRefinement.lean#L113). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 0DBF, part (1).** Every Zariski open covering of an affine scheme has
> a refinement which is a standard ph covering.
>
> The standard ph covering is the finite affine refinement of
> `AlgebraicGeometry.exists_finite_affine_refinement`, presented by the identity of `T`, which is
> proper and surjective.

```lean
theorem exists_standardPHCovering_refinement_of_openCover {T : Scheme.{u}} [IsAffine T]
    (U : T.OpenCover.{v}) :
    ∃ E : PreZeroHypercover.{v} T,
      StandardPHCovering E.f ∧ Nonempty (E.Hom U.toPreZeroHypercover)
```

## Tag 0DBG, a definition

[Tag 0DBG](https://stacks.math.columbia.edu/tag/0DBG) in the Stacks Project.

**`AlgebraicGeometry.IsPHCovering`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean#L62).

> **Stacks 0DBG.** A family `{X i ⟶ T}` is a **ph covering** if every member is locally
> of finite type and, over every affine open `U` of `T`, a standard ph covering of
> `U.toScheme` refines the pullback of the family to `U`.

```lean
public noncomputable def IsPHCovering {T : Scheme.{u}}
    {I : Type v} (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T) : Prop
```

## Tag 0DBH, a lemma

[Tag 0DBH](https://stacks.math.columbia.edu/tag/0DBH) in the Stacks Project.

**`AlgebraicGeometry.IsPHCovering.of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/StandardPhRefinement.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/StandardPhRefinement.lean#L128).

> **Stacks Project, Tag 0DBH.** A Zariski open covering of a scheme is a ph covering.
>
> Over an affine open `V` of the target, the base change of the covering is again a Zariski open
> covering, so `AlgebraicGeometry.exists_standardPHCovering_refinement_of_openCover` refines it by
> a standard ph covering; that covering is then reindexed into the universe of the schemes by
> `AlgebraicGeometry.StandardPHCovering.reindex`.

```lean
theorem IsPHCovering.of_openCover {T : Scheme.{u}} (𝒰 : T.OpenCover.{v}) :
    IsPHCovering 𝒰.X 𝒰.f
```

## Tag 0DES, a lemma

[Tag 0DES](https://stacks.math.columbia.edu/tag/0DES) in the Stacks Project.

**`AlgebraicGeometry.surjective_proper_isPHCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean#L107).

> **Stacks 0DES.** A proper surjection of schemes is a ph covering.

```lean
public theorem surjective_proper_isPHCovering {X Y : Scheme.{u}} (f : Y ⟶ X)
    [Surjective f] [IsProper f] :
    IsPHCovering (fun _ : Unit ↦ Y) (fun _ ↦ f)
```

## Tag 0ET9, a lemma

[Tag 0ET9](https://stacks.math.columbia.edu/tag/0ET9) in the Stacks Project.

**`AlgebraicGeometry.isPHCovering_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhCoveringRefinement.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhCoveringRefinement.lean#L60).

> A family of locally finite type morphisms is a ph covering if and only if some ph
> covering refines it, if and only if its disjoint-union morphism is a ph covering.

```lean
public theorem isPHCovering_tfae {T : Scheme.{u}} {I : Type v} [Small.{u} I]
    (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T)
    (hf : ∀ i, LocallyOfFiniteType (f i)) :
    List.TFAE [
      IsPHCovering X f,
      ∃ (K : Type v) (Y : K → Scheme.{u}) (g : ∀ k, Y k ⟶ T),
        IsPHCovering Y g ∧
          Nonempty
            (({ I₀ := K, X := Y, f := g } : PreZeroHypercover T).Hom
              ({ I₀ := I, X := X, f := f } : PreZeroHypercover T)),
      IsPHCovering
        (fun _ : Unit ↦ ∐ X) (fun _ ↦ Sigma.desc f)]
```

## Tag 0DBI, a lemma

[Tag 0DBI](https://stacks.math.columbia.edu/tag/0DBI) in the Stacks Project.

**`AlgebraicGeometry.isPHCovering_of_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/Coverings.lean#L101). The attribute's comment: “isomorphisms”.

> **Stacks 0DBI.** A singleton isomorphism is a ph covering of schemes.

```lean
public theorem isPHCovering_of_isIso {T' T : Scheme.{u}} (f : T' ⟶ T) [IsIso f] :
    IsPHCovering (fun _ : Unit ↦ T') (fun _ ↦ f)
```

**`AlgebraicGeometry.isPHCovering_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/CoveringsParts0DBI.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/CoveringsParts0DBI.lean#L178). The attribute's comment: “part (3)”.

> **Stacks 0DBI part (3).** If `{X i ⟶ T}` is a ph covering and `g : T' ⟶ T` is any morphism of
> schemes, then the base change `{X i ×_T T' ⟶ T'}` is a ph covering of `T'`.
>
> Fix an affine open `U'` of `T'`. It is a compact space, so
> `AlgebraicGeometry.exists_finite_affineOpens_confined` covers it by finitely many affine opens
> `W l`, each mapping into an affine open `V l` of `T`; the family `{W l ⟶ U'}` is a standard ph
> covering of `U'` presented by the identity of `U'`. Over `V l` the given covering has a standard
> ph refinement, and `W l ⟶ V l` base changes it to a standard ph covering of `W l` refining the
> base changed family, by the universal property of the fibre products involved. Stacks 0DBF
> part (2), `AlgebraicGeometry.exists_standardPHCovering_refinement_bind`, collapses this two-step
> covering of `U'` into a single standard ph covering.

```lean
public theorem isPHCovering_pullback {T T' : Scheme.{u}} {I : Type v} {X : I → Scheme.{u}}
    {f : ∀ i, X i ⟶ T} (hf : IsPHCovering X f) (g : T' ⟶ T) :
    IsPHCovering (fun i ↦ pullback (f i) g) (fun i ↦ pullback.snd (f i) g)
```

**`AlgebraicGeometry.isPHCovering_bind`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/CoveringsParts0DBI.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/CoveringsParts0DBI.lean#L246). The attribute's comment: “part (2)”.

> **Stacks 0DBI part (2).** If `E` is a ph covering of `T` and `F i` is a ph covering of the
> member `E.X i` for each `i`, then the family of all composites `(F i).X j ⟶ E.X i ⟶ T`, which is
> `CategoryTheory.PreZeroHypercover.bind`, is a ph covering of `T`.
>
> Fix an affine open `U` of `T`. The outer covering has a standard ph refinement `𝒜` over `U`, say
> with `𝒜.X q` mapping to `E.X (i q)` by a morphism `c q` over `U`. Each `𝒜.X q` is affine, so the
> base change of the inner covering `F (i q)` along `c q`, which is a ph covering of `𝒜.X q` by
> `AlgebraicGeometry.isPHCovering_pullback`, has a standard ph refinement
> `𝒞 q` by `AlgebraicGeometry.IsPHCovering.exists_standardPHCovering`. The two-step covering
> `𝒜.bind 𝒞` of `U` refines the base change of `E.bind F` to `U`, and Stacks 0DBF part (2),
> `AlgebraicGeometry.exists_standardPHCovering_refinement_bind`, collapses it into a single standard
> ph covering of `U`.

```lean
public theorem isPHCovering_bind {T : Scheme.{u}} (E : PreZeroHypercover.{v} T)
    (hE : IsPHCovering E.X E.f) (F : ∀ i, PreZeroHypercover.{w} (E.X i))
    (hF : ∀ i, IsPHCovering (F i).X (F i).f) :
    IsPHCovering (E.bind F).X (E.bind F).f
```

## Tag 0DBJ, a definition

[Tag 0DBJ](https://stacks.math.columbia.edu/tag/0DBJ) in the Stacks Project.

**`AlgebraicGeometry.BigPHSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L71).

> **Stacks 0DBJ.** A big ph site consists of an initial set of schemes and initial ph
> coverings, a sufficiently large cutoff category containing them, and a bounded collection
> of ph coverings satisfying the site axioms and representing every ph covering.

```lean
public structure BigPHSite
```

## Tag 0DBK, a lemma

[Tag 0DBK](https://stacks.math.columbia.edu/tag/0DBK) in the Stacks Project.

**`AlgebraicGeometry.standardPHCovering_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean#L180). The attribute's comment: “part (2)”.

> **Stacks 0DBK, part (2).** A standard ph covering is tautologically equivalent to a covering
> in the big ph site.

```lean
public theorem standardPHCovering_tautologicallyEquivalent
    (B : BigPHSite.{u}) (T : B.Schemes) [IsAffine T.1]
    (E : PreZeroHypercover.{v} T.1) (hE : StandardPHCovering E.f) :
    ∃ F : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, F⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent E (F.map B.inclusion)
```

**`AlgebraicGeometry.openCover_tautologicallyEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean#L209). The attribute's comment: “part (3)”.

> **Stacks 0DBK, part (3).** A Zariski open covering is tautologically equivalent to a covering
> in the big ph site.

```lean
public theorem openCover_tautologicallyEquivalent
    (B : BigPHSite.{u}) (T : B.Schemes) (U : T.1.OpenCover.{v}) :
    ∃ F : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, F⟩ ∧
        PreZeroHypercover.TautologicallyEquivalent U.toPreZeroHypercover
          (F.map B.inclusion)
```

**`AlgebraicGeometry.exists_isCovering_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSiteCoverings.lean#L277). The attribute's comment: “part (1)”.

> **Stacks 0DBK, part (1).** Every ph covering of an object of a big ph site is refined by one
> of the site's own covering families.
>
> The refinement is assembled from parts (2) and (3) by the site's composition axiom: the affine
> opens of the target form a Zariski covering, hence by part (3) are tautologically equivalent to a
> covering `G` of the site, and each member of `G` is isomorphic over the target to an affine open,
> hence by the definition of a ph covering carries a standard ph covering refining the given family
> there, which by part (2) is tautologically equivalent to a covering of the site.

```lean
public theorem exists_isCovering_refinement
    (B : BigPHSite.{u}) (T : B.Schemes)
    (E : PreZeroHypercover.{v} T.1) (hE : IsPHCovering E.X E.f) :
    ∃ F : PreZeroHypercover.{u + 1} T,
      B.IsCovering ⟨T, F⟩ ∧ Nonempty ((F.map B.inclusion).Hom E)
```

## Tag 0DBL, a definition

[Tag 0DBL](https://stacks.math.columbia.edu/tag/0DBL) in the Stacks Project.

**`AlgebraicGeometry.BigPHOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L173). The attribute's comment: “part (1), category”.

> **Stacks 0DBL, part (1).** The big ph category of `S` is the slice of the chosen big ph
> category over its object `S`.

```lean
public abbrev BigPHOver
```

**`AlgebraicGeometry.BigPHOver.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 188](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L188). The attribute's comment: “part (1), coverings”.

> **Stacks 0DBL, part (1).** A family in the slice covers precisely when its underlying
> family covers in the chosen big ph site.

```lean
public abbrev IsCovering (E : Covering (BigPHOver B S hS)) : Prop
```

**`AlgebraicGeometry.BigAffinePH`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L204). The attribute's comment: “part (2), category”.

> **Stacks 0DBL, part (2).** The big affine ph category is the full subcategory of affine
> objects in the big ph category over `S`.

```lean
public abbrev BigAffinePH
```

**`AlgebraicGeometry.BigAffinePH.IsCovering`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L223). The attribute's comment: “part (2), coverings”.

> **Stacks 0DBL, part (2).** An affine family covers exactly when it is a finite covering
> family in the big ph site over `S`.

```lean
public abbrev IsCovering (E : Covering (BigAffinePH B S hS)) : Prop
```

## Tag 0DBM, a lemma

[Tag 0DBM](https://stacks.math.columbia.edu/tag/0DBM) in the Stacks Project.

**`AlgebraicGeometry.BigAffinePH.isSite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/BigSite.lean#L274).

> **Stacks 0DBM.** Finite ph covering families of affine objects over `S` satisfy the
> axioms of a site.

```lean
public lemma isSite (B : BigPHSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) : IsSite (BigAffinePH.IsCovering B S hS)
```

## Tag 0DBN, a lemma

[Tag 0DBN](https://stacks.math.columbia.edu/tag/0DBN) in the Stacks Project.

Declarations registered for the tag:

- [`schemeSizeBelow_isClosedUnderLimitsOfShape_walkingCospan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=schemeSizeBelow_isClosedUnderLimitsOfShape_walkingCospan#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L91) (StacksFrontier): “closure of size-bounded schemes under fibre products”.
- [`CategoryTheory.Limits.hasLimitsOfShape_of_closedUnderLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.hasLimitsOfShape_of_closedUnderLimits#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L94) (StacksFrontier): “fibre products in the big ph site”.
- [`CategoryTheory.Limits.createsLimitsOfShapeFullSubcategoryInclusion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.createsLimitsOfShapeFullSubcategoryInclusion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L97) (StacksFrontier): “preservation by the big ph site inclusion”.
- [`CategoryTheory.Over.instHasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.instHasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L144) (StacksFrontier): “fibre products in the big ph slice”.
- [`CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.preservesLimitsOfShape_forget_of_isConnected#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L154) (StacksFrontier): “preservation by the big ph slice forgetful functor”. References: SGA 4 IV (5.10), “more general”; SGA 4 IV (5.3), “partial”.
- [`CategoryTheory.Limits.comp_preservesLimitsOfShape`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.comp_preservesLimitsOfShape#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L157) (StacksFrontier): “preservation under composition for the big ph slice functor”.
- [`CategoryTheory.Over.mkIdTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mkIdTerminal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Fppf/FibreProducts.lean#L167) (StacksFrontier): “the final object of the big ph slice”. References: EGA 0 (8.1.10), “more general”; SGA 3 I (1.3); SGA 4 IV (5.11.1), “terminal object (X”.

## Tag 0DBP, a lemma

[Tag 0DBP](https://stacks.math.columbia.edu/tag/0DBP) in the Stacks Project.

**`AlgebraicGeometry.BigAffinePH.inclusion_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffinePhDenseSubsite.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffinePhDenseSubsite.lean#L200). The attribute's comment: “cocontinuity”.

> **Stacks 0DBP, cocontinuity.** The inclusion of affine objects over `S`
> in a chosen big ph site is cocontinuous.

```lean
public instance BigAffinePH.inclusion_isCocontinuous
    (B : BigPHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigAffinePH.inclusion B S hS).IsCocontinuous
      (BigAffinePH.topology B S hS)
      (BigPHOver.topology B S hS)
```

**`AlgebraicGeometry.BigAffinePH.inclusion_isDenseSubsite`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffinePhDenseSubsite.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/AffinePhDenseSubsite.lean#L287). The attribute's comment: “equivalence of topoi”.

> **Stacks 0DBP, equivalence of topoi.** The inclusion of affine objects
> is a dense subsite, hence its induced morphism of sheaf topoi is an equivalence.

```lean
public instance BigAffinePH.inclusion_isDenseSubsite
    (B : BigPHSite.{u}) (S : Scheme.{u}) (hS : B.Contains S) :
    (BigAffinePH.inclusion B S hS).IsDenseSubsite
      (BigAffinePH.topology B S hS)
      (BigPHOver.topology B S hS)
```

## Tag 0DBQ, a lemma

[Tag 0DBQ](https://stacks.math.columbia.edu/tag/0DBQ) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_iff_zariski_and_properSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSheafCriterion.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSheafCriterion.lean#L959). The attribute's comment: “sheaf characterization”.

> **Stacks 0DBQ, characterization.** The ph sheaf condition is equivalent
> to Zariski descent together with proper-surjective descent.

```lean
public theorem isSheaf_iff_zariski_and_properSurjective :
    Presieve.IsSheaf (BigPHOver.topology B S hS) F ↔
      (IsZariskiSheaf B S hS F ∧ IsProperSurjectiveSheaf B S hS F)
```

**`AlgebraicGeometry.properSurjective_iff_affine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSheafCriterion.lean, line 981](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/BigSites/PhSheafCriterion.lean#L981). The attribute's comment: “affine reduction”.

> **Stacks 0DBQ, affine reduction.** Under Zariski descent, proper-surjective
> descent may be checked only when the target is affine.

```lean
public theorem properSurjective_iff_affine (hF : IsZariskiSheaf B S hS F) :
    IsProperSurjectiveSheaf B S hS F ↔
      IsAffineProperSurjectiveSheaf B S hS F
```

## Tag 0DBR, a lemma

[Tag 0DBR](https://stacks.math.columbia.edu/tag/0DBR) in the Stacks Project.

**`AlgebraicGeometry.bigPHMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L71). The attribute's comment: “the morphism of topoi”.

> **Stacks 0DBR.** The morphism of big ph topoi induced by `f`.

```lean
public noncomputable def bigPHMorphism :
    MorphismOfTopoi
      (Sheaf (BigPHOver.topology B T.obj T.property) (Type (u + 1)))
      (Sheaf (BigPHOver.topology B S.obj S.property) (Type (u + 1)))
```

**`AlgebraicGeometry.bigPHMorphismInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L89). The attribute's comment: “the inverse-image formula”.

> **Stacks 0DBR.** Inverse image is restriction along postcomposition, naturally in
> sheaves and objects.

```lean
public noncomputable def bigPHMorphismInverseImageIso :
    (bigPHMorphism B T S f).inverseImage ≅
      (Over.map f).sheafPushforwardContinuous (Type (u + 1))
        (BigPHOver.topology B T.obj T.property)
        (BigPHOver.topology B S.obj S.property)
```

**`AlgebraicGeometry.bigPHMorphismPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L101). The attribute's comment: “the direct-image formula”.

> **Stacks 0DBR.** Direct image is restriction along base change, naturally in sheaves
> and objects.

```lean
public noncomputable def bigPHMorphismPushforwardIso :
    (bigPHMorphism B T S f).pushforward ≅
      (Over.pullback f).sheafPushforwardContinuous (Type (u + 1))
        (BigPHOver.topology B S.obj S.property)
        (BigPHOver.topology B T.obj T.property)
```

**`AlgebraicGeometry.bigPHLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L110). The attribute's comment: “existence of lower shriek”.

> **Stacks 0DBR.** The lower shriek functor is left adjoint to inverse image.

```lean
public noncomputable def bigPHLowerShriekAdjunction :
    (Over.map f).sheafPullback (Type (u + 1))
      (BigPHOver.topology B T.obj T.property)
      (BigPHOver.topology B S.obj S.property) ⊣
        (bigPHMorphism B T S f).inverseImage
```

**`AlgebraicGeometry.bigPHLowerShriek_preservesPullbacks`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L122). The attribute's comment: “lower shriek preserves fibre products”.

> **Stacks 0DBR.** Lower shriek preserves fibre products.

```lean
public instance bigPHLowerShriek_preservesPullbacks :
    PreservesLimitsOfShape WalkingCospan
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigPHOver.topology B T.obj T.property)
        (BigPHOver.topology B S.obj S.property))
```

**`AlgebraicGeometry.bigPHLowerShriek_preservesEqualizers`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L135). The attribute's comment: “lower shriek preserves equalizers”.

> **Stacks 0DBR.** Lower shriek preserves equalizers.

```lean
public instance bigPHLowerShriek_preservesEqualizers :
    PreservesLimitsOfShape WalkingParallelPair
      ((Over.map f).sheafPullback (Type (u + 1))
        (BigPHOver.topology B T.obj T.property)
        (BigPHOver.topology B S.obj S.property))
```

Declarations registered for the tag:

- [`CategoryTheory.Over.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.map#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L55) (StacksFrontier): “the postcomposition functor”. References: EGA I (2.5.3); EGA I (2.5.4), “more general”; SGA 3 I (1.6); SGA 4 IV (5.5).
- [`CategoryTheory.Over.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L56) (StacksFrontier): “the base-change functor”. References: EGA I (3.3.7), “more general”; EGA IV (8.2.6); SGA 3 I (1.6); SGA 4 III (5.5); SGA 4 IV (5.2), “more general”; SGA 4 IV (5.5).
- [`CategoryTheory.Over.mapPullbackAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Over.mapPullbackAdj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/MorphismOfTopoi.lean#L57) (StacksFrontier): “the base-change adjunction”.

## Tag 0DBS, a lemma

[Tag 0DBS](https://stacks.math.columbia.edu/tag/0DBS) in the Stacks Project.

**`AlgebraicGeometry.bigPHMorphism_comp_pushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/Composition.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/Composition.lean#L45). The attribute's comment: “direct-image composition”.

> **Stacks 0DBS.** Direct image for the composite morphism of big ph topoi is naturally
> isomorphic to the composite of the direct-image functors.

```lean
public noncomputable def bigPHMorphism_comp_pushforwardIso :
    (bigPHMorphism B X Z (f ≫ g)).pushforward ≅
      (bigPHMorphism B X Y f).pushforward ⋙
      (bigPHMorphism B Y Z g).pushforward
```

**`AlgebraicGeometry.bigPHMorphism_comp_inverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/Ph/Composition.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/Ph/Composition.lean#L67). The attribute's comment: “inverse-image composition”.

> **Stacks 0DBS.** Inverse image for the composite morphism of big ph topoi is naturally
> isomorphic to the composite of the inverse-image functors.

```lean
public noncomputable def bigPHMorphism_comp_inverseImageIso :
    (bigPHMorphism B X Z (f ≫ g)).inverseImage ≅
      (bigPHMorphism B Y Z g).inverseImage ⋙
        (bigPHMorphism B X Y f).inverseImage
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 34.8, Tag 0DBC](https://stacks.math.columbia.edu/tag/0DBC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
