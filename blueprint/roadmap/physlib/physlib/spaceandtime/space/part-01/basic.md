---
declaration: module
origin: cited
lean: Space, Space.eq_of_val, Space.val_eq_iff, Space.eq_of_apply, Space.vadd_val, Space.vadd_apply, Space.vadd_transitive, Space.vsub_apply
statement: formalized
proof: formalized
---

# Space

The module `Physlib.SpaceAndTime.Space.Basic`, [Physlib/SpaceAndTime/Space/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean): 25 declarations (13 instances with no name), 2 with a docstring.

> In this module, we define the the type `Space d` which corresponds
> to `d`-dimensional flat Euclidean space and prove some properties about it.
>
> The scope of this module is to define on `Space d` basic instances related translations and
> the metric. We do not here define the structure of a `Module` on `Space d`, as this is done in
> `Physlib.SpaceAndTime.Space.Module`.
>
> Physlib sits downstream of Mathlib, and above we import the necessary Mathlib modules
> which contain (perhaps transitively through imports) the definitions and theorems we need.

## Implementation details

> The exact implementation of `Space d` into Physlib is discussed in numerous places
> on the Lean Zulip, including:
>
> - https://leanprover.zulipchat.com/#narrow/channel/479953-Physlib/topic/Space.20vs.20EuclideanSpace/with/575332888
>
> There is a choice between defining `Space d` as an `abbrev` of `EuclideanSpace ℝ (Fin d)`,
> as a `def` of a type with value `EuclideanSpace ℝ (Fin d)` or as a structure
> with a field `val : Fin d → ℝ` :
>
> +---------------------------------------------------+---------+-------+-----------+
> |                                                   | abbrev  |  def  | structure |
> +---------------------------------------------------+---------+-------+-----------+
> | allows casting from `EuclideanSpace`              |   yes   |  yes  |    no     |
> | carries instances from `EuclideanSpace`           |   yes   |  no   |    no     |
> | requires reproving of lemmas from `EuclideanSpace`|   no    |  yes  |    yes    |
> +---------------------------------------------------+---------+-------+-----------+
>
> The `structure` is the most conservative choice, as everything needs redefining. However,
> there is are two benefits of using it:
>
> 1. It allows us to be precise about the instances we define on `Space d`, and makes
>   future refactoring of those instances easier.
> 2. It allows us to give the necessary physics context to results about `Space d`, which
>   would not otherwise be possible if we reuse results from Mathlib.
>
> In this module we give `Space d` the instances of a `NormedAddTorsor`
> and a `MetricSpace`. These physically correspond to the statement that
> you can add a vector to a point in space, and that there is a notion of distance between
> points in space. This notion of distance corresponds to a choice of length unit.
>
> In `Physlib.SpaceAndTime.Space.Module` we give `Space d` the structure of a `Module`
> (aka vector space), a `Norm` and an `InnerProductSpace`. These require certain choices, for example
> the choice of a zero in `Space d`.
>
> This module structure is necessary in numerous places. For example,
> the normal derivatives used by physicists `∂_x, ∂_y, ∂_z` require a
> module structure.
>
> Because of this, one should be careful to avoid using the explicit zero in `Space d`,
> or adding two `Space d` values together. Where possible one should use
> the `VAdd (EuclideanSpace ℝ (Fin d)) (Space d)` instance instead.

## A. The `Space` type

**`Space`**, a structure, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L82).

> The type `Space d` is the world-volume which corresponds to
> `d` dimensional (flat) Euclidean space with a given (but arbitrary)
> choice of length unit, and a given (but arbitrary) choice of zero.
>
> The default value of `d` is `3`. Thus `Space = Space 3`

```lean
structure Space (d : ℕ := 3) where
  /-- The underlying map `Fin d → ℝ` associated with a point in `Space`. -/
  val : Fin d → ℝ
```

**`Space.eq_of_val`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L88).

```lean
lemma eq_of_val {d} {p q : Space d} (h : p.val = q.val) :
    p = q
```

**`Space.val_eq_iff`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L95).

```lean
lemma val_eq_iff {d} {p q : Space d} :
    p.val = q.val ↔ p = q
```

## B. Instances on `Space`

## B.1. Instance of coercion to functions

