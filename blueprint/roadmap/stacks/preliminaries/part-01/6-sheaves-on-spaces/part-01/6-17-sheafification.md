---
declaration: section
origin: cited
lean: TopCat.Presheaf.sheafify, stalkFunctor_map_toSheafify_isIso, TopCat.Presheaf.existsUnique_toSheafify_comp_eq, TopCat.isIso_sheafifyLift_constantPresheafToLocallyConstant, separated_iff_toSheafify_injective, TopCat.Presheaf.isLocallyInjective_presheafToSheaf_map_of_injective, TopCat.Presheaf.isLocallySurjective_presheafToSheaf_map_of_surjective
statement: formalized
proof: formalized
---

# 6.17 Sheafification

Section 6.17 of the Stacks Project, [Tag 007X](https://stacks.math.columbia.edu/tag/007X). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 007Y, a lemma

[Tag 007Y](https://stacks.math.columbia.edu/tag/007Y) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/Basic.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/Basic.lean#L22) (StacksFrontier): “the sheafification `F^#` of a presheaf of sets, as a sheaf”. References: EGA 0 (3.7.1).

## Tag 007Z, a lemma

[Tag 007Z](https://stacks.math.columbia.edu/tag/007Z) in the Stacks Project.

**`stalkFunctor_map_toSheafify_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Stalk.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/Stalk.lean#L82).

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

**`TopCat.Presheaf.existsUnique_toSheafify_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/UniversalProperty.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/UniversalProperty.lean#L123). The attribute's comment: “The sheafification `F^#` is Mathlib's `TopCat.Presheaf.sheafify`, built from locally-germ sections as in 007Y, with `toSheafify` the map to it. The factorization is obtained from local injectivity and local surjectivity of `toSheafify` for open covers.”.

> **Stacks tag 0080.** Let `F` be a presheaf of sets on a topological space `X`. Any morphism
> `η : F ⟶ G` into a sheaf of sets `G` factors uniquely as `F → F^# → G`, where `F^#` is the
> sheafification `TopCat.Presheaf.sheafify` of tag 007Y (sections that are locally germs) and
> `F → F^#` is `TopCat.Presheaf.toSheafify`.

```lean
theorem existsUnique_toSheafify_comp_eq (G : Sheaf (Type v) X) (η : F ⟶ G.presheaf) :
    ∃! γ : F.sheafify.presheaf ⟶ G.presheaf, F.toSheafify ≫ γ = η
```

## Tag 0081, an example

[Tag 0081](https://stacks.math.columbia.edu/tag/0081) in the Stacks Project.

**`TopCat.isIso_sheafifyLift_constantPresheafToLocallyConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/LocallyConstant.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/LocallyConstant.lean#L96).

> **Stacks 0081** (Example 6.17.4). Let `X` be a topological space and `A` a set. The map
> `A_p ⟶ A̲` from the constant presheaf with value `A` to the constant sheaf with value `A`
> (the sheaf of locally constant maps to `A`) induces an isomorphism `A_p^# ⟶ A̲`: the
> sheafification of the constant presheaf with value `A` is the constant sheaf with value `A`.

```lean
theorem isIso_sheafifyLift_constantPresheafToLocallyConstant :
    IsIso (sheafifyLift (Opens.grothendieckTopology X) (constantPresheafToLocallyConstant X A)
      (locallyConstantSheaf X A).property)
```

## Tag 0082, a lemma

[Tag 0082](https://stacks.math.columbia.edu/tag/0082) in the Stacks Project.

**`separated_iff_toSheafify_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/Separated.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/Separated.lean#L103).

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

**`TopCat.Presheaf.isLocallyInjective_presheafToSheaf_map_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean#L54).

> The sheafification of an injective morphism of presheaves of sets is injective: if every
> `φ.app U` is injective, then the sheafified morphism is locally injective, which for a morphism of
> sheaves is injectivity (see `TopCat.Presheaf.injective_app_presheafToSheaf_map_of_injective`).

```lean
theorem isLocallyInjective_presheafToSheaf_map_of_injective
    (hφ : ∀ U, Function.Injective (φ.app U)) :
    Sheaf.IsLocallyInjective
      ((presheafToSheaf (Opens.grothendieckTopology X) (Type u)).map φ)
```

**`TopCat.Presheaf.isLocallySurjective_presheafToSheaf_map_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/PreservesMonoEpi.lean#L66).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
