---
declaration: section
origin: cited
lean: Deformation.Examples.continuous_representation_iff_continuousSMul, Deformation.Examples.FiniteProjectiveRepresentation.continuousObjects, Deformation.Examples.FiniteProjectiveRepresentation.continuousProjection, Deformation.Examples.FiniteProjectiveRepresentation.continuousProjection_isCofiberedInGroupoids, Deformation.Examples.FiniteProjectiveRepresentation.continuousSpecialFiber, Deformation.Examples.FiniteProjectiveRepresentation.continuousDeformationCategory, Deformation.Examples.FiniteProjectiveRepresentation.isCofiberedInGroupoids_continuousProjection, Deformation.Examples.isContinuousRepresentation_iff_isContinuous
statement: formalized
proof: formalized
---

# 93.6 Continuous representations

Section 93.6 of the Stacks Project, [Tag 0DVU](https://stacks.math.columbia.edu/tag/0DVU). 4 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D3K, an example

[Tag 0D3K](https://stacks.math.columbia.edu/tag/0D3K) in the Stacks Project.

**`Deformation.Examples.continuous_representation_iff_continuousSMul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentations.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentations.lean#L45). The attribute's comment: “continuity\_equivalence”.

> For a finitely generated module over a semiring, a representation is continuous into the
> discrete general linear group if and only if the induced action on the discrete module is
> continuous.

```lean
public theorem continuous_representation_iff_continuousSMul
    (R M : Type*) [Semiring R] [AddCommMonoid M] [Module R M] [Module.Finite R M]
    (Γ : Type*) [Group Γ] [TopologicalSpace Γ] [IsTopologicalGroup Γ]
    (ρ : Γ →* LinearMap.GeneralLinearGroup R M) :
    letI : TopologicalSpace (LinearMap.GeneralLinearGroup R M) := ⊥
    letI : TopologicalSpace M := ⊥
    letI : MulAction Γ M := MulAction.compHom M ρ
    Continuous ρ ↔ ContinuousSMul Γ M
```

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousObjects`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean#L114). The attribute's comment: “continuous\_representation\_category”.

> The objects of the category of finite projective representations of Stacks 0D3J whose
> representation is continuous. The category `ℱ` of Stacks 0D3K is the full subcategory they
> span.

```lean
public def continuousObjects (Λ : Type u) (k : Type w) (Γ : Type*) [CommRing Λ] [Field k]
    [Algebra Λ k] [Group Γ] [TopologicalSpace Γ] :
    ObjectProperty (FiniteProjectiveRepresentation.{u, v, w, m} Λ k Γ)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousProjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean#L152). The attribute's comment: “continuous\_representation\_category”.

> The functor remembering only the coefficient algebra of a continuous finite projective
> representation.

```lean
public def continuousProjection :
    (continuousObjects.{u, v, w, m} Λ k Γ).FullSubcategory ⥤
      ArtinianLocalAlgCat.{u, v, w} Λ k
```

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousProjection_isCofiberedInGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean#L175). The attribute's comment: “continuous\_representation\_category”.

> The category of continuous finite projective representations is cofibered in groupoids
> over the category of Artinian local coefficient algebras: the pushforward of a continuous
> representation is continuous, and fill-ins are those of the ambient category.

```lean
public theorem continuousProjection_isCofiberedInGroupoids
    (hp : IsCofiberedInGroupoids
      (projection (Λ := Λ) (k := k) (Γ := Γ) :
        FiniteProjectiveRepresentation.{u, v, w, m} Λ k Γ ⥤
          ArtinianLocalAlgCat.{u, v, w} Λ k)) :
    IsCofiberedInGroupoids (continuousProjection.{u, v, w, m} (Λ := Λ) (k := k) (Γ := Γ))
```

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousSpecialFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean#L186). The attribute's comment: “continuous\_representation\_deformation\_category”.

> The continuous representation `(V, ρ₀)` over the residue field `k`, viewed as the
> special-fibre object `(k, V, ρ₀)` of the category of continuous representations.

```lean
public noncomputable def continuousSpecialFiber (V : Type m) [AddCommGroup V] [Module k V]
    [Module.Finite k V] (ρ₀ : Representation k Γ V)
    (hρ₀ : IsContinuousRepresentation ρ₀) :
    (continuousObjects.{u, w, w, m} Λ k Γ).FullSubcategory
```

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousDeformationCategory`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofibered.lean#L195). The attribute's comment: “continuous\_representation\_deformation\_category”.

> The category of deformations of a finite-dimensional continuous representation of `Γ`.

```lean
public abbrev continuousDeformationCategory (V : Type m) [AddCommGroup V]
    [Module k V] [Module.Finite k V] (ρ₀ : Representation k Γ V)
    (hρ₀ : IsContinuousRepresentation ρ₀)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.isCofiberedInGroupoids_continuousProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofiberedUnconditional.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsCofiberedUnconditional.lean#L115). The attribute's comment: “continuous\_representation\_category: p is cofibred in groupoids”.

> The functor `p : ℱ → 𝒞_Λ` sending a continuous finite projective representation `(A, M, ρ)`
> of the topological group `Γ` to its coefficient algebra `A` is cofibered in groupoids, for an
> arbitrary module universe and with no hypothesis on the ambient projection of finite projective
> representations.

```lean
public theorem isCofiberedInGroupoids_continuousProjection :
    IsCofiberedInGroupoids (continuousProjection.{u, v, w, m} (Λ := Λ) (k := k) (Γ := Γ))
```

**`Deformation.Examples.isContinuousRepresentation_iff_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsGModule.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsGModule.lean#L59). The attribute's comment: “continuity\_equivalence”.

> **The footnote of Stacks 0D3K.** For a finite module over a commutative ring, a
> representation of a topological group is continuous into the general linear group with the
> discrete topology exactly when the module, with the action given by the representation, is an
> `A`-`Γ`-module in the sense of Stacks 04JP.

```lean
public theorem isContinuousRepresentation_iff_isContinuous
    {R : Type u} [CommRing R] {Γ : Type v} [Group Γ] [TopologicalSpace Γ]
    [IsTopologicalGroup Γ] {M : Type w} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (ρ : Representation R Γ M) :
    IsContinuousRepresentation ρ ↔
      (Stacks.GroupCohomology.actionOfRepresentation R Γ M ρ).IsContinuous
```

## Tag 0DVV, a lemma

[Tag 0DVV](https://stacks.math.columbia.edu/tag/0DVV) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveRepresentation.satisfiesRS_continuousProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsRimSchlessinger.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsRimSchlessinger.lean#L167). The attribute's comment: “Rim-Schlessinger condition”.

> Continuous finite projective representations of a topological group satisfy the
> Rim–Schlessinger condition.

```lean
public theorem satisfiesRS_continuousProjection {Λ : Type u} {k : Type w} {Γ : Type*}
    [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ] [TopologicalSpace Γ] :
    SatisfiesRS
      (continuousProjection.{u, v, w, max v m} (Λ := Λ) (k := k) (Γ := Γ))
```

**`Deformation.Examples.FiniteProjectiveRepresentation.isDeformationCategory_continuousDeformationCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsRimSchlessinger.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsRimSchlessinger.lean#L187). The attribute's comment: “deformation category”.

> The deformations of a finite-dimensional continuous representation of a topological group
> form a deformation category.

```lean
public theorem isDeformationCategory_continuousDeformationCategory {Λ : Type u} {k : Type w}
    {Γ : Type*} [CommRing Λ] [Field k] [Algebra Λ k] [Group Γ] [TopologicalSpace Γ]
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀) :
    IsDeformationCategory
      (objectsOverFunctor
        (continuousProjection.{u, w, w, m} (Λ := Λ) (k := k) (Γ := Γ))
        (continuousSpecialFiber (Λ := Λ) V ρ₀ hρ₀))
```

## Tag 0DVW, a lemma

[Tag 0DVW](https://stacks.math.columbia.edu/tag/0DVW) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveRepresentation.continuousInfinitesimalAutomorphismsEquivH0`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean#L304). The attribute's comment: “Inf”.

> The infinitesimal automorphisms of the deformation category of a finite-dimensional
> continuous representation `ρ₀` of a topological group are the degree-zero cohomology of the
> conjugation action on its endomorphisms, `H⁰(Γ, End_k(V))`.

```lean
public noncomputable def continuousInfinitesimalAutomorphismsEquivH0
    (V : Type w) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀)
    {A₀ Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x₀ : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).Fiber A₀}
    {xε : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).Fiber Aε}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).IsHomLift g i) :
    ↥(infinitesimalAutomorphisms
        (continuousDeformationProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀ hρ₀)
        g e hpair i hi) ≃*
      Multiplicative (groupCohomology (Rep.of (Representation.linHom ρ₀ ρ₀)) 0)
```

**`Deformation.Examples.FiniteProjectiveRepresentation.finiteDimensional_continuousInfinitesimalAutomorphisms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean#L341). The attribute's comment: “Inf is always finite dimensional”.

> **Stacks 0DVW**, the clause that the infinitesimal automorphisms are *always* finite
> dimensional: the infinitesimal automorphism group of the deformation category of a
> finite-dimensional continuous representation `ρ₀` carries a `k`-vector space structure whose
> addition is composition of automorphisms, and that vector space is finite dimensional.
>
> No hypothesis on `Γ` is needed. The group is `H⁰(Γ, End_k(V))` by
> `continuousInfinitesimalAutomorphismsEquivH0`, and degree-zero cohomology is the subspace of
> `Γ`-invariants of `End_k(V)`, which is finite dimensional because `V` is.

```lean
public theorem finiteDimensional_continuousInfinitesimalAutomorphisms
    (V : Type w) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀)
    {A₀ Aε : ArtinianLocalAlgCat.{u, w, w} Λ k}
    {x₀ : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).Fiber A₀}
    {xε : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).Fiber Aε}
    (g : A₀ ⟶ Aε) (e : Aε ⟶ A₀) (hpair : IsCanonicalDualNumberPair g e)
    (i : x₀.1 ⟶ xε.1)
    (hi : (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀).IsHomLift g i) :
    let G := ↥(infinitesimalAutomorphisms
      (continuousDeformationProjection_isCofiberedInGroupoids (Λ := Λ) V ρ₀ hρ₀)
      g e hpair i hi)
    ∃ hA : AddCommGroup G,
      letI := hA
      ∃ hM : Module k G,
        letI := hM
        (∀ a b : G, a + b = a * b) ∧ FiniteDimensional k G
