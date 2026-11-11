---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsBirational, AlgebraicGeometry.IsBirational.isDominant, AlgebraicGeometry.isIso_pullback_snd_fromSpecStalk_of_isBirational, AlgebraicGeometry.localization_isBirational, AlgebraicGeometry.exists_nonzero_away_isUnit_of_isIso_restrict, AlgebraicGeometry.oddIntegers, AlgebraicGeometry.localization_not_isIso_restrict_nonempty, AlgebraicGeometry.PolynomialRetract.retractionMap_comp_inclusionMap
statement: formalized
proof: formalized
---

# 29.51 Birational morphisms

Section 29.51 of the Stacks Project, [Tag 01RN](https://stacks.math.columbia.edu/tag/01RN). 7 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01RO, a definition

[Tag 01RO](https://stacks.math.columbia.edu/tag/01RO) in the Stacks Project.

**`AlgebraicGeometry.IsBirational`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Basic.lean#L67). References: EGA I (2.2.9); EGA IV (6.15.4), “finitely many comps”; EGA I (6.5.5).

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

**`AlgebraicGeometry.IsBirational.isDominant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Dominant.lean#L57). References: EGA I (2.2.9), “more general”.

> A birational morphism of schemes is dominant.

```lean
theorem IsBirational.isDominant {X Y : Scheme.{u}} {f : X ⟶ Y} (hf : IsBirational f) :
    IsDominant f
```

## Tag 0BAB, a lemma

[Tag 0BAB](https://stacks.math.columbia.edu/tag/0BAB) in the Stacks Project.

**`AlgebraicGeometry.isIso_pullback_snd_fromSpecStalk_of_isBirational`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericBaseChange.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericBaseChange.lean#L131).

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

**`AlgebraicGeometry.localization_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L57). The attribute's comment: “localization\_birational”.

> The localization morphism of spectra is birational: both spectra are irreducible with generic
> point the zero ideal, and the local rings there agree.

```lean
theorem localization_isBirational (A : Type u) [CommRing A] [IsDomain A]
    (S : Submonoid A) (hS : (0 : A) ∉ S) :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (algebraMap A (Localization S))).op)
```

**`AlgebraicGeometry.exists_nonzero_away_isUnit_of_isIso_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L80). The attribute's comment: “localization\_open\_criterion”.

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

**`AlgebraicGeometry.oddIntegers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L132). The attribute's comment: “integer\_counterexample”.

> The multiplicative submonoid of odd integers.

```lean
def oddIntegers : Submonoid ℤ
```

**`AlgebraicGeometry.localization_not_isIso_restrict_nonempty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/Localization.lean#L140). The attribute's comment: “integer\_counterexample”.

> The localization of `ℤ` at all odd integers is not an isomorphism over any
> nonempty open of its target.

```lean
theorem localization_not_isIso_restrict_nonempty
    (U : (Scheme.Spec.obj (Opposite.op (CommRingCat.of ℤ))).Opens) (hU : U ≠ ⊥) :
    ¬ IsIso
      ((Scheme.Spec.map
        (CommRingCat.ofHom (algebraMap ℤ (Localization oddIntegers))).op) ∣_ U)
```

**`AlgebraicGeometry.PolynomialRetract.retractionMap_comp_inclusionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean#L97). The attribute's comment: “ring\_maps”.

> Setting every `y_a` to zero is a retraction of the canonical inclusion of `k[x]`.

```lean
theorem retractionMap_comp_inclusionMap :
    (retractionMap k).comp (inclusionMap k) = RingHom.id (baseRing k)
```

**`AlgebraicGeometry.PolynomialRetract.inclusionMap_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetract.lean#L109). The attribute's comment: “ring\_maps”.

> The canonical map from `k[x]` to the quotient ring is injective, being a section of the
> retraction.

```lean
theorem inclusionMap_injective : Function.Injective (inclusionMap k)
```

**`AlgebraicGeometry.PolynomialRetract.inclusionMap_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean#L185). The attribute's comment: “projection\_birational”.

> The canonical inclusion `k[x] → B` induces a birational morphism on spectra.

```lean
theorem inclusionMap_isBirational (k : Type u) [Field k] :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (inclusionMap k)).op)
```

**`AlgebraicGeometry.PolynomialRetract.retraction_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractBirational.lean#L209). The attribute's comment: “section\_birational”.

> The retraction `B → k[x]`, setting every `y_a` to zero, induces a birational morphism on
> spectra: the section `Spec k[x] ⟶ Spec B` is birational.

```lean
theorem retraction_isBirational (k : Type u) [Field k] :
    IsBirational
      (Scheme.Spec.map (CommRingCat.ofHom (retractionMap k)).op)
```

**`AlgebraicGeometry.PolynomialRetract.not_isIso_restrict_specMap_inclusionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean#L59). The attribute's comment: “projection\_not\_iso”.

> The spectrum of the polynomial retract is not isomorphic to the base over
> any nonempty open.

```lean
theorem not_isIso_restrict_specMap_inclusionMap
    (k : Type u) [Field k] [Infinite k]
    (U : (Spec (.of (baseRing k))).Opens) (hU : (U : Set (Spec (.of (baseRing k)))).Nonempty) :
    ¬ IsIso ((Spec.map (CommRingCat.ofHom (inclusionMap k))) ∣_ U)
```

**`AlgebraicGeometry.PolynomialRetract.not_isIso_restrict_specMap_retractionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/Examples/PolynomialRetractNotIso.lean#L119). The attribute's comment: “section\_not\_iso”.

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

**`AlgebraicGeometry.exists_dense_opens_isIso_resLE_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean#L138). The attribute's comment: “dense open isomorphism”.

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

