---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_sequential_presentation_iff_exists_countable_presentation, AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_exists_countable_presentation, AlgebraicGeometry.IsCountablyIndexed, AlgebraicGeometry.FormalSpace.IsCountablyIndexed, AlgebraicGeometry.FormalSpace.isAdicStar_of_isNoetherian, AlgebraicGeometry.FormalSpace.isAdic_of_isAdicStar, AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_isAdic, AlgebraicGeometry.FormalSpace.isClassical_of_isWeaklyAdic
statement: formalized
proof: formalized
---

# 87.10 Countably indexed affine formal algebraic spaces

Section 87.10 of the Stacks Project, [Tag 0AIH](https://stacks.math.columbia.edu/tag/0AIH). 5 tags here are carried by 29 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AII, a lemma

[Tag 0AII](https://stacks.math.columbia.edu/tag/0AII) in the Stacks Project.

**`AlgebraicGeometry.exists_sequential_presentation_iff_exists_countable_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/CountablyIndexed.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/CountablyIndexed.lean#L75).

> **Stacks 0AII.** A sequential affine presentation by thickenings exists exactly when a
> countably indexed directed affine presentation by thickenings exists.

```lean
theorem exists_sequential_presentation_iff_exists_countable_presentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) :
    (∃ D : ℕ ⥤ BigAffineFppf B S hS,
      (∀ ⦃i j : ℕ⦄ (f : i ⟶ j),
        Stacks.Thickenings.IsThickening
          ((BigAffineFppf.toScheme B S hS).map (D.map f))) ∧
        Nonempty (X ≅ colimit
          (D ⋙ BigAffineFppf.inclusion B S hS ⋙
            Sheaf.sheafifiedYoneda
              (BigFppfOver.topology B S hS)))) ↔
    (∃ (I : Type (u + 1)) (pre : Preorder I),
      letI : Preorder I := pre
      Nonempty I ∧ IsDirected I (· ≤ ·) ∧ Countable I ∧
        ∃ D : I ⥤ BigAffineFppf B S hS,
          (∀ ⦃i j : I⦄ (f : i ⟶ j),
            Stacks.Thickenings.IsThickening
              ((BigAffineFppf.toScheme B S hS).map (D.map f))) ∧
            Nonempty (X ≅ colimit
              (D ⋙ BigAffineFppf.inclusion B S hS ⋙
                Sheaf.sheafifiedYoneda
                  (BigFppfOver.topology B S hS))))
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_iff_exists_countable_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentation.lean#L59).

> **Stacks Project, Tag 0AII.** An fppf sheaf has a sequential presentation by affine
> schemes and thickenings if and only if it has one indexed by a countable nonempty directed
> preorder.

```lean
theorem isCountablyIndexed_iff_exists_countable_presentation (X : FppfSheaf B S hS) :
    IsCountablyIndexed B S hS X ↔
      ∃ (I : Type (u + 1)) (pre : Preorder I),
        letI : Preorder I := pre
        Nonempty I ∧ IsDirected I (· ≤ ·) ∧ Countable I ∧
          ∃ D : I ⥤ BigAffineFppf B S hS,
            (∀ ⦃i j : I⦄ (f : i ⟶ j),
              Stacks.Thickenings.IsThickening
                ((BigAffineFppf.toScheme B S hS).map (D.map f))) ∧
              Nonempty (X ≅ colimit
                (D ⋙ BigAffineFppf.inclusion B S hS ⋙
                  Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)))
```

## Tag 0AIJ, a definition

[Tag 0AIJ](https://stacks.math.columbia.edu/tag/0AIJ) in the Stacks Project.

**`AlgebraicGeometry.IsCountablyIndexed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/CountablyIndexed.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/CountablyIndexed.lean#L58).

> **Stacks 0AIJ.** A sheaf on the big fppf site of `S` is *countably indexed* when it is
> the colimit of a sequence of sheaves represented by affine schemes whose transition
> morphisms are thickenings.

```lean
abbrev IsCountablyIndexed (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1))) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsCountablyIndexed`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexed.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexed.lean#L47).

> **Stacks 0AIJ.** An fppf sheaf is *countably indexed* when it admits a presentation indexed
> by `ℕ` by affine schemes whose transition maps are thickenings. For an affine formal algebraic
> space this is the countably indexed property.

```lean
abbrev IsCountablyIndexed (X : FppfSheaf B S hS) : Prop
```

## Tag 0AIK, a lemma

[Tag 0AIK](https://stacks.math.columbia.edu/tag/0AIK) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean#L79). The attribute's comment: “noetherian\_adic\_star”.

> **Stacks 0AIK, item (1).** A Noetherian affine formal algebraic space is adic\*: its
> presenting ring is adic, and an ideal of definition of a Noetherian ring is finitely
> generated.

```lean
theorem isAdicStar_of_isNoetherian {X : FppfSheaf B S hS} (hX : IsNoetherian B S hS X) :
    IsAdicStar B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAdic_of_isAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean#L91). The attribute's comment: “adic\_star\_adic”.

