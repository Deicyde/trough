---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.AlgebraicStacks.closure_image_chartPointMap_mem_irreducibleComponents, AlgebraicGeometry.Stack.AlgebraicStacks.exists_mem_irreducibleComponents_closure_image_eq, Stacks.Chow.componentMultiplicity_id_eq_of_smooth, AlgebraicGeometry.Stack.componentMultiplicity_eq_of_closure_image_eq, AlgebraicGeometry.Stack.componentMultiplicity, AlgebraicGeometry.Stack.componentMultiplicity_eq
statement: formalized
proof: formalized
---

# 107.3 Multiplicities of components of algebraic stacks

Section 107.3 of the Stacks Project, [Tag 0DR4](https://stacks.math.columbia.edu/tag/0DR4). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DR5, a lemma

[Tag 0DR5](https://stacks.math.columbia.edu/tag/0DR5) in the Stacks Project.

**`AlgebraicGeometry.Stack.AlgebraicStacks.closure_image_chartPointMap_mem_irreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicity.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicity.lean#L229). The attribute's comment: “closure of the image of an irreducible component”.

> For a smooth 1-morphism to a locally Noetherian algebraic stack over `S` from the algebraic
> stack of a scheme `U` of the site, the closure of the image of any irreducible component of `U` is
> an irreducible component of the space of points of Stacks 04XL.

```lean
theorem closure_image_chartPointMap_mem_irreducibleComponents (U : BigFppfOver B S hS)
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳)
    (f : Stack.schemeStack.{u, w} B S hS U ⟶ 𝒳) (hf : IsSmooth B S hS f)
    (T : Set ((BigFppfOver.toScheme B S hS).obj U))
    (hT : T ∈ irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U)) :
    letI := Stack.pointTopology B S hS 𝒳.val
    closure (chartPointMap B S hS U 𝒳 f '' T) ∈ irreducibleComponents (points B S hS 𝒳)
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.exists_mem_irreducibleComponents_closure_image_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicity.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicity.lean#L249). The attribute's comment: “surjective charts give every irreducible component”.

> For a smooth *surjective* 1-morphism to a locally Noetherian algebraic stack over `S` from the
> algebraic stack of a scheme `U` of the site, every irreducible component of the space of points of
> Stacks 04XL is the closure of the image of an irreducible component of `U`.

```lean
theorem exists_mem_irreducibleComponents_closure_image_eq (U : BigFppfOver B S hS)
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS)
    (hN : Stack.HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳)
    (f : Stack.schemeStack.{u, w} B S hS U ⟶ 𝒳) (hf : IsSmooth B S hS f)
    (hfs : Stack.IsSurjective B S hS f) :
    letI := Stack.pointTopology B S hS 𝒳.val
    ∀ Z ∈ irreducibleComponents (points B S hS 𝒳),
      ∃ T ∈ irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U),
        closure (chartPointMap B S hS U 𝒳 f '' T) = Z
```

## Tag 0DR6, a lemma

