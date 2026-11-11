---
declaration: section
origin: cited
lean: SkyscraperSheaves.IsSkyscraperSheaf, Stacks.Modules.skyscraper, skyscraperSheaf, skyscraperPresheaf_eq_pushforward, skyscraperPresheafStalkOfSpecializes, skyscraperPresheafStalkOfNotSpecializes, Stacks.Modules.skyscraperHomEquiv, stalkSkyscraperSheafAdjunction
statement: formalized
proof: formalized
---

# 6.27 Skyscraper sheaves and stalks

Section 6.27 of the Stacks Project, [Tag 0099](https://stacks.math.columbia.edu/tag/0099). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 009A, a definition

[Tag 009A](https://stacks.math.columbia.edu/tag/009A) in the Stacks Project.

**`SkyscraperSheaves.IsSkyscraperSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L72). The attribute's comment: “(5), (6), (7)”.

> **Stacks 009A (5), (6), (7).** A sheaf `F` on `X` is a *skyscraper sheaf* if there are a
> point `x` of `X` and an object `A` of the target category with `F ≅ i_{x,*} A`.
>
> The target category is arbitrary, so this single predicate is the tag's clause (5) for sheaves
> of sets, its clause (6) for sheaves of abelian groups and its clause (7) for sheaves of
> algebraic structures. Clause (8), for sheaves of modules on a ringed space, is not covered
> here.

```lean
def IsSkyscraperSheaf (F : TopCat.Sheaf C X) : Prop
```

**`Stacks.Modules.skyscraper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean, line 411](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean#L411). The attribute's comment: “(4)”.

> **Stacks 009A (4).** The skyscraper sheaf of `𝒪_X`-modules at the point `z` with value the
> `𝒪_{X,z}`-module `V`: the pushforward of `V` along the inclusion of `z`, read as a morphism of
> ringed spaces `({z}, 𝒪_{X,z}) ⟶ (X, 𝒪_X)`.

```lean
noncomputable def skyscraper :
    SheafOfModules.{u} ((sheafCompose _ (forget₂ CommRingCat RingCat.{u})).obj R)
```

Declarations registered for the tag:

- [`skyscraperSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L41) (StacksFrontier): “The skyscraper sheaf at a point with a given value: the sheaf whose sections over `U` are the given object if `x ∈ U` and a terminal object otherwise. Mathlib's construction is uniform in the target category, so one declaration covers the tag's set, abelian-group and algebraic-structure cases; the ringed-space case, clause (4), is not covered.”.
- [`skyscraperPresheaf_eq_pushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheaf_eq_pushforward#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Basic.lean#L50) (StacksFrontier): “The skyscraper is the pushforward along the map from the one-point space sending the point to `x`, which is how the tag defines `i_{x,*} A`.”.

## Tag 009B, a lemma

[Tag 009B](https://stacks.math.columbia.edu/tag/009B) in the Stacks Project.

Declarations registered for the tag:

- [`skyscraperSheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperSheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L28) (StacksFrontier): “the skyscraper sheaf `i_{x,*}A`”.
- [`skyscraperPresheafStalkOfSpecializes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkOfSpecializes#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L29) (StacksFrontier): “stalk at a point of the closure of `{x}`, i.e. a specialization of `x`: it is `A`”. References: EGA IV (21.9.1), “stalk on closure”.
- [`skyscraperPresheafStalkOfNotSpecializes`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkOfNotSpecializes#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Stalk.lean#L33) (StacksFrontier): “stalk at a point outside the closure of `{x}`: it is terminal, a singleton for sheaves of sets”. References: EGA IV (21.9.1), “stalk off closure”.

## Tag 009C, a lemma

[Tag 009C](https://stacks.math.columbia.edu/tag/009C) in the Stacks Project.

**`Stacks.Modules.skyscraperHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Modules.lean#L443). The attribute's comment: “sheaves of modules”.

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

- [`stalkSkyscraperSheafAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=stalkSkyscraperSheafAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean#L28) (StacksFrontier).
- [`skyscraperPresheafStalkAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=skyscraperPresheafStalkAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Skyscraper/Adjunction.lean#L30) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.27, Tag 0099](https://stacks.math.columbia.edu/tag/0099)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
