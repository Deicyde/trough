---
declaration: section
origin: cited
lean: AlgebraicGeometry.separableDegreeWeightedFiberSum_comp_of_isPullback, AlgebraicGeometry.IsWeighting, AlgebraicGeometry.IsWeighting.comp_of_isPullback, AlgebraicGeometry.IsWeighting.comp_isOpenImmersion, AlgebraicGeometry.IsWeighting.mul_comp, AlgebraicGeometry.universallyOpen_of_positive_weighting, AlgebraicGeometry.flatQuasiFiniteWeight, AlgebraicGeometry.flatQuasiFiniteWeight_pos
statement: formalized
proof: formalized
---

# 37.75 Weightings

Section 37.75 of the Stacks Project, [Tag 0F38](https://stacks.math.columbia.edu/tag/0F38). 8 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F39, a lemma

[Tag 0F39](https://stacks.math.columbia.edu/tag/0F39) in the Stacks Project.

**`AlgebraicGeometry.separableDegreeWeightedFiberSum_comp_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/WeightedFibreSum.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/WeightedFibreSum.lean#L392).

> Weighted fibre sums by separable residue degrees commute with cartesian
> base change.

```lean
theorem separableDegreeWeightedFiberSum_comp_of_isPullback
    {U U' V V' : Scheme.{u}} (f : U ⟶ V) (h : U' ⟶ U)
    (f' : U' ⟶ V') (g : V' ⟶ V) (sq : IsPullback h f' f g)
    [LocallyQuasiFinite f] (hfinite : ∀ v, (f ⁻¹' {v}).Finite) (w : U → ℤ) :
    separableDegreeWeightedFiberSum f w ∘ g =
      separableDegreeWeightedFiberSum f' (w ∘ h)
```

## Tag 0F3A, a definition

[Tag 0F3A](https://stacks.math.columbia.edu/tag/0F3A) in the Stacks Project.

**`AlgebraicGeometry.IsWeighting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Weighting.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Weighting.lean#L56). References: SGA 4 XVII (6.2.4), “condition (*)”.

> An integer-valued function `w` on `X` is a weighting of `f : X ⟶ Y` if its
> separable-degree weighted fibre sum is locally constant on every finite open
> piece of every étale base change of `f`.

```lean
def IsWeighting {X Y : Scheme.{u}} (f : X ⟶ Y) (w : X → ℤ) : Prop
```

## Tag 0F3B, a lemma

[Tag 0F3B](https://stacks.math.columbia.edu/tag/0F3B) in the Stacks Project.

**`AlgebraicGeometry.IsWeighting.comp_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/BaseChange.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/BaseChange.lean#L619). References: SGA 4 XVII (6.2.4), “base change”.

> A weighting pulls back to a weighting along an arbitrary base change.

```lean
theorem IsWeighting.comp_of_isPullback {X Y X' Y' : Scheme.{u}}
    {f : X ⟶ Y} {p : X' ⟶ X} {f' : X' ⟶ Y'} {g : Y' ⟶ Y}
    {w : X → ℤ} (hw : IsWeighting f w)
    (sq : IsPullback p f' f g) [LocallyOfFiniteType f] [LocallyQuasiFinite f] :
    IsWeighting f' (w ∘ p)
```

## Tag 0GK8, a lemma

[Tag 0GK8](https://stacks.math.columbia.edu/tag/0GK8) in the Stacks Project.

**`AlgebraicGeometry.IsWeighting.comp_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Weighting.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/WeaklyEtale/Weighting.lean#L79).

> The restriction of a weighting to an open subscheme of the source is a
> weighting of the restricted morphism.

```lean
theorem IsWeighting.comp_isOpenImmersion {X' X Y : Scheme.{u}}
    (j : X' ⟶ X) [IsOpenImmersion j] {f : X ⟶ Y} {w : X → ℤ}
    (hw : IsWeighting f w) : IsWeighting (j ≫ f) (w ∘ j)
```

## Tag 0GK9, a lemma

[Tag 0GK9](https://stacks.math.columbia.edu/tag/0GK9) in the Stacks Project.

**`AlgebraicGeometry.IsWeighting.mul_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Composition.lean, line 827](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/Composition.lean#L827). References: SGA 4 XVII (6.2.4), “composite”.

> The pointwise product of a weighting of `f` and the pullback of a weighting
> of `g` is a weighting of `f ≫ g`.

```lean
theorem IsWeighting.mul_comp {X Y Z : Scheme.{u}}
    {f : X ⟶ Y} {g : Y ⟶ Z}
    [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    [LocallyOfFiniteType g] [LocallyQuasiFinite g]
    {w_f : X → ℤ} {w_g : Y → ℤ}
    (hw_f : IsWeighting f w_f)
    (hw_g : IsWeighting g w_g) :
    IsWeighting (f ≫ g) (fun x ↦ w_f x * w_g (f x))
```

## Tag 0F3C, a lemma

[Tag 0F3C](https://stacks.math.columbia.edu/tag/0F3C) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_positive_weighting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/UniversallyOpen.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/UniversallyOpen.lean#L126).

> **Stacks Project, Tag 0F3C.** A locally quasi-finite morphism carrying an everywhere
> positive weighting is universally open.

```lean
theorem universallyOpen_of_positive_weighting {X Y : Scheme.{u}}
    {f : X ⟶ Y} [LocallyOfFiniteType f] [LocallyQuasiFinite f]
    {w : X → ℤ} (hw : IsWeighting f w) (hpositive : ∀ x : X, 0 < w x) :
    UniversallyOpen f
```

## Tag 0F3D, a lemma

[Tag 0F3D](https://stacks.math.columbia.edu/tag/0F3D) in the Stacks Project.

**`AlgebraicGeometry.flatQuasiFiniteWeight`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean, line 960](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L960). The attribute's comment: “the formula”.

> The local-fibre length times the inseparable degree of the residue-field
> extension at a point of a scheme morphism.

```lean
noncomputable def flatQuasiFiniteWeight {X Y : Scheme.{u}} (f : X ⟶ Y) : X → ℤ
```

**`AlgebraicGeometry.flatQuasiFiniteWeight_pos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean, line 1070](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L1070). The attribute's comment: “positivity”.

> The canonical local-fibre weighting is strictly positive.

```lean
theorem flatQuasiFiniteWeight_pos {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyQuasiFinite f] [LocallyOfFinitePresentation f] [Flat f]
    (x : X) : 0 < flatQuasiFiniteWeight f x
```

**`AlgebraicGeometry.flatQuasiFiniteWeight_isWeighting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean, line 1097](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLength.lean#L1097). The attribute's comment: “weighting”.

> The canonical local-fibre function is a weighting.

```lean
theorem flatQuasiFiniteWeight_isWeighting {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyQuasiFinite f] [LocallyOfFinitePresentation f] [Flat f] :
    IsWeighting f (flatQuasiFiniteWeight f)
```

**`AlgebraicGeometry.flatQuasiFiniteWeight_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLengthBaseChange.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/FlatLengthBaseChange.lean#L203). The attribute's comment: “base-change invariance of the function of the formula”.

> **Stacks Project, Example 0GKI, final claim.** Let `f : X ⟶ Y` be flat, locally quasi-finite
> and locally of finite presentation and let `f' : X' ⟶ Y'` be a base change of `f` along
> `g : Y' ⟶ Y`, with `p : X' ⟶ X` the projection. Then the canonical weighting of `f'` is the
> restriction along `p` of the canonical weighting of `f`.
>
> The weight at a point is the length of the local ring of the scheme-theoretic fibre through it
> times the inseparable degree of the residue field extension. The comparison morphism of fibres
> `N` is flat, so Tag `02M1` splits the length upstairs as the length downstairs times the length
> of the local ring of the fibre of `N`, and
> `Stacks.Chow.length_fiberStalk_mul_finInsepDegree_of_isPullback` trades that last length against
> the two inseparable degrees.

```lean
theorem flatQuasiFiniteWeight_of_isPullback {X Y X' Y' : Scheme.{u}} (f : X ⟶ Y)
    {p : X' ⟶ X} {f' : X' ⟶ Y'} {g : Y' ⟶ Y} (sq : IsPullback p f' f g)
    [LocallyQuasiFinite f] [LocallyOfFinitePresentation f] [Flat f] :
    flatQuasiFiniteWeight f' = flatQuasiFiniteWeight f ∘ p
```

## Tag 0F3E, a lemma

[Tag 0F3E](https://stacks.math.columbia.edu/tag/0F3E) in the Stacks Project.

**`AlgebraicGeometry.exists_weighting_genericSeparableDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/GenericSeparableDegree/Weighting.lean, line 441](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/Weighting/GenericSeparableDegree/Weighting.lean#L441). References: SGA 4 XVII (6.2.6), “n(x) is a weighting”.

> **The generic-separable-degree weighting.** For `f : X ⟶ Y` locally quasi-finite and locally of
> finite type over a geometrically unibranch locally Noetherian scheme `Y`, there is a weighting
> `w` of `f` whose value at `x` is, for all compatible strict henselizations `Rsh` of `𝒪_{Y,f(x)}`
> and `Ssh` of `𝒪_{X,x}`, every minimal prime `p` of `Rsh` and every algebraic closure `Kbar` of
> `κ(p)`, the number of `κ(p)`-algebra maps `κ(p) ⊗[Rsh] Ssh → Kbar`.

```lean
public theorem exists_weighting_genericSeparableDegree
    {X Y : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    [LocallyQuasiFinite f] [IsLocallyNoetherian Y]
    (hY : IsGeometricallyUnibranch Y) :
    ∃ w : X → ℕ,
      IsWeighting f (fun x ↦ (w x : ℤ)) ∧
      ∀ (x : X)
        (κY : Type u) [Field κY]
        [Algebra (maximalIdeal (Y.presheaf.stalk (f x))).ResidueField κY]
        [IsSepClosure (maximalIdeal (Y.presheaf.stalk (f x))).ResidueField κY]
        (Rsh : Type u) [CommRing Rsh] [IsLocalRing Rsh]
        [Algebra (Y.presheaf.stalk (f x)) Rsh]
        (_hRsh : Stacks.StrictHenselization.IsStrictHenselization
          (Y.presheaf.stalk (f x)) κY Rsh)
        (κX : Type u) [Field κX]
        [Algebra (maximalIdeal (X.presheaf.stalk x)).ResidueField κX]
        [IsSepClosure (maximalIdeal (X.presheaf.stalk x)).ResidueField κX]
        (Ssh : Type u) [CommRing Ssh] [IsLocalRing Ssh]
        [Algebra (X.presheaf.stalk x) Ssh] [Algebra Rsh Ssh]
        [Algebra (Y.presheaf.stalk (f x)) Ssh]
        [IsScalarTower (Y.presheaf.stalk (f x)) Rsh Ssh]
        (_hSsh : Stacks.StrictHenselization.IsStrictHenselization
          (X.presheaf.stalk x) κX Ssh)
        (_hcomp : (algebraMap (Y.presheaf.stalk (f x)) Ssh) =
          (algebraMap (X.presheaf.stalk x) Ssh).comp (f.stalkMap x).hom)
        (p : Ideal Rsh) [p.IsPrime] (_hp : p ∈ minimalPrimes Rsh)
        (Kbar : Type u) [Field Kbar]
        [Algebra p.ResidueField Kbar] [IsAlgClosure p.ResidueField Kbar],
        w x = Nat.card (AlgHom p.ResidueField
          (TensorProduct Rsh p.ResidueField Ssh) Kbar)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.75, Tag 0F38](https://stacks.math.columbia.edu/tag/0F38)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