> **Stacks 0AIK, item (2).** An adic\* affine formal algebraic space is adic: adic\* is
> adicness of the presenting ring together with the extra demand that some ideal of definition
> be finitely generated.

```lean
theorem isAdic_of_isAdicStar {X : FppfSheaf B S hS} (hX : IsAdicStar B S hS X) :
    IsAdic B S hS X
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_isAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean#L99). The attribute's comment: “adic\_weakly\_adic”.

> **Stacks 0AIK, item (3).** An adic affine formal algebraic space is weakly adic, because
> an adic linearly topologized ring is weakly adic.

```lean
theorem isWeaklyAdic_of_isAdic {X : FppfSheaf B S hS} (hX : IsAdic B S hS X) :
    IsWeaklyAdic B S hS X
```

**`AlgebraicGeometry.FormalSpace.isClassical_of_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean#L107). The attribute's comment: “weakly\_adic\_classical”.

> **Stacks 0AIK, item (4).** A weakly adic affine formal algebraic space is classical,
> because a weakly adic linearly topologized ring is admissible (Stacks 0GXF).

```lean
theorem isClassical_of_isWeaklyAdic {X : FppfSheaf B S hS} (hX : IsWeaklyAdic B S hS X) :
    IsClassical B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/TypeImplications.lean#L125). The attribute's comment: “weakly\_adic\_countable”.

> **Stacks 0AIK, item (5).** A weakly adic affine formal algebraic space is countably
> indexed.
>
> Let `A` be the presenting ring, `W` one of its weak ideals of definition, and `I` an ideal
> whose closed powers are open and form a fundamental system of neighbourhoods of `0`, which is
> what weak adicness of `A` provides. The ideals `W ⊓ (I ^ n)‾` are then weak ideals of
> definition, they decrease in `n`, and every weak ideal of definition contains one of them,
> being open. So the sequence they form is a final functor into the index of the canonical
> weak-ideal presentation of `X`, and restricting that presentation along it exhibits `X` as the
> colimit of a sequence of affine schemes whose transition morphisms are thickenings.

```lean
theorem isCountablyIndexed_of_isWeaklyAdic {X : FppfSheaf B S hS}
    (hX : IsWeaklyAdic B S hS X) : IsCountablyIndexed B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_of_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedMcQuillan.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedMcQuillan.lean#L125). The attribute's comment: “countable\_mcquillan”.

> **Stacks Project, Tag 0AIK**, item (6). A countably indexed affine formal algebraic space
> is McQuillan: it has a presentation by affine thickenings all of whose section-ring projections
> are surjective, which is condition (4) of Stacks 0AIC.

