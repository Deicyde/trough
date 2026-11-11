---
declaration: section
origin: cited
lean: Stacks.Topology.SheafStalk.mono_iff_stalk_injective, Stacks.Topology.SheafStalk.epi_iff_stalk_surjective, Stacks.Topology.SheafStalk.isIso_iff_stalk_bijective, SheafInjectiveSurjective.presheaf_mono_iff_injective, SheafInjectiveSurjective.presheaf_epi_iff_surjective, SheafInjectiveSurjective.sheaf_mono_iff_injective, SheafInjectiveSurjective.isLocallySurjective_iff_exists_cover, CategoryTheory.Subfunctor
statement: formalized
proof: formalized
---

# 6.16 Exactness and points

Section 6.16 of the Stacks Project, [Tag 007S](https://stacks.math.columbia.edu/tag/007S). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 007T, a lemma

[Tag 007T](https://stacks.math.columbia.edu/tag/007T) in the Stacks Project.

**`Stacks.Topology.SheafStalk.mono_iff_stalk_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean#L44). The attribute's comment: “(1)”.

> A morphism of sheaves of sets is a monomorphism in the category of
> sheaves if and only if it is injective on stalks at every point.

```lean
theorem mono_iff_stalk_injective {X : TopCat.{u}} {F G : TopCat.Sheaf (Type u) X}
    (φ : F ⟶ G) : Mono φ ↔ ∀ x : X, Function.Injective (stalkMap φ x)
```

**`Stacks.Topology.SheafStalk.epi_iff_stalk_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean#L89). The attribute's comment: “(2)”.

> A morphism of sheaves of sets is an epimorphism in the category of
> sheaves if and only if it is surjective on stalks at every point.

```lean
theorem epi_iff_stalk_surjective {X : TopCat.{u}} {F G : TopCat.Sheaf (Type u) X}
    (φ : F ⟶ G) : Epi φ ↔ ∀ x : X, Function.Surjective (stalkMap φ x)
```

**`Stacks.Topology.SheafStalk.isIso_iff_stalk_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Stalk.lean#L96). The attribute's comment: “(3)”.

> A morphism of sheaves of sets is an isomorphism if and only if it is
> bijective on stalks at every point.

```lean
theorem isIso_iff_stalk_bijective {X : TopCat.{u}} {F G : TopCat.Sheaf (Type u) X}
    (φ : F ⟶ G) : IsIso φ ↔ ∀ x : X, Function.Bijective (stalkMap φ x)
```

## Tag 007U, a definition

[Tag 007U](https://stacks.math.columbia.edu/tag/007U) in the Stacks Project.

**`SheafInjectiveSurjective.presheaf_mono_iff_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L69). The attribute's comment: “(2)”.

> **Stacks 007U (2).** A morphism of presheaves of sets is injective in the sense of the
> tag — injective on sections over every open — exactly when it is a monomorphism of
> presheaves. Monomorphisms in a functor category into `Type u` are detected objectwise, and
> monomorphisms of types are the injections.

```lean
theorem presheaf_mono_iff_injective {F G : TopCat.Presheaf (Type u) X} (φ : F ⟶ G) :
    Mono φ ↔ ∀ U : (Opens X)ᵒᵖ, Function.Injective (φ.app U)
```

**`SheafInjectiveSurjective.presheaf_epi_iff_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L82). The attribute's comment: “(3)”.

> **Stacks 007U (3).** A morphism of presheaves of sets is surjective in the sense of the
> tag — surjective on sections over every open — exactly when it is an epimorphism of
> presheaves. Epimorphisms in a functor category into `Type u` are detected objectwise, and
> epimorphisms of types are the surjections.
>
> Contrast clause (5): for *sheaves* this pointwise condition is strictly stronger than being
> an epimorphism.

```lean
theorem presheaf_epi_iff_surjective {F G : TopCat.Presheaf (Type u) X} (φ : F ⟶ G) :
    Epi φ ↔ ∀ U : (Opens X)ᵒᵖ, Function.Surjective (φ.app U)
```

**`SheafInjectiveSurjective.sheaf_mono_iff_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L97). The attribute's comment: “(4)”.