```

**`Deformation.Examples.FiniteProjectiveRepresentation.finiteDimensional_continuousTangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsInfinitesimalAutomorphisms.lean#L405). The attribute's comment: “the tangent space is finite dimensional”.

> **Stacks 0DVW**, the tangent clause: for a topologically finitely generated topological
> group `Γ` the tangent space of the deformation category of a finite-dimensional continuous
> representation `ρ₀` is finite dimensional over `k`.
>
> Topological finite generation enters through a dense finitely generated subgroup `H ≤ Γ`.
> A continuous deformation is locally constant, so an `H`-equivariant map between two of them is
> `Γ`-equivariant: the agreement locus is closed and contains `H`. Hence restriction of the
> action to `H` is fully faithful, so its differential is an injective `k`-linear map from the
> tangent space into the tangent space of the deformation category of `ρ₀|_H`, and the latter is
> finite dimensional by Stacks 0DVT.

```lean
public theorem finiteDimensional_continuousTangentSpace
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀)
    (hΓ : ∃ H : Subgroup Γ, Group.FG ↥H ∧ Dense (H : Set Γ)) :
    let 𝓕 := BasedCategory.ofFunctor (Deformation.objectsOverFunctor
      (continuousProjection.{u, w, w, m} (Λ := Λ) (k := k) (Γ := Γ))
      (continuousSpecialFiber (Λ := Λ) V ρ₀ hρ₀))
    let hD := isDeformationCategory_continuousDeformationCategory (Λ := Λ) V ρ₀ hρ₀
    letI : Fact (Deformation.IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (Deformation.SchlessingerConditionS2 (CategoryOfElements.π
        (Deformation.isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
      ⟨Deformation.Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
        𝓕 hD⟩
    FiniteDimensional k (Deformation.artinianTangentSpace Λ k
      (Deformation.isomorphismClasses 𝓕 hD.predeformation.cofibered))
```

