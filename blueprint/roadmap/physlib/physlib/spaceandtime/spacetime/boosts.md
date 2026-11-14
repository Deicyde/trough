---
declaration: module
origin: cited
lean: SpaceTime.boost_x_smul, SpaceTime.boost_zero_apply_time_space
statement: formalized
proof: formalized
---

# Boosts of space time

The module `Physlib.SpaceAndTime.SpaceTime.Boosts`, [Physlib/SpaceAndTime/SpaceTime/Boosts.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Boosts.lean): 2 declarations, none with a docstring.

## i. Overview

> In this module we consider boosts acting on points in space time,and recover simple
> formulae for such applications.
>
> Note that the material here currently assumes that the speed of light `c = 1`.

## ii. Key results

> - `boost_x_smul` : The action of a boost in the x-direction on a point in space time.

## iv. References

> * https://en.wikipedia.org/wiki/Lorentz\_transformation. [ref: wiki\_lorentz\_transformation]

## A. The action of a boost in the x-direction

> We show that boosting in the `x`-direction takes `(t, x, y, z)` to
> `(γ (t - β x), γ (x - β t), y, z)`.

**`SpaceTime.boost_x_smul`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Boosts.lean#L52).

```lean
lemma boost_x_smul (β : ℝ) (hβ : |β| < 1) (x : SpaceTime) :
    LorentzGroup.boost (d := 3) 0 β hβ • x =
      fun | Sum.inl 0 => γ β * (x (Sum.inl 0) - β * x (Sum.inr 0))
          | Sum.inr 0 => γ β * (x (Sum.inr 0) - β * x (Sum.inl 0))
          | Sum.inr 1=> x (Sum.inr 1)
          | Sum.inr 2=> x (Sum.inr 2)
```

**`SpaceTime.boost_zero_apply_time_space`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Boosts.lean#L64).

```lean
lemma boost_zero_apply_time_space {d : ℕ} {β : ℝ} (hβ : |β| < 1) (c : SpeedOfLight)
    (t : Time) (x : Space d.succ) :
    ((boost (0 : Fin d.succ) β hβ)⁻¹ • (SpaceTime.toTimeAndSpace c).symm (t, x)) =
    (SpaceTime.toTimeAndSpace c).symm
    (γ β * (t.val + β /c * x 0),
    ⟨fun
      | (0 : Fin d.succ) => γ β * (x 0 + c * β * t.val)
      | ⟨Nat.succ n, ih⟩ => x ⟨Nat.succ n, ih⟩⟩)
```

## Depends on

- [Boosts in the Lorentz group](../../relativity/lorentzgroup/boosts-basic.md)
- [Spacetime](basic.md)

## Sources

- [Physlib/SpaceAndTime/SpaceTime/Boosts.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/SpaceAndTime/SpaceTime/Boosts.lean)
