---
declaration: section
origin: cited
lean: Crystalline.AffineCrystallineSituation, Crystalline.DividedPowerThickening, Crystalline.DividedPowerThickening.Hom, Crystalline.CrystallineThickening, Crystalline.quotientFunctor, Crystalline.DividedPowerThickening.hasFiniteProducts, Crystalline.DividedPowerThickening.hasProducts_of_charP, Crystalline.hasNonemptyFiniteColimits_dividedPowerThickening
statement: formalized
proof: formalized
---

# 60.5 Affine crystalline site

Section 60.5 of the Stacks Project, [Tag 07HL](https://stacks.math.columbia.edu/tag/07HL). 8 tags here are carried by 33 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07MD, a situation

[Tag 07MD](https://stacks.math.columbia.edu/tag/07MD) in the Stacks Project.

**`Crystalline.AffineCrystallineSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L87).

> **Stacks Project, Tag 07MD.** The standing affine crystalline situation over a divided
> power ring `(A, I, γ)`: the ring `A` is a `ℤ_(p)`-algebra, `I` vanishes in `C`, and `p`
> is nilpotent in `C`.

```lean
public structure AffineCrystallineSituation
```

## Tag 07HM, a definition

[Tag 07HM](https://stacks.math.columbia.edu/tag/07HM) in the Stacks Project.

**`Crystalline.DividedPowerThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L113). The attribute's comment: “divided power thickenings and CRIS(C/A)”.

> **Stacks Project, Tag 07HM, part (1).** A divided power thickening in an affine
> crystalline situation.

```lean
public structure DividedPowerThickening (S : AffineCrystallineSituation.{u, v})
```

**`Crystalline.DividedPowerThickening.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L138). The attribute's comment: “homomorphisms of divided power thickenings”.

> **Stacks Project, Tag 07HM, part (2).** A morphism of divided power thickenings is a
> divided power map over the base whose induced quotient map is compatible with the maps from
> `C`.

```lean
public structure Hom (X Y : DividedPowerThickening.{u, v, w} S)
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L147). The attribute's comment: “category structure on CRIS(C/A)”.

```lean
public instance : Category (DividedPowerThickening.{u, v, w} S)
```

**`Crystalline.CrystallineThickening`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L178). The attribute's comment: “the full subcategory Cris(C/A)”.

> **Stacks Project, Tag 07HM, part (4).** The little crystalline category `Cris(C/A)`,
> the full subcategory of divided power thickenings for which `C → B/J` is an isomorphism.

```lean
public abbrev CrystallineThickening (S : AffineCrystallineSituation.{u, v})
```

## Tag 07KF, an equation

[Tag 07KF](https://stacks.math.columbia.edu/tag/07KF) in the Stacks Project.

**`Crystalline.quotientFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean#L84).

> **Stacks Project, Tag 07KF.** The functor sending a divided power thickening
> `(B, J, δ)` in `CRIS(C/A)` to the `C`-algebra `B/J`.

```lean
public def quotientFunctor (S : AffineCrystallineSituation.{u, v}) :
    DividedPowerThickening.{u, v, w} S ⥤ CommAlgCat.{w, v} S.C
```

## Tag 07HN, a lemma

[Tag 07HN](https://stacks.math.columbia.edu/tag/07HN) in the Stacks Project.

**`Crystalline.DividedPowerThickening.hasFiniteProducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L473). The attribute's comment: “finite\_products”.

> **Stacks Project, Tag 07HN, finite-products part.** The category `CRIS(C/A)` of divided
> power thickenings in an affine crystalline situation has finite products.

```lean
public instance hasFiniteProducts (S : AffineCrystallineSituation.{u, v}) :
    HasFiniteProducts (DividedPowerThickening.{u, v, w} S)
```

**`Crystalline.DividedPowerThickening.hasProducts_of_charP`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite.lean#L503). The attribute's comment: “infinite\_products\_caveat”.

> **Stacks Project, Tag 07HN, infinite-products caveat.** If the base ring has
> characteristic `p`, the category `CRIS(C/A)` has arbitrary products.

```lean
public instance hasProducts_of_charP (S : AffineCrystallineSituation.{u, v}) [CharP S.A S.p] :
    HasProducts.{w} (DividedPowerThickening.{u, v, w} S)
```

**`Crystalline.hasNonemptyFiniteColimits_dividedPowerThickening`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean#L41). The attribute's comment: “cris\_colimits”.

