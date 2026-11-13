---
declaration: module
origin: cited
lean: SpecialRelativity.InstantaneousTwinParadox, SpecialRelativity.InstantaneousTwinParadox.properTimeTwinA, SpecialRelativity.InstantaneousTwinParadox.properTimeTwinB, SpecialRelativity.InstantaneousTwinParadox.ageGap, SpecialRelativity.InstantaneousTwinParadox.ageGap_eq, SpecialRelativity.InstantaneousTwinParadox.ageGap_eq_zero_iff, SpecialRelativity.InstantaneousTwinParadox.ageGap_nonneg, SpecialRelativity.InstantaneousTwinParadox.example1
statement: formalized
proof: formalized
---

# Twin Paradox

The module `Physlib.Relativity.Special.TwinParadox.Basic`, [Physlib/Relativity/Special/TwinParadox/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean): 12 declarations, 9 with a docstring.

> The twin paradox corresponds to the following scenario:
>
> Two twins start at the same point `startPoint` in spacetime.
> Twin A travels at constant speed to the spacetime point `endPoint`,
> whilst twin B makes a detour through the spacetime `twinBMid` and then to `endPoint`.
>
> In this file, we assume that both twins travel at constant speed,
> and that the acceleration of Twin B is instantaneous.
>
> The conclusion of this scenario is that Twin A will be older than Twin B when they meet at
> `endPoint`. This is something we show here with an explicit example.
>
> The origin of the twin paradox dates back to Paul Langevin in 1911.

**`SpecialRelativity.InstantaneousTwinParadox`**, a structure, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L41).

> The twin paradox assuming instantaneous acceleration.

```lean
structure InstantaneousTwinParadox where
  /-- The starting point of both twins. -/
  startPoint : SpaceTime 3
  /-- The end point of both twins. -/
  endPoint : SpaceTime 3
  /-- The point twin B travels to between the start point and the end point. -/
  twinBMid : SpaceTime 3
  endPoint_causallyFollows_startPoint : causallyFollows startPoint endPoint
  twinBMid_causallyFollows_startPoint : causallyFollows startPoint twinBMid
  endPoint_causallyFollows_twinBMid : causallyFollows twinBMid endPoint
```

**`SpecialRelativity.InstantaneousTwinParadox.properTimeTwinA`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L58).

> The proper time experienced by twin A travelling at constant speed
> from `T.startPoint` to `T.endPoint`.

```lean
def properTimeTwinA : ℝ
```

**`SpecialRelativity.InstantaneousTwinParadox.properTimeTwinB`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L63).

> The proper time experienced by twin B travelling at constant speed
> from `T.startPoint` to `T.twinBMid`, and then from `T.twinBMid`
> to `T.endPoint`.

```lean
def properTimeTwinB : ℝ
```

**`SpecialRelativity.InstantaneousTwinParadox.ageGap`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L67).

> The proper time of twin A minus the proper time of twin B.

```lean
def ageGap : ℝ
```

**`SpecialRelativity.InstantaneousTwinParadox.ageGap_eq`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L71).

> The age gap in terms of the two legs of Twin B, `u = twinBMid - startPoint` and
> `v = endPoint - twinBMid`: `ageGap = √⟪u + v, u + v⟫ₘ - (√⟪u, u⟫ₘ + √⟪v, v⟫ₘ)`.

```lean
lemma ageGap_eq :
    T.ageGap = √⟪(T.twinBMid - T.startPoint) + (T.endPoint - T.twinBMid),
      (T.twinBMid - T.startPoint) + (T.endPoint - T.twinBMid)⟫ₘ
      - (√⟪T.twinBMid - T.startPoint, T.twinBMid - T.startPoint⟫ₘ
        + √⟪T.endPoint - T.twinBMid, T.endPoint - T.twinBMid⟫ₘ)
```

**`SpecialRelativity.InstantaneousTwinParadox.ageGap_eq_zero_iff`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L86).

> The age gap vanishes if and only if the turning point of Twin B lies on the straight
> worldline of Twin A between the start and end points: Twin B does not turn. This is the
> equality case of the reverse triangle inequality (`sqrt_add_eq_iff_of_causallyFollows`,
> `minkowskiProduct_eq_iff_of_causallyFollows`).

```lean
lemma ageGap_eq_zero_iff : T.ageGap = 0 ↔
    ∃ μ ∈ Set.Icc (0 : ℝ) 1, T.twinBMid = T.startPoint + μ • (T.endPoint - T.startPoint)
```

**`SpecialRelativity.InstantaneousTwinParadox.ageGap_nonneg`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L127).

> In the twin paradox with instantaneous acceleration, Twin A is always at least as old as
> Twin B: the age gap is nonnegative. This is the reverse triangle inequality of Minkowski space
> (`sqrt_add_sqrt_le_sqrt_add_of_causallyFollows`) applied to the two legs of Twin B.

```lean
lemma ageGap_nonneg : 0 ≤ T.ageGap
```

## Example 1

**`SpecialRelativity.InstantaneousTwinParadox.example1`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L145).

> The twin paradox in which:
> - Twin A starts at `0` and travels at constant
>   speed to `[15, 0, 0, 0]`.
> - Twin B starts at `0` and travels at constant speed to
>   `[7.5, 6, 0, 0]` and then at (different) constant speed to `[15, 0, 0, 0]`.

```lean
def example1 : InstantaneousTwinParadox
```

**`SpecialRelativity.InstantaneousTwinParadox.example1_properTimeTwinA`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L182).

```lean
lemma example1_properTimeTwinA : example1.properTimeTwinA = 15
```

**`SpecialRelativity.InstantaneousTwinParadox.example1_properTimeTwinB`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L186).

```lean
lemma example1_properTimeTwinB : example1.properTimeTwinB = 9
```

**`SpecialRelativity.InstantaneousTwinParadox.example1_ageGap`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L191).

```lean
lemma example1_ageGap : example1.ageGap = 6
```

**`SpecialRelativity.InstantaneousTwinParadox.example1_ageGap_ne_zero`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean#L195).

> The example above has a nonzero age gap.

```lean
lemma example1_ageGap_ne_zero : example1.ageGap ≠ 0
```

## Depends on

- [Proper Time](propertime.md)

## Proof depends on

- [Vectors in the causal future of the origin](../causality/causallyfollows.md)

## Sources

- [Physlib/Relativity/Special/TwinParadox/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/TwinParadox/Basic.lean)
