---
declaration: section
origin: cited
lean: Deformation.Examples.FiniteProjectiveRepresentation, Deformation.Examples.FiniteProjectiveRepresentation.Hom, Deformation.Examples.FiniteProjectiveRepresentation.instCategory, Deformation.Examples.FiniteProjectiveRepresentation.specialFiber, Deformation.Examples.FiniteProjectiveRepresentation.deformationCategory, Deformation.Examples.FiniteProjectiveRepresentation.projection, Deformation.Examples.FiniteProjectiveRepresentation.projection_isCofiberedInGroupoids, Deformation.RepresentationCategory
statement: formalized
proof: formalized
---

# 93.5 Representations of a group

Section 93.5 of the Stacks Project, [Tag 0DVR](https://stacks.math.columbia.edu/tag/0DVR). 4 tags here are carried by 24 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D3J, an example

[Tag 0D3J](https://stacks.math.columbia.edu/tag/0D3J) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveRepresentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/Representations.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/Representations.lean#L58). The attribute's comment: “representation\_category: objects”.

> A finite projective representation of `Γ` over an Artinian local `Λ`-algebra with residue
> field `k`.

```lean
public structure FiniteProjectiveRepresentation
    (Λ : Type u) (k : Type w) (Γ : Type*) [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ]
```

**`Deformation.Examples.FiniteProjectiveRepresentation.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/Representations.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/Representations.lean#L78). The attribute's comment: “representation\_category: morphisms”.

> A morphism of finite projective representations with varying coefficient ring.

```lean
public structure Hom
    {Λ : Type u} {k : Type w} {Γ : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ] (X Y : FiniteProjectiveRepresentation.{u, v, w, m} Λ k Γ)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/Representations.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/Representations.lean#L101). The attribute's comment: “representation\_category”.

> The category structure on finite projective representations with varying coefficient
> algebra.

```lean
public instance instCategory
    {Λ : Type u} {k : Type w} {Γ : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ] : Category (FiniteProjectiveRepresentation.{u, v, w, m} Λ k Γ)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.specialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/Representations.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/Representations.lean#L159). The attribute's comment: “representation\_deformation\_category”.

> The representation `(V, ρ₀)` over `k`, viewed as the special-fibre object.

```lean
public noncomputable def specialFiber
    {Λ : Type u} {k : Type w} {Γ : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ] (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) : FiniteProjectiveRepresentation.{u, w, w, m} Λ k Γ
```

**`Deformation.Examples.FiniteProjectiveRepresentation.deformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/Representations.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/Representations.lean#L169). The attribute's comment: “representation\_deformation\_category”.

> The category of deformations of a finite-dimensional representation of `Γ`.

```lean
public abbrev deformationCategory
    {Λ : Type u} {k : Type w} {Γ : Type*} [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ] (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.projection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/RepresentationsCofibered.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/RepresentationsCofibered.lean#L159). The attribute's comment: “the projection”.

> Forget the module and action of a finite projective representation, retaining its
> coefficient algebra.

```lean
public def projection :
    FiniteProjectiveRepresentation.{u, v, w, m} Λ k Γ ⥤
      ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.Examples.FiniteProjectiveRepresentation.projection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/RepresentationsCofibered.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/RepresentationsCofibered.lean#L170). The attribute's comment: “cofibered in groupoids”.

> The category of finite projective representations is cofibered in groupoids over the
> category of Artinian local coefficient algebras.

```lean
public theorem projection_isCofiberedInGroupoids :
    IsCofiberedInGroupoids
      (projection (Λ := Λ) (k := k) (Γ := Γ) :
        FiniteProjectiveRepresentation.{u, v, w, max v m} Λ k Γ ⥤
          ArtinianLocalAlgCat.{u, v, w} Λ k)
```

**`Deformation.RepresentationCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L58). The attribute's comment: “second presentation: representation\_category, objects”.

> A finite projective representation of `Γ` over an Artinian local `Λ`-algebra with
> residue field `k`.

```lean
structure RepresentationCategory.{u', v', w', m', x'}
    (Λ : Type u') (k : Type w') (Γ : Type x') [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ]
```

**`Deformation.RepresentationCategory.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L78). The attribute's comment: “second presentation: representation\_category, morphisms”.

> A morphism of finite projective representations with varying coefficient ring.

```lean
structure Hom {Λ : Type u} {k : Type w} {Γ : Type x} [CommRing Λ] [Field k] [Algebra Λ k]
    [Group Γ] (X Y : RepresentationCategory.{u, v, w, m, x} Λ k Γ)
```

**`Deformation.RepresentationCategory.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L127). The attribute's comment: “second presentation: representation\_category”.

> The category structure on finite projective representations with varying coefficient
> algebra.

```lean
instance instCategory {Λ : Type u} {k : Type w} {Γ : Type x} [CommRing Λ] [Field k]
    [Algebra Λ k] [Group Γ] : Category (RepresentationCategory.{u, v, w, m, x} Λ k Γ)
```

**`Deformation.representationProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L187). The attribute's comment: “second presentation: representation\_category”.

> The coefficient algebra underlying a finite projective representation, as a
> functor.

```lean
def representationProjection {Λ : Type u} {k : Type w} {Γ : Type x} [CommRing Λ]
    [Field k] [Algebra Λ k] [Group Γ] :
    RepresentationCategory.{u, v, w, m, x} Λ k Γ ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.RepresentationCategory.specialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L214). The attribute's comment: “second presentation: representation\_deformation\_category”.

> The representation `(V, ρ₀)` over the residue field `k`, viewed as the special-fibre
> object of the category `ℱ`.

```lean
noncomputable def specialFiber {Λ : Type u} {k : Type w} {Γ : Type x} [CommRing Λ]
    [Field k] [Algebra Λ k] [Group Γ] (V : Type m) [AddCommGroup V] [Module k V]
    [Module.Finite k V] (ρ₀ : Representation k Γ V) :
    RepresentationCategory.{u, w, w, m, x} Λ k Γ
```

**`Deformation.RepresentationCategory.deformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L224). The attribute's comment: “second presentation: representation\_deformation\_category”.

> The category of deformations of a finite-dimensional representation of `Γ`.

```lean
abbrev deformationCategory {Λ : Type u} {k : Type w} {Γ : Type x} [CommRing Λ] [Field k]
    [Algebra Λ k] [Group Γ] (V : Type m) [AddCommGroup V] [Module k V]
    [Module.Finite k V] (ρ₀ : Representation k Γ V)
```

**`Deformation.deformationCategoryProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Basic.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Basic.lean#L234). The attribute's comment: “second presentation: representation\_deformation\_category”.

> The coefficient algebra of a deformation of `ρ₀`, as a functor from the deformation
> category of `ρ₀` to `𝒞_Λ`.

```lean
noncomputable def deformationCategoryProjection {Λ : Type u} {k : Type w} {Γ : Type x}
    [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ] (V : Type m) [AddCommGroup V]
    [Module k V] [Module.Finite k V] (ρ₀ : Representation k Γ V) :
    RepresentationCategory.deformationCategory (Λ := Λ) V ρ₀ ⥤
      ArtinianLocalAlgCat.{u, w, w} Λ k
```

**`Deformation.RepresentationCategory.representationProjection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Cofibered.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Cofibered.lean#L260). The attribute's comment: “second presentation: representation\_category”.

> The category of finite projective representations is cofibered in groupoids over the
> category of Artinian local coefficient algebras.

```lean
theorem representationProjection_isCofiberedInGroupoids :
    IsCofiberedInGroupoids
      (representationProjection.{u, v, w, m, x} (Λ := Λ) (k := k) (Γ := Γ))
```

## Tag 0DVS, a lemma

[Tag 0DVS](https://stacks.math.columbia.edu/tag/0DVS) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveRepresentation.satisfiesRS_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/RepresentationsRimSchlessinger.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/RepresentationsRimSchlessinger.lean#L546). The attribute's comment: “Rim-Schlessinger condition”.

> Finite projective representations satisfy the Rim–Schlessinger condition.

```lean
public theorem satisfiesRS_projection
    {Λ : Type u} {k : Type w} {Γ : Type*}
    [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ] :
    SatisfiesRS
      (FiniteProjectiveRepresentation.projection.{u, v, w, max v m}
        (Λ := Λ) (k := k) (Γ := Γ))
```

**`Deformation.Examples.FiniteProjectiveRepresentation.isDeformationCategory_deformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/RepresentationsRimSchlessinger.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/RepresentationsRimSchlessinger.lean#L581). The attribute's comment: “deformation category”.

> The deformations of a finite-dimensional representation form a deformation category.

```lean
public theorem isDeformationCategory_deformationCategory
    {Λ : Type u} {k : Type w} {Γ : Type*}
    [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ]
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) :
    IsDeformationCategory
      (objectsOverFunctor
        (FiniteProjectiveRepresentation.projection.{u, w, w, m}
          (Λ := Λ) (k := k) (Γ := Γ))
        (FiniteProjectiveRepresentation.specialFiber (Λ := Λ) V ρ₀))
```

## Tag 0DVT, a lemma

[Tag 0DVT](https://stacks.math.columbia.edu/tag/0DVT) in the Stacks Project.

**`Deformation.finiteDimensional_tangentSpace_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Hull.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Hull.lean#L98). The attribute's comment: “clause 5: `T Def_{V,ρ₀}` is finite dimensional over `k` when `Γ` is finitely generated, for the canonical vector space structure of Stacks 06IH. The hypothesis `Group.FG Γ` is what separates this from clause 4, which holds for every `Γ`”.

> The tangent space of the deformation category of a finite-dimensional representation of a
> finitely generated group is finite dimensional over `k`, for the canonical vector space structure
> of Stacks 06IH.

```lean
theorem finiteDimensional_tangentSpace_representation (V : Type m) [AddCommGroup V] [Module k V]
    [Module.Finite k V] [Group.FG Γ] (ρ₀ : Representation k Γ V) :
    let 𝓕 := BasedCategory.ofFunctor (deformationCategoryProjection (Λ := Λ) V ρ₀)
    let ee := tangentSpaceEquivSelfExt (Λ := Λ) V ρ₀
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨ee.1⟩
    letI : Fact (SchlessingerConditionS2
      (CategoryOfElements.π (isomorphismClasses 𝓕 ee.1.cofibered))) := ⟨ee.2.1⟩
    FiniteDimensional k (artinianTangentSpace Λ k (isomorphismClasses 𝓕 ee.1.cofibered))
```

**`Deformation.infinitesimalAutomorphismsEquivH0`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/InfinitesimalAutomorphisms.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/InfinitesimalAutomorphisms.lean#L589). The attribute's comment: “clause 3: `Inf Def_{V,ρ₀} = H⁰(Γ, End_k(V))`, the infinitesimal automorphisms of the deformation category of a finite-dimensional representation `ρ₀` are the `Γ`-invariant `k`-endomorphisms of `V`, i.e. the `ψ` with `id + εψ` an automorphism of `V ⊗_k k[ε]`”.

> The infinitesimal automorphisms of the deformation category of a finite-dimensional
> representation `ρ₀` are the degree-zero group cohomology of the conjugation action on its
> endomorphisms.

```lean
noncomputable def infinitesimalAutomorphismsEquivH0
    (V : Type w) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V)
    {A₀ Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x₀ : (deformationCategoryProjection (Λ := Λ) V ρ₀).Fiber A₀}
    {xε : (deformationCategoryProjection (Λ := Λ) V ρ₀).Fiber Aε}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (deformationCategoryProjection (Λ := Λ) V ρ₀).IsHomLift g i) :
    ↥(infinitesimalAutomorphisms
        (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
        g e hpair i hi) ≃*
      Multiplicative (groupCohomology (Rep.of (Representation.linHom ρ₀ ρ₀)) 0)
```

**`Deformation.exists_infinitesimalAutomorphismsLinearEquivH0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/InfinitesimalAutomorphisms.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/InfinitesimalAutomorphisms.lean#L659). The attribute's comment: “clause 4: `Inf Def_{V,ρ₀}` is ALWAYS finite dimensional over `k`, with no hypothesis whatsoever on `Γ`. Stated of `Inf Def_{V,ρ₀}` itself, which is a subgroup of an automorphism group and so is given here the `k`-vector space structure the claim needs: addition is composition of automorphisms and the clause-3 identification with `H⁰(Γ, End_k(V))` is `k`-linear. Contrast clause 5, where `Γ` must be finitely generated”.

> **Stacks 0DVT**, the finiteness clause for infinitesimal automorphisms, stated of
> `Inf Def_{V,ρ₀}` itself: the group of infinitesimal automorphisms of the deformation category
> of a finite-dimensional representation carries a `k`-vector space structure whose addition is
> composition of automorphisms, for which the identification of clause 3 with `H⁰(Γ, End_k(V))`
> is `k`-linear, and it is *always* finite dimensional over `k` — no hypothesis whatsoever on
> the group `Γ`.
>
> `Inf Def_{V,ρ₀}` is presented as a subgroup of the automorphism group of a dual-number
> pushforward (`Deformation.infinitesimalAutomorphisms`), so it carries no `k`-module structure
> to begin with and `FiniteDimensional k` does not even typecheck on it. The structure is
> therefore produced here, exactly as in `Stacks 0DVQ`'s version of the same statement for
> finite projective modules
> (`Deformation.Examples.FiniteProjectiveModule.exists_infinitesimalAutomorphismsLinearEquivEnd`),
> and it is pinned: addition is composition, which fixes the additive group, and the `k`-linear
> equivalence is required to be the group isomorphism
> `Deformation.infinitesimalAutomorphismsEquivH0` of clause 3, which fixes the scalar action.
> Compare Stacks 06JV (1), which puts the same structure on the tangent space at the identity of
> the automorphism functor of a category cofibered in groupoids satisfying (RS).
>
> Finite dimensionality is then `Deformation.finiteDimensional_groupCohomology_zero_linHom`
> transported along that equivalence. This is in contrast with the tangent space, whose
> finiteness needs `Γ` to be finitely generated
> (`Deformation.finiteDimensional_tangentSpace_representation`).

```lean
theorem exists_infinitesimalAutomorphismsLinearEquivH0
    (V : Type w) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V)
    {A₀ Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x₀ : (deformationCategoryProjection (Λ := Λ) V ρ₀).Fiber A₀}
    {xε : (deformationCategoryProjection (Λ := Λ) V ρ₀).Fiber Aε}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (deformationCategoryProjection (Λ := Λ) V ρ₀).IsHomLift g i) :
    ∃ A : AddCommGroup ↥(infinitesimalAutomorphisms
        (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
        g e hpair i hi),
      letI := A
      ∃ _ : Module k ↥(infinitesimalAutomorphisms
          (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
          g e hpair i hi),
        (∀ a b : ↥(infinitesimalAutomorphisms
            (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
            g e hpair i hi), a + b = a * b) ∧
        (∃ L : ↥(infinitesimalAutomorphisms
              (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
              g e hpair i hi) ≃ₗ[k]
            groupCohomology (Rep.of (Representation.linHom ρ₀ ρ₀)) 0,
          ∀ a, Multiplicative.ofAdd (L a) =
            infinitesimalAutomorphismsEquivH0 (Λ := Λ) V ρ₀ g e hpair i hi a) ∧
        FiniteDimensional k ↥(infinitesimalAutomorphisms
          (deformationCategoryProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀)
          g e hpair i hi)
```

**`Deformation.selfExtEquivGroupCohomologyOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/SelfExtGroupCohomology.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/SelfExtGroupCohomology.lean#L74). The attribute's comment: “clause 2: `Ext¹_{k[Γ]}(V, V) = H¹(Γ, End_k(V))` for the conjugation action of `Γ` on `End_k(V)`, over the `k[Γ]`-module attached to `ρ₀` by `Rep.equivalenceModuleMonoidAlgebra`, which is the module clause 1 states its `Ext¹` over. No hypothesis on `Γ`”.

> **Stacks 0DVT.** The first self-extension group over the group algebra of a
> finite-dimensional representation `ρ₀` of `Γ` on `V` is the first group cohomology of the
> conjugation action of `Γ` on `End_k(V)`:
>
> `Ext¹_{k[Γ]}(V, V) = H¹(Γ, End_k(V))`.
>
> The extension group is taken over the `k[Γ]`-module attached to `ρ₀`, which is the module over
> which the tangent-space clause `Deformation.tangentSpaceEquivSelfExt` of the same tag is
> stated. No hypothesis on `Γ` is needed.

```lean
def selfExtEquivGroupCohomologyOne (V : Type w) [AddCommGroup V] [Module k V]
    [Module.Finite k V] (ρ₀ : Representation k Γ V) :
    Abelian.Ext
        ((Rep.equivalenceModuleMonoidAlgebra (k := k) (G := Γ)).functor.obj (Rep.of ρ₀))
        ((Rep.equivalenceModuleMonoidAlgebra (k := k) (G := Γ)).functor.obj (Rep.of ρ₀)) 1 ≃ₗ[k]
      (groupCohomology (Rep.of (Representation.linHom ρ₀ ρ₀)) 1 : Type w)
```

**`Deformation.tangentSpaceEquivSelfExt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/TangentSelfExt/Linearity.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/TangentSelfExt/Linearity.lean#L514). The attribute's comment: “clause 1: `T Def_{V,ρ₀} = Ext¹_{k[Γ]}(V, V)`, the tangent space of the deformation category of a finite-dimensional representation `ρ₀` is its first self-extension group over the group algebra. The identification of that `Ext¹` with `H¹(Γ, End_k(V))` is clause 2, `Deformation.selfExtEquivGroupCohomologyOne`”.

> The canonical tangent space of a finite-dimensional representation deformation category
> is linearly equivalent to its first self-Ext over the group algebra.

```lean
public noncomputable def tangentSpaceEquivSelfExt
    {Λ : Type u} {k : Type w} {Γ : Type*}
    [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ]
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) :
    let p := deformationCategoryProjection (Λ := Λ) V ρ₀
    let 𝓕 := BasedCategory.ofFunctor p
    let M₀ := (Rep.equivalenceModuleMonoidAlgebra (k := k) (G := Γ)).functor.obj
      (Rep.of ρ₀)
    let E := Abelian.Ext M₀ M₀ 1
    Σ' (hpre : Deformation.IsPredeformationCategory 𝓕.p)
      (hS2 : Deformation.SchlessingerConditionS2
        (CategoryOfElements.π
          (Deformation.isomorphismClasses 𝓕 hpre.cofibered))),
      letI : Fact (Deformation.IsPredeformationCategory 𝓕.p) := ⟨hpre⟩
      letI : Fact (Deformation.SchlessingerConditionS2
        (CategoryOfElements.π
          (Deformation.isomorphismClasses 𝓕 hpre.cofibered))) := ⟨hS2⟩
      letI : AddCommGroup
        (Deformation.artinianTangentSpace Λ k
          (Deformation.isomorphismClasses 𝓕 hpre.cofibered)) :=
        Deformation.associatedTangentSpaceAddCommGroupUnlifted 𝓕
      letI : Module k
        (Deformation.artinianTangentSpace Λ k
          (Deformation.isomorphismClasses 𝓕 hpre.cofibered)) :=
        Deformation.associatedTangentSpaceModuleUnlifted 𝓕
      { L : Deformation.artinianTangentSpace Λ k
          (Deformation.isomorphismClasses 𝓕 hpre.cofibered) ≃ₗ[k] E //
        (∀ x : p.Fiber (Deformation.augmentedDualNumbers (Λ := Λ) (k := k)),
          ∃ (M : ModuleCat (MonoidAlgebra k Γ)) (f : M₀ ⟶ M) (g : M ⟶ M₀)
            (hfg : f ≫ g = 0),
            (ShortComplex.mk f g hfg).ShortExact ∧
              IsAssociatedSelfExtension V ρ₀ x M f g) ∧
        (∀ (x : p.Fiber (Deformation.augmentedDualNumbers (Λ := Λ) (k := k)))
          (M : ModuleCat (MonoidAlgebra k Γ)) (f : M₀ ⟶ M) (g : M ⟶ M₀)
          (hfg : f ≫ g = 0) (hexact : (ShortComplex.mk f g hfg).ShortExact),
          IsAssociatedSelfExtension V ρ₀ x M f g →
            L (Deformation.classOf 𝓕 hpre.cofibered x) = hexact.extClass) }
```

## Tag 0ET1, a lemma

[Tag 0ET1](https://stacks.math.columbia.edu/tag/0ET1) in the Stacks Project.

**`Deformation.exists_hull_isomorphismClasses_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Hull.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Hull.lean#L121). The attribute's comment: “representation\_hull”.

> The functor of isomorphism classes of deformations of a finite-dimensional representation of
> a finitely generated group over a classical base has a hull: a versal formal object with
> bijective differential.

```lean
theorem exists_hull_isomorphismClasses_representation (V : Type m) [AddCommGroup V] [Module k V]
    [Module.Finite k V] [Group.FG Γ] (ρ₀ : Representation k Γ V) (hΛ : IsClassical Λ k) :
    let 𝓕 := BasedCategory.ofFunctor (deformationCategoryProjection (Λ := Λ) V ρ₀)
    let hpre := (tangentSpaceEquivSelfExt (Λ := Λ) V ρ₀).1
    let F := isomorphismClasses 𝓕 hpre.cofibered
    ∃ ξ : FormalObject (CategoryOfElements.π F),
      IsVersal (categoryOfElements_projection_isCofibered F) ξ ∧
        HasBijectiveDifferential (categoryOfElements_projection_isCofibered F) ξ
```

**`Deformation.isProrepresentableULift_isomorphismClasses_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Representation/Prorepresentable.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Representation/Prorepresentable.lean#L323). The attribute's comment: “prorepresentability”.

> **Stacks 0ET1**, prorepresentability: the functor of isomorphism classes of deformations of a
> finite-dimensional representation of a finitely generated group over a classical base is
> prorepresentable, as soon as the `Γ`-equivariant endomorphisms of the representation are exactly
> the scalars, that is `H⁰(Γ, End_k(V)) = k`.
>
> Prorepresentability is stated in the universe-raised form `Deformation.IsProrepresentableULift`,
> because the values of the functor of isomorphism classes lie in the universe of the objects of
> the deformation category rather than in the morphism universe of `𝒞_Λ`. The functor is the one
> whose hull is `Deformation.exists_hull_isomorphismClasses_representation`, the other clause of
> this tag.

```lean
public theorem isProrepresentableULift_isomorphismClasses_representation
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V] [Group.FG Γ]
    (ρ₀ : Representation k Γ V) (hΛ : IsClassical Λ k)
    (h : ∀ f : IntertwiningMap ρ₀ ρ₀,
      ∃! a : k, (a • LinearMap.id : Module.End k V) = f.toLinearMap) :
    IsProrepresentableULift (isomorphismClasses
      (BasedCategory.ofFunctor (deformationCategoryProjection (Λ := Λ) V ρ₀))
      (isDeformationCategory_deformationCategoryProjection
        (Λ := Λ) V ρ₀).predeformation.cofibered)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.5, Tag 0DVR](https://stacks.math.columbia.edu/tag/0DVR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
