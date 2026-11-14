---
declaration: module
origin: cited
lean: TwoHiggsDoublet.add_fst, TwoHiggsDoublet.add_snd, TwoHiggsDoublet.zero_fst, TwoHiggsDoublet.zero_snd, TwoHiggsDoublet.smul_fst, TwoHiggsDoublet.smul_snd, TwoHiggsDoublet.neg_fst, TwoHiggsDoublet.neg_snd
statement: formalized
proof: formalized
---

# The Module structure on the two Higgs doublet model

The module `PhyslibAlpha.Particles.BeyondTheStandardModel.TwoHDM.Module`, [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean): 14 declarations (6 instances with no name), none with a docstring.

> The complex vector space (module) structure on two Higgs doublet configurations.

## i. Overview

> Configurations of the two Higgs doublet model are pairs of Higgs vectors `(Φ1, Φ2)`. This file
> defines addition, zero, negation and complex scalar multiplication componentwise, and assembles
> them into an additive commutative group and a `ℂ`-module structure on `TwoHiggsDoublet`.

## ii. Key results

> - `AddCommGroup TwoHiggsDoublet` : the additive commutative group structure (an instance).
> - `Module ℂ TwoHiggsDoublet` : the `ℂ`-module structure (an instance).

## iv. References

> * None.

## A. The structure of a module

**An instance with no name**, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L44).

```lean
instance : Add TwoHiggsDoublet
```

**`TwoHiggsDoublet.add_fst`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L48).

```lean
lemma add_fst (H1 H2 : TwoHiggsDoublet) : (H1 + H2).Φ1 = H1.Φ1 + H2.Φ1
```

**`TwoHiggsDoublet.add_snd`**, a lemma, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L51).

```lean
lemma add_snd (H1 H2 : TwoHiggsDoublet) : (H1 + H2).Φ2 = H1.Φ2 + H2.Φ2
```

**An instance with no name**, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L53).

```lean
instance : Zero TwoHiggsDoublet
```

**`TwoHiggsDoublet.zero_fst`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L57).

```lean
lemma zero_fst : (0 : TwoHiggsDoublet).Φ1 = 0
```

**`TwoHiggsDoublet.zero_snd`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L60).

```lean
lemma zero_snd : (0 : TwoHiggsDoublet).Φ2 = 0
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L62).

```lean
instance : SMul ℂ TwoHiggsDoublet
```

**`TwoHiggsDoublet.smul_fst`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L66).

```lean
lemma smul_fst (c : ℂ) (H : TwoHiggsDoublet) : (c • H).Φ1 = c • H.Φ1
```

**`TwoHiggsDoublet.smul_snd`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L69).

```lean
lemma smul_snd (c : ℂ) (H : TwoHiggsDoublet) : (c • H).Φ2 = c • H.Φ2
```

**An instance with no name**, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L71).

```lean
instance : Neg TwoHiggsDoublet
```

**`TwoHiggsDoublet.neg_fst`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L75).

```lean
lemma neg_fst (H : TwoHiggsDoublet) : (-H).Φ1 = -H.Φ1
```

**`TwoHiggsDoublet.neg_snd`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L78).

```lean
lemma neg_snd (H : TwoHiggsDoublet) : (-H).Φ2 = -H.Φ2
```

**An instance with no name**, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L80).

```lean
instance : AddCommGroup TwoHiggsDoublet
```

**An instance with no name**, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean#L94).

```lean
instance : Module ℂ TwoHiggsDoublet
```

## Depends on

- [The Two Higgs Doublet Model](../../../physlib/particles/beyondthestandardmodel/twohdm/basic.md)

## Sources

- [PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/BeyondTheStandardModel/TwoHDM/Module.lean)
