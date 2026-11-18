---
declaration: module
origin: cited
lean: PoincareGroup.timeComponent_eq_minkowski, PoincareGroup.causallyFollows_zero_smul, PoincareGroup.smul_sub_smul, PoincareGroup.causallyFollows_zero_smul_iff, PoincareGroup.causallyFollows_smul_iff, PoincareGroup.causallyFollows_smul_iff_of_not, PoincareGroup.causalFuture_smul, PoincareGroup.causalPast_smul
statement: formalized
proof: formalized
---

# The causal structure is Poincaré invariant

The module `PhyslibAlpha.Relativity.Poincare.Causality`, [PhyslibAlpha/Relativity/Poincare/Causality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean): 11 declarations, 11 with a docstring.

> Orthochronous Poincaré transformations preserve causal futures and pasts.

## i. Overview

> An event `q` causally follows `p` when the difference lies in the closed future light cone.
> A Lorentz transformation preserves the Minkowski product. An orthochronous one also preserves the
> direction of time, so it maps the future light cone to itself. A translation does not change
> differences. So an orthochronous Poincaré transformation maps the causal future of a set to the
> causal future of the image. A transformation that reverses time exchanges causal future and past.

## ii. Key results

> - `causallyFollows_zero_smul` : orthochronous Lorentz maps preserve the future light cone.
> - `causallyFollows_smul_iff` : orthochronous Poincaré maps preserve causal order.
> - `causalFuture_smul` : the causal future of the image is the image of the causal future.
> - `causalFuture_smul_of_not` : a time-reversing map sends the causal future to the causal past.

## iv. References

> None.

## A. The future light cone

> - `causallyFollows_zero_smul` : orthochronous Lorentz maps preserve the future light cone.

## B. The causal order

> - `causallyFollows_smul_iff` : orthochronous Poincaré maps preserve causal order.

## C. Causal futures and pasts of sets

> - `causalFuture_smul` : the causal future of the image is the image of the causal future.

**`PoincareGroup.timeComponent_eq_minkowski`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L69).

> The time component is the Minkowski product with the unit time vector.

```lean
lemma timeComponent_eq_minkowski (p : SpaceTime d) :
    p.timeComponent = ⟪p, Lorentz.Vector.basis (Sum.inl 0)⟫ₘ
```

**`PoincareGroup.causallyFollows_zero_smul`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L75).

> An orthochronous Lorentz transformation maps the closed future light cone into itself.

```lean
lemma causallyFollows_zero_smul {Λ : LorentzGroup d} (hΛ : LorentzGroup.IsOrthochronous Λ)
    {u : SpaceTime d} (hu : causallyFollows 0 u) : causallyFollows 0 (Λ • u)
```

**`PoincareGroup.smul_sub_smul`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L103).

> The vectors between two transformed events are the Lorentz image of the original vector.

```lean
lemma smul_sub_smul (g : PoincareGroup d) (p q : SpaceTime d) :
    g • q - g • p = g.lorentz • (q - p)
```

**`PoincareGroup.causallyFollows_zero_smul_iff`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L113).

> An orthochronous Lorentz transformation preserves the closed future light cone.

```lean
lemma causallyFollows_zero_smul_iff {Λ : LorentzGroup d} (hΛ : LorentzGroup.IsOrthochronous Λ)
    (u : SpaceTime d) : causallyFollows 0 (Λ • u) ↔ causallyFollows 0 u
```

**`PoincareGroup.causallyFollows_smul_iff`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L119).

> An orthochronous Poincaré transformation preserves the causal order.

```lean
lemma causallyFollows_smul_iff {g : PoincareGroup d} (hg : g.IsOrthochronous) (p q : SpaceTime d) :
    causallyFollows (g • p) (g • q) ↔ causallyFollows p q
```

**`PoincareGroup.causallyFollows_smul_iff_of_not`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L127).

> A Poincaré transformation that reverses time reverses the causal order.

```lean
lemma causallyFollows_smul_iff_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (p q : SpaceTime d) : causallyFollows (g • p) (g • q) ↔ causallyFollows q p
```

**`PoincareGroup.causalFuture_smul`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L143).

> An orthochronous Poincaré transformation maps the causal future of a set to the causal
> future of its image.

```lean
lemma causalFuture_smul {g : PoincareGroup d} (hg : g.IsOrthochronous) (K : Set (SpaceTime d)) :
    (causalRelation d).causalFuture (g • K) = g • (causalRelation d).causalFuture K
```

**`PoincareGroup.causalPast_smul`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L159).

> An orthochronous Poincaré transformation maps the causal past of a set to the causal past of
> its image.

```lean
lemma causalPast_smul {g : PoincareGroup d} (hg : g.IsOrthochronous) (K : Set (SpaceTime d)) :
    (causalRelation d).causalPast (g • K) = g • (causalRelation d).causalPast K
```

**`PoincareGroup.causalFuture_smul_of_not`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L175).

> A Poincaré transformation that reverses time maps the causal future of a set to the causal
> past of its image.

```lean
lemma causalFuture_smul_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (K : Set (SpaceTime d)) :
    (causalRelation d).causalFuture (g • K) = g • (causalRelation d).causalPast K
```

**`PoincareGroup.causalPast_smul_of_not`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L192).

> A Poincaré transformation that reverses time maps the causal past of a set to the causal
> future of its image.

```lean
lemma causalPast_smul_of_not {g : PoincareGroup d} (hg : ¬ g.IsOrthochronous)
    (K : Set (SpaceTime d)) :
    (causalRelation d).causalPast (g • K) = g • (causalRelation d).causalFuture K
```

**`PoincareGroup.causalHull_smul`**, a lemma, [line 208](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean#L208).

> A Poincaré transformation maps the causal hull of a set to the causal hull of its image.

```lean
lemma causalHull_smul (g : PoincareGroup d) (K : Set (SpaceTime d)) :
    (causalRelation d).causalHull (g • K) = g • (causalRelation d).causalHull K
```

## Depends on

- [Light cones in time and space](../causality/lightcone.md)
- [The Poincaré group](basic.md)

## Sources

- [PhyslibAlpha/Relativity/Poincare/Causality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/Poincare/Causality.lean)