> **Stacks Project, Tag 07HN.** In an affine crystalline situation, the
> category `CRIS(C/A)` has all nonempty finite colimits.

```lean
public instance hasNonemptyFiniteColimits_dividedPowerThickening
    (S : AffineCrystallineSituation.{u, v}) :
    HasNonemptyFiniteColimits
      (DividedPowerThickening.{u, v, w} S)
```

**`Crystalline.preservesColimitsOfShape_quotientFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean#L250). The attribute's comment: “quotient\_preserves\_colimits”.

> **Stacks Project, Tag 07HN.** The quotient functor from `CRIS(C/A)` to
> commutative `C`-algebras preserves all nonempty finite colimits.

```lean
public instance preservesColimitsOfShape_quotientFunctor
    (S : AffineCrystallineSituation.{u, v})
    (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J] :
    PreservesColimitsOfShape J (quotientFunctor.{u, v, w} S)
```

**`Crystalline.DividedPowerThickening.instHasNonemptyFiniteColimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean#L334). The attribute's comment: “little\_cris\_colimits”.

> **Stacks Project, Tag 07HN.** In an affine crystalline situation, the little
> crystalline category `Cris(C/A)` has all finite nonempty colimits.

```lean
public instance instHasNonemptyFiniteColimits
    (S : AffineCrystallineSituation.{u, v}) :
    HasNonemptyFiniteColimits
      (CrystallineThickening.{u, v, w} S)
```

**`Crystalline.preservesColimitsOfShape_crystallineThickeningInclusion`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Colimit/NonemptyFiniteColimits.lean#L352). The attribute's comment: “little\_cris\_inclusion”.

> **Stacks Project, Tag 07HN.** The inclusion `Cris(C/A) ⥤ CRIS(C/A)`
> preserves finite nonempty colimits.

```lean
public instance preservesColimitsOfShape_crystallineThickeningInclusion
    (S : AffineCrystallineSituation.{u, v})
    (J : Type) [SmallCategory J] [FinCategory J] [Nonempty J] :
    PreservesColimitsOfShape J
      ((DividedPowerThickening.IsCrystalline (S := S) :
      ObjectProperty (DividedPowerThickening.{u, v, w} S)).ι)
```

## Tag 07KH, a remark

