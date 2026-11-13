---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.idealMap, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderSurjection, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderSurjection_epi, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderIdealMap, AlgebraicGeometry.RingedSpaceThickening.exists_factorization_of_comp_idealι_eq_zero, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.epi_baseToSourceIdeal, AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.IsStrict
statement: formalized
proof: formalized
---

# 91.3 Thickenings of ringed spaces

Section 91.3 of the Stacks Project, [Tag 08KY](https://stacks.math.columbia.edu/tag/08KY). 3 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08KZ, a situation

[Tag 08KZ](https://stacks.math.columbia.edu/tag/08KZ) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L416). The attribute's comment: “the commutative square”.

> A morphism of thickenings: a commutative square of ringed spaces whose horizontal arrows are
> thickenings.

```lean
structure MorphismOfThickenings
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.idealMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L465). The attribute's comment: “the canonical ideal map”.

> The canonical map `(f')^* J ⟶ I`: after inclusion into `𝒪_{X'}`, it is the restriction of
> `(f')^♯` to the pullback of `J`.

```lean
noncomputable def idealMap (D : MorphismOfThickenings.{u}) :
    { g : (modulePullback D.f').obj D.idealJ ⟶ D.idealI //
      g ≫ kernel.ι (SheafOfModules.unitToPushforwardObjUnit (structureSheafHom D.i)) =
        D.ambientIdealMap }
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderSurjection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L544). The attribute's comment: “the first-order canonical map”.

> The canonical reduction map `(f')^* J ⟶ i_* f^* t^* J`: the unit of `i^* ⊣ i_*`, followed by
> the pushforward of `reducedPullbackComparison`.

```lean
noncomputable def firstOrderSurjection (D : MorphismOfThickenings.{u})
    (_hi : IsFirstOrderThickening D.i) (_ht : IsFirstOrderThickening D.t) :
    (modulePullback D.f').obj D.idealJ ⟶ D.reducedPullbackIdeal
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderSurjection_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 553](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L553). The attribute's comment: “surjectivity of the first-order canonical map”.

> When both thickenings are first order, the canonical reduction map
> `(f')^* J ⟶ i_* f^* t^* J` is an epimorphism.

```lean
theorem firstOrderSurjection_epi (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) :
    Epi (D.firstOrderSurjection hi ht)
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.firstOrderIdealMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 566](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L566). The attribute's comment: “the first-order factorization”.

> If both thickenings are first order, the canonical ideal map `(f')^* J ⟶ I` factors uniquely
> through the reduction `(f')^* J ⟶ i_* f^* J`, giving a map `f^* J ⟶ I`.

```lean
noncomputable def firstOrderIdealMap (D : MorphismOfThickenings.{u})
    (hi : IsFirstOrderThickening D.i) (ht : IsFirstOrderThickening D.t) :
    { g : D.reducedPullbackIdeal ⟶ D.idealI //
      D.firstOrderSurjection hi ht ≫ g = D.idealMap.1 ∧
        ∀ g' : D.reducedPullbackIdeal ⟶ D.idealI,
          D.firstOrderSurjection hi ht ≫ g' = D.idealMap.1 → g' = g }
```

**`AlgebraicGeometry.RingedSpaceThickening.exists_factorization_of_comp_idealι_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningTrivialization.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/ThickeningTrivialization.lean#L197). The attribute's comment: “factoring through a thickening”.

> **Stacks Project, Tag 08KZ.** Let `i : X ⟶ X'` be a thickening and `f : Y ⟶ X'` a morphism
> of ringed spaces whose comorphism kills the kernel ideal `ℐ = ker(i^♯)`. Then `f` factors
> through `i`.
>
> The factorization of sheaves of modules exists because `i^♯` is an epimorphism killed by `ℐ`,
> which is what `Abelian.epiDesc` supplies; `exists_ringHom_of_additive_factorization` upgrades
> its underlying additive map to a map of sheaves of rings.

```lean
theorem exists_factorization_of_comp_idealι_eq_zero
    {X Y X' : RingedSpace.{u, u}} (i : X ⟶ X') (f : Y ⟶ X')
    (hi : IsThickening i)
    (h : kernel.ι (SheafOfModules.unitToPushforwardObjUnit (structureSheafHom i)) ≫
      SheafOfModules.unitToPushforwardObjUnit (structureSheafHom f) = 0) :
    ∃ p : Y ⟶ X, p ≫ i = f
```

## Tag 08L1, a definition

[Tag 08L1](https://stacks.math.columbia.edu/tag/08L1) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.epi_baseToSourceIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/StrictThickening.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/StrictThickening.lean#L77). The attribute's comment: “surjectivity of the reduced canonical ideal map”.

> For a strict morphism of thickenings the reduced canonical ideal map `f^* t^* J ⟶ i^* I` is
> surjective.

```lean
theorem epi_baseToSourceIdeal (D : MorphismOfThickenings.{u}) (hs : D.IsStrict) :
    Epi D.baseToSourceIdeal
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.IsStrict`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean, line 599](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/RingedSpace/Thickening.lean#L599). The attribute's comment: “strict morphism of thickenings”.

> A morphism of thickenings is *strict* when the canonical map `(f')^* J ⟶ I` of ideal sheaves
> is surjective, i.e. an epimorphism of sheaves of `𝒪_{X'}`-modules.

```lean
noncomputable abbrev IsStrict (D : MorphismOfThickenings.{u}) : Prop
```

## Tag 08L2, a lemma

[Tag 08L2](https://stacks.math.columbia.edu/tag/08L2) in the Stacks Project.

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.isStrict_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/CartesianStrict.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/CartesianStrict.lean#L284). The attribute's comment: “a cartesian square is strict”.

> **Stacks Project, Tag 08L2.** A cartesian square of thickenings is strict.
>
> For a point `x` of `X'` the test object `testPoint x` maps to `X'`, and its composite with `f'`
> factors through the thickening `t`; the square, being cartesian, therefore lifts it to `X`, and
> the lift forces the comorphism of `testPoint x` to kill `I`. So the germ at `x` of a section of
> `I` is a germ of a section in the range of the ambient ideal map, and `(f')^* J ⟶ I` is locally
> surjective.

```lean
theorem isStrict_of_isPullback (hc : IsPullback D.i D.f D.f' D.t) : D.IsStrict
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.isStrict_iff_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/CartesianStrict.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/CartesianStrict.lean#L329). The attribute's comment: “strict iff cartesian”.

> **Stacks Project, Tag 08L2.** A morphism of thickenings of ringed spaces is strict if and
> only if its square is cartesian in the category of ringed spaces. The forward implication is
> `isPullback_of_isStrict`; the converse is `isStrict_of_isPullback`.

```lean
theorem isStrict_iff_isPullback : D.IsStrict ↔ IsPullback D.i D.f D.f' D.t
```

**`AlgebraicGeometry.RingedSpaceThickening.MorphismOfThickenings.isPullback_of_isStrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RingedSpaceThickening/StrictCartesian.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RingedSpaceThickening/StrictCartesian.lean#L90). The attribute's comment: “a strict morphism has a cartesian square”.

> **Stacks Project, Tag 08L2.** A strict morphism of thickenings has a cartesian square: both
> thickenings are monomorphisms, so uniqueness of a lift is automatic, and existence is the
> factorization of a test morphism through `i` supplied by
> `exists_factorization_of_comp_idealι_eq_zero`.

```lean
theorem isPullback_of_isStrict (D : MorphismOfThickenings.{u}) (hs : D.IsStrict) :
    IsPullback D.i D.f D.f' D.t
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.3, Tag 08KY](https://stacks.math.columbia.edu/tag/08KY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
