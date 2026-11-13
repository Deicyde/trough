---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.associatedInvertibleSheaf, AlgebraicGeometry.Space.associatedInvertibleSheaf_isInvertible, AlgebraicGeometry.Space.idealSheafHom, AlgebraicGeometry.Space.associatedInvertibleSheafHomEquiv, AlgebraicGeometry.Space.associatedInvertibleSheafHomEquiv_apply, AlgebraicGeometry.Space.canonicalSection, AlgebraicGeometry.Space.canonicalSection_apply, AlgebraicGeometry.Space.negativeDivisorSheaf
statement: formalized
proof: formalized
---

# 71.7 Effective Cartier divisors and invertible sheaves

Section 71.7 of the Stacks Project, [Tag 0CPG](https://stacks.math.columbia.edu/tag/0CPG). 8 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0841, a definition

[Tag 0841](https://stacks.math.columbia.edu/tag/0841) in the Stacks Project.

**`AlgebraicGeometry.Space.associatedInvertibleSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L179). The attribute's comment: “part (1): the associated invertible sheaf”.

> The *invertible sheaf `𝒪_X(D)` associated to an effective Cartier divisor* `D ⊆ X`: the
> inverse tensor power `𝓘_D^{⊗ -1}` of its defining ideal sheaf.

```lean
noncomputable def associatedInvertibleSheaf (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    SheafOfModules.{u} (structureRingSheaf B S hS X)
```

**`AlgebraicGeometry.Space.associatedInvertibleSheaf_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L195). The attribute's comment: “part (1): the associated invertible sheaf”.

> The sheaf `𝒪_X(D)` associated to an effective Cartier divisor is invertible.

```lean
theorem associatedInvertibleSheaf_isInvertible (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property
      (associatedInvertibleSheaf B S hS X D hD)
```

**`AlgebraicGeometry.Space.idealSheafHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L208). The attribute's comment: “part (1): the associated invertible sheaf”.

> The sheaf-hom `SheafHom_{𝒪_X}(𝓘_D, 𝒪_X)`, the second description of `𝒪_X(D)`. Its sections over
> an étale chart `U` are the morphisms `𝓘_D|_U ⟶ 𝒪_X|_U` of `𝒪_X|_U`-modules on the slice site over
> `U`, hence live one universe above the sections of the structure sheaf.

```lean
noncomputable def idealSheafHom (Z : ClosedSubspaces B S hS X.1) :
    SheafOfModules.{u + 1} (structureRingSheaf B S hS X)
```

**`AlgebraicGeometry.Space.associatedInvertibleSheafHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L236). The attribute's comment: “part (1): the associated invertible sheaf”.

> The two descriptions of `𝒪_X(D)` agree: a section of `𝓘_D^{⊗ -1}` over an étale chart `U`
> is the same thing as a morphism `𝓘_D|_U ⟶ 𝒪_X|_U`, by a linear equivalence of sections.

```lean
noncomputable def associatedInvertibleSheafHomEquiv (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) (U : SmallEtale B S hS X.1) :
    (modulePresheaf B S hS X (associatedInvertibleSheaf B S hS X D hD)).obj (Opposite.op U)
        ≃ₗ[(structureCommRings B S hS X).obj (Opposite.op U)]
      internalHomObj (structureCommRings B S hS X)
        (modulePresheaf B S hS X (idealSheafOfModules B S hS X D))
        (modulePresheaf B S hS X (SheafOfModules.unit (structureRingSheaf B S hS X))) U
```

**`AlgebraicGeometry.Space.associatedInvertibleSheafHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L273). The attribute's comment: “part (1): the associated invertible sheaf”.

> The identification of the two descriptions of `𝒪_X(D)` is given by the evaluation pairing: the
> morphism `𝓘_D|_U ⟶ 𝒪_X|_U` attached to a section `s` of `𝓘_D^{⊗ -1}` over `U` sends a section `t`
> of `𝓘_D` over an étale chart `V` over `U` to the value of the evaluation pairing on the restriction
> of `s` tensored with `t`.

```lean
theorem associatedInvertibleSheafHomEquiv_apply (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) (U : SmallEtale B S hS X.1)
    (s : (modulePresheaf B S hS X
      (associatedInvertibleSheaf B S hS X D hD)).obj (Opposite.op U))
    (V : (SmallEtale B S hS X.1)ᵒᵖ) (f : V.unop ⟶ U)
    (t : (modulePresheaf B S hS X (idealSheafOfModules B S hS X D)).obj V) :
    homSectionCoeff (structureCommRings B S hS X)
        (modulePresheaf B S hS X (idealSheafOfModules B S hS X D))
        (modulePresheaf B S hS X (SheafOfModules.unit (structureRingSheaf B S hS X))) U
        (associatedInvertibleSheafHomEquiv B S hS X D hD U s) V f t =
      tensorHomAt (structureCommRings B S hS X)
        (modulePresheaf B S hS X (associatedInvertibleSheaf B S hS X D hD))
        (modulePresheaf B S hS X (idealSheafOfModules B S hS X D))
        (modulePresheaf B S hS X (SheafOfModules.unit (structureRingSheaf B S hS X)))
        (tensorPairing (structureCommRings B S hS X) (structureRingSheaf B S hS X).property
          (idealSheafOfModules B S hS X D) (associatedInvertibleSheaf B S hS X D hD)
          (SheafOfModules.unit (structureRingSheaf B S hS X))
          (associatedInvertibleSheafEvaluation B S hS X D hD)) V
        ((modulePresheaf B S hS X
          (associatedInvertibleSheaf B S hS X D hD)).restrictₛₗ f.op s ⊗ₜ t)
```

**`AlgebraicGeometry.Space.canonicalSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L332). The attribute's comment: “part (2): the canonical section”.