[Tag 07KH](https://stacks.math.columbia.edu/tag/07KH) in the Stacks Project.

**`Crystalline.CompletedCrystallineThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean#L95). The attribute's comment: “completed\_affine\_crystalline\_site”.

> An object of the completed affine crystalline category `Cris^∧(C/A)`: a divided
> power thickening whose underlying ring is complete for the `p`-adic topology.

```lean
public structure CompletedCrystallineThickening
    (S : AffineCrystallineSituation.{u, v})
```

**`Crystalline.CompletedCrystallineThickening.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean#L119). The attribute's comment: “completed\_affine\_crystalline\_site”.

> A morphism in `Cris^∧(C/A)` is a divided power map over `A` whose induced quotient
> map is compatible with the structural maps from `C`.

```lean
public structure Hom
    (X Y : CompletedCrystallineThickening.{u, v, w} S)
```

**An instance with no name** in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean#L129). The attribute's comment: “completed\_affine\_crystalline\_site”.

> The category structure on the completed affine crystalline category `Cris^∧(C/A)`.

```lean
public instance :
    Category (CompletedCrystallineThickening.{u, v, w} S)
```

**`Crystalline.crystallineEquivalenceNilpotentCompleted`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean#L230). The attribute's comment: “nilpotent\_objects”.

> The ordinary crystalline category is canonically the full subcategory of the
> completed crystalline category consisting of the `p`-nilpotent objects.

```lean
public noncomputable def crystallineEquivalenceNilpotentCompleted
    (S : AffineCrystallineSituation.{u, v}) :
    { E : CrystallineThickening.{u, v, w} S ≌ NilpotentCompleted.{u, v, w} S //
      (∀ X, (E.functor.obj X).1.ring = X.1.ring) ∧
      (∀ X, HEq (E.functor.obj X).1.fromBase X.1.fromBase) ∧
      (∀ X, HEq (E.functor.obj X).1.toQuotient X.1.toQuotient) ∧
      (∀ X Y (f : X ⟶ Y), HEq (E.functor.map f).hom.hom f.hom.hom) }
```

**`Crystalline.exists_finiteLevelSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FiniteLevel.lean#L383). The attribute's comment: “finite\_level\_approximation”.

> A completed crystalline thickening is the inverse limit of its finite-level
> crystalline quotients by powers of `p`.

```lean
public theorem exists_finiteLevelSystem
    (X : CompletedCrystallineThickening.{u, v, w} S) :
    Nonempty (FiniteLevelSystem X)
```

**`Crystalline.completedCrystallineToPro`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FullyFaithful.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FullyFaithful.lean#L569). The attribute's comment: “pro\_objects”.

> The canonical pro-object construction sends each completed thickening to its
> system of sufficiently deep crystalline quotients. On a morphism, its component
> at each finite quotient is induced by a map from a sufficiently deep quotient
> of the source.

```lean
public noncomputable def completedCrystallineToPro
    (S : AffineCrystallineSituation.{u, v}) :
    { F : CompletedCrystallineThickening.{u, v, w} S ⥤
        ProCrystallineThickening.{u, v, w} S //
      ∃ (T : ∀ X, FiniteLevelSystem X)
        (α : ∀ X, (F.obj X).unop.obj ≅
          colimit ((FiniteLevelSystem.diagram (T X)).op ⋙
            yoneda (C := (CrystallineThickening.{u, v, w} S)ᵒᵖ))),
        ∀ (X Y :
          CompletedCrystallineThickening.{u, v, w} S)
          (f : X ⟶ Y) (e : ℕ),
          ∃ (i : ℕ) (g : (T X).term i ⟶ (T Y).term e),
            (g.hom.hom.comp ((T X).projection i) =
              ((T Y).projection e).comp f.hom) ∧
            (colimit.ι ((FiniteLevelSystem.diagram (T Y)).op ⋙
                yoneda (C := (CrystallineThickening.{u, v, w} S)ᵒᵖ)) (op (op e)) ≫
                (α Y).inv ≫ ((F.map f).unop).hom ≫ (α X).hom =
              (yoneda (C := (CrystallineThickening.{u, v, w} S)ᵒᵖ)).map g.op ≫
                colimit.ι ((FiniteLevelSystem.diagram (T X)).op ⋙
                  yoneda (C := (CrystallineThickening.{u, v, w} S)ᵒᵖ))
                  (op (op i))) }
```

**`Crystalline.completedCrystallineToPro_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FullyFaithful.lean, line 634](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/ProObject/FullyFaithful.lean#L634). The attribute's comment: “pro\_objects”.

> Completed crystalline thickenings form a full subcategory of crystalline
> pro-objects under the finite-level quotient construction.

```lean
public theorem completedCrystallineToPro_fullyFaithful
    (S : AffineCrystallineSituation.{u, v}) :
    Nonempty (completedCrystallineToPro.{u, v, w} S).val.FullyFaithful
```

## Tag 07KG, a lemma

[Tag 07KG](https://stacks.math.columbia.edu/tag/07KG) in the Stacks Project.

**`Crystalline.eventually_pAdicIdeal_isSubDPIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean#L392). The attribute's comment: “part (1), envelope”.

> Eventually the powers of `(p)` lie in the envelope ideal and are preserved
> by its divided powers. This is the uncompleted assertion of part (1).

```lean
public theorem eventually_pAdicIdeal_isSubDPIdeal
    (hf : Function.Surjective f) :
    let D := (presentationEnvelope s f).object
    ∃ N : ℕ, ∀ e, N ≤ e →
      (DividedPowers.pAdicIdeal (A := D) s.p ^ e ≤ D.ideal) ∧
        D.dividedPowers.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := D) s.p ^ e)
```

**`Crystalline.eventually_completed_pAdicIdeal_isSubDPIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/Envelope.lean#L410). The attribute's comment: “part (1), completion”.

> The corresponding eventual stability in the completed envelope.

```lean
public theorem eventually_completed_pAdicIdeal_isSubDPIdeal
    (hf : Function.Surjective f) :
    let D := (presentationEnvelope s f).object
    ∃ hp : IsNilpotent (Ideal.Quotient.mk D.ideal (s.p : D)),
      ∃ N : ℕ, ∀ e, N ≤ e →
        let I := DividedPowers.completionIdeal D.ideal s.p hp
        let γ := (DividedPowers.completedDividedPowers D.ideal D.dividedPowers s.p hp).1
        (DividedPowers.pAdicIdeal
            (A := AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D)
          s.p ^ e ≤ I) ∧
          γ.IsSubDPIdeal
            (DividedPowers.pAdicIdeal
              (A := AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D)
              s.p ^ e)
```