```lean
theorem hasSomeSurjectivePresentation_of_isCountablyIndexed {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) (hc : IsCountablyIndexed B S hS X) :
    HasSomeSurjectivePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.isPresentingRing_of_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedMcQuillan.lean, line 207](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedMcQuillan.lean#L207). The attribute's comment: “(6), countably indexed implies McQuillan”.

> **Stacks Project, Tag 0AIK**, item (6). A countably indexed affine formal algebraic space
> is McQuillan: it has a presentation by affine thickenings all of whose section-ring projections
> are surjective, which is condition (4) of Stacks 0AIC, and it is the formal spectrum of a
> weakly admissible topological ring, which is condition (1).

```lean
theorem isPresentingRing_of_isCountablyIndexed {X : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) (hc : IsCountablyIndexed B S hS X) :
    HasSomeSurjectivePresentation B S hS X ∧
      ∃ (A : Type u) (_ : CommRing A) (_ : TopologicalSpace A) (_ : IsTopologicalRing A)
        (_ : IsLinearTopology A A), IsPresentingRing B S hS A X
```

## Tag 0AN1, a lemma

[Tag 0AN1](https://stacks.math.columbia.edu/tag/0AN1) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.exists_countable_isPresentingRing_of_isCountablyIndexed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentingRing.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentingRing.lean#L78). The attribute's comment: “condition (1) implies condition (2), with `X = Spf A` read as the weak-ideal colimit presentation of Stacks 0AIC rather than as an isomorphism with a formal spectrum”.

> **Stacks 0AN1, condition (1) implies condition (2)**, in the `IsPresentingRing` shape. A
> countably indexed affine formal algebraic space over `S` has a presenting weakly admissible
> topological ring whose neighbourhood filter of zero is countably generated.

```lean
theorem exists_countable_isPresentingRing_of_isCountablyIndexed (X : FppfSheaf B S hS)
    (hX : IsAffineFormalAlgebraicSpace B S hS X) (hXc : IsCountablyIndexed B S hS X) :
    ∃ (C : Type u) (_ : CommRing C) (_ : TopologicalSpace C) (_ : IsTopologicalRing C)
      (_ : IsLinearTopology C C), IsPresentingRing B S hS C X ∧
        (nhds (0 : C)).IsCountablyGenerated
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_of_isPresentingRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentingRing.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablePresentingRing.lean#L93). The attribute's comment: “condition (2) implies condition (1), with `X = Spf A` read as the weak-ideal colimit presentation of Stacks 0AIC rather than as an isomorphism with a formal spectrum”.

> **Stacks 0AN1, condition (2) implies condition (1)**, in the `IsPresentingRing` shape. If a
> weakly admissible topological ring with countably generated neighbourhood filter of zero
> presents `X`, then `X` is countably indexed.

```lean
theorem isCountablyIndexed_of_isPresentingRing (X : FppfSheaf B S hS) (A : Type u) [CommRing A]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    (hA : IsPresentingRing B S hS A X) (hc : (nhds (0 : A)).IsCountablyGenerated) :
    IsCountablyIndexed B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasCountableWeakPresentation_iff_hasWeakIdealChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L249). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0AN1**, conditions (2) and (3) are equivalent. A countably generated filter of
> neighbourhoods of `0` in a weakly admissible ring is based on a descending chain of weak ideals
> of definition, and such a chain is in particular a countable fundamental system.

```lean
theorem hasCountableWeakPresentation_iff_hasWeakIdealChain (X : FppfSheaf B S hS) :
    HasCountableWeakPresentation B S hS X ↔ HasWeakIdealChain B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasWeakIdealChain_iff_hasNilpotentIdealChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L264). The attribute's comment: “conditions (3) and (4)”.

> **Stacks 0AN1**, conditions (3) and (4) are equivalent. A chain of weak ideals of definition
> has locally nilpotent successive quotients because its members consist of topologically
> nilpotent elements; conversely, if the successive quotients are locally nilpotent then every
> element of a member of the chain is topologically nilpotent, so each member is a weak ideal of
> definition and the ring is weakly pre-admissible.

```lean
theorem hasWeakIdealChain_iff_hasNilpotentIdealChain (X : FppfSheaf B S hS) :
    HasWeakIdealChain B S hS X ↔ HasNilpotentIdealChain B S hS X
```

