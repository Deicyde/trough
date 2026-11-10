---
declaration: section
origin: cited
lean: RingHom.StacksPropertyIsLocal, RingHom.IsStableUnderBaseChange, RingHom.StableUnderComposition, AlgebraicGeometry.locallyOfType, AlgebraicGeometry.appLE_of_locallyOfType, AlgebraicGeometry.locallyOfType_resLE, AlgebraicGeometry.locallyOfType_tfae, AlgebraicGeometry.locallyOfType_tfae_and_resLE
statement: formalized
proof: formalized
---

# 29.14 Types of morphisms defined by properties of ring maps

Section 29.14 of the Stacks Project, [Tag 01SQ](https://stacks.math.columbia.edu/tag/01SQ). 9 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01SR, a definition

[Tag 01SR](https://stacks.math.columbia.edu/tag/01SR) in the Stacks Project.

**`RingHom.StacksPropertyIsLocal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean#L71). The attribute's comment: “(1) local, all three conditions (a), (b), (c)”.

> A property of commutative-ring homomorphisms is local if it is preserved
> by simultaneous principal localization, passes from a map `R_f → A` to the
> composite `R → A_a`, and can be checked on a finite principal open cover of
> the target.

```lean
structure StacksPropertyIsLocal
    (P : ∀ {R S : Type u} [CommRing R] [CommRing S], (R →+* S) → Prop) : Prop
```

Declarations registered for the tag:

- [`RingHom.IsStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.IsStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean#L100) (StacksFrontier): “(2) stable under base change, in the pushout formulation”.
- [`RingHom.StableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.StableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean#L102) (StacksFrontier): “(3) stable under composition”.

## Tag 01SS, a definition

[Tag 01SS](https://stacks.math.columbia.edu/tag/01SS) in the Stacks Project.

**`AlgebraicGeometry.locallyOfType`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/Defs.lean#L109).

> A morphism of schemes is locally of type `P` if every point of its source lies in
> an affine open mapping into an affine open of the target on whose rings of sections
> the induced homomorphism satisfies `P`.

```lean
abbrev locallyOfType (P : ∀ {R S : Type u} [CommRing R] [CommRing S],
    (R →+* S) → Prop) : MorphismProperty Scheme.{u}
```

## Tag 01ST, a lemma

[Tag 01ST](https://stacks.math.columbia.edu/tag/01ST) in the Stacks Project.

**`AlgebraicGeometry.appLE_of_locallyOfType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L149).

> If `f` is locally of type `P` for a local property `P`, then `P` holds for the ring map
> `𝒪_S(V) → 𝒪_X(U)` of any affine opens `U ⊆ X`, `V ⊆ S` with `f(U) ⊆ V`.

```lean
theorem appLE_of_locallyOfType (hP : RingHom.StacksPropertyIsLocal P) {f : X ⟶ S}
    (hf : locallyOfType P f) (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1) :
    P (f.appLE V U e).hom
```

## Tag 01SU, a lemma

[Tag 01SU](https://stacks.math.columbia.edu/tag/01SU) in the Stacks Project.

**`AlgebraicGeometry.locallyOfType_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L158). The attribute's comment: “moreover: restriction to open subschemes”.

> If `f` is locally of type `P` for a local property `P`, then so is its restriction
> `U → V` to any opens `U ⊆ X`, `V ⊆ S` with `f(U) ⊆ V`.

```lean
theorem locallyOfType_resLE (hP : RingHom.StacksPropertyIsLocal P) {f : X ⟶ S}
    (hf : locallyOfType P f) (V : S.Opens) (U : X.Opens) (e : U ≤ f ⁻¹ᵁ V) :
    locallyOfType P (f.resLE V U e)
```

**`AlgebraicGeometry.locallyOfType_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L167). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> For a local property `P`, being locally of type `P` can be checked on all pairs of affine
> opens, on open coverings of target and preimages, or on affine such coverings.

```lean
theorem locallyOfType_tfae (hP : RingHom.StacksPropertyIsLocal P) (f : X ⟶ S) :
    List.TFAE [
      locallyOfType P f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1), P (f.appLE V U e).hom,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, locallyOfType P (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1, P (f.appLE V U e).hom]
```

**`AlgebraicGeometry.locallyOfType_tfae_and_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L226).

> The whole statement: for a local property `P`, the four characterizations of being locally
> of type `P` agree, and being locally of type `P` passes to restrictions to open subschemes.

```lean
theorem locallyOfType_tfae_and_resLE (hP : RingHom.StacksPropertyIsLocal P) (f : X ⟶ S) :
    List.TFAE [
      locallyOfType P f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1), P (f.appLE V U e).hom,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, locallyOfType P (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1, P (f.appLE V U e).hom] ∧
    (locallyOfType P f → ∀ (U : X.Opens) (V : S.Opens) (e : U ≤ f ⁻¹ᵁ V),
      locallyOfType P (f.resLE V U e))
```

## Tag 01SV, a lemma

[Tag 01SV](https://stacks.math.columbia.edu/tag/01SV) in the Stacks Project.

**`AlgebraicGeometry.locallyOfType_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocallyOfType.lean#L241).

> For a local property `P` stable under composition, a composition of morphisms locally of
> type `P` is locally of type `P`.

```lean
theorem locallyOfType_comp (hP : RingHom.StacksPropertyIsLocal P)
    (hPc : RingHom.StableUnderComposition P) {X Y Z : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : locallyOfType P f) (hg : locallyOfType P g) : locallyOfType P (f ≫ g)
```

## Tag 01SW, a lemma

[Tag 01SW](https://stacks.math.columbia.edu/tag/01SW) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.HasRingHomProperty.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.HasRingHomProperty.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L189) (StacksFrontier).

## Tag 01SX, a lemma

[Tag 01SX](https://stacks.math.columbia.edu/tag/01SX) in the Stacks Project.

**`RingHom.isOpenImmersion_localizationAwayPreserves`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean#L118). The attribute's comment: “part (2) (open immersion), locality condition (1)(a) of 01SR only: the criterion is preserved by simultaneous principal localization. Part (2) itself is false; see not\_stacksPropertyIsLocal\_isOpenImmersion”.

> Locality condition (1)(a): the affine open-immersion criterion is preserved by
> simultaneous principal localization. This is base change along `R → R_r`.

```lean
theorem isOpenImmersion_localizationAwayPreserves :
    RingHom.LocalizationAwayPreserves
      (fun {R A : Type u} [CommRing R] [CommRing A] (φ : R →+* A) ↦ φ.IsOpenImmersion)
```

**`RingHom.isOpenImmersion_compPrincipalLocalizations`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean#L128). The attribute's comment: “part (2) (open immersion), locality condition (1)(b) of 01SR only: `P (R_f → A) ⟹ P (R → A_a)`. Part (2) itself is false; see not\_stacksPropertyIsLocal\_isOpenImmersion”.

> Locality condition (1)(b): if `R_f → A` satisfies the affine open-immersion criterion then
> so does the induced composite `R → A_a`.

```lean
theorem isOpenImmersion_compPrincipalLocalizations
    {R A Rf Aa : Type u} [CommRing R] [CommRing A] [CommRing Rf] [CommRing Aa] (f : R) (a : A)
    [Algebra R Rf] [IsLocalization.Away f Rf] [Algebra A Aa] [IsLocalization.Away a Aa]
    (g : Rf →+* A) (hg : g.IsOpenImmersion) :
    ((algebraMap A Aa).comp (g.comp (algebraMap R Rf))).IsOpenImmersion
```

**`RingHom.not_ofLocalizationFiniteSpanTarget_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean#L231). The attribute's comment: “refutation of part (2) (open immersion): locality condition (1)(c) of 01SR fails for the criterion, the witness being the diagonal `k → k × k` of a field, whose two localizations at the coordinate idempotents are bijective while the diagonal itself is not a principal localization”.

> The affine open-immersion criterion does not descend from a finite principal open cover of
> the target: this is the third locality condition of `RingHom.StacksPropertyIsLocal`.

```lean
theorem not_ofLocalizationFiniteSpanTarget_isOpenImmersion :
    ¬ RingHom.OfLocalizationFiniteSpanTarget
      (fun {R S : Type u} [CommRing R] [CommRing S] (φ : R →+* S) ↦ φ.IsOpenImmersion)
```

**`RingHom.not_stacksPropertyIsLocal_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersionNotLocal.lean#L244). The attribute's comment: “refutation of part (2) (open immersion): the criterion is NOT a local property of ring maps, so part (2) is false as stated. Conditions (1)(a) and (1)(b) of 01SR do hold and are the two carriers above; (1)(c) fails by not\_ofLocalizationFiniteSpanTarget\_isOpenImmersion. Parts (1), (3), (4) and (5) of the tag are true and carried in LocalRingIso, ReducedFibers, FiberDimension and NoetherianTarget”.

> The affine open-immersion criterion is not a local property of commutative-ring
> homomorphisms.

```lean
theorem not_stacksPropertyIsLocal_isOpenImmersion :
    ¬ RingHom.StacksPropertyIsLocal
      (fun {R S : Type u} [CommRing R] [CommRing S] (φ : R →+* S) ↦ φ.IsOpenImmersion)
```

**`RingHom.fiberDimensionLE_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FiberDimension.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FiberDimension.lean#L127). The attribute's comment: “fibre\_dimension\_bound\_is\_local”.

> A uniform bound on the Krull dimensions of the fibres is a local property of
> commutative-ring homomorphisms.

```lean
theorem fiberDimensionLE_propertyIsLocal (n : ℕ) :
    RingHom.StacksPropertyIsLocal
      (fun {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) =>
        letI : Algebra R S := f.toAlgebra
        ∀ (p : Ideal R) [p.IsPrime], ringKrullDim (p.Fiber S) ≤ (n : WithBot ℕ∞))
```

**`RingHom.localRingHom_bijective_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean#L230). The attribute's comment: “isomorphism\_on\_local\_rings\_is\_local”.

> Having isomorphisms on the local rings at every prime of the target is a
> local property of ring homomorphisms.

```lean
theorem localRingHom_bijective_propertyIsLocal :
    RingHom.StacksPropertyIsLocal
      (fun {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) ↦
        ∀ (q : Ideal S) [q.IsPrime],
          Function.Bijective
            (Localization.localRingHom (Ideal.comap f q) q f rfl))
```

**`RingHom.noetherianTarget_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/NoetherianTarget.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/NoetherianTarget.lean#L37). The attribute's comment: “noetherian\_target\_is\_local”.

> Having Noetherian target is local for commutative-ring homomorphisms.

```lean
theorem noetherianTarget_propertyIsLocal :
    RingHom.StacksPropertyIsLocal
      (fun {R S : Type u} [CommRing R] [CommRing S] (_ : R →+* S) =>
        IsNoetherianRing S)
```

**`RingHom.reducedFibers_propertyIsLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/ReducedFibers.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/ReducedFibers.lean#L152). The attribute's comment: “reduced\_fibres\_is\_local”.

> Having reduced fibres is local for ring homomorphisms.

```lean
theorem reducedFibers_propertyIsLocal :
    RingHom.StacksPropertyIsLocal (fun f => RingHom.ReducedFibers f)
```

## Tag 01SY, a lemma

[Tag 01SY](https://stacks.math.columbia.edu/tag/01SY) in the Stacks Project.

**`RingHom.isOpenImmersion_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersion.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersion.lean#L229). The attribute's comment: “open\_immersion\_base\_change”. References: EGA I (4.3.2), “affine open immersions”; EGA I (4.5.5), “(iii), special case”; SGA 1 VIII (5.5), “special case”.

> The principal-localization criterion for an affine open immersion is
> stable under arbitrary base change of commutative rings.

```lean
theorem isOpenImmersion_isStableUnderBaseChange :
    RingHom.IsStableUnderBaseChange
      (fun {R A : Type u} [CommRing R] [CommRing A] (φ : R →+* A) =>
        φ.IsOpenImmersion)
```

**`RingHom.localRingHom_bijective_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean#L368). The attribute's comment: “local\_rings\_base\_change”.

> Isomorphisms on local rings at every prime of the target are preserved by
> arbitrary base change of commutative rings.

```lean
theorem localRingHom_bijective_isStableUnderBaseChange :
    RingHom.IsStableUnderBaseChange
      (fun {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) ↦
        ∀ (q : Ideal S) [q.IsPrime],
          Function.Bijective
            (Localization.localRingHom (Ideal.comap f q) q f rfl))
```

## Tag 01SZ, a lemma

[Tag 01SZ](https://stacks.math.columbia.edu/tag/01SZ) in the Stacks Project.

**`RingHom.isOpenImmersion_stableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersion.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/AffineOpenImmersion.lean#L268). The attribute's comment: “open\_immersion\_composition”.

> Being an isomorphism on some principal neighborhood of each target prime
> is stable under composition of commutative-ring homomorphisms.

```lean
theorem isOpenImmersion_stableUnderComposition :
    RingHom.StableUnderComposition
      (fun {R S : Type u} [CommRing R] [CommRing S] (φ : R →+* S) ↦
        φ.IsOpenImmersion)
```

**`RingHom.localRingHom_bijective_stableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/LocalRingIso.lean#L381). The attribute's comment: “local\_rings\_composition”.

> The property that all induced maps on local rings are isomorphisms is
> stable under composition.

```lean
theorem localRingHom_bijective_stableUnderComposition :
    RingHom.StableUnderComposition
      (fun {R S : Type u} [CommRing R] [CommRing S] (f : R →+* S) ↦
        ∀ (q : Ideal S) [q.IsPrime],
          Function.Bijective
            (Localization.localRingHom (Ideal.comap f q) q f rfl))
```

**`RingHom.noetherianTarget_stableUnderComposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/NoetherianTarget.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/NoetherianTarget.lean#L54). The attribute's comment: “noetherian\_target\_composition”.

> Having Noetherian target is stable under composition of commutative-ring
> homomorphisms.

```lean
theorem noetherianTarget_stableUnderComposition : RingHom.StableUnderComposition
    (fun {R S : Type u} [CommRing R] [CommRing S] (_ : R →+* S) => IsNoetherianRing S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.14, Tag 01SQ](https://stacks.math.columbia.edu/tag/01SQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
