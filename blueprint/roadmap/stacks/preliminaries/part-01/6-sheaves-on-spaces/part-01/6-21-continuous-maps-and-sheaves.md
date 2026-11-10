---
declaration: section
origin: cited
lean: TopCat.Sheaf.pushforward_sheaf_of_sheaf, pushforward_comp_presheaf, pushforward_comp_sheaf, TopCat.Presheaf.pushforward, TopCat.Presheaf.pullback, TopCat.Presheaf.pullbackPushforwardAdjunction, TopCat.Presheaf.pullbackObjObjOfImageOpen, TopCat.Presheaf.stalkPullbackHom
statement: formalized
proof: formalized
---

# 6.21 Continuous maps and sheaves

Section 6.21 of the Stacks Project, [Tag 008C](https://stacks.math.columbia.edu/tag/008C). 10 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 008D, a lemma

[Tag 008D](https://stacks.math.columbia.edu/tag/008D) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Sheaf.pushforward_sheaf_of_sheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Sheaf.pushforward_sheaf_of_sheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pushforward/IsSheaf.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pushforward/IsSheaf.lean#L22) (StacksFrontier): “the pushforward of a sheaf along a continuous map is a sheaf”. References: EGA 0 (3.4.1).

## Tag 008E, a lemma

[Tag 008E](https://stacks.math.columbia.edu/tag/008E) in the Stacks Project.

**`pushforward_comp_presheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pushforward/Comp.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pushforward/Comp.lean#L63). References: EGA 0 (3.4.3).

> For continuous maps `f : X ⟶ Y` and `g : Y ⟶ Z` of topological spaces, the pushforward
> functor `(g ∘ f)_*` on presheaves is equal to the composition `g_* ∘ f_*`.

```lean
theorem pushforward_comp_presheaf :
    TopCat.Presheaf.pushforward C (f ≫ g) =
      (TopCat.Presheaf.pushforward C f) ⋙ (TopCat.Presheaf.pushforward C g)
```

**`pushforward_comp_sheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pushforward/Comp.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pushforward/Comp.lean#L71). References: EGA 0 (3.4.3), “special case”.

> For continuous maps `f : X ⟶ Y` and `g : Y ⟶ Z` of topological spaces, the pushforward
> functor `(g ∘ f)_*` on sheaves is equal to the composition `g_* ∘ f_*`.

```lean
theorem pushforward_comp_sheaf
    {A : Type u} [Category.{v} A]
    {FA : A → A → Type*} {CA : A → Type v}
    [∀ X Y : A, FunLike (FA X Y) (CA X) (CA Y)]
    [ConcreteCategory A FA]
    [Limits.HasColimits A] [Limits.HasLimits A]
    [Limits.PreservesLimits (forget A)]
    [Limits.PreservesFilteredColimits (forget A)]
    [(forget A).ReflectsIsomorphisms] :
    TopCat.Sheaf.pushforward A (f ≫ g) =
      (TopCat.Sheaf.pushforward A f) ⋙ (TopCat.Sheaf.pushforward A g)
```

## Tag 008F, a lemma

[Tag 008F](https://stacks.math.columbia.edu/tag/008F) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.pushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.pushforward#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean#L25) (StacksFrontier): “the pushforward `f_*` on presheaves”. References: EGA 0 (3.4.1); EGA 0 (3.4.2); SGA 4 IV (4.1.1), “(F)”.
- [`TopCat.Presheaf.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean#L29) (StacksFrontier): “the pullback `f_p` on presheaves, the left Kan extension along `Opens.map f`”.
- [`TopCat.Presheaf.pullbackPushforwardAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.pullbackPushforwardAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean#L31) (StacksFrontier): “`f_p` is left adjoint to `f_*`”.
- [`TopCat.Presheaf.pullbackObjObjOfImageOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.pullbackObjObjOfImageOpen#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Adjunction.lean#L33) (StacksFrontier): “the value of `f_p G` on an open with open image”.

## Tag 008G, a lemma

[Tag 008G](https://stacks.math.columbia.edu/tag/008G) in the Stacks Project.

Declarations registered for the tag:

- [`TopCat.Presheaf.stalkPullbackHom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.stalkPullbackHom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/PresheafStalk.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/PresheafStalk.lean#L21) (StacksFrontier): “the canonical map `G_{f x} ⟶ (f_p G)_x` of stalks”.
- [`TopCat.Presheaf.stalkPullbackIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=TopCat.Presheaf.stalkPullbackIso#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/Pullback/PresheafStalk.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/PresheafStalk.lean#L23) (StacksFrontier): “that map is an isomorphism, i.e. a bijection of stalks for sets”.

## Tag 008H, a lemma

[Tag 008H](https://stacks.math.columbia.edu/tag/008H) in the Stacks Project.

**`stalkPullbackSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/SheafStalk.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/SheafStalk.lean#L70). References: SGA 4 IV (7.1), “partial”.

> For a continuous map `f : X ⟶ Y` of topological spaces, a point `x : X`, and a sheaf of sets `G`
> on `Y`, the canonical isomorphism between the stalk of the pullback sheaf `f⁻¹ G` at `x` and the
> stalk of `G` at `f x`.

```lean
noncomputable def stalkPullbackSheafIso (G : Y.Sheaf (Type u)) (x : X) :
    ((TopCat.Sheaf.pullback (Type u) f).obj G).presheaf.stalk x ≅
      G.presheaf.stalk (f x)
```

## Tag 008I, a lemma

[Tag 008I](https://stacks.math.columbia.edu/tag/008I) in the Stacks Project.

**`presheafPullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Comp.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Comp.lean#L110). The attribute's comment: “(1)”. References: SGA 4 VI (7.1.3), “special case”.

> **Stacks tag 008I, part (1): Composition of presheaf pullbacks.**
>
> For continuous maps `f : X ⟶ Y` and `g : Y ⟶ Z` of topological spaces, the
> presheaf pullback along the composition `f ≫ g` is canonically naturally
> isomorphic to the composition `pullback g ⋙ pullback f` (i.e., `f_p ∘ g_p` in
> the informal notation, where `f_p` and `g_p` denote presheaf pullback).
>
> The isomorphism is the canonical one obtained from uniqueness of left
> adjoints: `pullback (f ≫ g)` is a left adjoint of `pushforward (f ≫ g)`,
> while `pullback g ⋙ pullback f` is a left adjoint of
> `pushforward f ⋙ pushforward g`, and these two right adjoints are equal
> (Stacks tag 008E, captured by `presheafPushforwardCompIso`).

```lean
noncomputable def presheafPullbackCompIso
    (C : Type*) [Category C] [Limits.HasColimits C] :
    TopCat.Presheaf.pullback C (f ≫ g) ≅
      TopCat.Presheaf.pullback C g ⋙ TopCat.Presheaf.pullback C f
```

**`sheafPullbackCompIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/Pullback/Comp.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/Pullback/Comp.lean#L141). The attribute's comment: “(2)”. References: EGA 0 (3.5.5), “partial”; SGA 4 VI (7.1.3), “special case”.

> **Stacks tag 008I, part (2): Composition of sheaf pullbacks.**
>
> For continuous maps `f : X ⟶ Y` and `g : Y ⟶ Z` of topological spaces, the
> sheaf pullback along the composition `f ≫ g` is canonically naturally
> isomorphic to the composition `pullback g ⋙ pullback f` (i.e., `f⁻¹ ∘ g⁻¹` in
> the informal notation, where `f⁻¹` and `g⁻¹` denote sheaf pullback).
>
> The isomorphism is again the canonical one obtained from uniqueness of left
> adjoints, this time using `TopCat.Sheaf.pullbackPushforwardAdjunction` and
> `sheafPushforwardCompIso`.

```lean
noncomputable def sheafPullbackCompIso
    (A : Type*) [Category A]
    {FA : A → A → Type*} {CA : A → Type*}
    [∀ X Y : A, FunLike (FA X Y) (CA X) (CA Y)]
    [ConcreteCategory A FA]
    [Limits.HasColimits A] [Limits.HasLimits A]
    [Limits.PreservesLimits (CategoryTheory.forget A)]
    [Limits.PreservesFilteredColimits (CategoryTheory.forget A)]
    [(CategoryTheory.forget A).ReflectsIsomorphisms] :
    TopCat.Sheaf.pullback A (f ≫ g) ≅
      TopCat.Sheaf.pullback A g ⋙ TopCat.Sheaf.pullback A f
```

## Tag 008J, a definition

[Tag 008J](https://stacks.math.columbia.edu/tag/008J) in the Stacks Project.

**`IsStacksCompatible`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Defs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Defs.lean#L65).

> **Stacks 008J.** The compatibility condition on a family of section-level maps
> `app V : G(V) → F(f⁻¹V)`: for every inclusion `V' ≤ V` of opens of `Y`, restricting `app V s` to
> `f⁻¹V'` gives `app V'` applied to the restriction of `s`.  This is the commuting square of the
> Stacks text.

```lean
def IsStacksCompatible
    (G : TopCat.Sheaf (Type u) Y) (F : TopCat.Sheaf (Type u) X)
    (app : ∀ V : Opens Y, G.1.obj (op V) → F.1.obj (op ((Opens.map f).obj V))) :
    Prop
```

## Tag 008K, a lemma

[Tag 008K](https://stacks.math.columbia.edu/tag/008K) in the Stacks Project.

**`equiv_S1_S3`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L185).

> **Stacks 008K, (1) ↔ (3).**  Sheaf maps `G ⟶ f_* F` are in bijection with
> `f`-maps from `G` to `F`.  Functoriality in `F` and `G` is
> `equiv_S1_S3_naturality_F` and `equiv_S1_S3_naturality_G`.

```lean
noncomputable def equiv_S1_S3 : S1 f F G ≃ S3 f F G
```

**`equiv_S3_S4`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L253). References: SGA 4 XVII (0.2.1), “(ii), special case”.

> **Stacks 008K, (3) ↔ (4).**  `f`-maps from `G` to `F` are in bijection with
> compatible collections of section-level maps.  Functoriality in `F` and `G` is
> `equiv_S3_S4_naturality_F` and `equiv_S3_S4_naturality_G`.

```lean
noncomputable def equiv_S3_S4 : S3 f F G ≃ S4 f F G
```

**`equiv_S1_S2`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L262). References: SGA 4 XVII (0.2.1), “(i), special case”.

> **Stacks 008K, (1) ↔ (2)** via the pullback/pushforward adjunction.  Functoriality in
> `F` and `G` is recorded, in composite form, by `equiv_S2_S4_naturality_F` and
> `equiv_S2_S4_naturality_G`.

```lean
noncomputable def equiv_S1_S2 : S1 f F G ≃ S2 f F G
```

**`equiv_S1_S3_naturality_F`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L352).

> Naturality in `F` of the bijection `S₁ ≃ S₃`.

```lean
theorem equiv_S1_S3_naturality_F
    (F' : TopCat.Sheaf (Type u) X) (α : F ⟶ F') (a : S1 f F G) (V : Opens Y)
    (s : G.obj.obj (op V)) :
    (equiv_S1_S3 f F' G
        (a ≫ ((TopCat.Sheaf.pushforward (Type u) f).map α))).app V s
      = α.hom.app (op ((Opens.map f).obj V)) ((equiv_S1_S3 f F G a).app V s)
```

**`equiv_S1_S3_naturality_G`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 362](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L362).

> Naturality in `G` of the bijection `S₁ ≃ S₃`.

```lean
theorem equiv_S1_S3_naturality_G
    (G' : TopCat.Sheaf (Type u) Y) (β : G' ⟶ G) (a : S1 f F G) (V : Opens Y)
    (s : G'.obj.obj (op V)) :
    (equiv_S1_S3 f F G' (β ≫ a)).app V s
      = (equiv_S1_S3 f F G a).app V (β.hom.app (op V) s)
```

**`equiv_S3_S4_naturality_F`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L371).

> Naturality in `F` of the bijection `S₃ ≃ S₄`.

```lean
theorem equiv_S3_S4_naturality_F
    (F' : TopCat.Sheaf (Type u) X) (α : F ⟶ F') (ξ : S3 f F G) :
    equiv_S3_S4 f F' G (FMapAppNaturalityStruct.postcomp f G α ξ)
      = CompatibleCollection.postcomp f G α (equiv_S3_S4 f F G ξ)
```

**`equiv_S3_S4_naturality_G`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L383).

> Naturality in `G` of the bijection `S₃ ≃ S₄`.

```lean
theorem equiv_S3_S4_naturality_G
    (G' : TopCat.Sheaf (Type u) Y) (β : G' ⟶ G) (ξ : S3 f F G) :
    equiv_S3_S4 f F G' (FMapAppNaturalityStruct.precomp f F β ξ)
      = CompatibleCollection.precomp f F β (equiv_S3_S4 f F G ξ)
```

**`equiv_S2_S4_naturality_F`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L391).

> Naturality in `F` of the bijection `S₂ ≃ S₄`.

```lean
theorem equiv_S2_S4_naturality_F
    (F' : TopCat.Sheaf (Type u) X) (α : F ⟶ F') (b : S2 f F G)
    (U : Opens X) (V : Opens Y) (hUV : U ≤ (Opens.map f).obj V)
    (s : G.obj.obj (op V)) :
    (equiv_S2_S4 f F' G (b ≫ α)).app U V hUV s
      = α.hom.app (op U) ((equiv_S2_S4 f F G b).app U V hUV s)
```

**`equiv_S2_S4_naturality_G`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Bijections.lean#L405).

> Naturality in `G` of the bijection `S₂ ≃ S₄`.

```lean
theorem equiv_S2_S4_naturality_G
    (G' : TopCat.Sheaf (Type u) Y) (β : G' ⟶ G) (b : S2 f F G)
    (U : Opens X) (V : Opens Y) (hUV : U ≤ (Opens.map f).obj V)
    (s : G'.obj.obj (op V)) :
    (equiv_S2_S4 f F G'
          ((TopCat.Sheaf.pullback (Type u) f).map β ≫ b)).app U V hUV s
      = (equiv_S2_S4 f F G b).app U V hUV (β.hom.app (op V) s)
```

## Tag 008L, a definition

[Tag 008L](https://stacks.math.columbia.edu/tag/008L) in the Stacks Project.

**`StacksFMap.compPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Comp.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Comp.lean#L123). References: EGA 0 (4.4.2); EGA 0 (4.4.8), “definition of v''”; EGA 0 (3.5.2).

> The composition of an `f`-map `φ : G → F` and a `g`-map `ψ : H → G` of presheaves: the
> `(f ≫ g)`-map with components `ψ_W ≫ φ_{g⁻¹ W}`.

```lean
def compPresheaf {f : X ⟶ Y} {g : Y ⟶ Z}
    {F : TopCat.Presheaf C X} {G : TopCat.Presheaf C Y} {H : TopCat.Presheaf C Z}
    (φ : StacksFMap f F G) (ψ : StacksFMap g G H) :
    StacksFMap (f ≫ g) F H
```

**`fMapComp`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Functors/FMap/Comp.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Comp.lean#L143). References: EGA 0 (4.4.2); EGA 0 (4.4.8), “definition of v''”; EGA 0 (3.5.2), “special case”.

> The composition of `f`-maps of sheaves, as the morphism `ψ ≫ (pushforward g).map φ`.

```lean
noncomputable def fMapComp {C : Type*} [Category C] {X Y Z : TopCat}
    (f : X ⟶ Y) (g : Y ⟶ Z)
    (F : TopCat.Sheaf C X) (G : TopCat.Sheaf C Y) (H : TopCat.Sheaf C Z)
    (φ : G ⟶ (TopCat.Sheaf.pushforward C f).obj F)
    (ψ : H ⟶ (TopCat.Sheaf.pushforward C g).obj G) :
    H ⟶ (TopCat.Sheaf.pushforward C (f ≫ g)).obj F
```

## Tag 008M, a lemma

[Tag 008M](https://stacks.math.columbia.edu/tag/008M) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.PresheafedSpace.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean#L26) (StacksFrontier): “an f-map `(f, φ)`, i.e. a morphism `G ⟶ f_* F` of presheaves on `Y` over a continuous `f`”. References: EGA 0 (3.5.1); EGA 0 (4.1.1), “morphism definition”; EGA 0 (3.5.2), “category of pairs”.
- [`AlgebraicGeometry.PresheafedSpace.Hom.stalkMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.Hom.stalkMap#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean#L29) (StacksFrontier): “the map of stalks `G_{f x} ⟶ F_x` induced by an f-map”. References: EGA 0 (3.5.1); EGA 0 (4.4.3), “partial”; EGA 0 (3.4.4), “construction of ψ_x”.
- [`AlgebraicGeometry.PresheafedSpace.stalkMap.comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.PresheafedSpace.stalkMap.comp#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Functors/FMap/Stalk.lean#L34) (StacksFrontier): “the stalk map of a composition is the composition of the stalk maps”. References: EGA 0 (3.4.4), “ψ''_x = ψ_x ∘ ψ'_{ψ(x)}”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.21, Tag 008C](https://stacks.math.columbia.edu/tag/008C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
