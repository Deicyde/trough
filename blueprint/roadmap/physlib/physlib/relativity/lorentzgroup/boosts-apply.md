---
declaration: module
origin: cited
lean: Lorentz.Vector.boost_time_eq, Lorentz.Vector.boost_inr_self_eq, Lorentz.Vector.boost_inr_other_eq, Lorentz.Vector.boost_toCoord_eq
statement: formalized
proof: formalized
---

# Physlib.Relativity.LorentzGroup.Boosts.Apply

The module `Physlib.Relativity.LorentzGroup.Boosts.Apply`, [Physlib/Relativity/LorentzGroup/Boosts/Apply.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean): 4 declarations, 0 with a docstring.

## Boosts applied to Lorentz vectors

> These recover what one would describe as the ordinary Lorentz transformations
> of Lorentz vectors.

**`Lorentz.Vector.boost_time_eq`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean#L28).

```lean
lemma boost_time_eq (i : Fin d) (β : ℝ) (hβ : |β| < 1) (p : Vector d) :
    (boost i β hβ • p) (Sum.inl 0) = γ β * (p (Sum.inl 0) - β * p (Sum.inr i))
```

**`Lorentz.Vector.boost_inr_self_eq`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean#L36).

```lean
lemma boost_inr_self_eq (i : Fin d) (β : ℝ) (hβ : |β| < 1) (p : Vector d) :
    (boost i β hβ • p) (Sum.inr i) = γ β * (p (Sum.inr i) - β * p (Sum.inl 0))
```

**`Lorentz.Vector.boost_inr_other_eq`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean#L44).

```lean
lemma boost_inr_other_eq (i j : Fin d) (hji : j ≠ i) (β : ℝ) (hβ : |β| < 1) (p : Vector d) :
    (boost i β hβ • p) (Sum.inr j) = p (Sum.inr j)
```

**`Lorentz.Vector.boost_toCoord_eq`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean#L50).

```lean
lemma boost_toCoord_eq (i : Fin d) (β : ℝ) (hβ : |β| < 1) (p : Vector d) :
    (boost i β hβ • p) = fun j =>
      match j with
      | Sum.inl 0 => γ β * (p (Sum.inl 0) - β * p (Sum.inr i))
      | Sum.inr j =>
        if j = i then γ β * (p (Sum.inr i) - β * p (Sum.inl 0))
        else p (Sum.inr j)
```

## Depends on

- [Boosts in the Lorentz group](boosts-basic.md)
- [Tensorial nature of Lorentz vectors](../tensors/part-04/realtensor-vector-tensorial.md)

## Sources

- [Physlib/Relativity/LorentzGroup/Boosts/Apply.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Relativity/LorentzGroup/Boosts/Apply.lean)
