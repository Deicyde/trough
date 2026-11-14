---
declaration: module
origin: cited
lean: TimeMan, TimeMan.val_surjective, TimeMan.val_range, TimeMan.val_inducing, TimeMan.val_injective, TimeMan.val_isOpenEmbedding, TimeMan.isOpen_iff, TimeMan.valHomeomorphism
statement: formalized
proof: formalized
---

# The time manifold

The module `Physlib.SpaceAndTime.Time.TimeMan`, [Physlib/SpaceAndTime/Time/TimeMan.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean): 14 declarations (4 instances with no name), 7 with a docstring.

> In this module we define the type `TimeMan`, corresponding to the time manifold,
> without any additional structures except an orientation, such as a choice of metric or origin.
> I.e. it is a manifold diffeomorphic to `ℝ` with no additional structure.
>
> If you are looking for a more standard version of time see the type `Time`.
>
> `TimeMan` is sometimes called topological time, due to the absence of a metric, and its use in
> topological field theories.

## Implementation details

> The manifold `TimeMan` is defined via the type `ℝ`, and thus inherits a given choice
> of map `TimeMan.val : TimeMan → ℝ`, which can be extended to a homeomorphism or a
> diffeomorphism. When using `TimeMan.val`, one should be aware that using it does
> constitute a choice being made.

**`TimeMan`**, a structure, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L36).

> The type `TimeMan` represents the time manifold.
> Mathematically `TimeMan` is a manifold diffeomorphic to `ℝ` with an orientation but no additional
> structure.

```lean
structure TimeMan where
  /-- The choice of a map from `TimeMan` to `ℝ`. -/
  val : ℝ
```

## The topology on TimeMan.

> The topology on `TimeMan` is induced from the topology on `ℝ`, via the choice
> of map `TimeMan.val`.

**An instance with no name**, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L52).

> The instance of a topological space on `TimeMan` induced by the map `TimeMan.val`. s

```lean
instance : TopologicalSpace TimeMan
```

**`TimeMan.val_surjective`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L55).

```lean
lemma val_surjective : Function.Surjective TimeMan.val
```

**`TimeMan.val_range`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L60).

```lean
lemma val_range : Set.range val = Set.univ
```

**`TimeMan.val_inducing`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L63).

```lean
lemma val_inducing : Topology.IsInducing TimeMan.val
```

**`TimeMan.val_injective`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L66).

```lean
lemma val_injective : Function.Injective TimeMan.val
```

**`TimeMan.val_isOpenEmbedding`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L72).

```lean
lemma val_isOpenEmbedding : Topology.IsOpenEmbedding TimeMan.val
```

**`TimeMan.isOpen_iff`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L78).

```lean
lemma isOpen_iff {s : Set TimeMan} :
    IsOpen s ↔ IsOpen (TimeMan.val '' s)
```

**`TimeMan.valHomeomorphism`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L83).

> The choice of map `Time.val` from `TimeMan` to `ℝ` as a homeomorphism.

```lean
def valHomeomorphism : TimeMan ≃ₜ ℝ
```

## The manifold structure on TimeMan

**An instance with no name**, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L112).

> The structure of a charted space on `TimeMan`

```lean
instance : ChartedSpace ℝ TimeMan
```

**An instance with no name**, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L124).

> The structure of a manifold on `TimeMan` induced by the choice of map `Time.val`.

```lean
instance : IsManifold 𝓘(ℝ, ℝ) ω TimeMan
```

**`TimeMan.val_contDiff`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L131).

```lean
lemma val_contDiff : ContMDiff 𝓘(ℝ, ℝ) 𝓘(ℝ, ℝ) ω TimeMan.val
```

**`TimeMan.valDiffeomorphism`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L136).

> The choice of map `Time.val` from `TimeMan` to `ℝ` as a diffeomorphism.

```lean
noncomputable def valDiffeomorphism : TimeMan ≃ₘ^ω⟮𝓘(ℝ, ℝ), 𝓘(ℝ, ℝ)⟯ ℝ
```

## The orientation on TimeMan

**An instance with no name**, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean#L150).

> The instance of an orientation on TimeMan.

```lean
instance : LE TimeMan
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/Time/TimeMan.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Time/TimeMan.lean)