[Tag 0DR6](https://stacks.math.columbia.edu/tag/0DR6) in the Stacks Project.

**`Stacks.Chow.componentMultiplicity_id_eq_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/SmoothComponentMultiplicity.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/SmoothComponentMultiplicity.lean#L119).

> **Stacks 0DR6.** Let `f : U ⟶ X` be a smooth morphism of locally Noetherian schemes, let
> `T'` be an irreducible component of `U` and let `T` be the irreducible component of `X` obtained
> as the closure of the image of `T'`. Then `T'` and `T` have the same multiplicity.

```lean
public theorem componentMultiplicity_id_eq_of_smooth
    {X U : Scheme.{u}} (f : U ⟶ X) [Smooth f] [IsLocallyNoetherian X]
    (T' : irreducibleComponents U) (T : irreducibleComponents X)
    (hT : closure (f.base '' (T' : Set U)) = (T : Set X)) :
    Stacks.Chow.componentMultiplicity (𝟙 U) (genericPoints.ofComponent T') =
      Stacks.Chow.componentMultiplicity (𝟙 X) (genericPoints.ofComponent T)
```

## Tag 0DR7, a lemma

[Tag 0DR7](https://stacks.math.columbia.edu/tag/0DR7) in the Stacks Project.

**`AlgebraicGeometry.Stack.componentMultiplicity_eq_of_closure_image_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicityIndependence.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ComponentMultiplicityIndependence.lean#L227).

> **Stacks 0DR7.** Let `f₁ : U₁ → 𝒳` and `f₂ : U₂ → 𝒳` be smooth 1-morphisms to a locally
> Noetherian algebraic stack over `S` from the algebraic stacks of two schemes `U₁`, `U₂` of the
> site, and let `T₁`, `T₂` be irreducible components of `U₁`, `U₂`. If the closures of the images of
> `T₁` and `T₂` in the space of points of Stacks 04XL of `𝒳` are the same irreducible component `T`,
> then `T₁` and `T₂` have the same multiplicity.
>
> Together with Stacks 0DR5 this makes the multiplicity of an irreducible component of `|𝒳|` well
> defined: it may be computed on any smooth scheme chart, by any component lying over it.

```lean
theorem componentMultiplicity_eq_of_closure_image_eq
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hN : HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳)
    (U₁ U₂ : BigFppfOver B S hS)
    (f₁ : schemeStack.{u, w} B S hS U₁ ⟶ 𝒳) (f₂ : schemeStack.{u, w} B S hS U₂ ⟶ 𝒳)
    (hf₁ : AlgebraicStacks.IsSmooth B S hS f₁) (hf₂ : AlgebraicStacks.IsSmooth B S hS f₂)
    (T₁ : irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U₁))
    (T₂ : irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U₂)) :
    letI := pointTopology B S hS (schemeStack.{u, w} B S hS U₁).val
    letI := pointTopology B S hS (schemeStack.{u, w} B S hS U₂).val
    ∀ T ∈ irreducibleComponents (AlgebraicStacks.points B S hS 𝒳),
      closure (AlgebraicStacks.pointsMap B S hS f₁ ''
          ((pointsHomeomorphScheme B S hS U₁).symm '' (T₁ : Set _))) = T →
        closure (AlgebraicStacks.pointsMap B S hS f₂ ''
            ((pointsHomeomorphScheme B S hS U₂).symm '' (T₂ : Set _))) = T →
          _root_.Stacks.Chow.componentMultiplicity
                (𝟙 ((BigFppfOver.toScheme B S hS).obj U₁)) (genericPoints.ofComponent T₁) =
            _root_.Stacks.Chow.componentMultiplicity
                (𝟙 ((BigFppfOver.toScheme B S hS).obj U₂)) (genericPoints.ofComponent T₂)
```

## Tag 0DR8, a definition

[Tag 0DR8](https://stacks.math.columbia.edu/tag/0DR8) in the Stacks Project.

**`AlgebraicGeometry.Stack.componentMultiplicity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StackComponentMultiplicity.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StackComponentMultiplicity.lean#L147).

> **Stacks 0DR8.** The multiplicity `m_{T, 𝒳}` of an irreducible component `T` of the space of
> points of Stacks 04XL of a locally Noetherian algebraic stack `𝒳` over `S`: the multiplicity of
> Stacks 02QU of an irreducible component of a smooth scheme chart of `𝒳` whose image on points has
> closure `T`.

```lean
noncomputable def componentMultiplicity (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hN : HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳)
    (T : Set (AlgebraicStacks.points B S hS 𝒳))
    (hT : T ∈ irreducibleComponents (AlgebraicStacks.points B S hS 𝒳)) : ℤ
```

**`AlgebraicGeometry.Stack.componentMultiplicity_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StackComponentMultiplicity.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StackComponentMultiplicity.lean#L170). The attribute's comment: “the multiplicity is computed by any smooth chart”.

> **Stacks 0DR8.** The multiplicity of an irreducible component `T` of the space of points of a
> locally Noetherian algebraic stack over `S` is computed by *any* smooth 1-morphism `f : U → 𝒳` from
> the algebraic stack of a scheme of the site and any irreducible component `T'` of `U` whose image
> on points has closure `T`: it is the length of the local ring of `U` at the generic point of
> `T'`.

```lean
theorem componentMultiplicity_eq (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hN : HasPropertyOnSomeSchemeAtlas B S hS
      (fun X : Scheme.{u} => IsLocallyNoetherian X) 𝒳)
    (T : Set (AlgebraicStacks.points B S hS 𝒳))
    (hT : T ∈ irreducibleComponents (AlgebraicStacks.points B S hS 𝒳))
    (U : BigFppfOver B S hS) (f : schemeStack.{u, w} B S hS U ⟶ 𝒳)
    (hf : AlgebraicStacks.IsSmooth B S hS f)
    (T' : irreducibleComponents ((BigFppfOver.toScheme B S hS).obj U))
    (hT' : closure (AlgebraicStacks.chartPointMap B S hS U 𝒳 f '' (T' : Set _)) = T) :
    componentMultiplicity.{u, w} B S hS 𝒳 hN T hT =
      _root_.Stacks.Chow.componentMultiplicity
        (𝟙 ((BigFppfOver.toScheme B S hS).obj U)) (genericPoints.ofComponent T')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 107.3, Tag 0DR4](https://stacks.math.columbia.edu/tag/0DR4)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
