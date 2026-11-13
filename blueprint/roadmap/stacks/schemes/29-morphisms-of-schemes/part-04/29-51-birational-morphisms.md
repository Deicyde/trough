---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsBirational, AlgebraicGeometry.IsBirational.isDominant, AlgebraicGeometry.isIso_pullback_snd_fromSpecStalk_of_isBirational, AlgebraicGeometry.localization_isBirational, AlgebraicGeometry.exists_nonzero_away_isUnit_of_isIso_restrict, AlgebraicGeometry.oddIntegers, AlgebraicGeometry.localization_not_isIso_restrict_nonempty, AlgebraicGeometry.PolynomialRetract.retractionMap_comp_inclusionMap
statement: formalized
proof: formalized
---

# 29.51 Birational morphisms

Section 29.51 of the Stacks Project, [Tag 01RN](https://stacks.math.columbia.edu/tag/01RN). 7 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01RO, a definition

[Tag 01RO](https://stacks.math.columbia.edu/tag/01RO) in the Stacks Project.

**`AlgebraicGeometry.IsBirational`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean#L62). References: EGA I (2.2.9); EGA IV (6.15.4), “finitely many comps”; EGA I (6.5.5).

> A morphism of schemes is **birational** if it induces a bijection on the generic points of
> irreducible components and an isomorphism on the local rings at every such point of its source.
>
> This definition is meaningful without the finiteness hypotheses on the sets of irreducible
> components imposed in [Stacks Project, Tag 01RO].

```lean
def IsBirational {X Y : Scheme.{u}} (f : X ⟶ Y) : Prop
```

## Tag 01RP, a lemma

[Tag 01RP](https://stacks.math.columbia.edu/tag/01RP) in the Stacks Project.

**`AlgebraicGeometry.IsBirational.isDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean#L57). References: EGA I (2.2.9), “more general”.

> A birational morphism of schemes is dominant.

```lean
theorem IsBirational.isDominant {X Y : Scheme.{u}} {f : X ⟶ Y} (hf : IsBirational f) :
    IsDominant f
```

## Tag 0BAB, a lemma

[Tag 0BAB](https://stacks.math.columbia.edu/tag/0BAB) in the Stacks Project.

**`AlgebraicGeometry.isIso_pullback_snd_fromSpecStalk_of_isBirational`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericBaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericBaseChange.lean#L131).

> The base change of a birational morphism to the spectrum of the local ring at a generic
> point of an irreducible component of the target is an isomorphism.

```lean
lemma isIso_pullback_snd_fromSpecStalk_of_isBirational
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Finite (irreducibleComponents X)] [Finite (irreducibleComponents Y)]
    (hf : IsBirational f) (y : Y) (hy : y ∈ genericPoints Y) :
    IsIso (pullback.snd f (Y.fromSpecStalk y))
```

## Tag 01RQ, an example

[Tag 01RQ](https://stacks.math.columbia.edu/tag/01RQ) in the Stacks Project.

**`AlgebraicGeometry.localization_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L57). The attribute's comment: “localization\_birational”.

> The localization morphism of spectra is birational: both spectra are irreducible with generic
> point the zero ideal, and the local rings there agree.

```lean
theorem localization_isBirational (A : Type u) [CommRing A] [IsDomain A]
    (S : Submonoid A) (hS : (0 : A) ∉ S) :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (Localization S))).op)
```

**`AlgebraicGeometry.exists_nonzero_away_isUnit_of_isIso_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L80). The attribute's comment: “localization\_open\_criterion”.

> If the localization morphism is an isomorphism over a nonempty open, then every denominator
> already becomes a unit on some nonempty principal open.

```lean
theorem exists_nonzero_away_isUnit_of_isIso_restrict
    (A : Type u) [CommRing A] [IsDomain A]
    (S : Submonoid A) (_hS : (0 : A) ∉ S)
    (U : (Spec (CommRingCat.of A)).Opens)
    (hU : Set.Nonempty (U : Set (Spec (CommRingCat.of A))))
    (hiso : IsIso
      ((Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (Localization S))).op) ∣_ U)) :
    ∃ a : A, a ≠ 0 ∧ ∀ s : S, IsUnit (algebraMap A (Localization.Away a) s.1)
```

**`AlgebraicGeometry.oddIntegers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L132). The attribute's comment: “integer\_counterexample”.

> The multiplicative submonoid of odd integers.

```lean
def oddIntegers : Submonoid ℤ
```

