---
declaration: section
origin: cited
lean: Stacks.Groupoids.IsInvariantClosedSubscheme, Stacks.Groupoids.IsInvariantMonomorphism, Stacks.Groupoids.IsInvariantSet, Stacks.Groupoids.IsInvariantOpen, AlgebraicGeometry.GroupoidScheme.isInvariantSet_target_image_source_preimage, AlgebraicGeometry.GroupoidScheme.isOpen_target_image_source_preimage, AlgebraicGeometry.GroupoidScheme.exists_invariant_compact_open_neighborhood, AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_eq_target_image_source_preimage
statement: formalized
proof: formalized
---

# 39.19 Invariant subschemes

Section 39.19 of the Stacks Project, [Tag 03LN](https://stacks.math.columbia.edu/tag/03LN). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03BC, a definition

[Tag 03BC](https://stacks.math.columbia.edu/tag/03BC) in the Stacks Project.

**`Stacks.Groupoids.IsInvariantClosedSubscheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean#L113). The attribute's comment: “part (3): invariant closed subschemes”.

> A closed subscheme of the objects of a groupoid scheme is invariant when its
> scheme-theoretic inverse images along source and target agree.

```lean
abbrev IsInvariantClosedSubscheme {S : Scheme.{u}} (G : GroupoidScheme S)
    (Z : G.objects.left.IdealSheafData) : Prop
```

**`Stacks.Groupoids.IsInvariantMonomorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Basic.lean#L120). The attribute's comment: “part (4): invariant monomorphisms”.

> A monomorphism of schemes into the objects of a groupoid scheme is invariant when its
> source and target pullbacks define the same subobject of the arrow scheme.

```lean
abbrev IsInvariantMonomorphism {S : Scheme.{u}} (G : GroupoidScheme S) {T : Scheme.{u}}
    (i : T ⟶ G.objects.left) [Mono i] : Prop
```

**`Stacks.Groupoids.IsInvariantSet`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean#L61). The attribute's comment: “part (1): set-theoretic invariance”.

> **Stacks Project, Tag 03BC, part (1).**  A subset of the objects of a groupoid scheme is
> invariant if every arrow starting in it also ends in it.

```lean
abbrev IsInvariantSet {S : AlgebraicGeometry.Scheme.{u}} (G : GroupoidScheme S)
    (W : Set G.objects.left) : Prop
```

**`Stacks.Groupoids.IsInvariantOpen`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean#L68). The attribute's comment: “part (2): invariant opens”.

> **Stacks Project, Tag 03BC, part (2).**  An open subscheme of the objects of a groupoid
> scheme is invariant if its underlying set is.

```lean
abbrev IsInvariantOpen {S : AlgebraicGeometry.Scheme.{u}} (G : GroupoidScheme S)
    (W : G.objects.left.Opens) : Prop
```

## Tag 03LO, a lemma

[Tag 03LO](https://stacks.math.columbia.edu/tag/03LO) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.isInvariantSet_target_image_source_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean#L88). The attribute's comment: “part (1): set-theoretic invariance”.

> **Stacks Project, Tag 03LO (1).** The saturation of any subset by the arrows of a groupoid
> scheme is invariant.

```lean
theorem isInvariantSet_target_image_source_preimage {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S) (W : Set G.objects.left) :
    IsInvariantSet G (G.target.left.base '' (G.source.left.base ⁻¹' W))
```

**`AlgebraicGeometry.GroupoidScheme.isOpen_target_image_source_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean#L106). The attribute's comment: “part (2): invariant open saturation”.

> **Stacks Project, Tag 03LO (2).** The saturation of an open set is open when the target map
> is an open map.

```lean
theorem isOpen_target_image_source_preimage {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S)
    (ht : IsOpenMap G.target.left.base)
    (W : G.objects.left.Opens) :
    IsOpen (G.target.left.base '' (G.source.left.base ⁻¹' (W : Set G.objects.left)))
```

**`AlgebraicGeometry.GroupoidScheme.exists_invariant_compact_open_neighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/Basic.lean#L117). The attribute's comment: “part (3): invariant quasi-compact open covering”.

> **Stacks Project, Tag 03LO (3).** If the target map is open and the source map is
> quasi-compact, every point of the object scheme has an invariant quasi-compact open
> neighbourhood.

```lean
theorem exists_invariant_compact_open_neighborhood {S : Scheme.{u}}
    (G : Stacks.Groupoids.GroupoidScheme S)
    (ht : IsOpenMap G.target.left.base)
    [QuasiCompact G.source.left]
    (x : G.objects.left) :
    ∃ V : G.objects.left.Opens,
      x ∈ (V : Set G.objects.left) ∧
        IsInvariantOpen G V ∧ IsCompact (V : Set G.objects.left)
```

**`AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_eq_target_image_source_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/ConstructingInvariantOpens.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/ConstructingInvariantOpens.lean#L145). The attribute's comment: “(2) t(s⁻¹(W)) is an invariant open subscheme”.

> **Stacks Project, Tag 03LO, part (2).** If the target map of a groupoid scheme is open then
> the saturation `t(s⁻¹(W))` of an open subscheme `W` of the object scheme is an invariant open
> subscheme.

```lean
theorem exists_isInvariantOpen_eq_target_image_source_preimage
    (ht : IsOpenMap G.target.left.base) (W : G.objects.left.Opens) :
    ∃ V : G.objects.left.Opens,
      (V : Set G.objects.left) =
        G.target.left.base '' (G.source.left.base ⁻¹' (W : Set G.objects.left)) ∧
      (W : Set G.objects.left) ⊆ (V : Set G.objects.left) ∧ IsInvariantOpen G V
```

**`AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_isCompact_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/ConstructingInvariantOpens.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/ConstructingInvariantOpens.lean#L174). The attribute's comment: “(3) covering by invariant quasi-compact opens”.

> **Stacks Project, Tag 03LO, part (3).** If the target map of a groupoid scheme is open and
> its source map is quasi-compact, then the object scheme has an open covering consisting of
> invariant quasi-compact open subschemes.

```lean
theorem exists_isInvariantOpen_isCompact_cover [QuasiCompact G.source.left]
    (ht : IsOpenMap G.target.left.base) :
    ∃ (ι : Type u) (V : ι → G.objects.left.Opens),
      (∀ i, IsInvariantOpen G (V i)) ∧
      (∀ i, IsCompact (V i : Set G.objects.left)) ∧
      ⨆ i, V i = ⊤
```

## Tag 0APA, a lemma

[Tag 0APA](https://stacks.math.columbia.edu/tag/0APA) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.target_image_source_preimage_eq_iInter_compact_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantOpen.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantOpen.lean#L60).

> The target-image of the source-preimage of a quasi-compact open in the object scheme of a
> flat quasi-compact groupoid is an intersection of a nonempty family of quasi-compact opens.

```lean
theorem target_image_source_preimage_eq_iInter_compact_open
    {S : Scheme.{u}} (G : Stacks.Groupoids.GroupoidScheme S)
    [QuasiCompact G.source.left] [Flat G.source.left]
    [QuasiCompact G.target.left] [Flat G.target.left]
    [QuasiSeparatedSpace G.objects.left]
    (W : G.objects.left.Opens) (hW : IsCompact (W : Set G.objects.left)) :
    ∃ (I : Type u) (_ : Nonempty I) (V : I → Set G.objects.left),
      (∀ i, IsOpen (V i) ∧ IsCompact (V i)) ∧
        G.target.left.base '' (G.source.left.base ⁻¹' (W : Set G.objects.left)) = ⋂ i, V i
```

## Tag 0APB, a lemma

[Tag 0APB](https://stacks.math.columbia.edu/tag/0APB) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.exists_invariant_open_between_compact_opens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/FlatGroupoid.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/InvariantSubscheme/FlatGroupoid.lean#L118).

> **Stacks Project, Tag 0APB.** A quasi-compact open in the object scheme of a quasi-compact
> flat groupoid scheme has an invariant open neighbourhood contained in a quasi-compact open.

```lean
theorem exists_invariant_open_between_compact_opens
    (G : GroupoidScheme S)
    [QuasiCompact G.source.left] [Flat G.source.left]
    [QuasiCompact G.target.left] [Flat G.target.left]
    [QuasiSeparatedSpace G.objects.left]
    (W : G.objects.left.Opens) (hW : IsCompact (W : Set G.objects.left)) :
    ∃ (V W' : G.objects.left.Opens),
      IsInvariantOpen G V ∧ IsCompact (W' : Set G.objects.left) ∧
        W ≤ V ∧ V ≤ W'
```

**`AlgebraicGeometry.GroupoidScheme.exists_isInvariantOpen_isCompact_between`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantOpenBetween.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/Stabilizer/InvariantOpenBetween.lean#L103).

> Let `(U, R, s, t, c)` be a groupoid scheme with `s` and `t`
> quasi-compact and flat and with `U` quasi-separated, and let `W ⊆ U` be a quasi-compact open.
> Then there is an invariant open `V` and a quasi-compact open `W'` with `W ⊆ V ⊆ W' ⊆ U`.

```lean
theorem exists_isInvariantOpen_isCompact_between
    [QuasiCompact G.source.left] [Flat G.source.left]
    [QuasiCompact G.target.left] [Flat G.target.left]
    [QuasiSeparatedSpace G.objects.left]
    (W : G.objects.left.Opens) (hW : IsCompact (W : Set G.objects.left)) :
    ∃ V W' : G.objects.left.Opens,
      IsInvariantOpen G V ∧ IsCompact (W' : Set G.objects.left) ∧
        (W : Set G.objects.left) ⊆ (V : Set G.objects.left) ∧
        (V : Set G.objects.left) ⊆ (W' : Set G.objects.left)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 39.19, Tag 03LN](https://stacks.math.columbia.edu/tag/03LN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
