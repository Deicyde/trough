---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.representableBy_isContinuous_and_isCocontinuous, AlgebraicGeometry.Stack.structureSheaf_representableBy, AlgebraicGeometry.Stack.structureSheafRepresentableByIso, AlgebraicGeometry.Stack.representingObjectHom, AlgebraicGeometry.Stack.eq_map_representingObjectHom, AlgebraicGeometry.Stack.representableBySquareIso, AlgebraicGeometry.Stack.whiskerRight_representableBySquareIso_hom, AlgebraicGeometry.Stack.representingObjectRingedToposHom
statement: formalized
proof: formalized
---

# 96.8 Representable categories

Section 96.8 of the Stacks Project, [Tag 076N](https://stacks.math.columbia.edu/tag/076N). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 075I, a lemma

[Tag 075I](https://stacks.math.columbia.edu/tag/075I) in the Stacks Project.

**`AlgebraicGeometry.Stack.representableBy_isContinuous_and_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean#L71). The attribute's comment: “the equivalence of the underlying sites”.

> **Stacks 075I.** The equivalence over the base representing `p` by `X` is continuous and
> cocontinuous for the associated topologies (Stacks 06TP) of `𝒳` and of the slice `(Sch/S)/X`,
> so it is an equivalence of the two sites. It is a 1-morphism of categories fibred in groupoids
> because the slice is fibred in groupoids over the base, so this is Stacks 06NW.

```lean
theorem representableBy_isContinuous_and_isCocontinuous :
    e.hom.functor.IsContinuous (associatedTopology B S hS p τ)
        (associatedTopology B S hS (Over.forget X) τ) ∧
      e.hom.functor.IsCocontinuous (associatedTopology B S hS p τ)
        (associatedTopology B S hS (Over.forget X) τ)
```

**`AlgebraicGeometry.Stack.structureSheaf_representableBy`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean#L88). The attribute's comment: “the structure sheaves agree”.

> **Stacks 075I.** The representing equivalence carries the structure sheaf of the slice
> `(Sch/S)/X` to the structure sheaf of `𝒳`: restriction along it of the one is the other, as
> sheaves of commutative rings.

```lean
theorem structureSheaf_representableBy
    [e.hom.functor.IsContinuous (associatedTopology B S hS p τ)
      (associatedTopology B S hS (Over.forget X) τ)] :
    (e.hom.functor.sheafPushforwardContinuous CommRingCat.{u}
          (associatedTopology B S hS p τ)
          (associatedTopology B S hS (Over.forget X) τ)).obj
        (structureSheaf B S hS (Over.forget X)
          (Functor.IsFiberedInGroupoids.over_forget X) τ hτ) =
      structureSheaf B S hS p hp τ hτ
```

**`AlgebraicGeometry.Stack.structureSheafRepresentableByIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentable.lean#L115). The attribute's comment: “the comparison of structure sheaves”.

> **Stacks 075I.** The comparison isomorphism of structure sheaves under the representing
> equivalence. It is the canonical isomorphism attached to the equality
> `AlgebraicGeometry.Stack.structureSheaf_representableBy`, hence the identity on sections.

```lean
noncomputable def structureSheafRepresentableByIso
    [e.hom.functor.IsContinuous (associatedTopology B S hS p τ)
      (associatedTopology B S hS (Over.forget X) τ)] :
    (e.hom.functor.sheafPushforwardContinuous CommRingCat.{u}
          (associatedTopology B S hS p τ)
          (associatedTopology B S hS (Over.forget X) τ)).obj
        (structureSheaf B S hS (Over.forget X)
          (Functor.IsFiberedInGroupoids.over_forget X) τ hτ) ≅
      structureSheaf B S hS p hp τ hτ
```

## Tag 075J, a lemma

[Tag 075J](https://stacks.math.columbia.edu/tag/075J) in the Stacks Project.

**`AlgebraicGeometry.Stack.representingObjectHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L239). The attribute's comment: “the corresponding morphism of schemes”.

> **Stacks 075J.** The morphism of schemes `X ⟶ Y` over `S` corresponding to a 1-morphism
> `F : 𝒳 ⥤ 𝒴` of categories representable by `X` and by `Y`: the morphism carried by the functor
> of slices that `F` becomes under the two representing equivalences.

```lean
def representingObjectHom (hF : F ⋙ q = p) : X ⟶ Y
```

**`AlgebraicGeometry.Stack.eq_map_representingObjectHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L246). The attribute's comment: “the 1-morphism of slices is the one of the morphism of schemes”.

> **Stacks 075J.** Read through the two representing equivalences, the 1-morphism `F` *is*
> postcomposition with the corresponding morphism of schemes `g : X ⟶ Y`, as an equality of
> functors `(Sch/S)/X ⥤ (Sch/S)/Y`.

```lean
theorem eq_map_representingObjectHom (hF : F ⋙ q = p) :
    e.inv.functor ⋙ F ⋙ d.hom.functor =
      Over.map (representingObjectHom B S hS p q F X Y e d hF)
```

**`AlgebraicGeometry.Stack.representableBySquareIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L255). The attribute's comment: “the square of 1-morphisms 2-commutes”.

> **Stacks 075J.** The square formed by `F`, the two representing equivalences and
> postcomposition with the corresponding morphism of schemes 2-commutes: its 2-cell is the unit of
> the representing equivalence of `X`, whiskered with `F ⋙ d`.

```lean
def representableBySquareIso (hF : F ⋙ q = p) :
    F ⋙ d.hom.functor ≅
      e.hom.functor ⋙ Over.map (representingObjectHom B S hS p q F X Y e d hF)
```

**`AlgebraicGeometry.Stack.whiskerRight_representableBySquareIso_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L266). The attribute's comment: “the 2-cell of the square is over the base”.

> **Stacks 075J.** The 2-cell filling the square is a 2-cell *over* `(Sch/S)`: whiskering it
> with the projection of `(Sch/S)/Y` gives the identity 2-cell. So the square 2-commutes in the
> 2-category of categories fibred in groupoids over `(Sch/S)`, which is where the comparison of
> Stacks 075I takes place.

```lean
theorem whiskerRight_representableBySquareIso_hom (hF : F ⋙ q = p) :
    Functor.whiskerRight (representableBySquareIso B S hS p q F X Y e d hF).hom
        (Over.forget Y) =
      eqToHom (by
        rw [Functor.assoc, d.hom.w, hF, Functor.assoc, Over.mapForget_eq, e.hom.w])
```

**`AlgebraicGeometry.Stack.representingObjectRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L371). The attribute's comment: “the morphism of ringed topoi of the morphism of schemes”.

> **Stacks 075J.** The morphism of ringed topoi
> `(Sh((Sch/X)_τ), O_X) → (Sh((Sch/Y)_τ), O_Y)` of the morphism of schemes `g : X ⟶ Y` over `S`
> corresponding to `F`: the morphism of ringed topoi of Stacks 06TW of the 1-morphism
> `CategoryTheory.Over.map g` of slices.

```lean
noncomputable def representingObjectRingedToposHom (hF : F ⋙ q = p) :
    RingedToposHom (associatedRingedTopos B S hS (Over.forget X) (.over_forget X) τ hτ)
      (associatedRingedTopos B S hS (Over.forget Y) (.over_forget Y) τ hτ)
```

**`AlgebraicGeometry.Stack.conjugatedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 399](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L399). The attribute's comment: “the morphism of ringed topoi of the 1-morphism, read on the representing sites”.