**`AlgebraicGeometry.localization_not_isIso_restrict_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L140). The attribute's comment: “integer\_counterexample”.

> The localization of `ℤ` at all odd integers is not an isomorphism over any
> nonempty open of its target.

```lean
theorem localization_not_isIso_restrict_nonempty
    (U : (Scheme.Spec.obj (Opposite.op (CommRingCat.of ℤ))).Opens) (hU : U ≠ ⊥) :
    ¬ IsIso
      ((Scheme.Spec.map
        (CommRingCat.ofHom (algebraMap ℤ (Localization oddIntegers))).op) ∣_ U)
```

**`AlgebraicGeometry.PolynomialRetract.retractionMap_comp_inclusionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean#L97). The attribute's comment: “ring\_maps”.

> Setting every `y_a` to zero is a retraction of the canonical inclusion of `k[x]`.

```lean
theorem retractionMap_comp_inclusionMap :
    (retractionMap k).comp (inclusionMap k) = RingHom.id (baseRing k)
```

**`AlgebraicGeometry.PolynomialRetract.inclusionMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean#L109). The attribute's comment: “ring\_maps”.

> The canonical map from `k[x]` to the quotient ring is injective, being a section of the
> retraction.

```lean
theorem inclusionMap_injective : Function.Injective (inclusionMap k)
```

**`AlgebraicGeometry.PolynomialRetract.inclusionMap_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean#L185). The attribute's comment: “projection\_birational”.

> The canonical inclusion `k[x] → B` induces a birational morphism on spectra.

```lean
theorem inclusionMap_isBirational (k : Type u) [Field k] :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (inclusionMap k)).op)
```

**`AlgebraicGeometry.PolynomialRetract.retraction_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean#L209). The attribute's comment: “section\_birational”.

> The retraction `B → k[x]`, setting every `y_a` to zero, induces a birational morphism on
> spectra: the section `Spec k[x] ⟶ Spec B` is birational.

```lean
theorem retraction_isBirational (k : Type u) [Field k] :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (retractionMap k)).op)
```

**`AlgebraicGeometry.PolynomialRetract.not_isIso_restrict_specMap_inclusionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean#L59). The attribute's comment: “projection\_not\_iso”.

> The spectrum of the polynomial retract is not isomorphic to the base over
> any nonempty open.

```lean
theorem not_isIso_restrict_specMap_inclusionMap
    (k : Type u) [Field k] [Infinite k]
    (U : (Spec (.of (baseRing k))).Opens) (hU : (U : Set (Spec (.of (baseRing k)))).Nonempty) :
    ¬ IsIso ((Spec.map (CommRingCat.ofHom (inclusionMap k))) ∣_ U)
```

**`AlgebraicGeometry.PolynomialRetract.not_isIso_restrict_specMap_retractionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean#L119). The attribute's comment: “section\_not\_iso”.

> The section induced by the polynomial-ring retraction is not an isomorphism
> over any nonempty open of the target.

```lean
theorem not_isIso_restrict_specMap_retractionMap
    (k : Type u) [Field k] [Infinite k]
    (U : (Spec (.of (extensionRing k))).Opens)
    (hU : (U : Set (Spec (.of (extensionRing k)))).Nonempty) :
    ¬ IsIso ((Spec.map (CommRingCat.ofHom (retractionMap k))) ∣_ U)
```

## Tag 0BAC, a lemma

[Tag 0BAC](https://stacks.math.columbia.edu/tag/0BAC) in the Stacks Project.

**`AlgebraicGeometry.exists_dense_opens_isIso_resLE_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean#L142). The attribute's comment: “dense open isomorphism”.

> A birational morphism between schemes with finitely many irreducible components is an
> isomorphism between dense open subschemes, provided that it is locally of finite type with reduced
> target or locally of finite presentation.

```lean
public theorem exists_dense_opens_isIso_resLE_of_isBirational
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Finite (irreducibleComponents X)] [Finite (irreducibleComponents Y)]
    (hf : IsBirational f)
    (hfin : (LocallyOfFiniteType f ∧ IsReduced Y) ∨ LocallyOfFinitePresentation f) :
    ∃ (U : X.Opens) (V : Y.Opens) (hUV : U ≤ f ⁻¹ᵁ V),
      Dense (U : Set X) ∧ Dense (V : Set Y) ∧ IsIso (f.resLE V U hUV)
```