**`AlgebraicGeometry.FormalSpace.isLimitOfNilpotentQuotients_of_hasWeakIdealChain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 369](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L369). The attribute's comment: “condition (3) implies condition (5)”.

> **Stacks 0AN1**, condition (3) implies condition (5). A chain of weak ideals of definition
> basing the topology of a weakly admissible `A` exhibits `A` itself as the inverse limit
> `lim A/Iₙ` with the limit topology, and the `S`-algebra of condition (5) can be taken to be `A`:
> the successive quotients `Iₙ/Iₙ₊₁` are locally nilpotent, the kernels of the quotient maps are
> the `Iₙ`, and the structure morphisms of the quotient system are already indexed by weak ideals
> of definition, each of which contains some `Iₙ`.

```lean
theorem isLimitOfNilpotentQuotients_of_hasWeakIdealChain (X : FppfSheaf B S hS)
    (hX : HasWeakIdealChain B S hS X) : IsLimitOfNilpotentQuotients B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasCountableWeakPresentation_of_isLimitOfNilpotentQuotients`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L488). The attribute's comment: “condition (5) implies condition (2)”.

> **Stacks 0AN1**, condition (5) implies condition (2). The presenting ring of an inverse
> limit presentation is weakly admissible, and the kernels of the projections are a countable
> fundamental system of neighbourhoods of `0`.

```lean
theorem hasCountableWeakPresentation_of_isLimitOfNilpotentQuotients (X : FppfSheaf B S hS)
    (hX : IsLimitOfNilpotentQuotients B S hS X) : HasCountableWeakPresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAffine_of_hasCountableWeakPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 624](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L624). The attribute's comment: “condition (2) implies condition (1)”.

> **Stacks 0AN1**, condition (2) implies condition (1). The formal spectrum of a weakly
> admissible ring over `S` is an affine formal algebraic space (**Stacks 0AIF**) once the site is
> large enough, which a countable fundamental system of neighbourhoods of `0` guarantees, and it
> is countably indexed because such a system is cofinal in the weak ideals of definition.