> The *canonical section* `1_D` of `𝒪_X(D)`: the global section corresponding, under the
> identification of `𝒪_X(D)` with `SheafHom_{𝒪_X}(𝓘_D, 𝒪_X)`, to the inclusion `𝓘_D ⟶ 𝒪_X`.

```lean
noncomputable def canonicalSection (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    (associatedInvertibleSheaf B S hS X D hD).sections
```

**`AlgebraicGeometry.Space.canonicalSection_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L348). The attribute's comment: “part (2): the canonical section”.

> The canonical section of `𝒪_X(D)` is, on every étale chart, the inclusion `𝓘_D ⟶ 𝒪_X` read
> through the identification of `𝒪_X(D)` with `SheafHom_{𝒪_X}(𝓘_D, 𝒪_X)`.

```lean
theorem canonicalSection_apply (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) (U : (SmallEtale B S hS X.1)ᵒᵖ) :
    associatedInvertibleSheafHomEquiv B S hS X D hD U.unop
        ((canonicalSection B S hS X D hD).val U) =
      idealInclusionSection B S hS X D U
```

**`AlgebraicGeometry.Space.negativeDivisorSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L359). The attribute's comment: “part (3): the negative of a divisor”.

> The sheaf `𝒪_X(-D) = 𝒪_X(D)^{⊗ -1}`.

```lean
noncomputable def negativeDivisorSheaf (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    SheafOfModules.{u} (structureRingSheaf B S hS X)
```

