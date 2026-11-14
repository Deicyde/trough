---
declaration: module
origin: cited
lean: SpaceTime.properTime, SpaceTime.properTime_pos_ofTimeLike, SpaceTime.properTime_zero_ofLightLike, SpaceTime.properTime_zero_ofSpaceLike
statement: formalized
proof: formalized
---

# Proper Time

The module `Physlib.Relativity.Special.ProperTime`, [Physlib/Relativity/Special/ProperTime.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean): 4 declarations, 1 with a docstring.

> This file introduces 4d Minkowski spacetime.

**`SpaceTime.properTime`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean#L33).

> The proper time from `q` to `p`. Defaults to zero if `p` and `q`
> have a space-like separation.

```lean
def properTime {d : ℕ} (q p : SpaceTime d) : ℝ
```

**`SpaceTime.properTime_pos_ofTimeLike`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean#L36).

```lean
lemma properTime_pos_ofTimeLike {d : ℕ} (q p : SpaceTime d)
    (h : causalCharacter (p - q) = .timeLike) :
    0 < properTime q p
```

**`SpaceTime.properTime_zero_ofLightLike`**, a lemma, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean#L43).

```lean
lemma properTime_zero_ofLightLike {d : ℕ} (q p : SpaceTime d)
    (h : causalCharacter (p - q) = .lightLike) :
    properTime q p = 0
```

**`SpaceTime.properTime_zero_ofSpaceLike`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean#L50).

```lean
lemma properTime_zero_ofSpaceLike {d : ℕ} (q p : SpaceTime d)
    (h : causalCharacter (p - q) = .spaceLike) :
    properTime q p = 0
```

## Depends on

- [Physlib.Relativity.Causality.Basic](../causality/basic.md)
- [Spacetime](../../spaceandtime/spacetime/basic.md)

## Proof depends on

- [Physlib.Relativity.Causality.LightLike](../causality/lightlike.md)
- [Physlib.Relativity.Causality.TimeLike](../causality/timelike.md)

## Sources

- [Physlib/Relativity/Special/ProperTime.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/Special/ProperTime.lean)