**`AlgebraicGeometry.birationalOver_of_isBirational`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean, line 285](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/DenseOpenIso.lean#L285). The attribute's comment: “over-base consequence”.

> A birational morphism of schemes over a base, under either finiteness hypothesis of the
> theorem, makes the schemes birational over that base.

```lean
public theorem birationalOver_of_isBirational
    {S X Y : Scheme.{u}} (sX : X ⟶ S) (sY : Y ⟶ S) (f : X ⟶ Y)
    [Finite (irreducibleComponents X)] [Finite (irreducibleComponents Y)]
    (hf : IsBirational f) (hfS : f ≫ sY = sX)
    (hfin : (LocallyOfFiniteType f ∧ IsReduced Y) ∨ LocallyOfFinitePresentation f) :
    Scheme.BirationalOver sX sY
```

## Tag 0BAD, a lemma

[Tag 0BAD](https://stacks.math.columbia.edu/tag/0BAD) in the Stacks Project.

**`AlgebraicGeometry.birationalOver_iff_exists_nonempty_open_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean#L113). The attribute's comment: “parts (1) and (2)”.

> For irreducible schemes, birationality over a base is witnessed by an
> isomorphism of nonempty open subschemes over that base.

```lean
public theorem birationalOver_iff_exists_nonempty_open_iso
    {S X Y : Scheme.{u}} (sX : X ⟶ S) (sY : Y ⟶ S)
    [IrreducibleSpace X] [IrreducibleSpace Y] :
    Scheme.BirationalOver sX sY ↔
      ∃ (U : X.Opens) (V : Y.Opens),
        (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
          ∃ e : U.toScheme ≅ V.toScheme,
            e.hom ≫ V.ι ≫ sY = U.ι ≫ sX
```

**`AlgebraicGeometry.birationalOver_iff_generic_stalk_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean#L133). The attribute's comment: “parts (1) and (3)”. References: EGA I (6.5.4), “(ii), special case”.

> For irreducible schemes locally of finite presentation over a base,
> birationality over that base is equivalent to an isomorphism of their generic
> local rings as algebras over the local ring of the common image.

```lean
public theorem birationalOver_iff_generic_stalk_iso
    {S X Y : Scheme.{u}} (sX : X ⟶ S) (sY : Y ⟶ S)
    [IrreducibleSpace X] [IrreducibleSpace Y]
    [LocallyOfFinitePresentation sX] [LocallyOfFinitePresentation sY] :
    Scheme.BirationalOver sX sY ↔
      ∃ (h : sX (genericPoint X) = sY (genericPoint Y))
        (e : X.presheaf.stalk (genericPoint X) ≅
          Y.presheaf.stalk (genericPoint Y)),
          h ▸ (sX.stalkMap (genericPoint X) ≫ e.hom) =
            sY.stalkMap (genericPoint Y)
```

## Tag 0552, a lemma

[Tag 0552](https://stacks.math.columbia.edu/tag/0552) in the Stacks Project.

**`AlgebraicGeometry.birationalOver_tfae_of_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/CommonOpen.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/CommonOpen.lean#L206).

> **Stacks Project, Tag 0552.** For integral schemes locally of finite type over a base,
> birationality over the base, the existence of isomorphic nonempty open subschemes over the
> base, and the existence of an isomorphism of the residue fields at the generic points over the
> base are equivalent.

```lean
public theorem birationalOver_tfae_of_isIntegral {S X Y : Scheme.{u}}
    (sX : X ⟶ S) (sY : Y ⟶ S) [IsIntegral X] [IsIntegral Y]
    [LocallyOfFiniteType sX] [LocallyOfFiniteType sY] :
    List.TFAE
      [Scheme.BirationalOver sX sY,
        ∃ (U : X.Opens) (V : Y.Opens), (U : Set X).Nonempty ∧ (V : Set Y).Nonempty ∧
          ∃ e : U.toScheme ≅ V.toScheme, e.hom ≫ V.ι ≫ sY = U.ι ≫ sX,
        ∃ (h : sX (genericPoint X) = sY (genericPoint Y))
          (e : X.residueField (genericPoint X) ≅ Y.residueField (genericPoint Y)),
          h ▸ (sX.residueFieldMap (genericPoint X) ≫ e.hom) =
            sY.residueFieldMap (genericPoint Y)]
```

**`AlgebraicGeometry.birationalOver_iff_generic_residueField_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GeometricallyIntegral/BirationalResidueField.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/BirationalResidueField.lean#L75). The attribute's comment: “parts (1) and (3)”.

> **Stacks 0552, parts (1) and (3).** Birationality over a base of two integral schemes
> locally of finite type over it is equivalent to their generic points having the same image in
> the base together with an isomorphism of their residue fields at those generic points over the
> residue field of that common image.

```lean
theorem birationalOver_iff_generic_residueField_iso
    {S X Y : Scheme.{u}} (sX : X ⟶ S) (sY : Y ⟶ S)
    [IsIntegral X] [IsIntegral Y]
    [LocallyOfFiniteType sX] [LocallyOfFiniteType sY] :
    Scheme.BirationalOver sX sY ↔
      ∃ (h : sX (genericPoint X) = sY (genericPoint Y))
        (e : X.residueField (genericPoint X) ≅ Y.residueField (genericPoint Y)),
        h ▸ (sX.residueFieldMap (genericPoint X) ≫ e.hom) =
          sY.residueFieldMap (genericPoint Y)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.birationalOver_iff_exists_nonempty_open_iso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Birational/GenericStalkCriterion.lean#L113), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/GeometricallyIntegral/BirationalResidueField.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GeometricallyIntegral/BirationalResidueField.lean#L163) (StacksFrontier): “parts (1) and (2)”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.51, Tag 01RN](https://stacks.math.columbia.edu/tag/01RN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
