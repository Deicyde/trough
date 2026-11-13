---
declaration: section
origin: cited
lean: IsOpenMap, AlgebraicGeometry.UniversallyOpen, AlgebraicGeometry.isOpenMap_of_liftsGeneralizations, AlgebraicGeometry.universallyOpen_of_universally_liftsGeneralizations, AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionSchemeTopologicallyIsOpenMap, AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionScheme, AlgebraicGeometry.universallyOpen_of_field, AlgebraicGeometry.liftsGeneralizations_of_isOpenMap
statement: formalized
proof: formalized
---

# 29.24 Open morphisms

Section 29.24 of the Stacks Project, [Tag 01TZ](https://stacks.math.columbia.edu/tag/01TZ). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01U0, a definition

[Tag 01U0](https://stacks.math.columbia.edu/tag/01U0) in the Stacks Project.

Declarations registered for the tag:

- [`IsOpenMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsOpenMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 315](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L315) (StacksFrontier): “(1), open: `IsOpenMap f.base`, which Mathlib writes `topologically @IsOpenMap f`”. References: EGA I (2.2.6); EGA IV (1.10.4); SGA 1 IV (6.6).
- [`AlgebraicGeometry.UniversallyOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 318](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L318) (StacksFrontier): “(2), universally open”. References: EGA III (4.3.11); EGA IV (14.3.1); EGA IV (14.4.9); EGA IV (2.4.2).

## Tag 01U1, a lemma

[Tag 01U1](https://stacks.math.columbia.edu/tag/01U1) in the Stacks Project.

**`AlgebraicGeometry.isOpenMap_of_liftsGeneralizations`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Open/LiftsGeneralizations.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Open/LiftsGeneralizations.lean#L50). The attribute's comment: “part (1): locally of finite presentation and generalizations lift implies open”. References: EGA IV (1.10.4), “b) ⇒ a)”; EGA IV (14.1.6), “partial”.

> **Stacks Project, Tag 01U1**, part (1). A morphism of schemes which is locally of finite
> presentation and along which generalizations lift is open.

```lean
public lemma isOpenMap_of_liftsGeneralizations {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f] (hf : LiftsGeneralizations f) : IsOpenMap f
```

**`AlgebraicGeometry.universallyOpen_of_universally_liftsGeneralizations`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Open/LiftsGeneralizations.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Open/LiftsGeneralizations.lean#L58). The attribute's comment: “part (2): lfp and generalizations lift along every base change implies univ. open”. References: EGA IV (1.10.4), “b) ⇒ a), special case”.

> **Stacks Project, Tag 01U1**, part (2). A morphism of schemes which is locally of finite
> presentation and along every base change of which generalizations lift is universally open.

```lean
public lemma universallyOpen_of_universally_liftsGeneralizations {X S : Scheme.{u}} (f : X ⟶ S)
    [LocallyOfFinitePresentation f]
    (hf : universally (topologically @LiftsGeneralizations) f) : UniversallyOpen f
```

## Tag 02V2, a lemma

[Tag 02V2](https://stacks.math.columbia.edu/tag/02V2) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionSchemeTopologicallyIsOpenMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionSchemeTopologicallyIsOpenMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L187) (StacksFrontier): “composition of open morphisms”. References: EGA I (2.2.7).
- [`AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyOpen.instIsStableUnderCompositionScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L189) (StacksFrontier): “composition of universally open morphisms”. References: EGA IV (14.3.4), “(i), special case”; EGA IV (2.4.3), “(ii), universally open”.

## Tag 0383, a lemma

[Tag 0383](https://stacks.math.columbia.edu/tag/0383) in the Stacks Project.

**`AlgebraicGeometry.universallyOpen_of_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Open/OverField.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Open/OverField.lean#L41).

> Let `k` be a field and let `X` be a scheme over `k`. The structure morphism `X ⟶ Spec k` is
> universally open.

```lean
public theorem universallyOpen_of_field (k : Type u) [Field k] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of k)) : UniversallyOpen f
```

## Tag 040F, a lemma

[Tag 040F](https://stacks.math.columbia.edu/tag/040F) in the Stacks Project.

**`AlgebraicGeometry.liftsGeneralizations_of_isOpenMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Open/Generizing.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Open/Generizing.lean#L48). The attribute's comment: “open morphisms”. References: EGA IV (1.10.3), “a) ⇒ b)”; EGA IV (2.3.5), “partial”.

> An open morphism of schemes lifts generalizations of points.

```lean
public lemma liftsGeneralizations_of_isOpenMap {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : IsOpenMap f) : LiftsGeneralizations f
```

**`AlgebraicGeometry.universally_liftsGeneralizations_of_universallyOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Open/Generizing.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Open/Generizing.lean#L77). The attribute's comment: “universally open morphisms”. References: EGA IV (2.3.5), “special case”.

> A universally open morphism of schemes lifts generalizations after every base change.

```lean
public lemma universally_liftsGeneralizations_of_universallyOpen {X Y : Scheme.{u}} (f : X ⟶ Y)
    [UniversallyOpen f] : universally (topologically @LiftsGeneralizations) f
```

## Tag 04ZE, a lemma

[Tag 04ZE](https://stacks.math.columbia.edu/tag/04ZE) in the Stacks Project.

**`AlgebraicGeometry.quasiCompact_of_isOpenMap_surjective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/QuasiCompact.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/QuasiCompact.lean#L52).

> Quasi-compactness of a morphism of schemes descends along an open,
> surjective morphism of target schemes.

```lean
public theorem quasiCompact_of_isOpenMap_surjective_baseChange
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hopen : IsOpenMap g.base) [Surjective g]
    [QuasiCompact (pullback.snd f g)] : QuasiCompact f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.24, Tag 01TZ](https://stacks.math.columbia.edu/tag/01TZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
