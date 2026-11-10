---
declaration: section
origin: cited
lean: AlgebraicGeometry.SyntomicAt, AlgebraicGeometry.Syntomic, AlgebraicGeometry.IsStandardSyntomic, AlgebraicGeometry.IsLocalCompleteIntersectionOverField, AlgebraicGeometry.syntomic_tfae, AlgebraicGeometry.syntomic_resLE, AlgebraicGeometry.syntomic_isStableUnderComposition, AlgebraicGeometry.syntomic_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 29.31 Syntomic morphisms

Section 29.31 of the Stacks Project, [Tag 01UB](https://stacks.math.columbia.edu/tag/01UB). 16 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01UC, a definition

[Tag 01UC](https://stacks.math.columbia.edu/tag/01UC) in the Stacks Project.

**`AlgebraicGeometry.SyntomicAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean#L51). The attribute's comment: “syntomic_at_point”.

> A morphism of schemes `f : X ⟶ S` is *syntomic at* `x : X` if there are affine open
> neighbourhoods `U` of `x` and `V` of `f(x)`, with `f(U) ⊆ V`, for which the induced map
> `Γ(S, V) → Γ(X, U)` is syntomic.

```lean
def SyntomicAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.Syntomic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean#L65). The attribute's comment: “syntomic_morphism”.

> A morphism of schemes is syntomic if it is syntomic at every point of its source.

```lean
abbrev Syntomic {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.IsStandardSyntomic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean#L73). The attribute's comment: “standard_syntomic_morphism”.

> A morphism `f : X ⟶ S` of affine schemes is **standard syntomic** if the induced ring map
> `Γ(S, ⊤) → Γ(X, ⊤)` is a relative global complete intersection. Via the canonical isomorphisms of
> affine schemes with the spectra of their global sections, this says precisely that `f` is
> isomorphic to the spectrum of a relative global complete intersection.

```lean
abbrev IsStandardSyntomic {X S : Scheme.{u}} [IsAffine X] [IsAffine S]
    (f : X ⟶ S) : Prop
```

**`AlgebraicGeometry.IsLocalCompleteIntersectionOverField`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Defs.lean#L100). The attribute's comment: “local_complete_intersection_over_field”.

> A scheme over a field is a **local complete intersection over the field** if its structure
> morphism to the spectrum of the field is syntomic.

```lean
abbrev IsLocalCompleteIntersectionOverField {k : Type u} [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : Prop
```

## Tag 01UD, a lemma

[Tag 01UD](https://stacks.math.columbia.edu/tag/01UD) in the Stacks Project.

**`AlgebraicGeometry.syntomic_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Basic.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Basic.lean#L59). The attribute's comment: “syntomic characterization”.

> The four characterizations of a syntomic morphism: the global condition, the condition on
> every compatible pair of affine opens, an open-covering criterion, and an affine-open-covering
> criterion on rings of sections.

```lean
theorem syntomic_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE [
      Syntomic f,
      ∀ (U : X.Opens) (_ : IsAffineOpen U) (V : S.Opens) (_ : IsAffineOpen V)
        (hUV : U ≤ f ⁻¹ᵁ V),
        letI : Algebra Γ(S, V) Γ(X, U) := (f.appLE V U hUV).hom.toAlgebra
        Algebra.Syntomic Γ(S, V) Γ(X, U),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            ∀ i, Syntomic (f.resLE (V j) (U i) ((le_iSup U i).trans hU.le)),
      ∃ (J : Type u) (V : J → S.Opens),
        IsOpenCover V ∧
          (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens)
            (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i,
                let hUV : U i ≤ f ⁻¹ᵁ V j := (le_iSup U i).trans hU.le
                letI : Algebra Γ(S, V j) Γ(X, U i) := (f.appLE (V j) (U i) hUV).hom.toAlgebra
                Algebra.Syntomic Γ(S, V j) Γ(X, U i)]
```

**`AlgebraicGeometry.syntomic_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Basic.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Basic.lean#L123). The attribute's comment: “restriction of a syntomic morphism”.

> Restricting a syntomic morphism to compatible open subschemes of its source and target is
> syntomic.

```lean
theorem syntomic_resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : Syntomic f) (U : X.Opens) (V : S.Opens) (hUV : U ≤ f ⁻¹ᵁ V) :
    Syntomic (f.resLE V U hUV)
```

## Tag 01UH, a lemma

[Tag 01UH](https://stacks.math.columbia.edu/tag/01UH) in the Stacks Project.

**`AlgebraicGeometry.syntomic_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Comp.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Comp.lean#L63).

> **Stacks Project, Tag 01UH.** Syntomic morphisms of schemes are stable under composition.

```lean
instance syntomic_isStableUnderComposition :
    MorphismProperty.IsStableUnderComposition (@Syntomic.{u})
```

## Tag 01UI, a lemma

[Tag 01UI](https://stacks.math.columbia.edu/tag/01UI) in the Stacks Project.

**`AlgebraicGeometry.syntomic_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/BaseChange.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/BaseChange.lean#L39).

> **Stacks Project, Tag 01UI.** A base change of a syntomic morphism is syntomic.

```lean
instance syntomic_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange (@Syntomic : MorphismProperty Scheme.{u})
```

## Tag 01UJ, a lemma

[Tag 01UJ](https://stacks.math.columbia.edu/tag/01UJ) in the Stacks Project.

**`AlgebraicGeometry.syntomic_of_isOpenImmersion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/OpenImmersion.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/OpenImmersion.lean#L29).

> Every open immersion of schemes is syntomic.

```lean
lemma syntomic_of_isOpenImmersion {X S : Scheme.{u}} (f : X ⟶ S)
    [IsOpenImmersion f] : Syntomic f
```

## Tag 01UK, a lemma

[Tag 01UK](https://stacks.math.columbia.edu/tag/01UK) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean#L44).

> A syntomic morphism of schemes is locally of finite presentation.

```lean
lemma locallyOfFinitePresentation {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : Syntomic f) : LocallyOfFinitePresentation f
```

## Tag 01UL, a lemma

[Tag 01UL](https://stacks.math.columbia.edu/tag/01UL) in the Stacks Project.

**`AlgebraicGeometry.flat`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean#L58).

> A syntomic morphism of schemes is flat.

```lean
lemma flat {X S : Scheme.{u}} {f : X ⟶ S} (hf : Syntomic f) : Flat f
```

## Tag 056F, a lemma

[Tag 056F](https://stacks.math.columbia.edu/tag/056F) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Properties.lean#L70).

> A syntomic morphism of schemes is universally open.

```lean
theorem universallyOpen_of_syntomic {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : Syntomic f) : UniversallyOpen f
```

## Tag 01UG, a lemma

[Tag 01UG](https://stacks.math.columbia.edu/tag/01UG) in the Stacks Project.

**`AlgebraicGeometry.localCompleteIntersection_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/LocalCompleteIntersection.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/LocalCompleteIntersection.lean#L194).

> **Stacks Project, Tag 01UG.** For a scheme locally of finite type over a field, being a
> local complete intersection is equivalent to the existence of affine neighbourhoods with
> global-complete-intersection coordinate rings, and to all local rings being complete
> intersections over the field.

```lean
theorem localCompleteIntersection_tfae (k : Type u) [Field k]
    (X : Scheme.{u}) (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f] :
    let globalCI := fun U : X.Opens ↦
      letI : Algebra k Γ(X, U) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appLE ⊤ U (by simp)).hom.toAlgebra
      IsGlobalCompleteIntersection k Γ(X, U)
    let localCI := fun x : X ↦
      letI : Algebra k (X.presheaf.stalk x) :=
        ((Scheme.ΓSpecIso (.of k)).inv ≫ f.appTop ≫
          X.presheaf.germ ⊤ x (by simp)).hom.toAlgebra
      IsCompleteIntersection k (X.presheaf.stalk x)
    List.TFAE [
      IsLocalCompleteIntersectionOverField f,
      ∀ x : X, ∃ U : X.affineOpens, x ∈ U.1 ∧ globalCI U.1,
      ∀ x : X, localCI x]
```

## Tag 01UE, a lemma

[Tag 01UE](https://stacks.math.columbia.edu/tag/01UE) in the Stacks Project.

**`AlgebraicGeometry.syntomicAt_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Local.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/Local.lean#L482).

> Let `x : X` map to `s : S`, and let `V` be an affine open neighbourhood of `s`. Then the
> following are equivalent:
>
> 1. `f` is syntomic at `x`;
> 2. some affine open neighbourhood `U` of `x`, mapping into `V`, makes the
>    restricted morphism `U ⟶ V` standard syntomic;
> 3. `f` is of finite presentation at `x`, its map on local rings is flat, and
>    its local fibre ring at `x` is a complete intersection over `κ(s)`.

```lean
theorem syntomicAt_tfae {X S : Scheme.{u}} (f : X ⟶ S) (x : X)
    (V : S.affineOpens) (_hxV : f x ∈ V.1) :
    List.TFAE [
      SyntomicAt f x,
      ∃ (U : X.affineOpens) (_ : x ∈ U.1) (hUV : U.1 ≤ f ⁻¹ᵁ V.1),
        IsStandardSyntomic (f.resLE V.1 U.1 hUV),
      AlgebraicGeometry.FinitePresentationAt f x ∧
        (f.stalkMap x).hom.Flat ∧
        (let A := S.presheaf.stalk (f x)
         let B := X.presheaf.stalk x
         letI : Algebra A B := (f.stalkMap x).hom.toAlgebra
         IsCompleteIntersection (IsLocalRing.ResidueField A)
           (IsLocalRing.ResidueField A ⊗[A] B))]
```

## Tag 01UF, a lemma

[Tag 01UF](https://stacks.math.columbia.edu/tag/01UF) in the Stacks Project.

**`AlgebraicGeometry.syntomic_of_lci_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberCriterion.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberCriterion.lean#L58).

> **Stacks Project, Tag 01UF.** A flat morphism of schemes which is locally of finite
> presentation and whose every fibre is a local complete intersection over the residue field of
> its base point is syntomic.

```lean
theorem syntomic_of_lci_fibers {X S : Scheme.{u}} (f : X ⟶ S) [Flat f]
    [LocallyOfFinitePresentation f]
    (hlci : ∀ s : S, IsLocalCompleteIntersectionOverField (f.fiberToSpecResidueField s)) :
    Syntomic f
```

## Tag 02V3, a lemma

[Tag 02V3](https://stacks.math.columbia.edu/tag/02V3) in the Stacks Project.

**`AlgebraicGeometry.syntomicLocus_eq_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SyntomicBaseChange/Basic.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SyntomicBaseChange/Basic.lean#L129). The attribute's comment: “syntomic locus”.

> **Stacks Project, Tag 02V3.**  For a flat morphism locally of finite presentation, the
> syntomic locus commutes with arbitrary base change: if the square `g'`, `f'`, `f`, `g` is
> cartesian then the set of points where `f'` is syntomic is the `g'`-preimage of the set of points
> where `f` is syntomic.

```lean
theorem syntomicLocus_eq_preimage
    (g' : X' ⟶ X) (f' : X' ⟶ S') (f : X ⟶ S) (g : S' ⟶ S) (hpb : IsPullback g' f' f g)
    [Flat f] [LocallyOfFinitePresentation f] :
    {x' : X' | IsSyntomicAt f' x'} = g' ⁻¹' {x : X | IsSyntomicAt f x}
```

Declarations registered for the tag:

- [`Stacks.Tag02V3FibreStalk.completeIntersectionFibreStalkLocus_eq_preimage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreStalk/Basic.lean#L222), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FibreStalk/Basic.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FibreStalk/Basic.lean#L266) (StacksFrontier): “complete-intersection fibre locus”. References: EGA IV (19.3.4).

## Tag 02K0, a lemma

[Tag 02K0](https://stacks.math.columbia.edu/tag/02K0) in the Stacks Project.

**`AlgebraicGeometry.fiberDimensionAt_eq_card_sub_card`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean#L115).

> **Stacks 02K0.** For a presentation
> `S = R[x₁, …, xₙ]/(f₁, …, fᶜ)` which is a relative global complete intersection, the
> dimension at every point of the fibre of `Spec S → Spec R` is `n - c`.

```lean
lemma fiberDimensionAt_eq_card_sub_card
    {R S : Type u} [CommRing R] [CommRing S] [Algebra R S]
    {ι σ : Type*} [Finite ι] [Finite σ] (P : Algebra.Presentation R S ι σ)
    [P.IsRelativeGlobalCompleteIntersection] (x : Spec (.of S)) :
    let f : Spec (.of S) ⟶ Spec (.of R) := Spec.map (CommRingCat.ofHom (algebraMap R S))
    topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x) =
      ((Nat.card ι - Nat.card σ : ℕ) : WithBot ℕ∞)
```

## Tag 02K1, a lemma

[Tag 02K1](https://stacks.math.columbia.edu/tag/02K1) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstant_fiberDimensionAt`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean#L177).

> The local dimension of the fibre of a syntomic morphism is locally constant on its source.

```lean
lemma isLocallyConstant_fiberDimensionAt {X S : Scheme.{u}} (f : X ⟶ S) (hf : Syntomic f) :
    IsLocallyConstant (fun x : X => topologicalKrullDimAt (f.fiber (f x)) (f.asFiber x))
```

## Tag 02K2, a definition

[Tag 02K2](https://stacks.math.columbia.edu/tag/02K2) in the Stacks Project.

**`AlgebraicGeometry.SyntomicOfRelativeDimension`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Syntomic/FiberDimension.lean#L202).

> A syntomic morphism whose fibres have local dimension `d` at every point.

```lean
abbrev SyntomicOfRelativeDimension (d : ℕ) {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 02K3, a lemma

[Tag 02K3](https://stacks.math.columbia.edu/tag/02K3) in the Stacks Project.

**`Stacks.Syntomic.syntomic_of_comp_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/SyntomicLciDescent.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/SyntomicLciDescent.lean#L325).

> **Stacks Project, Tag 02K3.** Let `X ⟶ Y ⟶ S` be morphisms of schemes with `X ⟶ Y`
> surjective and syntomic and the composite `X ⟶ S` syntomic. If `Y ⟶ S` is locally of finite
> presentation, then `Y ⟶ S` is syntomic.

```lean
theorem syntomic_of_comp_of_locallyOfFinitePresentation (f : X ⟶ Y) (q : Y ⟶ S) [Surjective f]
    (hf : Syntomic f) (hcomp : Syntomic (f ≫ q)) [LocallyOfFinitePresentation q] :
    Syntomic q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.31, Tag 01UB](https://stacks.math.columbia.edu/tag/01UB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