**`Crystalline.eventually_quotient_envelope_equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean#L326). The attribute's comment: “part (2), finite-level envelope”.

> At large levels the envelope of the reduced presentation is canonically
> the reduction of the original envelope. The equation on presentation maps
> fixes the isomorphism, and the last condition preserves divided powers.

```lean
public noncomputable def eventually_quotient_envelope_equiv
    (hf : Function.Surjective f) :
    let env := presentationEnvelope s f
    let D := env.object
    Σ' N : ℕ, ∀ e, N ≤ e →
      Σ' hcontained : DividedPowers.pAdicIdeal (A := D) s.p ^ e ≤ D.ideal,
      Σ' hstable : D.dividedPowers.IsSubDPIdeal
          (DividedPowers.pAdicIdeal (A := D) s.p ^ e),
      {φ : (D ⧸ (DividedPowers.pAdicIdeal (A := D) s.p ^ e)) ≃+*
          (levelEnvelope s f e).object //
        (∀ x : P,
          φ (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := D) s.p ^ e)
            (env.algebraMap.toRingHom x)) =
              (levelEnvelope s f e).algebraMap.toRingHom
                (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ e) x)) ∧
          (DividedPowers.quotientDividedPowers D.ideal D.dividedPowers s.p e
            hcontained hstable).IsDPMorphism
              (levelEnvelope s f e).object.dividedPowers φ.toRingHom ∧
          (levelEnvelope s f e).object.dividedPowers.IsDPMorphism
                (DividedPowers.quotientDividedPowers D.ideal D.dividedPowers s.p e
                hcontained hstable) φ.symm.toRingHom}
```

**`Crystalline.eventually_completed_quotient_equiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean#L360). The attribute's comment: “part (2), completion quotient”.

> Completion does not change the finite quotients, compatibly with their
> canonical maps and divided powers. This is the other identification in (2).

```lean
public noncomputable def eventually_completed_quotient_equiv
    (hf : Function.Surjective f) :
    let D := (presentationEnvelope s f).object
    Σ' hp : IsNilpotent (Ideal.Quotient.mk D.ideal (s.p : D)),
      Σ' N : ℕ, ∀ e, N ≤ e →
        Σ' hD : DividedPowers.pAdicIdeal (A := D) s.p ^ e ≤ D.ideal,
        Σ' hDstable : D.dividedPowers.IsSubDPIdeal
            (DividedPowers.pAdicIdeal (A := D) s.p ^ e),
        let Dhat := AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D
        let Ihat := DividedPowers.completionIdeal D.ideal s.p hp
        let γhat := (DividedPowers.completedDividedPowers D.ideal D.dividedPowers s.p hp).1
        Σ' hhat : DividedPowers.pAdicIdeal (A := Dhat) s.p ^ e ≤ Ihat,
        Σ' hhatStable : γhat.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := Dhat) s.p ^ e),
        {φ : (Dhat ⧸ (DividedPowers.pAdicIdeal (A := Dhat) s.p ^ e)) ≃+*
            (D ⧸ (DividedPowers.pAdicIdeal (A := D) s.p ^ e)) //
          (∀ x : D,
            φ (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := Dhat) s.p ^ e)
              (algebraMap D Dhat x)) =
                Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := D) s.p ^ e) x) ∧
            (DividedPowers.quotientDividedPowers Ihat γhat s.p e hhat hhatStable).IsDPMorphism
              (DividedPowers.quotientDividedPowers D.ideal D.dividedPowers s.p e hD hDstable)
                φ.toRingHom ∧
            (DividedPowers.quotientDividedPowers D.ideal D.dividedPowers s.p e hD
                hDstable).IsDPMorphism
            (DividedPowers.quotientDividedPowers Ihat γhat s.p e hhat hhatStable)
                φ.symm.toRingHom}
```

**`Crystalline.levelCrystallineThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/FiniteLevels.lean#L424). The attribute's comment: “part (3)”.

> For large `e`, the finite envelope is a crystalline thickening of `C/A`.

```lean
public noncomputable def levelCrystallineThickening
    (hf : Function.Surjective f) :
    Σ' N : ℕ, ∀ e, N ≤ e →
      {X : DividedPowerThickening.{u, v, u} s //
        DividedPowerThickening.IsCrystalline X ∧
          X.ring = (levelEnvelope s f e).object ∧
          HEq X.fromBase.toRingHom
            (levelEnvelope s f e).structureMap.toRingHom ∧
          ∀ x : P, HEq (X.toQuotient (f x))
            (Ideal.Quotient.mk (levelEnvelope s f e).object.ideal
              ((levelEnvelope s f e).algebraMap.toRingHom
                (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ e) x)))}