```lean
theorem isCountablyIndexedAffine_of_hasCountableWeakPresentation (X : FppfSheaf B S hS)
    (hX : HasCountableWeakPresentation B S hS X) : IsCountablyIndexedAffine B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasCountableWeakPresentation_of_isCountablyIndexedAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 640](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L640). The attribute's comment: “condition (1) implies condition (2)”.

> **Stacks 0AN1**, condition (1) implies condition (2). A countably indexed affine formal
> algebraic space is the formal spectrum of the limit of the section rings of a sequential
> presentation (**Stacks 0AIK**, item (6)); that ring is weakly admissible and the kernels of
> its projections are a countable fundamental system of neighbourhoods of `0`.

```lean
theorem hasCountableWeakPresentation_of_isCountablyIndexedAffine (X : FppfSheaf B S hS)
    (hX : IsCountablyIndexedAffine B S hS X) : HasCountableWeakPresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexedAffine_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean, line 659](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexedSpectrum.lean#L659).

> **Stacks 0AN1.** For an fppf sheaf `X` on the big fppf site of `S` the following are
> equivalent:
>
> 1. `X` is a countably indexed affine formal algebraic space;
> 2. `X = Spf A` for a weakly admissible topological `S`-algebra `A` with a countable
>    fundamental system of neighbourhoods of `0`;
> 3. `X = Spf A` for a weakly admissible `A` with a descending chain of weak ideals of
>    definition as a fundamental system of neighbourhoods of `0`;
> 4. `X = Spf A` for a complete and separated `A` with a descending chain of open ideals with
>    locally nilpotent successive quotients as a fundamental system of neighbourhoods of `0`;
> 5. `X = Spf A` for `A` the inverse limit of a sequence of quotients of a ring with locally
>    nilpotent successive quotients, with the limit topology.

```lean
theorem isCountablyIndexedAffine_tfae (X : FppfSheaf B S hS) :
    List.TFAE
      [IsCountablyIndexedAffine B S hS X,
        HasCountableWeakPresentation B S hS X,
        HasWeakIdealChain B S hS X,
        HasNilpotentIdealChain B S hS X,
        IsLimitOfNilpotentQuotients B S hS X]
```

## Tag 0AKM, a lemma

[Tag 0AKM](https://stacks.math.columbia.edu/tag/0AKM) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasNoetherianClosedSubschemes_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionComparison.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionComparison.lean#L212). The attribute's comment: “(1) ⇒ (2)”.

> **Stacks 0AKM, (1) ⇒ (2).** Every scheme of the site admitting a closed immersion into a
> Noetherian affine formal algebraic space `X` is a Noetherian scheme.
>
> By the implication (1) ⇒ (3) of the same tag, `X` has a presentation by Noetherian affine
> schemes. A closed immersion `T ⟶ X` in the sense of Stacks 0ANP is one in the sense of
> Stacks 0AIC, so the geometric step of Stacks 0AIC factors it through a stage of that
> presentation by a closed immersion of schemes `T ⟶ X_λ`. As `X_λ` is Noetherian, so is `T`.

```lean
theorem hasNoetherianClosedSubschemes_of_isNoetherian {X : FppfSheaf B S hS}
    (hX : IsNoetherian B S hS X) : HasNoetherianClosedSubschemes B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_tfae'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionComparison.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/ClosedImmersionComparison.lean#L241).

> **Stacks 0AKM.** For an fppf sheaf `X` on the big fppf site of `S` the following are
> equivalent:
>
> 1. `X` is a Noetherian affine formal algebraic space;
> 2. `X` is adic\* and every scheme of the site closed-immersed in `X` is Noetherian;
> 3. `X` is adic\* and some presentation of it by affine thickenings has Noetherian stages;
> 4. `X` is weakly adic and some presentation of it by affine thickenings has Noetherian stages.
>
> Each condition already contains the requirement that `X` be a McQuillan affine formal
> algebraic space. This is the primed form of
> `AlgebraicGeometry.FormalSpace.isNoetherian_tfae`, which records the equivalence of
> conditions (1), (3) and (4) alone.

```lean
theorem isNoetherian_tfae' (X : FppfSheaf B S hS) :
    List.TFAE
      [IsNoetherian B S hS X,
        IsAdicStar B S hS X ∧ HasNoetherianClosedSubschemes B S hS X,
        IsAdicStar B S hS X ∧ HasNoetherianAffinePresentation B S hS X,
        IsWeaklyAdic B S hS X ∧ HasNoetherianAffinePresentation B S hS X]
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_and_hasNoetherianAffinePresentation_of_isNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L311). The attribute's comment: “(1) ⇒ (3)”.

> **Stacks 0AKM, (1) ⇒ (3).** A Noetherian affine formal algebraic space is adic\* and every
> presentation of it by affine thickenings has Noetherian stages. Indeed an ideal of definition
> of a Noetherian ring is finitely generated, and every stage of a presentation is the spectrum
> of a quotient of the presenting ring, hence of a Noetherian ring.

```lean
theorem isAdicStar_and_hasNoetherianAffinePresentation_of_isNoetherian
    {X : FppfSheaf B S hS} (hX : IsNoetherian B S hS X) :
    IsAdicStar B S hS X ∧ HasNoetherianAffinePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_isAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L337). The attribute's comment: “(3) ⇒ (1)”.

> **Stacks 0AKM, (3) ⇒ (1).** An adic\* affine formal algebraic space with a presentation by
> Noetherian affine schemes is Noetherian. Let `I` be a finitely generated ideal of definition of
> the presenting ring `A`. The weak ideals of definition cutting out the stages are cofinal, so
> one of them is contained in `I`; the corresponding stage being Noetherian makes `A ⧸ I` a
> quotient of a Noetherian ring, and `A` is `I`-adically complete, so Stacks 05GH makes `A`
> Noetherian.

```lean
theorem isNoetherian_of_isAdicStar {X : FppfSheaf B S hS} (hX : IsAdicStar B S hS X)
    (hpres : HasNoetherianAffinePresentation B S hS X) : IsNoetherian B S hS X
```

**`AlgebraicGeometry.FormalSpace.isWeaklyAdic_of_isAdicStar`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L363). The attribute's comment: “(3) ⇒ (4)”.

> **Stacks 0AKM, (3) ⇒ (4).** An adic\* affine formal algebraic space is weakly adic, because
> an adic topological ring is weakly adic.

```lean
theorem isWeaklyAdic_of_isAdicStar {X : FppfSheaf B S hS} (hX : IsAdicStar B S hS X) :
    IsWeaklyAdic B S hS X
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_of_isWeaklyAdic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L380). The attribute's comment: “(4) ⇒ (3)”.