**`Deformation.Examples.FiniteProjectiveRepresentation.tangentSpaceEquivContinuousCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsTangentSpace.lean, line 814](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsTangentSpace.lean#L814). The attribute's comment: “tangent\_space”.

> **Stacks 0DVW, the tangent clause.** For a finite-dimensional continuous representation
> `ρ₀ : Γ → GL_k(V)` of a topological group, the tangent space of the deformation category of
> Stacks 0D3K — in its natural `k`-vector space structure of Stacks 06IH — is the first
> continuous cohomology `H¹(Γ, End_k(V))` of the conjugation action on the endomorphisms of `V`.
>
> The coefficient module is the dual tensor module `Vᵛ ⊗_k V` of Stacks 0DVE, and the second
> component of the statement identifies its representation equivariantly with
> `Representation.linHom ρ₀ ρ₀`, the conjugation action on `End_k(V)`, so the cohomology on the
> right is `H¹(Γ, End_k(V))`.
>
> The proof is the one of Stacks 0DVT: `tangentSpaceEquivContinuousSelfExt` identifies the
> tangent space with `Ext¹` of `V` by itself in continuous discrete modules, and Stacks 0DVE turns
> that `Ext¹` into continuous cohomology of `Vᵛ ⊗_k V`.

```lean
def tangentSpaceEquivContinuousCohomology [IsTopologicalGroup Γ]
    [HasDerivedCategory.{d} (Stacks.Injectives.ContinuousModule.{w, w, w} k Γ)]
    [HasDerivedCategory.{d} (ModuleCat.{w} k)]
    (V : Type w) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀) :
    let 𝓕 := BasedCategory.ofFunctor (continuousDeformationProjection (Λ := Λ) V ρ₀ hρ₀)
    let hD := isDeformationCategory_continuousDeformationCategory (Λ := Λ) V ρ₀ hρ₀
    letI : Fact (IsPredeformationCategory 𝓕.p) := ⟨hD.predeformation⟩
    letI : Fact (SchlessingerConditionS2
        (CategoryOfElements.π
          (isomorphismClasses 𝓕 hD.predeformation.cofibered))) :=
      ⟨Deformation.Artin.schlessingerConditionS2_isomorphismClasses_of_isDeformationCategory
        𝓕 hD⟩
    letI := Stacks.ContinuousCohomology.hasExt_continuousModule.{w, w, w} k Γ
    let M := continuousModuleOfContinuousRepresentation V ρ₀ hρ₀
    letI : Module.Finite k (M.obj.obj.V : Type w) := inferInstanceAs (Module.Finite k V)
    letI : Module.Projective k (M.obj.obj.V : Type w) :=
      inferInstanceAs (Module.Projective k V)
    Σ' _ : artinianTangentSpace Λ k
          (isomorphismClasses 𝓕 hD.predeformation.cofibered) ≃ₗ[k]
        (Stacks.ContinuousCohomology.cohomologyFunctor.{d, w, w, w} k Γ 1).obj
          (Stacks.ContinuousCohomology.dualTensorContinuousModule k Γ M M),
      (Stacks.ContinuousCohomology.rep k Γ
        (Stacks.ContinuousCohomology.dualTensorContinuousModule k Γ M M)).Equiv
          (Representation.linHom ρ₀ ρ₀)