> **Stacks 007U (4).** A morphism of sheaves of sets is injective in the sense of the tag —
> injective on sections over every open — exactly when it is a monomorphism of sheaves.
>
> A morphism of sheaves is a monomorphism precisely when the underlying morphism of presheaves
> is (`CategoryTheory.Sheaf.Hom.mono_iff_presheaf_mono`, which uses that `sheafToPresheaf` is a
> right adjoint), and then clause (2) applies. So, unlike surjectivity, injectivity of a
> morphism of sheaves is the same condition whether it is read in presheaves or in sheaves.

```lean
theorem sheaf_mono_iff_injective {F G : TopCat.Sheaf (Type u) X} (φ : F ⟶ G) :
    Mono φ ↔ ∀ U : (Opens X)ᵒᵖ, Function.Injective (φ.hom.app U)
```

**`SheafInjectiveSurjective.isLocallySurjective_iff_exists_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L115). The attribute's comment: “(5)”.

> **Stacks 007U (5).** A morphism `φ : F ⟶ G` of presheaves of sets on `X` is locally
> surjective exactly when for every open `U` and every section `t` of `G` over `U` there is an
> open covering `U = ⨆ i, V i` such that `t|_{V i}` lies in the image of `F(V i) → G(V i)` for
> every `i`. The right-hand side is the tag's definition of a surjective morphism of sheaves,
> verbatim; so `TopCat.Presheaf.IsLocallySurjective` is that notion.
>
> Mathlib's `TopCat.Presheaf.isLocallySurjective_iff` states the condition pointwise: every
> point of `U` has a neighbourhood inside `U` on which `t` is in the image. Passing between the
> two is exactly the passage between "an open cover of `U`" and "a neighbourhood for each point
> of `U`": indexing the chosen neighbourhoods by the points of `U` produces a cover, and
> conversely a member of a cover containing a given point is such a neighbourhood.

```lean
theorem isLocallySurjective_iff_exists_cover {F G : TopCat.Presheaf (Type u) X} (φ : F ⟶ G) :
    TopCat.Presheaf.IsLocallySurjective φ ↔
      ∀ (U : Opens X) (t : ToType (G.obj (op U))),
        ∃ (ι : Type u) (V : ι → Opens X) (hVU : ∀ i, V i ≤ U), U = iSup V ∧
          ∀ i, ∃ s : ToType (F.obj (op (V i))),
            φ.app (op (V i)) s = TopCat.Presheaf.restrictOpen t (V i) (hVU i)