> **Stacks 0AKM, (4) ⇒ (3).** A weakly adic affine formal algebraic space with a
> presentation by Noetherian affine schemes is adic\*.
>
> Let `A` be the presenting ring and `I` an ideal of definition, which exists because a weakly
> adic ring is admissible. By Stacks 0GXF the closure `I₂` of `I ^ 2` is open, so it is a weak
> ideal of definition; cofinality of the weak ideals cutting out the stages produces a stage
> contained in `I₂`, whence `A ⧸ I₂` is Noetherian. The image of `I` in `A ⧸ I₂` is then a
> finitely generated module, that is `I / I₂` is a finite `A`-module, and Stacks 0GXH produces a
> finitely generated ideal defining the topology of `A`.

```lean
theorem isAdicStar_of_isWeaklyAdic {X : FppfSheaf B S hS} (hX : IsWeaklyAdic B S hS X)
    (hpres : HasNoetherianAffinePresentation B S hS X) : IsAdicStar B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasNoetherianAffinePresentation_of_hasNoetherianClosedSubschemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L424). The attribute's comment: “(2) ⇒ (3)”.

> **Stacks 0AKM, (2) ⇒ (3).** If every scheme closed-immersed in an affine formal algebraic
> space `X` is Noetherian, then every presentation of `X` by affine thickenings has Noetherian
> stages: by Stacks 0AI9 each stage inclusion `X_λ → X` is a thickening, in particular a closed
> immersion of formal algebraic spaces, so the hypothesis applies to its source.

```lean
theorem hasNoetherianAffinePresentation_of_hasNoetherianClosedSubschemes
    {X : FppfSheaf B S hS} (hX : IsAffineFormalAlgebraicSpace B S hS X)
    (hclosed : HasNoetherianClosedSubschemes B S hS X) :
    HasNoetherianAffinePresentation B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_of_hasNoetherianClosedSubschemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L446). The attribute's comment: “(2) ⇒ (1)”.

> **Stacks 0AKM, (2) ⇒ (1).** An adic\* affine formal algebraic space all of whose
> closed subschemes that are schemes are Noetherian is itself Noetherian: the stages of any
> presentation are such closed subschemes, so condition (3) holds and (3) ⇒ (1) applies.

```lean
theorem isNoetherian_of_hasNoetherianClosedSubschemes {X : FppfSheaf B S hS}
    (hX : IsAdicStar B S hS X) (hclosed : HasNoetherianClosedSubschemes B S hS X) :
    IsNoetherian B S hS X
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoetherianCharacterization.lean#L460). The attribute's comment: “clauses (1), (3) and (4)”.

> **Stacks 0AKM, conditions (1), (3) and (4).** For an fppf sheaf `X` on the big fppf site of
> `S` the following are equivalent: `X` is a Noetherian affine formal algebraic space; `X` is
> adic\* and has a presentation by Noetherian affine schemes; `X` is weakly adic and has a
> presentation by Noetherian affine schemes. Each condition already contains the requirement that
> `X` be a McQuillan affine formal algebraic space.

```lean
theorem isNoetherian_tfae (X : FppfSheaf B S hS) :
    List.TFAE
      [IsNoetherian B S hS X,
        IsAdicStar B S hS X ∧ HasNoetherianAffinePresentation B S hS X,
        IsWeaklyAdic B S hS X ∧ HasNoetherianAffinePresentation B S hS X]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.10, Tag 0AIH](https://stacks.math.columbia.edu/tag/0AIH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