```

**`Crystalline.completedEnvelope_isLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean#L52). The attribute's comment: “part (4)”.

> The completed envelope is the inverse limit of the *envelopes* at large
> finite levels. The cone and the transition maps are fixed by the presentation
> maps; the universal property is for compatible divided-power morphisms.

```lean
public noncomputable def completedEnvelope_isLimit
    (hf : Function.Surjective f) :
    let env := presentationEnvelope s f
    let D := env.object
    Σ' hp : IsNilpotent (Ideal.Quotient.mk D.ideal (s.p : D)),
      Σ' N : ℕ,
        Σ' hlevel : ∀ e, N ≤ e →
          (DividedPowers.pAdicIdeal (A := D) s.p ^ e ≤ D.ideal) ∧
            D.dividedPowers.IsSubDPIdeal (DividedPowers.pAdicIdeal (A := D) s.p ^ e),
          let Dhat := AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D
          let δhat := (DividedPowers.completedDividedPowers D.ideal D.dividedPowers s.p hp).1
          Σ' π : ∀ e, N ≤ e → DividedPowers.DPMorphism δhat
                (levelEnvelope s f e).object.dividedPowers,
              Σ' t : ∀ m e, N ≤ m → N ≤ e → m ≤ e →
                  DividedPowers.DPMorphism
                    (levelEnvelope s f e).object.dividedPowers
                    (levelEnvelope s f m).object.dividedPowers,
                DividedPowers.IsDividedPowerCompletionLimit D.ideal D.dividedPowers s.p hp
                    N hlevel ∧
                (∀ e (he : N ≤ e) (x : P),
                  (π e he).toRingHom
                    (algebraMap D Dhat (env.algebraMap.toRingHom x)) =
                      (levelEnvelope s f e).algebraMap.toRingHom
                        (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ e) x)) ∧
                (∀ m e (hm : N ≤ m) (he : N ≤ e) (hme : m ≤ e) (x : P),
                  (t m e hm he hme).toRingHom
                    ((levelEnvelope s f e).algebraMap.toRingHom
                      (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ e) x)) =
                        (levelEnvelope s f m).algebraMap.toRingHom
                          (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ m) x)) ∧
                (∀ m e (hm : N ≤ m) (he : N ≤ e) (hme : m ≤ e),
                  (t m e hm he hme).comp (π e he) = π m hm) ∧
                (∀ e (he : N ≤ e),
                  t e e he he (le_refl e) =
                    DividedPowers.DPMorphism.id
                      (levelEnvelope s f e).object.dividedPowers) ∧
                (∀ l m e (hl : N ≤ l) (hm : N ≤ m) (he : N ≤ e)
                    (hlm : l ≤ m) (hme : m ≤ e),
                  (t l m hl hm hlm).comp (t m e hm he hme) =
                    t l e hl he (hlm.trans hme)) ∧
                (∀ {B : Type w} [CommRing B] (J : Ideal B)
                    (δ : DividedPowers J)
                    (cone : ∀ e, N ≤ e → DividedPowers.DPMorphism δ
                      (levelEnvelope s f e).object.dividedPowers),
                  (∀ m e (hm : N ≤ m) (he : N ≤ e) (hme : m ≤ e),
                    (t m e hm he hme).comp (cone e he) = cone m hm) →
                  ∃! g : DividedPowers.DPMorphism δ δhat,
                    ∀ e (he : N ≤ e), (π e he).comp g = cone e he)
```

**`Crystalline.completedCrystallineThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean#L365). The attribute's comment: “part (5)”.

> The canonical completed divided power envelope is an object of the
> completed affine crystalline site.

```lean
public noncomputable def completedCrystallineThickening
    (hf : Function.Surjective f) :
    let env := presentationEnvelope s f
    let D := env.object
    Σ' hp : IsNilpotent (Ideal.Quotient.mk D.ideal (s.p : D)),
      {X : CompletedCrystallineThickening.{u, v, u} s //
        X.ring = DividedPowerRing.of
          (AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D)
          (DividedPowers.completionIdeal D.ideal s.p hp)
          (DividedPowers.completedDividedPowers D.ideal D.dividedPowers s.p hp).1 ∧
        HEq X.fromBase.toRingHom
          ((algebraMap D (AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D)).comp
            env.structureMap.toRingHom) ∧
        ∀ x : P, HEq (X.toQuotient (f x))
          (Ideal.Quotient.mk (DividedPowers.completionIdeal D.ideal s.p hp)
            (algebraMap D (AdicCompletion (DividedPowers.pAdicIdeal (A := D) s.p) D)
              (env.algebraMap.toRingHom x)))}
