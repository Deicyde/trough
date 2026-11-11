---
declaration: section
origin: cited
lean: TopCat.Presheaf.sheafify, stalkFunctor_map_toSheafify_isIso, sheafify_universal_property, sheafifyConstantPresheafIso, separated_iff_toSheafify_injective, TopCat.Presheaf.isLocallyInjective_presheafToSheaf_map_of_injective, TopCat.Presheaf.isLocallySurjective_presheafToSheaf_map_of_surjective
statement: formalized
proof: formalized
---

# 6.17 Sheafification

Section 6.17 of the Stacks Project, [Tag 007X](https://stacks.math.columbia.edu/tag/007X). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 007Y, a lemma

[Tag 007Y](https://stacks.math.columbia.edu/tag/007Y) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/Basic.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Basic.lean#L22) (StacksFrontier): “the sheafification `F^#` of a presheaf of sets, as a sheaf”. References: EGA 0 (3.7.1).

## Tag 007Z, a lemma

[Tag 007Z](https://stacks.math.columbia.edu/tag/007Z) in the Stacks Project.

**`stalkFunctor_map_toSheafify_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Stalk.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Stalk.lean#L82).

> **Stacks tag 007Z.** Let `F` be a presheaf of sets on a topological space `X`
> and let `x : X`. The canonical map `F → F^#` induces an isomorphism of stalks
> `F_x ≃ F^#_x`.

```lean
theorem stalkFunctor_map_toSheafify_isIso
    {X : TopCat} (F : Presheaf (Type u) X) (x : X) :
    IsIso ((stalkFunctor (Type u) x).map (toSheafify F))
```

## Tag 0080, a lemma

[Tag 0080](https://stacks.math.columbia.edu/tag/0080) in the Stacks Project.

**`sheafify_universal_property`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/UniversalProperty.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/UniversalProperty.lean#L65). References: EGA 0 (3.5.3), “partial, special case”; EGA 0 (3.5.6), “more general”.

> **Stacks tag 0080.** Any morphism from a presheaf `F` to a sheaf `G`
> factors uniquely as `F → F^# → G`, where `F → F^#` is the canonical
> morphism from `F` to its sheafification.

```lean
theorem sheafify_universal_property
    {C : Type u₁} [Category.{v₁} C] (J : GrothendieckTopology C)
    {D : Type u₂} [Category.{v₂} D] [HasWeakSheafify J D]
    {F G : Cᵒᵖ ⥤ D} (η : F ⟶ G) (hG : Presheaf.IsSheaf J G) :
    ∃! γ : sheafify J F ⟶ G, toSheafify J F ≫ γ = η
```

## Tag 0081, an example

[Tag 0081](https://stacks.math.columbia.edu/tag/0081) in the Stacks Project.

**`sheafifyConstantPresheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Constant.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Constant.lean#L68).

> **Stacks tag 0081.** The sheafification of the constant presheaf with value
> `A` is the constant sheaf with value `A`. Concretely, the underlying presheaf of
> the constant sheaf `(constantSheaf J D).obj A` is, by definition, the
> sheafification of the constant presheaf `(Functor.const Cᵒᵖ).obj A`, so the
> canonical comparison map is the identity isomorphism.

```lean
noncomputable def sheafifyConstantPresheafIso
    {C : Type u₁} [Category.{v₁} C] (J : GrothendieckTopology C)
    {D : Type u₂} [Category.{v₂} D] [HasWeakSheafify J D] (A : D) :
    sheafify J ((Functor.const Cᵒᵖ).obj A) ≅ ((constantSheaf J D).obj A).obj
```

## Tag 0082, a lemma

[Tag 0082](https://stacks.math.columbia.edu/tag/0082) in the Stacks Project.

**`separated_iff_toSheafify_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Separated.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Separated.lean#L103).

> **Stacks Project, tag 0082.** Let `F` be a presheaf of sets on a
> topological space `X`. Then `F` is separated if and only if the
> canonical morphism `θ_F : F ⟶ F^#` to its sheafification is
> sectionwise injective.

```lean
theorem separated_iff_toSheafify_injective (F : TopCat.Presheaf (Type v) X) :
    IsSeparated F ↔ MorphismInjective (F.toSheafify)
```

## Tag 0H7I, a lemma

[Tag 0H7I](https://stacks.math.columbia.edu/tag/0H7I) in the Stacks Project.

**`TopCat.Presheaf.isLocallyInjective_presheafToSheaf_map_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean#L54).

> The sheafification of an injective morphism of presheaves of sets is injective: if every
> `φ.app U` is injective, then the sheafified morphism is locally injective, which for a morphism of
> sheaves is injectivity (see `TopCat.Presheaf.injective_app_presheafToSheaf_map_of_injective`).

```lean
theorem isLocallyInjective_presheafToSheaf_map_of_injective
    (hφ : ∀ U, Function.Injective (φ.app U)) :
    Sheaf.IsLocallyInjective
      ((presheafToSheaf (Opens.grothendieckTopology X) (Type u)).map φ)
```

**`TopCat.Presheaf.isLocallySurjective_presheafToSheaf_map_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean#L66).

> The sheafification of a surjective morphism of presheaves of sets is surjective: if every
> `φ.app U` is surjective, then every section of the sheafification of `G` is locally in the image of
> the sheafification of `φ`.

```lean
theorem isLocallySurjective_presheafToSheaf_map_of_surjective
    (hφ : ∀ U, Function.Surjective (φ.app U)) :
    Sheaf.IsLocallySurjective
      ((presheafToSheaf (Opens.grothendieckTopology X) (Type u)).map φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.17, Tag 007X](https://stacks.math.columbia.edu/tag/007X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
