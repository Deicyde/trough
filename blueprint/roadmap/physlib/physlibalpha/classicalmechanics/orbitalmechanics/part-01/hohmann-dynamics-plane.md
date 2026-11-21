---
declaration: module
origin: cited
lean: ClassicalMechanics.HohmannTransfer.pack, ClassicalMechanics.HohmannTransfer.cross, ClassicalMechanics.HohmannTransfer.sqSpeed, ClassicalMechanics.HohmannTransfer.pack_re, ClassicalMechanics.HohmannTransfer.pack_im, ClassicalMechanics.HohmannTransfer.sqSpeed_eq_norm_sq, ClassicalMechanics.HohmannTransfer.norm_pack_sq, ClassicalMechanics.HohmannTransfer.norm_pack_eq
statement: formalized
proof: formalized
---

# Planar coordinates for the Hohmann transfer

The module `PhyslibAlpha.ClassicalMechanics.OrbitalMechanics.Hohmann.Dynamics.Plane`, [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean): 13 declarations, 3 with a docstring.

> Complex coordinates carry the Euclidean norm.

## i. Overview

> The real and imaginary parts represent Cartesian coordinates. The norm and derivative identities
> let later modules work with both components while retaining the Euclidean norm.

## ii. Key results

> - `pack_deriv` gives the main result of this module.

## iv. References

> - [ref: hohmann\_jpl\_orbital\_mechanics] describes the Hohmann ellipse and its apses.

## A. Cartesian coordinates and differentiation

**`ClassicalMechanics.HohmannTransfer.pack`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L52).

> A planar vector with the given Cartesian coordinates.

```lean
def pack (x y : ℝ) : ℂ
```

**`ClassicalMechanics.HohmannTransfer.cross`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L54).

> The signed scalar component of the cross product normal to the plane.

```lean
def cross (z w : ℂ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.sqSpeed`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L56).

> The squared Euclidean speed of a planar velocity.

```lean
def sqSpeed (z : ℂ) : ℝ
```

**`ClassicalMechanics.HohmannTransfer.pack_re`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L58).

```lean
lemma pack_re (x y : ℝ) : (pack x y).re = x
```

**`ClassicalMechanics.HohmannTransfer.pack_im`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L59).

```lean
lemma pack_im (x y : ℝ) : (pack x y).im = y
```

**`ClassicalMechanics.HohmannTransfer.sqSpeed_eq_norm_sq`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L60).

```lean
lemma sqSpeed_eq_norm_sq (z : ℂ) : sqSpeed z = ‖z‖ ^ 2
```

**`ClassicalMechanics.HohmannTransfer.norm_pack_sq`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L63).

```lean
lemma norm_pack_sq (x y : ℝ) : ‖pack x y‖ ^ 2 = x ^ 2 + y ^ 2
```

**`ClassicalMechanics.HohmannTransfer.norm_pack_eq`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L65).

```lean
lemma norm_pack_eq {x y r : ℝ} (hr : 0 ≤ r) (hs : x^2+y^2=r^2) :
    ‖pack x y‖ = r
```

**`ClassicalMechanics.HohmannTransfer.norm_pack_vertical`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L70).

```lean
lemma norm_pack_vertical (y : ℝ) : ‖pack 0 y‖ = |y|
```

**`ClassicalMechanics.HohmannTransfer.pack_deriv`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L73).

```lean
lemma pack_deriv {f g : ℝ → ℝ} {f' g' t : ℝ}
    (hf : HasDerivAt f f' t) (hg : HasDerivAt g g' t) :
    HasDerivAt (fun s => pack (f s) (g s)) (pack f' g') t
```

**`ClassicalMechanics.HohmannTransfer.pack_smul`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L81).

```lean
lemma pack_smul (c x y : ℝ) : c • pack x y = pack (c*x) (c*y)
```

**`ClassicalMechanics.HohmannTransfer.pack_sub`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L83).

```lean
lemma pack_sub (x y u v : ℝ) : pack x y - pack u v = pack (x-u) (y-v)
```

**`ClassicalMechanics.HohmannTransfer.pack_neg`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean#L84).

```lean
lemma pack_neg (x y : ℝ) : -pack x y = pack (-x) (-y)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ClassicalMechanics/OrbitalMechanics/Hohmann/Dynamics/Plane.lean)