```

Declarations registered for the tag:

- [`CategoryTheory.Subfunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Subfunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L48) (StacksFrontier): “A subpresheaf of a presheaf of sets `G` on `X`: `Subfunctor G` is a subset `F U ⊆ G U` for each object `U`, required to be carried into itself by every restriction map of `G`, which is the tag's condition. Instantiating the ambient category at `(Opens X)ᵒᵖ` gives subpresheaves on a topological space.”. References: SGA 3 I (1.2); SGA 3 IV (4.1.1), “more general”.
- [`CategoryTheory.Subfunctor.toFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Subfunctor.toFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Defs.lean#L57) (StacksFrontier): “The subpresheaf viewed as a presheaf in its own right, with the restriction maps induced by those of `G`. A subsheaf of a sheaf is a subpresheaf whose `toFunctor` is again a sheaf.”. References: SGA 3 I (1.2).

## Tag 0H7H, a lemma

[Tag 0H7H](https://stacks.math.columbia.edu/tag/0H7H) in the Stacks Project.

**`StacksDefinitionInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/Basic.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/Basic.lean#L136). References: SGA 4 IV (6.4.3), “sheaves on a space”; SGA 3 I (1.2), “special case”; SGA 4 IV (8.4.1), “fourth conjunct”.

> **Stacks 0H7H, full statement.**
>
> Let `X : TopCat`.
>
> 1. For a morphism `f : F ⟶ G` of presheaves of types on `X`:
>    - `f` is a monomorphism iff each component `f.app U` is injective;
>    - `f` is an epimorphism iff each component `f.app U` is surjective.
> 2. For a morphism `f : F ⟶ G` of sheaves of types on `X`:
>    - `f` is a monomorphism iff each component `f.1.app U` is injective,
>      iff `f` is injective on every stalk;
>    - `f` is an epimorphism iff `f` is surjective on every stalk.
>
> The Stacks notion of "injective map of sheaves" is "injective on every open set", and the
> Stacks notion of "surjective map of sheaves" is "surjective on every stalk"
> (cf. Stacks tag 008Q).  With those Stacks definitions, the two parts above show that
> in `Sh(X)` the epimorphisms are exactly the surjective maps of sheaves and the
> monomorphisms are exactly the injective maps of sheaves.

```lean
theorem StacksDefinitionInjective :
    -- Part (1): presheaves
    (∀ {F G : TopCat.Presheaf (Type u) X} (f : F ⟶ G),
        Mono f ↔ ∀ U : (Opens X)ᵒᵖ, Function.Injective (f.app U)) ∧
    (∀ {F G : TopCat.Presheaf (Type u) X} (f : F ⟶ G),
        Epi f ↔ ∀ U : (Opens X)ᵒᵖ, Function.Surjective (f.app U)) ∧
    -- Part (2): sheaves
    (∀ {F G : TopCat.Sheaf (Type u) X} (f : F ⟶ G),
        Mono f ↔ ∀ U : (Opens X)ᵒᵖ, Function.Injective (f.1.app U)) ∧
    (∀ {F G : TopCat.Sheaf (Type u) X} (f : F ⟶ G),
        Mono f ↔ ∀ x : X,
          Function.Injective ((TopCat.Presheaf.stalkFunctor (Type u) x).map f.1)) ∧
    (∀ {F G : TopCat.Sheaf (Type u) X} (f : F ⟶ G),
        Epi f ↔ ∀ x : X,
          Function.Surjective ((TopCat.Presheaf.stalkFunctor (Type u) x).map f.1))
```

## Tag 007W, a lemma

[Tag 007W](https://stacks.math.columbia.edu/tag/007W) in the Stacks Project.

**`ExactnessPoints.exists_unique_hom_of_stalkHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/EpiMono/AlgebraicStructure.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/EpiMono/AlgebraicStructure.lean#L232).

> **Stacks 007W (Lemma 6.15.6).** Let `X` be a topological space, let `(C, F)` be a type of
> algebraic structure, let `𝓕` and `𝓖` be sheaves on `X` with values in `C`, and let
> `φ : 𝓕 ⋙ F ⟶ 𝓖 ⋙ F` be a map of the underlying sheaves of sets. If for every `x ∈ X` the
> induced map `𝓕_x ⟶ 𝓖_x` is a morphism of algebraic structures, then `φ` is (uniquely) a
> morphism of sheaves with values in `C`.
>
> The hypothesis on stalks is `StalkHom S 𝓕 𝓖 φ`, and "is a morphism of sheaves with values in
> `C`" is: there is a unique `α : 𝓕 ⟶ 𝓖` in `C`-valued presheaves with
> `Functor.whiskerRight α S.F = φ`.
>
> Only the sheaf condition on `𝓖` is used.

```lean
theorem exists_unique_hom_of_stalkHom {𝓕 𝓖 : X.Presheaf S.C}
    (_h𝓕 : TopCat.Presheaf.IsSheaf (𝓕 ⋙ S.F))
    (h𝓖 : TopCat.Presheaf.IsSheaf (𝓖 ⋙ S.F))
    (φ : 𝓕 ⋙ S.F ⟶ 𝓖 ⋙ S.F) (T : StalkHom S 𝓕 𝓖 φ) :
    ∃! α : 𝓕 ⟶ 𝓖, Functor.whiskerRight α S.F = φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.16, Tag 007S](https://stacks.math.columbia.edu/tag/007S)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