> **Stacks 075J.** The morphism of ringed topoi `F : (Sh(𝒳_τ), O_𝒳) → (Sh(𝒴_τ), O_𝒴)` of
> Stacks 06TW, read through the two representing equivalences of Stacks 075I: the composite
> `(Sh((Sch/X)_τ), O_X) → (Sh(𝒳_τ), O_𝒳) → (Sh(𝒴_τ), O_𝒴) → (Sh((Sch/Y)_τ), O_Y)` of morphisms of
> ringed topoi, whose outer two factors are the morphisms of ringed topoi of the 1-morphisms `e⁻¹`
> and `d` of the two representing equivalences.

```lean
noncomputable def conjugatedRingedToposHom (hF : F ⋙ q = p) :
    RingedToposHom (associatedRingedTopos B S hS (Over.forget X) (.over_forget X) τ hτ)
      (associatedRingedTopos B S hS (Over.forget Y) (.over_forget Y) τ hτ)
```

**`AlgebraicGeometry.Stack.fSharpInverseImage_conjugatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L488). The attribute's comment: “the two morphisms of ringed topoi agree, structure sheaves included”.

> **Stacks 075J.** The two morphisms of ringed topoi agree. The morphism of ringed topoi
> `F : (Sh(𝒳_τ), O_𝒳) → (Sh(𝒴_τ), O_𝒴)` of Stacks 06TW, read through the two representing
> equivalences of Stacks 075I, and the morphism of ringed topoi
> `g : (Sh((Sch/X)_τ), O_X) → (Sh((Sch/Y)_τ), O_Y)` of the corresponding morphism of schemes have
> the same inverse image up to the canonical comparison
> `AlgebraicGeometry.Stack.conjugatedRingedToposHomInverseImageIso`, and under that comparison
> their structure maps `g⁻¹O_Y ⟶ O_X` coincide as morphisms of sheaves of *commutative rings*: the
> comparison of the two inverse images of the structure sheaf of `(Sch/S)/Y` takes the one to the
> other.

```lean
theorem fSharpInverseImage_conjugatedRingedToposHom (hF : F ⋙ q = p) :
    haveI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_representableBy B S hS p X e
    haveI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_representableBy B S hS q Y d
    (conjugatedRingedToposHom B S hS p q F X Y e d hp hq τ hτ hF).fSharpInverseImage =
      (pullbackCommRingSheafIsoOfNatIso (associatedTopology B S hS (Over.forget X) τ)
          (conjugatedRingedToposHomInverseImageIso B S hS p q F X Y e d hp hq τ hτ hF)
          (structureSheaf B S hS (Over.forget Y)
            (Functor.IsFiberedInGroupoids.over_forget Y) τ hτ)).hom ≫
        (representingObjectRingedToposHom B S hS p q F X Y e d τ hτ hF).fSharpInverseImage