**`AlgebraicGeometry.Space.negativeDivisorSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L370). The attribute's comment: “part (3): the negative of a divisor”.

> The identification `𝒪_X(-D) ≅ 𝓘_D`.

```lean
noncomputable def negativeDivisorSheafIso (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    negativeDivisorSheaf B S hS X D hD ≅ idealSheafOfModules B S hS X D
```

**`AlgebraicGeometry.Space.differenceDivisorSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean, line 400](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisor.lean#L400). The attribute's comment: “part (4): the difference of two divisors”.

> The sheaf `𝒪_X(D - D') = 𝒪_X(D) ⊗_{𝒪_X} 𝒪_X(-D')` attached to a pair of effective Cartier
> divisors.

```lean
noncomputable def differenceDivisorSheaf (D D' : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D)
    (hD' : IsEffectiveCartierDivisor B S hS X D') :
    SheafOfModules.{u} (structureRingSheaf B S hS X)
```

## Tag 0B4F, a lemma

[Tag 0B4F](https://stacks.math.columbia.edu/tag/0B4F) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalModuleIsoPullbackIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfEffectiveCartierDivisor.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfEffectiveCartierDivisor.lean#L77). The attribute's comment: “the conormal sheaf is the restriction of the ideal sheaf”.

> **The first identification of Stacks 0B4F**, `𝒞_{Z/X} = 𝓘_Z|_Z`: the conormal module of a
> closed subspace `Z` of an algebraic space `X` is the restriction to `Z` of the defining ideal
> sheaf `𝓘_Z ⊆ 𝒪_X`, where restriction is the inverse image along the inclusion `i : Z ⟶ X`.
> `Z` need not be an effective Cartier divisor.

```lean
noncomputable def conormalModuleIsoPullbackIdealSheaf (X : AlgebraicSpaces B S hS)
    (Z : ClosedSubspaces B S hS X.1) :
    conormalModule B S hS X Z ≅
      (modulePullback B S hS (subspaceInclusion B S hS X Z)).obj
        (idealSheafOfModules B S hS X Z)
```

**`AlgebraicGeometry.Space.pullbackIdealSheafIsoPullbackNegativeDivisorSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfEffectiveCartierDivisor.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ConormalModuleOfEffectiveCartierDivisor.lean#L99). The attribute's comment: “the restriction of the ideal sheaf is the restriction of the inverse of O\_X(D)”.

> **The second identification of Stacks 0B4F**, `𝓘_D|_D = 𝒪_X(D)^{⊗ -1}|_D`: for an effective
> Cartier divisor `D ⊆ X`, the restriction to `D` of the defining ideal sheaf `𝓘_D` agrees with the
> restriction to `D` of `𝒪_X(-D) = 𝒪_X(D)^{⊗ -1}`.
>
> It is the inverse image along the inclusion `i : D ⟶ X` of the canonical identification
> `𝒪_X(-D) ≅ 𝓘_D` of Stacks 0841, part 3 (`AlgebraicGeometry.Space.negativeDivisorSheafIso`).

```lean
noncomputable def pullbackIdealSheafIsoPullbackNegativeDivisorSheaf
    (X : AlgebraicSpaces B S hS) (D : ClosedSubspaces B S hS X.1)
    (hD : IsEffectiveCartierDivisor B S hS X D) :
    (modulePullback B S hS (subspaceInclusion B S hS X D)).obj
        (idealSheafOfModules B S hS X D) ≅
      (modulePullback B S hS (subspaceInclusion B S hS X D)).obj
        (negativeDivisorSheaf B S hS X D hD)
```

## Tag 0842, a lemma

[Tag 0842](https://stacks.math.columbia.edu/tag/0842) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_tensorInvertibleSheafIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorTensorIso.lean, line 1310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/EffectiveCartierDivisorTensorIso.lean#L1310).

> **Stacks 0842.** For two effective Cartier divisors `D₁, D₂` on an algebraic space `X` with
> sum `D = D₁ + D₂` there is a *unique* isomorphism
> `𝒪_X(D₁) ⊗_{𝒪_X} 𝒪_X(D₂) ⟶ 𝒪_X(D)` carrying `1_{D₁} ⊗ 1_{D₂}` to `1_D`.

```lean
theorem existsUnique_tensorInvertibleSheafIso :
    ∃! e : (((Stacks.SheafOfModules.Tensor.sheafTensor.{u + 1, u, u, u, u}
        ⟨(structureCommRings B S hS X), Presheaf.isSheaf_of_isSheaf_comp _
        ((structureCommRings B S hS X)) (forget₂ CommRingCat RingCat)
        ((structureRingSheaf B S hS X).property)⟩).obj
        ((associatedInvertibleSheaf B S hS X D₁ hD₁))).obj
        ((associatedInvertibleSheaf B S hS X D₂ hD₂))) ≅
        associatedInvertibleSheaf B S hS X (sumClosedSubspaces B S hS X D₁ D₂)
          (isEffectiveCartierDivisor_sumClosedSubspaces B S hS X D₁ D₂ hD₁ hD₂),
      ∀ U : (SmallEtale B S hS X.1)ᵒᵖ,
        (e.hom.val.app U).hom
            ((tensorCanonicalSection B S hS X D₁ D₂ hD₁ hD₂).val U) =
          (canonicalSection B S hS X (sumClosedSubspaces B S hS X D₁ D₂)
            (isEffectiveCartierDivisor_sumClosedSubspaces B S hS X D₁ D₂ hD₁ hD₂)).val U
```

## Tag 0843, a definition

[Tag 0843](https://stacks.math.columbia.edu/tag/0843) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsRegularSection`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Divisors/Meromorphic/RegularSections.lean#L107), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/RegularSectionsAndRepresentability.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/RegularSectionsAndRepresentability.lean#L27) (StacksFrontier).

## Tag 0844, a lemma

[Tag 0844](https://stacks.math.columbia.edu/tag/0844) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegularSection_iff_etaleLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean#L289). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0844, conditions (1) and (2).** A global regular function on an algebraic space
> is a regular section of the structure sheaf if and only if its image in the étale local ring
> at every geometric point is a nonzerodivisor.

```lean
theorem isRegularSection_iff_etaleLocalRing (f : GlobalFunctions B S hS X hX) :
    IsRegularSection (structurePresheaf B S hS X)
        (structureRingPresheaf_isSheaf B S hS X hX) f ↔
      ∀ (x : GeometricPoint B S hS X) (V : SmallEtaleNeighborhood x),
        IsSMulRegular (etaleLocalRing B S hS X x)
          (etaleLocalRingGerm B S hS X x (op V)
            (chartValue B S hS X hX f V.chart))
```

**`AlgebraicGeometry.Space.isRegularSection_iff_affineEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean#L320). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 0844, conditions (1) and (3).** A global regular function on an algebraic space
> is a regular section of the structure sheaf if and only if its restriction to every affine
> étale chart is a nonzerodivisor there.

```lean
theorem isRegularSection_iff_affineEtale (f : GlobalFunctions B S hS X hX) :
    IsRegularSection (structurePresheaf B S hS X)
        (structureRingPresheaf_isSheaf B S hS X hX) f ↔
      ∀ U : SmallEtale B S hS X, IsAffine (etaleChartScheme B S hS U) →
        IsSMulRegular (Γ(etaleChartScheme B S hS U, ⊤))
          (chartValue B S hS X hX f U)
```

**`AlgebraicGeometry.Space.isRegularSection_iff_exists_surjectiveChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSections.lean#L336). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 0844, conditions (1) and (4).** A global regular function on an algebraic space
> is a regular section of the structure sheaf if and only if there is a surjective étale scheme
> chart on which its restriction is a regular section.

```lean
theorem isRegularSection_iff_exists_surjectiveChart (f : GlobalFunctions B S hS X hX) :
    IsRegularSection (structurePresheaf B S hS X)
        (structureRingPresheaf_isSheaf B S hS X hX) f ↔
      ∃ C : SmallEtale B S hS X, IsSurjective B S hS C.obj.hom ∧
        IsRegularSection (etaleChartScheme B S hS C).presheaf
          ((Presheaf.isSheaf_iff_isSheaf_comp _ (etaleChartScheme B S hS C).presheaf
            (forget₂ CommRingCat.{u} RingCat.{u})).mp
              (etaleChartScheme B S hS C).IsSheaf)
          (chartFunctionSections B S hS X hX f C)
```

## Tag 0845, a definition

[Tag 0845](https://stacks.math.columbia.edu/tag/0845) in the Stacks Project.

**`AlgebraicGeometry.Space.zeroSchemeSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean, line 305](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean#L305). The attribute's comment: “underlying subfunctor construction”.

> **Stacks 0845.** Intersect the closed subspaces whose defining ideals are contained in the
> ideals generated by local evaluations of the section.

```lean
noncomputable def zeroSchemeSubfunctor (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections) : Subfunctor X.1
```

**`AlgebraicGeometry.Space.zeroSchemeSubfunctor_isClosedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean, line 319](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroScheme.lean#L319). The attribute's comment: “closedness”.

> **Stacks 0845.** The subfunctor cut out by evaluation at a section of a module sheaf is a
> closed subspace.

```lean
theorem zeroSchemeSubfunctor_isClosedSubspace (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections) :
    IsClosedSubspace B S hS (zeroSchemeSubfunctor B S hS X L s)
```

## Tag 0846, a lemma

[Tag 0846](https://stacks.math.columbia.edu/tag/0846) in the Stacks Project.

**`AlgebraicGeometry.Space.isGreatest_zeroScheme_of_exists_definingIdealAt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean#L179). The attribute's comment: “part (1): maximality, with vanishing on a closed subspace read chartwise and with the realization of the evaluation ideal by a closed subspace assumed”.

> **Stacks 0846 (1).**  Among the closed subspaces of `X` on which the section vanishes — read
> chartwise: those whose defining ideal contains the evaluation ideal of the section on every
> affine étale chart — the zero scheme of the section is the greatest.
>
> The hypothesis is the surjectivity half of Stacks 03MB for the evaluation ideal: some closed
> subspace of `X` has that ideal as its defining ideal on the affine étale charts.  It is used
> only to see that the zero scheme is itself a member of the ordered set; the upper-bound half
> `AlgebraicGeometry.Space.le_zeroSchemeSubfunctor` is unconditional.

```lean
theorem isGreatest_zeroScheme_of_exists_definingIdealAt_eq (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections)
    (hZ : ∃ Z : ClosedSubspaces B S hS X.1, ∀ U : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1 →
      definingIdealAt B S hS X Z (op U) = sectionEvaluationIdealAt B S hS X L s U) :
    IsGreatest {W : ClosedSubspaces B S hS X.1 |
      ∀ U : SmallEtale B S hS X.1,
        IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1 →
        sectionEvaluationIdealAt B S hS X L s U ≤ definingIdealAt B S hS X W (op U)}
      (zeroScheme B S hS X L s)
```

**`AlgebraicGeometry.Space.exists_comp_eq_zeroScheme_iff_of_exists_definingIdealAt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean#L205). The attribute's comment: “part (2): factorization, with vanishing of the pulled-back section read chartwise and with the realization of the evaluation ideal by a closed subspace assumed”.

> **Stacks 0846 (2).**  A morphism `f : Y ⟶ X` of algebraic spaces factors through the zero
> scheme of the section exactly when the section vanishes after pullback along `f` — read
> chartwise: on every affine étale chart `U` of `X` the evaluation ideal of the section is killed
> by pullback of regular functions along every point of `Y` lying over `U`.
>
> The hypothesis is the same one as in part (1), and is used only for the direction from factoring
> to vanishing; the converse
> `AlgebraicGeometry.Space.exists_comp_eq_zeroScheme_of_sectionEvaluationIdealAt_le` is
> unconditional.

```lean
theorem exists_comp_eq_zeroScheme_iff_of_exists_definingIdealAt_eq
    (X Y : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections)
    (hZ : ∃ Z : ClosedSubspaces B S hS X.1, ∀ U : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1 →
      definingIdealAt B S hS X Z (op U) = sectionEvaluationIdealAt B S hS X L s U)
    (f : Y ⟶ X) :
    (∃ g : Y ⟶ (⟨(zeroScheme B S hS X L s).1.toFunctor,
        (zeroScheme B S hS X L s).2.1⟩ : AlgebraicSpaces B S hS),
      g ≫ ObjectProperty.homMk (zeroScheme B S hS X L s).1.ι = f) ↔
      ∀ U : SmallEtale B S hS X.1,
        IsAffine ((BigFppfOver.toScheme B S hS).obj U.1.left) →
        ∀ (a : BigFppfOver B S hS) (k : a ⟶ U.1.left) (y : yoneda.obj a ⟶ Y.1),
          yoneda.map k ≫ U.1.hom = y ≫ f.hom →
            sectionEvaluationIdealAt B S hS X L s U ≤
              RingHom.ker (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map k).op).hom
```

**`AlgebraicGeometry.Space.isLocallyPrincipal_zeroScheme_of_epi_inverseTensorPower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean#L239). The attribute's comment: “part (3): locally principal, assuming an epimorphism onto the ideal sheaf from the inverse tensor power of the invertible module and local generation of that power by one section”.

> **Stacks 0846 (3).**  The zero scheme of a section of an invertible `𝒪_X`-module is a
> locally principal closed subspace of `X`.
>
> Two hypotheses are carried, and both are used.  The first is an epimorphism `p` onto the
> defining ideal sheaf of the zero scheme from the inverse tensor power `L^{⊗ -1}` of Stacks
> 01CU, which in the source is the image factorization of the evaluation map `L^{⊗ -1} ⟶ 𝒪_X`
> cutting out `Z(s)`; its source is pinned to `L^{⊗ -1}` rather than left arbitrary, since for an
> arbitrary source the identity of the ideal sheaf would witness the hypothesis.  The second is
> local generation of `L^{⊗ -1}` by one section, which for an invertible module is the descent
> clause of Stacks 0B8M.

```lean
theorem isLocallyPrincipal_zeroScheme_of_epi_inverseTensorPower (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2)
    [AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L]
    (s : L.sections)
    (hfree : _root_.SheafOfModules.IsLocallyGeneratedByOnSite
      (Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
        (structureRingSheaf B S hS X).property L (-1)) 1)
    (p : Stacks.SheafOfModules.Invertible.tensorPower (structureCommRings B S hS X)
        (structureRingSheaf B S hS X).property L (-1) ⟶
      idealSheafOfModules B S hS X (zeroScheme B S hS X L s))
    (hp : Epi p) :
    IsLocallyPrincipal B S hS X (zeroScheme B S hS X L s)
```

**`AlgebraicGeometry.Space.definingIdealAt_zeroScheme_eq_span_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertions.lean#L264). The attribute's comment: “part (4) read chartwise: the zero scheme is cut out on an affine chart by one regular function, with the realization of the evaluation ideal by a closed subspace assumed”.

> **Stacks 0846 (4), first half, read chartwise.**  On an affine étale chart `U` of `X` where
> `L` is free of rank one, with generator `t` and coordinate functional `l₀`, the zero scheme of
> the section is cut out by the single regular function `l₀(s|_U)`.
>
> The hypothesis is the one of parts (1) and (2): some closed subspace of `X` has the evaluation
> ideal of the section as its defining ideal on the affine étale charts.

```lean
theorem definingIdealAt_zeroScheme_eq_span_generator (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections)
    (hZ : ∃ Z : ClosedSubspaces B S hS X.1, ∀ U : SmallEtale B S hS X.1,
      IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1 →
      definingIdealAt B S hS X Z (op U) = sectionEvaluationIdealAt B S hS X L s U)
    (U : SmallEtale B S hS X.1)
    (hU : IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1)
    (t : ToType (L.val.obj (op U)))
    (l₀ : Module.Dual
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).obj.obj
        (op U))
      (L.val.obj (op U)))
    (hb : ∀ x, l₀ x • t = x) :
    definingIdealAt B S hS X (zeroScheme B S hS X L s) (op U) =
      Ideal.span {l₀ (s.eval (op U))}
```

**`AlgebraicGeometry.Space.isGreatest_zeroScheme_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean#L59). The attribute's comment: “part (1): maximality of the zero scheme among the closed subspaces on which the section vanishes, read chartwise, with no assumed inputs”.

> **Stacks 0846 (1).**  Let `L` be an invertible `𝒪_X`-module and `s` a global section of `L`.
> Among the closed subspaces of `X` on which `s` vanishes — read chartwise: those whose defining
> ideal contains the evaluation ideal of `s` on every affine étale chart — the zero scheme of `s`
> is the greatest.
>
> The hypotheses are the source's own and nothing else: invertibility of `L` discharges the
> realization of the evaluation ideal by a closed subspace, through
> `AlgebraicGeometry.Space.exists_definingIdealAt_eq_sectionEvaluationIdealAt_of_isInvertible`.

```lean
theorem isGreatest_zeroScheme_of_isInvertible (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hinv : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L)
    (s : L.sections) :
    IsGreatest {W : ClosedSubspaces B S hS X.1 |
      ∀ U : SmallEtale B S hS X.1,
        IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1 →
        sectionEvaluationIdealAt B S hS X L s U ≤ definingIdealAt B S hS X W (op U)}
      (zeroScheme B S hS X L s)
```

**`AlgebraicGeometry.Space.exists_comp_eq_zeroScheme_iff_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean#L83). The attribute's comment: “part (2): a morphism factors through the zero scheme exactly when the pulled-back section vanishes, read chartwise, with no assumed inputs”.

> **Stacks 0846 (2).**  Let `L` be an invertible `𝒪_X`-module and `s` a global section of `L`.
> A morphism `f : Y ⟶ X` of algebraic spaces factors through the zero scheme of `s` exactly when
> `s` vanishes after pullback along `f` — read chartwise: on every affine étale chart `U` of `X`
> the evaluation ideal of `s` is killed by pullback of regular functions along every point of `Y`
> lying over `U`.
>
> The hypotheses are the source's own and nothing else: invertibility of `L` discharges the
> realization of the evaluation ideal by a closed subspace, through
> `AlgebraicGeometry.Space.exists_definingIdealAt_eq_sectionEvaluationIdealAt_of_isInvertible`.

```lean
theorem exists_comp_eq_zeroScheme_iff_of_isInvertible (X Y : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hinv : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L)
    (s : L.sections) (f : Y ⟶ X) :
    (∃ g : Y ⟶ (⟨(zeroScheme B S hS X L s).1.toFunctor,
        (zeroScheme B S hS X L s).2.1⟩ : AlgebraicSpaces B S hS),
      g ≫ ObjectProperty.homMk (zeroScheme B S hS X L s).1.ι = f) ↔
      ∀ U : SmallEtale B S hS X.1,
        IsAffine ((BigFppfOver.toScheme B S hS).obj U.1.left) →
        ∀ (a : BigFppfOver B S hS) (k : a ⟶ U.1.left) (y : yoneda.obj a ⟶ Y.1),
          yoneda.map k ≫ U.1.hom = y ≫ f.hom →
            sectionEvaluationIdealAt B S hS X L s U ≤
              RingHom.ker (Scheme.Γ.map ((BigFppfOver.toScheme B S hS).map k).op).hom
```

**`AlgebraicGeometry.Space.definingIdealAt_zeroScheme_eq_span_generator_of_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeAssertionsInvertible.lean#L117). The attribute's comment: “part (4) read chartwise: the zero scheme is cut out on an affine chart by one regular function, with L carried as free of rank one on that chart by a generator t and a coordinate functional l₀; the chart U and the functional l₀ occur in the conclusion, which names the function as l₀ of the section over U”.

> **Stacks 0846 (4), first half, read chartwise.**  Let `L` be an invertible `𝒪_X`-module and
> `s` a global section of `L`.  On an affine étale chart `U` of `X` where `L` is free of rank one,
> with generator `t` and coordinate functional `l₀`, the zero scheme of `s` is cut out by the
> single regular function `l₀(s|_U)`.
>
> Invertibility of `L` discharges the realization of the evaluation ideal by a closed subspace,
> through
> `AlgebraicGeometry.Space.exists_definingIdealAt_eq_sectionEvaluationIdealAt_of_isInvertible`.
> The chart data `t`, `l₀`, `hb` is local freeness of rank one on `U`, which for an invertible `L`
> holds on a cover of `X` by Stacks 0B8Q; it is what makes the chartwise reading of the part a
> statement about one regular function, and it is what the global form
> `AlgebraicGeometry.Space.isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection` supplies for
> itself instead of assuming.

```lean
theorem definingIdealAt_zeroScheme_eq_span_generator_of_isInvertible (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2)
    (hinv : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L)
    (s : L.sections)
    (U : SmallEtale B S hS X.1)
    (hU : IsAffine ((SmallEtale.toSchemes B S hS X.1).obj U).1)
    (t : ToType (L.val.obj (op U)))
    (l₀ : Module.Dual
      ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS X.1 X.2).O).obj.obj
        (op U))
      (L.val.obj (op U)))
    (hb : ∀ x, l₀ x • t = x) :
    definingIdealAt B S hS X (zeroScheme B S hS X L s) (op U) =
      Ideal.span {l₀ (s.eval (op U))}
```

**`AlgebraicGeometry.Space.isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeEffectiveCartier.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeEffectiveCartier.lean#L382). The attribute's comment: “part (4): the zero scheme is an effective Cartier divisor exactly when the section is regular, with no assumed inputs”.

> **Stacks 0846 (4).**  Let `X` be an algebraic space over a scheme `S`, let `L` be an
> invertible `𝒪_X`-module and let `s` be a global section of `L`.  The zero scheme `Z(s)` of
> Stacks 0845 is an effective Cartier divisor on `X` if and only if `s` is a regular section of
> `L` in the sense of Stacks 0843.
>
> The hypotheses are the source's own and nothing else: no local freeness of `L` of rank one on a
> chart, and no chart data, is assumed.  Invertibility of `L` supplies that data chart by chart,
> by Stacks 0B8Q, and both sides of the equivalence are local on the small étale site of `X`, so
> the chartwise content of the part can be assembled into the global statement.

```lean
theorem isEffectiveCartierDivisor_zeroScheme_iff_isRegularSection
    (hinv : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L) :
    IsEffectiveCartierDivisor B S hS X (zeroScheme B S hS X L s) ↔
      AlgebraicGeometry.IsRegularSection (structurePresheaf B S hS X.1)
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS X.1 X.2).O).property s
```

**`AlgebraicGeometry.Space.isLocallyPrincipal_zeroScheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeLocallyPrincipal.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeLocallyPrincipal.lean#L270). The attribute's comment: “part (3): the zero scheme of a section of an invertible module is a locally principal closed subspace”.

> The zero scheme of a global section `s` of an invertible `𝒪_X`-module `L` is a locally
> principal closed subspace of `X`.

```lean
theorem isLocallyPrincipal_zeroScheme
    (hinv : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L) :
    IsLocallyPrincipal B S hS X (zeroScheme B S hS X L s)
```

**`AlgebraicGeometry.Space.isRegularSection_iff_forall_injective_mul_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeProperties.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeProperties.lean#L224). The attribute's comment: “part (4) read chartwise: the section is regular exactly when the functions cutting out the zero scheme are nonzerodivisors, with L carried as free of rank one on every chart”.

> **A global section of a module free of rank one on every étale chart is regular exactly when
> the generators of its evaluation ideals are nonzerodivisors.**  This is the chartwise content of
> Stacks 0846 (4): the zero scheme is cut out on each chart by the single element
> `l₀(s|_U)`, and regularity of `s` is injectivity of multiplication by each of them.

```lean
theorem isRegularSection_iff_forall_injective_mul_generator (X : AlgebraicSpaces B S hS)
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections)
    (t : ∀ U : SmallEtale B S hS X.1, ToType (L.val.obj (op U)))
    (l₀ : ∀ U : SmallEtale B S hS X.1,
      Module.Dual ((Stacks.SheafOfModules.Tensor.ringSheaf
          (smallEtaleRingedSite B S hS X.1 X.2).O).obj.obj (op U))
        (L.val.obj (op U)))
    (hb : ∀ (U : SmallEtale B S hS X.1) (x), l₀ U x • t U = x) :
    AlgebraicGeometry.IsRegularSection (structurePresheaf B S hS X.1)
        (Stacks.SheafOfModules.Tensor.ringSheaf
            (smallEtaleRingedSite B S hS X.1 X.2).O).property s ↔
      ∀ U : SmallEtale B S hS X.1,
        Function.Injective
          (fun r : ToType ((Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS X.1 X.2).O).obj.obj (op U)) =>
            r * l₀ U (s.eval (op U)))
```

## Tag 0847, a lemma

[Tag 0847](https://stacks.math.columbia.edu/tag/0847) in the Stacks Project.

**`AlgebraicGeometry.Space.iso_eq_of_canonicalSectionHom_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CanonicalSectionIsoUnique.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CanonicalSectionIsoUnique.lean#L169). The attribute's comment: “part (2): uniqueness of the isomorphism — two isomorphisms from the sheaf of an effective Cartier divisor to an invertible module, both carrying the canonical section to the given section, are equal; with no assumed inputs”.

> **Stacks 0847, part (2): the isomorphism is unique.**  Let `D ⊆ X` be an effective Cartier
> divisor on an algebraic space `X` and let `s` be a global section of an `𝒪_X`-module `L`.  Two
> isomorphisms `𝒪_X(D) ≅ L` which both carry the canonical section `1_D` of `𝒪_X(D)` to `s` are
> equal.
>
> Composing one with the inverse of the other gives an endomorphism of `𝒪_X(D)` fixing `1_D`, and
> `AlgebraicGeometry.Space.eq_id_of_comp_eq_of_isInvertible` makes it the identity: `𝒪_X(D)` is
> invertible and `1_D` is regular by part (1) of the same tag.

```lean
theorem iso_eq_of_canonicalSectionHom_comp_eq
    (L : SheafOfModules.{u} (structureRingSheaf B S hS X)) (s : L.sections)
    (i j : associatedInvertibleSheaf B S hS X D hD ≅ L)
    (hi : canonicalSectionHom B S hS X D hD ≫ i.hom = L.unitHomEquiv.symm s)
    (hj : canonicalSectionHom B S hS X D hD ≫ j.hom = L.unitHomEquiv.symm s) :
    i = j
```

**`AlgebraicGeometry.Space.canonicalSection_isRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CanonicalSectionRegular.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CanonicalSectionRegular.lean#L307). The attribute's comment: “part (1)”.

> **Stacks 0847, part (1).** The canonical section `1_D` of the invertible sheaf `𝒪_X(D)`
> attached to an effective Cartier divisor `D ⊆ X` is a regular section: multiplication by it is a
> monomorphism `𝒪_X ⟶ 𝒪_X(D)`.  Tensoring by the invertible sheaf `𝓘_D` reflects monomorphisms,
> and it turns multiplication by `1_D` into the inclusion `𝓘_D ⟶ 𝒪_X`.

```lean
theorem canonicalSection_isRegular :
    IsRegularSection (structureCommRings B S hS X) (structureRingSheaf B S hS X).property
      (canonicalSection B S hS X D hD)
```

**`AlgebraicGeometry.Space.exists_isEffectiveCartierDivisor_associatedInvertibleSheaf_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartier.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartier.lean#L81). The attribute's comment: “part (2), existence: a regular global section of an invertible module cuts out an effective Cartier divisor whose associated invertible sheaf it is”.

> **Stacks 0847, part (2), existence.**  Let `X` be an algebraic space over a scheme `S` and
> let `L` be an invertible `𝒪_X`-module with a regular global section `s`.  Then there is an
> effective Cartier divisor `D ⊆ X` and an isomorphism `𝒪_X(D) ≅ L`.
>
> Contraction with `s` is a monomorphism `L^{⊗ -1} ⟶ 𝒪_X` whose image is a quasi-coherent sheaf of
> ideals isomorphic to `L^{⊗ -1}`; by Stacks 03MB that sheaf of ideals is the defining ideal sheaf
> `𝓘_D` of a closed subspace `D`, which is therefore an effective Cartier divisor, and
> `𝒪_X(D) ≅ L` because both are inverse to `𝓘_D`.

```lean
theorem exists_isEffectiveCartierDivisor_associatedInvertibleSheaf_iso
    (L : SheafOfModules.{u} (structureRingSheaf B S hS X))
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L)
    (s : L.sections)
    (hs : AlgebraicGeometry.IsRegularSection (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property s) :
    ∃ (D : ClosedSubspaces B S hS X.1) (hD : IsEffectiveCartierDivisor B S hS X D),
      Nonempty (associatedInvertibleSheaf B S hS X D hD ≅ L)
```

**`AlgebraicGeometry.Space.exists_unique_isEffectiveCartierDivisor_iso_canonicalSectionHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartierUnique.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartierUnique.lean#L166). The attribute's comment: “part (2): a regular global section of an invertible module cuts out a unique effective Cartier divisor, the zero scheme of the section, carrying a unique isomorphism from its associated invertible sheaf to the module which takes the canonical section to the given section; with no assumed inputs”.

> **Stacks 0847, part (2).**  Let `X` be an algebraic space over a scheme `S` and let `L` be an
> invertible `𝒪_X`-module with a regular global section `s`.  Then there is a *unique* effective
> Cartier divisor `D ⊆ X`, namely the zero scheme `Z(s)` of Stacks 0845, carrying a *unique*
> isomorphism `𝒪_X(D) ≅ L` which takes the canonical section `1_D` of `𝒪_X(D)` to `s`.
>
> Contraction with `s` is a monomorphism `L^{⊗ -1} ⟶ 𝒪_X` whose image is a quasi-coherent sheaf of
> ideals isomorphic to `L^{⊗ -1}`; by Stacks 03MB that sheaf of ideals is the defining ideal sheaf
> `𝓘_D` of a closed subspace `D`, which is therefore an effective Cartier divisor.  The
> identification of `𝓘_D` with `L^{⊗ -1}` carries the inclusion `𝓘_D ⟶ 𝒪_X` to contraction with
> `s`, so the pairing `L ⊗ 𝓘_D ≅ 𝒪_X` it induces curries `s` to that inclusion, exactly as the
> evaluation pairing `𝒪_X(D) ⊗ 𝓘_D ≅ 𝒪_X` curries `1_D`; the isomorphism matching the two pairings
> therefore carries `1_D` to `s`.  Uniqueness of the divisor is
> `AlgebraicGeometry.Space.eq_zeroScheme_of_canonicalSectionHom_comp`, which also identifies it as
> `Z(s)`, and uniqueness of the isomorphism is
> `AlgebraicGeometry.Space.iso_eq_of_canonicalSectionHom_comp_eq`.

```lean
theorem exists_unique_isEffectiveCartierDivisor_iso_canonicalSectionHom_comp
    (L : SheafOfModules.{u} (structureRingSheaf B S hS X))
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property L)
    (s : L.sections)
    (hs : AlgebraicGeometry.IsRegularSection (structureCommRings B S hS X)
      (structureRingSheaf B S hS X).property s) :
    ∃ (D : ClosedSubspaces B S hS X.1) (hD : IsEffectiveCartierDivisor B S hS X D)
      (i : associatedInvertibleSheaf B S hS X D hD ≅ L),
      D = zeroScheme B S hS X L s ∧
      canonicalSectionHom B S hS X D hD ≫ i.hom = L.unitHomEquiv.symm s ∧
      (∀ (D' : ClosedSubspaces B S hS X.1) (hD' : IsEffectiveCartierDivisor B S hS X D')
          (i' : associatedInvertibleSheaf B S hS X D' hD' ≅ L),
        canonicalSectionHom B S hS X D' hD' ≫ i'.hom = L.unitHomEquiv.symm s → D' = D) ∧
      ∀ i' : associatedInvertibleSheaf B S hS X D hD ≅ L,
        canonicalSectionHom B S hS X D hD ≫ i'.hom = L.unitHomEquiv.symm s → i' = i
```

**`AlgebraicGeometry.Space.effectiveCartierDivisor_regularSectionPair_mutuallyInverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartierUnique.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularSectionEffectiveCartierUnique.lean#L221). The attribute's comment: “part (3): the constructions D ↦ (𝒪\_X(D), 1\_D) and (L, s) ↦ Z(s) are mutually inverse, hence a bijection between the effective Cartier divisors and the pairs of an invertible module with a regular global section taken up to isomorphism; with no assumed inputs”.

> **Stacks 0847, part (3).**  The constructions `D ↦ (𝒪_X(D), 1_D)` and `(L, s) ↦ Z(s)` are
> mutually inverse, so they are a bijection between the effective Cartier divisors on `X` and the
> pairs consisting of an invertible `𝒪_X`-module and a regular global section of it, taken up to
> isomorphism of pairs.
>
> The first conjunct is that `D ↦ (𝒪_X(D), 1_D)` lands in such pairs — `𝒪_X(D)` is invertible by
> Stacks 0841 and `1_D` is regular by part (1) — and that the round trip
> `D ↦ (𝒪_X(D), 1_D) ↦ Z(1_D)` is the identity, which is
> `AlgebraicGeometry.Space.zeroScheme_canonicalSection_eq`.  The second is that `(L, s) ↦ Z(s)`
> lands in the effective Cartier divisors and that the round trip
> `(L, s) ↦ Z(s) ↦ (𝒪_X(Z(s)), 1_{Z(s)})` returns `(L, s)` itself: there is an isomorphism
> `𝒪_X(Z(s)) ≅ L` carrying the canonical section to `s`, which is part (2).  The third is that
> `(L, s) ↦ Z(s)` is constant on isomorphism classes of pairs,
> `AlgebraicGeometry.Space.zeroScheme_eq_of_iso`, which is what makes it a map out of them.

```lean
theorem effectiveCartierDivisor_regularSectionPair_mutuallyInverse :
    (∀ (D : ClosedSubspaces B S hS X.1) (hD : IsEffectiveCartierDivisor B S hS X D),
        AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
            (structureRingSheaf B S hS X).property (associatedInvertibleSheaf B S hS X D hD) ∧
          AlgebraicGeometry.IsRegularSection (structureCommRings B S hS X)
            (structureRingSheaf B S hS X).property (canonicalSection B S hS X D hD) ∧
          zeroScheme B S hS X (associatedInvertibleSheaf B S hS X D hD)
            (canonicalSection B S hS X D hD) = D) ∧
      (∀ (L : SheafOfModules.{u} (structureRingSheaf B S hS X)),
        AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS X)
          (structureRingSheaf B S hS X).property L → ∀ (s : L.sections),
        AlgebraicGeometry.IsRegularSection (structureCommRings B S hS X)
          (structureRingSheaf B S hS X).property s →
        ∃ (hZ : IsEffectiveCartierDivisor B S hS X (zeroScheme B S hS X L s))
          (i : associatedInvertibleSheaf B S hS X (zeroScheme B S hS X L s) hZ ≅ L),
          canonicalSectionHom B S hS X (zeroScheme B S hS X L s) hZ ≫ i.hom =
            L.unitHomEquiv.symm s) ∧
      ∀ (L L' : SheafOfModules.{u} (structureRingSheaf B S hS X)) (s : L.sections)
        (s' : L'.sections) (i : L ≅ L'), SheafOfModules.sectionsMap i.hom s = s' →
        zeroScheme B S hS X L s = zeroScheme B S hS X L' s'
```

**`AlgebraicGeometry.Space.zeroScheme_canonicalSection_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeOfCanonicalSection.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeOfCanonicalSection.lean#L335). The attribute's comment: “part (2): the construction D ↦ (𝒪\_X(D), 1\_D) followed by (L, s) ↦ Z(s) is the identity on effective Cartier divisors, with no assumed inputs”.

> **Stacks 0847 (2): an effective Cartier divisor is the zero scheme of its canonical
> section.**  This is the assertion of the source that the construction `D ↦ (𝒪_X(D), 1_D)` followed
> by `(L, s) ↦ Z(s)` is the identity on effective Cartier divisors.
>
> The evaluation ideal of `(𝒪_X(D), 1_D)` of Stacks 0845 is the defining ideal of `D` on every
> affine étale chart, and a closed subspace whose defining ideal is the evaluation ideal on every
> affine chart is the zero scheme, by `AlgebraicGeometry.Space.zeroSchemeSubfunctor_eq`.

```lean
theorem zeroScheme_canonicalSection_eq :
    zeroScheme B S hS X (associatedInvertibleSheaf B S hS X D hD)
        (canonicalSection B S hS X D hD) = D
```

**`AlgebraicGeometry.Space.eq_zeroScheme_of_canonicalSectionHom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeOfCanonicalSection.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZeroSchemeOfCanonicalSection.lean#L396). The attribute's comment: “part (2): uniqueness of the divisor — an effective Cartier divisor with an isomorphism from its associated invertible sheaf to L carrying the canonical section to s is the zero scheme of s, with no assumed inputs”.

> **Stacks 0847 (2): the effective Cartier divisor is unique.**  Let `L` be an `𝒪_X`-module with
> a global section `s`.  An effective Cartier divisor `D ⊆ X` carrying an isomorphism
> `𝒪_X(D) ≅ L` which sends the canonical section `1_D` to `s` is the zero scheme `Z(s)` of
> Stacks 0845 — so there is at most one such divisor.
>
> The isomorphism matches the evaluation ideals of the two pairs, so the defining ideal of `D` is
> the evaluation ideal of `(L, s)` on every affine étale chart, which by
> `AlgebraicGeometry.Space.zeroSchemeSubfunctor_eq` makes `D` the zero scheme.

```lean
theorem eq_zeroScheme_of_canonicalSectionHom_comp
    (L : Modules.{u, u} B S hS X.1 X.2) (s : L.sections)
    (i : associatedInvertibleSheaf B S hS X D hD ≅ L)
    (hi : canonicalSectionHom B S hS X D hD ≫ i.hom = L.unitHomEquiv.symm s) :
    D = zeroScheme B S hS X L s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.7, Tag 0CPG](https://stacks.math.columbia.edu/tag/0CPG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