```

**`Crystalline.completedLevelEnvelopeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyIdentification.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyIdentification.lean#L297). The attribute's comment: “part (2), the reduction of the completed envelope is the finite-level envelope”.

> **The reduction of the completed envelope is the envelope of the reduced presentation**, as
> divided power rings, compatibly with the maps out of the presentation algebra `P`.
>
> This is the composite of the two halves of [Stacks, Tag 07KG] part (2) already in the tree,
> `Crystalline.eventually_completed_quotient_equiv` and
> `Crystalline.eventually_quotient_envelope_equiv`:
>
> `D̂/(p)^e ≅ D/(p)^e ≅ (levelEnvelope s f e).object`.
>
> Each half is a ring equivalence carrying its divided power compatibilities in both directions and
> its own `Classical.choose` cutoff; the cutoff here is the maximum of the two, and the divided
> power compatibilities compose, so the composite is an isomorphism in `DividedPowerRing` and not
> merely of rings.  The left-hand side is the ring of the level `Crystalline.levelThickening` of the
> completed envelope, by `Crystalline.levelThickening_ring`; the right-hand side is the ring of the
> level `Crystalline.levelCrystallineThickening`.  So this identifies the two families of finite
> levels at the level of their rings, and `Crystalline.levelFamilyIso` promotes it to an isomorphism
> of objects of the site.

```lean
def completedLevelEnvelopeIso (hf : Function.Surjective f) :
    Σ' hp : IsNilpotent (Ideal.Quotient.mk (presentationEnvelope s f).object.ideal
      (s.p : (presentationEnvelope s f).object)),
      Σ' N : ℕ, ∀ e, N ≤ e →
        Σ' h : IsPAdicLevel (completedPresentationEnvelope s f hp).ideal
            (completedPresentationEnvelope s f hp).dividedPowers s.p e,
          {ψ : dpQuotientLevelRing s.p (completedPresentationEnvelope s f hp) e h ≅
                (levelEnvelope s f e).object //
            ∀ x : P,
              (levelProj s.p (completedPresentationEnvelope s f hp) e h ≫ ψ.hom).toRingHom
                  (algebraMap (presentationEnvelope s f).object
                    (completedPresentationEnvelope s f hp)
                    ((presentationEnvelope s f).algebraMap.toRingHom x)) =
                (levelEnvelope s f e).algebraMap.toRingHom
                  (Ideal.Quotient.mk (DividedPowers.pAdicIdeal (A := P) s.p ^ e) x)}
```

## Tag 07HP, a lemma