```

**`AlgebraicGeometry.Stack.fSharp_conjugatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean, line 513](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/StructureSheafRepresentableMorphism.lean#L513). The attribute's comment: “the square of morphisms of ringed topoi commutes”.

> **Stacks 075J.** The square of morphisms of ringed topoi commutes, in the direct-image form
> in which a morphism of ringed topoi (Stacks 01D3) states its structure map: the structure map of
> `F` read through the two representing equivalences of Stacks 075I, transported along the adjoint
> mate of the comparison of the two inverse images, is the structure map of the morphism of ringed
> topoi of the corresponding morphism of schemes.

```lean
theorem fSharp_conjugatedRingedToposHom (hF : F ⋙ q = p) :
    haveI : EssentiallySmall.{u} 𝒳 := essentiallySmall_of_representableBy B S hS p X e
    haveI : EssentiallySmall.{u} 𝒴 := essentiallySmall_of_representableBy B S hS q Y d
    (associatedRingedTopos B S hS (Over.forget Y) (.over_forget Y) τ hτ).forgetRing.map
          (conjugatedRingedToposHom B S hS p q F X Y e d hp hq τ hτ hF).fSharp ≫
        (((conjugatedRingedToposHom B S hS p q F X Y e d hp hq τ hτ
              hF).toToposHom.adj.ofNatIsoLeft
            (conjugatedRingedToposHomInverseImageIso B S hS p q F X Y e d hp hq τ hτ
              hF)).rightAdjointUniq
          (representingObjectRingedToposHom B S hS p q F X Y e d τ hτ
            hF).toToposHom.adj).hom.app
          ((associatedRingedTopos B S hS (Over.forget X) (.over_forget X) τ hτ).forgetRing.obj
            (structureSheaf B S hS (Over.forget X)
              (Functor.IsFiberedInGroupoids.over_forget X) τ hτ)) =
      (associatedRingedTopos B S hS (Over.forget Y) (.over_forget Y) τ hτ).forgetRing.map
        (representingObjectRingedToposHom B S hS p q F X Y e d τ hτ hF).fSharp
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.8, Tag 076N](https://stacks.math.columbia.edu/tag/076N)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