```

## Tag 0ET2, a lemma

[Tag 0ET2](https://stacks.math.columbia.edu/tag/0ET2) in the Stacks Project.

**`Deformation.Examples.FiniteProjectiveRepresentation.exists_hull_continuousIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsHull.lean, line 529](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsHull.lean#L529). The attribute's comment: “the functor has a hull”.

> **Stacks 0ET2**, the hull: the functor of isomorphism classes of deformations of a
> finite-dimensional continuous representation of a topologically finitely generated group over a
> classical base has a hull, that is a versal formal object with bijective differential.
>
> Both hypotheses of Stacks 06IZ beyond the Rim–Schlessinger property are discharged: condition
> (S1) and (S2) come from the deformation-category property of the continuous deformations of
> `ρ₀`, and the finite-dimensionality of the tangent space is the tangent clause of Stacks
> 0DVW.

```lean
public theorem exists_hull_continuousIsomorphismClasses
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀)
    (hΛ : IsClassical Λ k)
    (hΓ : ∃ H : Subgroup Γ, Group.FG ↥H ∧ Dense (H : Set Γ)) :
    let 𝓕 := BasedCategory.ofFunctor (objectsOverFunctor
      (continuousProjection.{u, w, w, m} (Λ := Λ) (k := k) (Γ := Γ))
      (continuousSpecialFiber (Λ := Λ) V ρ₀ hρ₀))
    let hpre := (isDeformationCategory_continuousDeformationCategory
      (Λ := Λ) V ρ₀ hρ₀).predeformation
    let F := isomorphismClasses 𝓕 hpre.cofibered
    ∃ ξ : FormalObject (CategoryOfElements.π F),
      IsVersal (categoryOfElements_projection_isCofibered F) ξ ∧
        HasBijectiveDifferential (categoryOfElements_projection_isCofibered F) ξ
```

**`Deformation.Examples.FiniteProjectiveRepresentation.isProrepresentableULift_continuousIsomorphismClasses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsHull.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/Examples/Linear/ContinuousRepresentationsHull.lean#L581). The attribute's comment: “prorepresentability”.

> **Stacks 0ET2**, prorepresentability: the functor of isomorphism classes of deformations of
> a finite-dimensional continuous representation of a topologically finitely generated group over
> a classical base is prorepresentable, as soon as the `Γ`-equivariant endomorphisms of the
> representation are exactly the scalars, that is `H⁰(Γ, End_k(V)) = k`.
>
> Prorepresentability is stated in the universe-raised form `Deformation.IsProrepresentableULift`,
> because the values of the functor of isomorphism classes lie in the universe of the objects of
> the deformation category rather than in the morphism universe of `𝒞_Λ`.

```lean
public theorem isProrepresentableULift_continuousIsomorphismClasses
    (V : Type m) [AddCommGroup V] [Module k V] [Module.Finite k V]
    (ρ₀ : Representation k Γ V) (hρ₀ : IsContinuousRepresentation ρ₀)
    (hΛ : IsClassical Λ k)
    (h : ∀ f : IntertwiningMap ρ₀ ρ₀,
      ∃! a : k, (a • LinearMap.id : Module.End k V) = f.toLinearMap)
    (hΓ : ∃ H : Subgroup Γ, Group.FG ↥H ∧ Dense (H : Set Γ)) :
    IsProrepresentableULift (isomorphismClasses
      (BasedCategory.ofFunctor (objectsOverFunctor
        (continuousProjection.{u, w, w, m} (Λ := Λ) (k := k) (Γ := Γ))
        (continuousSpecialFiber (Λ := Λ) V ρ₀ hρ₀)))
      (isDeformationCategory_continuousDeformationCategory
        (Λ := Λ) V ρ₀ hρ₀).predeformation.cofibered)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 93.6, Tag 0DVU](https://stacks.math.columbia.edu/tag/0DVU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
