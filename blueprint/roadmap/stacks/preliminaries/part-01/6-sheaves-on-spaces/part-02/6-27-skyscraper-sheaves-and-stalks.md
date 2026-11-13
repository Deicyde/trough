---
declaration: section
origin: cited
lean: SkyscraperSheaves.IsSkyscraperSheaf, Stacks.Modules.skyscraper, Stacks.Modules.IsSkyscraperSheaf, skyscraperSheaf, skyscraperPresheaf_eq_pushforward, Stacks.Modules.skyscraperStalkIsoOfSpecializes, Stacks.Modules.isZero_skyscraper_stalk_of_not_specializes, skyscraperPresheafStalkOfSpecializes
statement: formalized
proof: formalized
---

# 6.27 Skyscraper sheaves and stalks

Section 6.27 of the Stacks Project, [Tag 0099](https://stacks.math.columbia.edu/tag/0099). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 009A, a definition

[Tag 009A](https://stacks.math.columbia.edu/tag/009A) in the Stacks Project.

**`SkyscraperSheaves.IsSkyscraperSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L73). The attribute's comment: “(5), (6), (7)”.

> **Stacks 009A (5), (6), (7).** A sheaf `F` on `X` is a *skyscraper sheaf* if there are a
> point `x` of `X` and an object `A` of the target category with `F ≅ i_{x,*} A`.
>
> The target category is arbitrary, so this single predicate is the tag's clause (5) for sheaves
> of sets, its clause (6) for sheaves of abelian groups and its clause (7) for sheaves of
> algebraic structures. Clause (8), for sheaves of modules on a ringed space, is
> `Stacks.Modules.IsSkyscraperSheaf`.

```lean
def IsSkyscraperSheaf (F : TopCat.Sheaf C X) : Prop
```

**`Stacks.Modules.skyscraper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean#L413). The attribute's comment: “(4)”.

> **Stacks 009A (4).** The skyscraper sheaf of `𝒪_X`-modules at the point `z` with value the
> `𝒪_{X,z}`-module `V`: the pushforward of `V` along the inclusion of `z`, read as a morphism of
> ringed spaces `({z}, 𝒪_{X,z}) ⟶ (X, 𝒪_X)`.

```lean
noncomputable def skyscraper :
    SheafOfModules.{u} ((sheafCompose _ (forget₂ CommRingCat RingCat.{u})).obj R)
```

**`Stacks.Modules.IsSkyscraperSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean, line 515](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean#L515). The attribute's comment: “(8)”.

> **Stacks 009A (8).** A sheaf `ℱ` of `𝒪_X`-modules is a *skyscraper sheaf* if there are a
> point `z` of `X` and an `𝒪_{X,z}`-module `V` with `ℱ ≅ i_{z,*} V` as sheaves of
> `𝒪_X`-modules.

```lean
def IsSkyscraperSheaf
    (F : SheafOfModules.{u} ((sheafCompose _ (forget₂ CommRingCat RingCat.{u})).obj R)) : Prop
```

Declarations registered for the tag:

- [`skyscraperSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L42) (StacksFrontier): “The skyscraper sheaf at a point with a given value: the sheaf whose sections over `U` are the given object if `x ∈ U` and a terminal object otherwise. Mathlib's construction is uniform in the target category, so one declaration covers the tag's set, abelian-group and algebraic-structure cases (1)–(3). The ringed-space case (4) is `Stacks.Modules.skyscraper`.”.
- [`skyscraperPresheaf_eq_pushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheaf_eq_pushforward#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L51) (StacksFrontier): “The skyscraper is the pushforward along the map from the one-point space sending the point to `x`, which is how the tag defines `i_{x,*} A`.”.

## Tag 009B, a lemma

[Tag 009B](https://stacks.math.columbia.edu/tag/009B) in the Stacks Project.

**`Stacks.Modules.skyscraperStalkIsoOfSpecializes`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/ModulesStalk.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/ModulesStalk.lean#L139). The attribute's comment: “sheaves of modules, stalk at a point `y` of the closure of `{z}`, i.e. `z ⤳ y`: it is `V`, an `𝒪_{X,y}`-module through the specialization map `𝒪_{X,y} ⟶ 𝒪_{X,z}`”.

> **Stacks 009B for sheaves of modules, on the closure of `{z}`.** For `z ⤳ y`, i.e. `y` in the
> closure of `{z}`, the stalk at `y` of the skyscraper sheaf of `𝒪_X`-modules at `z` with value
> `V` is `V`, as an `𝒪_{X,y}`-module through the specialization map `𝒪_{X,y} ⟶ 𝒪_{X,z}`.

```lean
noncomputable def skyscraperStalkIsoOfSpecializes {y : X} (h : z ⤳ y) :
    ModuleCat.of ↑(TopCat.Presheaf.stalk R.obj y)
        ↑(TopCat.Presheaf.stalk (skyscraper R z V).val.presheaf y) ≅
      (ModuleCat.restrictScalars (TopCat.Presheaf.stalkSpecializes R.obj h).hom).obj V
```

**`Stacks.Modules.isZero_skyscraper_stalk_of_not_specializes`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/ModulesStalk.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/ModulesStalk.lean#L159). The attribute's comment: “sheaves of modules, stalk at a point `y` outside the closure of `{z}`, i.e. `¬ z ⤳ y`: it is zero”.

> **Stacks 009B for sheaves of modules, off the closure of `{z}`.** For `y` not in the closure
> of `{z}`, i.e. `¬ z ⤳ y`, the stalk at `y` of the skyscraper sheaf of `𝒪_X`-modules at `z` is
> zero.

```lean
lemma isZero_skyscraper_stalk_of_not_specializes {y : X} (h : ¬z ⤳ y) :
    IsZero (ModuleCat.of ↑(TopCat.Presheaf.stalk R.obj y)
      ↑(TopCat.Presheaf.stalk (skyscraper R z V).val.presheaf y))
```

Declarations registered for the tag:

- [`skyscraperSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L31) (StacksFrontier): “the skyscraper sheaf `i_{x,*}A`”.
- [`skyscraperPresheafStalkOfSpecializes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkOfSpecializes#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L32) (StacksFrontier): “sets, abelian groups and algebraic structures (any target category with colimits and a terminal object), stalk at a point of the closure of `{x}`, i.e. a specialization of `x`: it is `A`”. References: EGA IV (21.9.1), “stalk on closure”.
- [`skyscraperPresheafStalkOfNotSpecializes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkOfNotSpecializes#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L37) (StacksFrontier): “sets, abelian groups and algebraic structures (any target category with colimits and a terminal object), stalk at a point outside the closure of `{x}`: it is terminal, a singleton for sheaves of sets”. References: EGA IV (21.9.1), “stalk off closure”.

## Tag 009C, a lemma

[Tag 009C](https://stacks.math.columbia.edu/tag/009C) in the Stacks Project.

**`Stacks.Modules.skyscraperHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean#L445). The attribute's comment: “sheaves of modules”.

> **Stacks 009C for sheaves of modules.** Morphisms of sheaves of `𝒪_X`-modules from `ℱ` into
> the skyscraper at `z` with value `V` are the same thing as `𝒪_{X,z}`-linear maps `ℱ_z ⟶ V`;
> this is the adjunction between the stalk functor and the skyscraper functor.

```lean
noncomputable def skyscraperHomEquiv
    (G : SheafOfModules.{u} ((sheafCompose _ (forget₂ CommRingCat RingCat.{u})).obj R)) :
    (G ⟶ skyscraper R z V) ≃
      (↑(TopCat.Presheaf.stalk G.val.presheaf z) →ₗ[↑(TopCat.Presheaf.stalk R.obj z)] ↑V)
```

Declarations registered for the tag:

- [`stalkSkyscraperSheafAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=stalkSkyscraperSheafAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean#L28) (StacksFrontier).
- [`skyscraperPresheafStalkAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean#L30) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.27, Tag 0099](https://stacks.math.columbia.edu/tag/0099)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