**`AlgebraicGeometry.Scheme.dominantBirationalOver_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DominantRationalMaps.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DominantRationalMaps.lean#L258). The attribute's comment: “in particular: irreducible X, Y are S-birational in the sense of 0A20”.

> **Stacks 0BAC**, the final assertion: a birational morphism `f : X ⟶ Y` over `S` between
> irreducible schemes, locally of finite type with `Y` reduced or locally of finite presentation,
> makes `X` and `Y` `S`-birational in the sense of [Stacks, Tag 0A20] (2), i.e. isomorphic in the
> category of irreducible schemes over `S` and dominant `S`-rational maps.

```lean
theorem dominantBirationalOver_of_isBirational [X.Over S] [Y.Over S] (f : X ⟶ Y) [f.IsOver S]
    [Finite (irreducibleComponents X)] [Finite (irreducibleComponents Y)]
    [IrreducibleSpace X] [IrreducibleSpace Y] (hf : IsBirational f)
    (hfin : (LocallyOfFiniteType f ∧ IsReduced Y) ∨ LocallyOfFinitePresentation f) :
    DominantBirationalOver S X Y
```

## Tag 0BAD, a lemma

[Tag 0BAD](https://stacks.math.columbia.edu/tag/0BAD) in the Stacks Project.

**`AlgebraicGeometry.Scheme.dominantBirationalOver_tfae_generic_stalk_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterionDominant.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterionDominant.lean#L54). The attribute's comment: “Conditions (1), (2) and (3) of the lemma, with (1) the `S`-birationality of Tag 0A20.”.

> For irreducible schemes `X` and `Y` locally of finite presentation over `S`, with generic
> points `x` and `y`, the following are equivalent: `X` and `Y` are `S`-birational (isomorphic in
> the category of irreducible schemes over `S` and dominant `S`-rational maps); there are nonempty
> opens of `X` and `Y` which are isomorphic over `S`; `x` and `y` map to the same point `s` of `S`
> and the local rings `𝒪_{X, x}` and `𝒪_{Y, y}` are isomorphic as `𝒪_{S, s}`-algebras.

```lean
theorem dominantBirationalOver_tfae_generic_stalk_iso {S X Y : Scheme.{u}} [X.Over S] [Y.Over S]
    [IrreducibleSpace X] [IrreducibleSpace Y]
    [LocallyOfFinitePresentation (X ↘ S)] [LocallyOfFinitePresentation (Y ↘ S)] :
    List.TFAE
      [DominantBirationalOver S X Y,
        ∃ (U : X.Opens) (V : Y.Opens),
          (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
            ∃ e : U.toScheme ≅ V.toScheme, e.hom ≫ V.ι ≫ Y ↘ S = U.ι ≫ X ↘ S,
        ∃ (h : (X ↘ S) (genericPoint X) = (Y ↘ S) (genericPoint Y))
          (e : X.presheaf.stalk (genericPoint X) ≅ Y.presheaf.stalk (genericPoint Y)),
            h ▸ ((X ↘ S).stalkMap (genericPoint X) ≫ e.hom) =
              (Y ↘ S).stalkMap (genericPoint Y)]
```

## Tag 0552, a lemma

[Tag 0552](https://stacks.math.columbia.edu/tag/0552) in the Stacks Project.

**`AlgebraicGeometry.tfae_dominantBirationalOver_residueField_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/ResidueFieldCriterion.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/ResidueFieldCriterion.lean#L50).

> **Stacks 0552.** Let `X` and `Y` be integral schemes locally of finite type over `S`, with
> generic points `x` and `y`. The following are equivalent: (1) `X` and `Y` are `S`-birational,
> that is, isomorphic in the category of irreducible schemes over `S` and dominant `S`-rational
> maps; (2) there are nonempty opens of `X` and `Y` which are `S`-isomorphic; (3) `x` and `y` map
> to the same point `s` of `S` and `κ(x) ≅ κ(y)` as extensions of `κ(s)`.

```lean
theorem tfae_dominantBirationalOver_residueField_genericPoint
    {S X Y : Scheme.{u}} [X.Over S] [Y.Over S]
    [IsIntegral X] [IsIntegral Y]
    [LocallyOfFiniteType (X ↘ S)] [LocallyOfFiniteType (Y ↘ S)] :
    List.TFAE
      [Scheme.DominantBirationalOver S X Y,
        ∃ (U : X.Opens) (V : Y.Opens),
          (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
            ∃ e : U.toScheme ≅ V.toScheme, e.hom ≫ V.ι ≫ Y ↘ S = U.ι ≫ X ↘ S,
        ∃ (h : (X ↘ S) (genericPoint X) = (Y ↘ S) (genericPoint Y))
          (e : X.residueField (genericPoint X) ≅ Y.residueField (genericPoint Y)),
          h ▸ ((X ↘ S).residueFieldMap (genericPoint X) ≫ e.hom) =
            (Y ↘ S).residueFieldMap (genericPoint Y)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.51, Tag 01RN](https://stacks.math.columbia.edu/tag/01RN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
