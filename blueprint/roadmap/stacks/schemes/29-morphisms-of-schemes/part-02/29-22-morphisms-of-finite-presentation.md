---
declaration: section
origin: cited
lean: AlgebraicGeometry.FinitePresentationAt, AlgebraicGeometry.FinitePresentation, AlgebraicGeometry.LocallyOfFinitePresentation, AlgebraicGeometry.locallyOfFinitePresentation_resLE, AlgebraicGeometry.locallyOfFinitePresentation_tfae, AlgebraicGeometry.locallyOfFinitePresentation_tfae_and_resLE, AlgebraicGeometry.locallyOfFinitePresentation_comp_and_finitePresentation_comp, AlgebraicGeometry.finitePresentation_isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 29.22 Morphisms of finite presentation

Section 29.22 of the Stacks Project, [Tag 01TO](https://stacks.math.columbia.edu/tag/01TO). 12 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01TP, a definition

[Tag 01TP](https://stacks.math.columbia.edu/tag/01TP) in the Stacks Project.

**`AlgebraicGeometry.FinitePresentationAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean#L52). The attribute's comment: “part (1)”. References: EGA IV (1.4.2), “fin. presentation at x”.

> A morphism of schemes is of finite presentation at `x` if it induces a
> ring map of finite presentation on some affine neighbourhood of `x` mapping
> into an affine open of the target.

```lean
public abbrev FinitePresentationAt {X S : Scheme.{u}} (f : X ⟶ S) (x : X) : Prop
```

**`AlgebraicGeometry.FinitePresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean#L63). The attribute's comment: “part (3)”.

> A morphism of schemes is of finite presentation if it is locally of finite
> presentation, quasi-compact, and quasi-separated.

```lean
public abbrev FinitePresentation {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyOfFinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.LocallyOfFinitePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean#L56) (StacksFrontier): “part (2)”. References: EGA IV (1.4.2); SGA 3 VIB (1.3).

## Tag 01TQ, a lemma

[Tag 01TQ](https://stacks.math.columbia.edu/tag/01TQ) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean#L74). The attribute's comment: “moreover: restriction to open subschemes”.

> If `f` is locally of finite presentation then so is its restriction `U → V` to any opens
> `U ⊆ X`, `V ⊆ S` with `f(U) ⊆ V`.

```lean
theorem locallyOfFinitePresentation_resLE {f : X ⟶ S} (hf : LocallyOfFinitePresentation f)
    (V : S.Opens) (U : X.Opens) (e : U ≤ f ⁻¹ᵁ V) :
    LocallyOfFinitePresentation (f.resLE V U e)
```

**`AlgebraicGeometry.locallyOfFinitePresentation_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean#L84). The attribute's comment: “equivalence of (1), (2), (3) and (4)”.

> Being locally of finite presentation can be checked on all pairs of affine opens, on open
> coverings of target and preimages, or on affine such coverings.

```lean
theorem locallyOfFinitePresentation_tfae (f : X ⟶ S) :
    List.TFAE [
      LocallyOfFinitePresentation f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.FinitePresentation,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, LocallyOfFinitePresentation (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.FinitePresentation]
```

**`AlgebraicGeometry.locallyOfFinitePresentation_tfae_and_resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/RingMapProperty/FinitePresentation.lean#L100).

> The whole statement: the four characterizations of being locally of finite presentation
> agree, and being locally of finite presentation passes to restrictions to open subschemes.

```lean
theorem locallyOfFinitePresentation_tfae_and_resLE (f : X ⟶ S) :
    List.TFAE [
      LocallyOfFinitePresentation f,
      ∀ (V : S.affineOpens) (U : X.affineOpens) (e : U.1 ≤ f ⁻¹ᵁ V.1),
        (f.appLE V U e).hom.FinitePresentation,
      ∃ 𝒱 : Set S.Opens, sSup 𝒱 = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.Opens, sSup 𝒰 = f ⁻¹ᵁ V ∧
        ∀ U ∈ 𝒰, ∃ e : U ≤ f ⁻¹ᵁ V, LocallyOfFinitePresentation (f.resLE V U e),
      ∃ 𝒱 : Set S.affineOpens, (⨆ V ∈ 𝒱, V.1) = ⊤ ∧ ∀ V ∈ 𝒱, ∃ 𝒰 : Set X.affineOpens,
        (⨆ U ∈ 𝒰, U.1) = f ⁻¹ᵁ V.1 ∧ ∀ U ∈ 𝒰, ∃ e : U.1 ≤ f ⁻¹ᵁ V.1,
          (f.appLE V U e).hom.FinitePresentation] ∧
    (LocallyOfFinitePresentation f → ∀ (U : X.Opens) (V : S.Opens) (e : U ≤ f ⁻¹ᵁ V),
      LocallyOfFinitePresentation (f.resLE V U e))
```

## Tag 01TR, a lemma

[Tag 01TR](https://stacks.math.columbia.edu/tag/01TR) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_comp_and_finitePresentation_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/Basic.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/Basic.lean#L107). The attribute's comment: “Both assertions: the first is Mathlib's `AlgebraicGeometry.locallyOfFinitePresentation_comp`, the second `AlgebraicGeometry.FinitePresentation.comp`.”.

> The composition of two morphisms locally of finite presentation is locally of finite
> presentation, and the composition of two morphisms of finite presentation is of finite
> presentation.
>
> The first assertion is Mathlib's instance `AlgebraicGeometry.locallyOfFinitePresentation_comp`;
> the second is `AlgebraicGeometry.FinitePresentation.comp`, for the Stacks notion
> `AlgebraicGeometry.FinitePresentation` (locally of finite presentation, quasi-compact and
> quasi-separated).

```lean
theorem locallyOfFinitePresentation_comp_and_finitePresentation_comp {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ Z) :
    (LocallyOfFinitePresentation f → LocallyOfFinitePresentation g →
        LocallyOfFinitePresentation (f ≫ g)) ∧
      (FinitePresentation f → FinitePresentation g → FinitePresentation (f ≫ g))
```

## Tag 01TS, a lemma

[Tag 01TS](https://stacks.math.columbia.edu/tag/01TS) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentationPoint.lean#L89). The attribute's comment: “finite presentation”.

> **Finite presentation is stable under base change.** Each of the three constituents of
> `AlgebraicGeometry.FinitePresentation` is: local finite presentation by Mathlib's
> `AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange`, and quasi-compactness
> and quasi-separatedness by Mathlib's `MorphismProperty.IsStableUnderBaseChange` instances.

```lean
public theorem finitePresentation_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun _ _ f => FinitePresentation f : MorphismProperty Scheme.{u})
```

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/QuasiAffine.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FiniteTypeClosedInFinitePresentation/QuasiAffine.lean#L74) (StacksFrontier): “locally of finite presentation: Mathlib's `locallyOfFinitePresentation_isStableUnderBaseChange`”. References: EGA IV (1.4.3); EGA IV (2.7.1), “(iv)”; EGA IV (20.6.9), “partial”; EGA IV (21.15.9), “partial”; EGA IV (8.6.2), “partial”; SGA 3 VIB (5.6.1.0), “partial”.

## Tag 01TT, a lemma

[Tag 01TT](https://stacks.math.columbia.edu/tag/01TT) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.locallyOfFinitePresentation_of_isOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.locallyOfFinitePresentation_of_isOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L302) (StacksFrontier). References: EGA IV (1.4.3), “(i), open immersions”; EGA IV (17.9.1), “(a)”.

## Tag 01TU, a lemma

[Tag 01TU](https://stacks.math.columbia.edu/tag/01TU) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_iff_quasiCompact_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/FinitePresentationOpenImmersion.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/ImmersionsAndAffine/FinitePresentationOpenImmersion.lean#L34). References: EGA IV (1.6.2).

> **Stacks Project, Tag 01TU.** An open immersion is of finite presentation if and only if
> it is quasi-compact.

```lean
theorem finitePresentation_iff_quasiCompact_of_isOpenImmersion
    {X S : Scheme.{u}} (f : X ⟶ S) [IsOpenImmersion f] :
    FinitePresentation f ↔ QuasiCompact f
```

## Tag 01TV, a lemma

[Tag 01TV](https://stacks.math.columbia.edu/tag/01TV) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_iff_fg_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ClosedImmersionFinitePresentation/Basic.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ClosedImmersionFinitePresentation/Basic.lean#L75). References: EGA IV (1.4.5), “closed immersion case”.

> **[Stacks Project, Tag 01TV].** A closed immersion is of finite presentation exactly when
> the associated quasi-coherent sheaf of ideals is of finite type, i.e. when its ideal over every
> affine open of the target is finitely generated.
>
> Quasi-compactness and quasi-separatedness of a closed immersion hold unconditionally, so
> finite presentation asks nothing beyond local finite presentation here.

```lean
theorem finitePresentation_iff_fg_ker (f : X ⟶ Y) [IsClosedImmersion f] :
    FinitePresentation f ↔ ∀ U : Y.affineOpens, (f.ker.ideal U).FG
```

## Tag 01TW, a lemma

[Tag 01TW](https://stacks.math.columbia.edu/tag/01TW) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instLocallyOfFiniteTypeOfLocallyOfFinitePresentation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instLocallyOfFiniteTypeOfLocallyOfFinitePresentation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L307) (StacksFrontier). References: EGA IV (8.8.2.4), “partial”.

## Tag 01TX, a lemma

[Tag 01TX](https://stacks.math.columbia.edu/tag/01TX) in the Stacks Project.

**`AlgebraicGeometry.finitePresentation_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/LocallyNoetherian.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/LocallyNoetherian.lean#L52). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 01TX, part (2).** A morphism of finite type over a locally Noetherian
> scheme is of finite presentation.

```lean
theorem finitePresentation_of_finiteType {X S : Scheme.{u}} (f : X ⟶ S)
    [IsLocallyNoetherian S] [LocallyOfFiniteType f] [QuasiCompact f] :
    AlgebraicGeometry.FinitePresentation f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.instLocallyOfFinitePresentationOfIsLocallyNoetherianOfLocallyOfFiniteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instLocallyOfFinitePresentationOfIsLocallyNoetherianOfLocallyOfFiniteType#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/LocallyNoetherian.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/LocallyNoetherian.lean#L38) (StacksFrontier): “part (1)”. References: SGA 1 IX (4.10), “more general”; SGA 1 IX (4.12), “partial”; SGA 1 IX (4.7), “partial”; SGA 3 V (6.1), “partial”.

## Tag 01TY, a lemma

[Tag 01TY](https://stacks.math.columbia.edu/tag/01TY) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact.compactSpace_of_compactSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L311) (StacksFrontier): “X is quasi-compact”. References: SGA 3 VIB (10.1), “Y is quasi-compact”; SGA 4 VI (1.14), “(i), special case”; SGA 4 VIII (5.1), “partial”.
- [`AlgebraicGeometry.quasiSeparatedSpace_of_quasiSeparated`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiSeparatedSpace_of_quasiSeparated#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L312) (StacksFrontier): “X is quasi-separated”. References: EGA IV (1.2.2), “(ii), special case”; EGA IV (1.2.3), “(ii), necessity”; EGA IV (1.2.6), “partial”; SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”; SGA 4 VI (1.14), “(ii), special case”; SGA 4 VIII (5.1), “partial”.

## Tag 02FV, a lemma

[Tag 02FV](https://stacks.math.columbia.edu/tag/02FV) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Basic.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Basic.lean#L76). The attribute's comment: “part (1)”.

> If `X ⟶ S` is locally of finite presentation and `Y ⟶ S` is locally of finite
> type, then a factor `X ⟶ Y` is locally of finite presentation.

```lean
theorem locallyOfFinitePresentation_of_comp {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S) [LocallyOfFinitePresentation (f ≫ g)]
    [LocallyOfFiniteType g] : LocallyOfFinitePresentation f
```

**`AlgebraicGeometry.finitePresentation_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Basic.lean#L87). The attribute's comment: “part (2)”.

> If `X ⟶ S` is of finite presentation and `Y ⟶ S` is quasi-separated and locally
> of finite type, then a factor `X ⟶ Y` is of finite presentation.

```lean
theorem finitePresentation_of_comp {X Y S : Scheme.{u}}
    (f : X ⟶ Y) (g : Y ⟶ S) (hX : AlgebraicGeometry.FinitePresentation (f ≫ g))
    [QuasiSeparated g] [LocallyOfFiniteType g] :
    AlgebraicGeometry.FinitePresentation f
```

## Tag 0818, a lemma

[Tag 0818](https://stacks.math.columbia.edu/tag/0818) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_diagonal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Diagonal.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Diagonal.lean#L44). The attribute's comment: “local finite-presentation assertion”. References: EGA IV (17.4.1.2), “Delta loc. of fin. pres.”; EGA IV (1.4.3.1).

> The diagonal of a morphism locally of finite type is locally of finite presentation.

```lean
lemma locallyOfFinitePresentation_diagonal {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] : LocallyOfFinitePresentation (pullback.diagonal f)
```

**`AlgebraicGeometry.finitePresentation_diagonal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Diagonal.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FinitePresentation/Diagonal.lean#L54). The attribute's comment: “finite-presentation assertion”. References: EGA IV (1.4.3.1), “special case”; EGA IV (17.4.1.2), “special case”.

> The diagonal of a quasi-separated morphism locally of finite type is of finite
> presentation.

```lean
lemma finitePresentation_diagonal {X Y : Scheme.{u}} (f : X ⟶ Y)
    [QuasiSeparated f] [LocallyOfFiniteType f] :
    AlgebraicGeometry.FinitePresentation (pullback.diagonal f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.22, Tag 01TO](https://stacks.math.columbia.edu/tag/01TO)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