**An instance with no name**, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L114).

```lean
instance {d} : CoeFun (Space d) (fun _ => Fin d → ℝ)
```

**`Space.eq_of_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L118).

```lean
lemma eq_of_apply {d} {p q : Space d}
    (h : ∀ i : Fin d, p i = q i) : p = q
```

## B.2. The Non-emptiness

**An instance with no name**, [line 130](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L130).

```lean
instance {d} : Nonempty (Space d)
```

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L133).

```lean
instance : Subsingleton (Space 0)
```

## B.3.1. The additive action

**An instance with no name**, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L142).

```lean
noncomputable instance : VAdd (EuclideanSpace ℝ (Fin d)) (Space d)
```

**`Space.vadd_val`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L146).

```lean
lemma vadd_val {d} (v : EuclideanSpace ℝ (Fin d)) (s : Space d) :
    (v +ᵥ s).val = fun i => v i + s.val i
```

**`Space.vadd_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L150).

```lean
lemma vadd_apply {d} (v : EuclideanSpace ℝ (Fin d))
    (s : Space d) (i : Fin d) :
    (v +ᵥ s) i = v i + s i
```

**`Space.vadd_transitive`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L154).

```lean
lemma vadd_transitive {d} (s1 s2 : Space d) :
    ∃ v : EuclideanSpace ℝ (Fin d), v +ᵥ s1 = s2
```

**An instance with no name**, [line 160](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L160).

```lean
noncomputable instance : AddAction (EuclideanSpace ℝ (Fin d)) (Space d)
```

## B.3.2. Subtraction

**An instance with no name**, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L175).

```lean
noncomputable instance {d} : VSub (EuclideanSpace ℝ (Fin d)) (Space d)
```

**`Space.vsub_apply`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L179).

```lean
lemma vsub_apply {d} (s1 s2 : Space d) (i : Fin d) :
    (s1 -ᵥ s2) i = s1 i - s2 i
```

## B.3.3. AddTorsor instance

**An instance with no name**, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L188).

```lean
noncomputable instance {d} : AddTorsor (EuclideanSpace ℝ (Fin d)) (Space d)
```

## B.4. PseudoMetricSpace

**An instance with no name**, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L202).

```lean
noncomputable instance {d} : Dist (Space d)
```

**`Space.dist_eq`**, a lemma, [line 205](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L205).

```lean
lemma dist_eq {d} (p q : Space d) : dist p q = √ (∑ i, (p i - q i) ^ 2)
```

**An instance with no name**, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L207).

```lean
noncomputable instance {d} : PseudoMetricSpace (Space d)
```

## B.5. NormAddTorsor instance

**An instance with no name**, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L223).

```lean
noncomputable instance {d} : NormedAddTorsor (EuclideanSpace ℝ (Fin d)) (Space d)
```

## B.6. Metric space instance

**An instance with no name**, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L232).

```lean
noncomputable instance {d} : MetricSpace (Space d)
```

## B.7. Non-trivality

**`Space.instNontrivial`**, an instance, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L241).

```lean
instance instNontrivial {d : ℕ} [NeZero d] : Nontrivial (Space d)
```

## C. Model structure (i.e. structure of a manifold)

**`Space.homEuclideanSpaceSpace`**, a def, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L260).

> `Space d` is homoemorphic to d-dimensional euclidean space. This is used to define the `IsManifold`
> instance on `Space d`.

```lean
noncomputable def homEuclideanSpaceSpace (d : ℕ) : EuclideanSpace ℝ (Fin d) ≃ₜ Space d
```

**An instance with no name**, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L274).

```lean
noncomputable instance (d : ℕ) : ChartedSpace (EuclideanSpace ℝ (Fin d)) (Space d)
```

**An instance with no name**, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L277).

```lean
instance (d : ℕ) : IsManifold (𝓡 d) ⊤ (Space d)
```

**`Space.chartAt_eq`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean#L280).

```lean
lemma chartAt_eq (d : ℕ) (p : Space d) :
    chartAt (EuclideanSpace ℝ (Fin d)) p =
    (homEuclideanSpaceSpace d).symm.toOpenPartialHomeomorph
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/SpaceAndTime/Space/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/Space/Basic.lean)