[Tag 07HP](https://stacks.math.columbia.edu/tag/07HP) in the Stacks Project.

**`Crystalline.exists_forall_le_levelEnvelope_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean#L504). The attribute's comment: “for every sufficiently large level”.

> **Every sufficiently high finite-level divided power envelope maps to a given affine divided
> power thickening.**  The level above which this holds is the larger of the cutoff of
> `Crystalline.levelCrystallineThickening` and the nilpotency exponent of `p` in `B`, and the
> exponent enters the construction only through those two facts: that it is a level, and that
> `(p)^e` vanishes in `B`.
>
> `Crystalline.exists_levelEnvelope_hom` is this at the cutoff itself.  The uniform form is what
> lets the morphism be produced at a level chosen for some other reason — for instance at a level
> past the cutoffs of the two halves of [Stacks, Tag 07KG] part (2), where
> `Crystalline.levelFamilyIso` identifies this family of levels with the finite levels of the
> completed envelope.

```lean
public theorem exists_forall_le_levelEnvelope_hom
    (s : AffineCrystallineSituation.{u, v})
    {P : Type u} [CommRing P] [Algebra s.A P]
    (hP : ∃ (σ : Type u), Nonempty (MvPolynomial σ s.A ≃ₐ[s.A] P))
    (f : P →ₐ[s.A] s.C) (hf : Function.Surjective f)
    (B : DividedPowerThickening.{u, v, u} s) :
    ∃ N : ℕ, ∀ e, N ≤ e →
      ∃ he : (levelCrystallineThickening s f hf).1 ≤ e,
        Nonempty (((levelCrystallineThickening s f hf).2 e he).1 ⟶ B)
```

**`Crystalline.exists_levelEnvelope_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean, line 645](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineSite/Completed/InverseLimit.lean#L645).

> A sufficiently high finite-level divided power envelope maps to any affine
> divided power thickening.

```lean
public theorem exists_levelEnvelope_hom
    (s : AffineCrystallineSituation.{u, v})
    {P : Type u} [CommRing P] [Algebra s.A P]
    (hP : ∃ (σ : Type u), Nonempty (MvPolynomial σ s.A ≃ₐ[s.A] P))
    (f : P →ₐ[s.A] s.C) (hf : Function.Surjective f)
    (B : DividedPowerThickening.{u, v, u} s) :
    ∃ e : ℕ,
      ∃ he : (levelCrystallineThickening s f hf).1 ≤ e,
        Nonempty (((levelCrystallineThickening s f hf).2 e he).1 ⟶ B)
```

**`Crystalline.exists_forall_le_levelThickening_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyFinality.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyFinality.lean#L197). The attribute's comment: “for every sufficiently large finite level of the completed envelope”.

> **[Stacks, Lemma 60.5.6, Tag 07HP] for the finite levels of the completed divided power
> envelope of a polynomial presentation, at every sufficiently large level**: every divided power
> thickening `B` of `C/A` receives a morphism from `D̂/(p)^e` for all large `e`.
>
> `Crystalline.exists_levelThickening_hom` is the same statement at the single object
> `Crystalline.completedCrystallineThickening s q hq` and for a single level.  Both generalisations
> are needed to reach the levels of `...SmallSite.wholeSpaceSystem`, which are the levels of
> `Crystalline.tensorPowerEnvelopeThickening` and not of
> `Crystalline.completedCrystallineThickening`: the object is arbitrary subject to being a
> realisation of the completed envelope of some polynomial presentation, which is what lets the
> *other* presentation `Crystalline.tensorPowerPresentation s q 0` be used, and the level is
> arbitrary subject to being large, which is what lets it be written in the form
> `Crystalline.uniformLevel s + e` the system is indexed by.
>
> The three hypotheses `Crystalline.levelFamilyIso` pins its object down with are three fields of
> `Crystalline.CompletedEnvelopeThickening`, read across the two `rfl`s
> `Crystalline.completedEnvelopeDPRing_eq` and
> `Crystalline.presentationEnvelope_eq_polynomialDividedPowerEnvelope`; so nothing is carried beyond
> surjectivity of the presentation.

```lean
theorem exists_forall_le_levelThickening_hom (W : CompletedEnvelopeThickening s q hq)
    (B : DividedPowerThickening.{u, u, u} s) :
    ∃ N : ℕ, ∀ e, N ≤ e →
      ∃ h : IsPAdicLevel W.thickening.ring.ideal W.thickening.ring.dividedPowers s.p e,
        Nonempty (levelThickeningObj W.thickening e h ⟶ B)
```

**`Crystalline.exists_levelThickening_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyIdentification.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyIdentification.lean#L489). The attribute's comment: “for the finite levels of the completed envelope”.

> **[Stacks, Tag 07HP] for the second family of levels: every divided power thickening of `C/A`
> receives a morphism from a finite level `D̂/(p)^e` of the completed envelope.**
>
> This is the statement the hypothesis `hdet` of
> `...SmallSite.LevelComparison07JG.faithful_functor_of_isLevel` wants, on the family `hdet` is
> stated over: the levels of `...SmallSite.wholeSpaceSystem` are the levels
> `Crystalline.levelThickening` of `Crystalline.tensorPowerEnvelopeThickening`, whose ring is
> `Crystalline.completedPresentationEnvelope` by `Crystalline.completedEnvelopeDPRing_eq`, and not
> the levels `Crystalline.levelCrystallineThickening` that [Stacks, Tag 07HP] produces morphisms out
> of.
>
> Two things are composed.  `Crystalline.exists_forall_le_levelEnvelope_hom` gives the morphism out
> of the first family at *every* sufficiently large level, so a level can be chosen past the cutoffs
> of the two halves of [Stacks, Tag 07KG] part (2) as well; there
> `Crystalline.completedLevelFamilyIso` identifies the two families.  The two proofs that the chosen
> level is past the cutoff of the first family are proofs of the same proposition, so the two levels
> of the first family they name are the same object.
>
> This is stated at the single object `Crystalline.completedCrystallineThickening s f hf`, the
> completed envelope of the presentation `f` itself, and at a single level.  Neither restriction can
> be lifted here, and both have to be for the levels of `...SmallSite.wholeSpaceSystem`, which are
> the levels of `Crystalline.tensorPowerEnvelopeThickening` in degree zero and so belong to a
> *different* presentation.  The generalisation on both counts is
> `Crystalline.exists_forall_le_levelThickening_hom` of
> `StacksFrontier/AlgebraicGeometry/Crystalline/LevelFamilyFinality.lean`, which applies
> `Crystalline.levelFamilyIso` at an arbitrary `Crystalline.CompletedEnvelopeThickening` — three of
> whose fields are its three pinning hypotheses on the nose — and so needs no comparison of the two
> presentations.
>
> This does not by itself discharge `hdet`: that a morphism of crystals is determined by its
> restrictions to the levels needs, beyond a morphism `B ⟶ T_e` for every `B`, the crystal
> property, which is `...SmallSite.moduleRestrictionSheafMap_eq_of_hom` of
> `StacksFrontier/AlgebraicGeometry/Crystalline/LevelCrystalDeterminacy.lean`.

```lean
theorem exists_levelThickening_hom (hf : Function.Surjective f)
    (hP : ∃ σ : Type u, Nonempty (MvPolynomial σ s.A ≃ₐ[s.A] P))
    (B : DividedPowerThickening.{u, u, u} s) :
    ∃ (e : ℕ) (h : IsPAdicLevel ((completedCrystallineThickening s f hf).2.1).ring.ideal
        ((completedCrystallineThickening s f hf).2.1).ring.dividedPowers s.p e),
      Nonempty (levelThickeningObj (completedCrystallineThickening s f hf).2.1 e h ⟶ B)
```

## Tag 07KI, a lemma

[Tag 07KI](https://stacks.math.columbia.edu/tag/07KI) in the Stacks Project.

**`Crystalline.completedPolynomialEnvelopeThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/Basic.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/Basic.lean#L357). The attribute's comment: “the completed crystalline object”.

> The completed divided power envelope of a surjective polynomial presentation,
> as an object of the completed crystalline site. Its underlying divided power
> ring is the canonical completion, not merely an abstract thickening.

```lean
public noncomputable def completedPolynomialEnvelopeThickening
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (hf : Function.Surjective f) :
    {D : CompletedCrystallineThickening.{u, v, max u w} s //
      let env := polynomialDividedPowerEnvelope s f
      let E := env.object
      ∃ hp : IsNilpotent (Ideal.Quotient.mk E.ideal (s.p : E)),
        (D.ring = DividedPowerRing.of
            (pAdicCompletedDividedPowerEnvelope s f hf)
            (DividedPowers.completionIdeal E.ideal s.p hp)
            (DividedPowers.completedDividedPowers E.ideal E.dividedPowers s.p hp).1) ∧
        HEq D.fromBase.toRingHom
          ((algebraMap E (pAdicCompletedDividedPowerEnvelope s f hf)).comp
            env.structureMap.toRingHom) ∧
        HEq (D.toQuotient.comp f.toRingHom)
          ((Ideal.Quotient.mk (DividedPowers.completionIdeal E.ideal s.p hp)).comp
            ((algebraMap E (pAdicCompletedDividedPowerEnvelope s f hf)).comp
              env.algebraMap.toRingHom))}
```

**`Crystalline.exists_hom_from_completedPolynomialEnvelope`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/Basic.lean, line 668](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/AffineCrystallineSite/Basic.lean#L668). The attribute's comment: “existence of a morphism to every completed crystalline object”.

> Every completed crystalline thickening receives a morphism from the
> completed divided power envelope of a surjective polynomial presentation.

```lean
public theorem exists_hom_from_completedPolynomialEnvelope
    (s : AffineCrystallineSituation.{u, v}) {ι : Type w}
    (f : MvPolynomial ι s.A →ₐ[s.A] s.C) (hf : Function.Surjective f)
    (B : CompletedCrystallineThickening.{u, v, x} s) :
    let D := (completedPolynomialEnvelopeThickening s f hf).1
    ∃ g : DividedPowers.DPMorphism D.ring.dividedPowers B.ring.dividedPowers,
      (g.comp D.fromBase = B.fromBase) ∧
        ((Ideal.quotientMap B.ring.ideal g.toRingHom
          (Ideal.map_le_iff_le_comap.mp g.ideal_comp)).comp D.toQuotient =
            B.toQuotient)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.5, Tag 07HL](https://stacks.math.columbia.edu/tag/07HL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
