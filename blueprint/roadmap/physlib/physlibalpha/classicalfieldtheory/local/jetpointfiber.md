---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.JetFiberData, ClassicalFieldTheory.Local.JetFiberData.ext, ClassicalFieldTheory.Local.JetFiberData.value, ClassicalFieldTheory.Local.JetFiberData.value_apply, ClassicalFieldTheory.Local.JetFiberData.zero_coord, ClassicalFieldTheory.Local.JetFiberData.add_coord, ClassicalFieldTheory.Local.JetFiberData.smul_coord, ClassicalFieldTheory.Local.JetPoint.addFiber
statement: formalized
proof: formalized
---

# Fiber directions on jet points

The module `PhyslibAlpha.ClassicalFieldTheory.Local.JetPointFiber`, [PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean): 23 declarations (4 instances with no name), 5 with a docstring.

> Affine fiber-direction structure on coordinate-level jet points.

## i. Overview

> This module adds the affine fiber-direction structure on coordinate-level jet points.
>
> At this stage, it introduces:
>
> - fiber-coordinate data on jet points,
> - affine translation and line maps in the jet fiber,
> - and the jet-fiber direction determined by a field.

## ii. Key results

> - `ClassicalFieldTheory.Local.JetFiberData`
> - `ClassicalFieldTheory.Local.JetPoint.addFiber`
> - `ClassicalFieldTheory.Local.JetPoint.lineMap`
> - `ClassicalFieldTheory.Local.jetDirectionAt`

## iv. References

> * None.

## A. Fiber-coordinate data

**`ClassicalFieldTheory.Local.JetFiberData`**, a structure, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L57).

> Fiber-coordinate data for jet points of order `k`. This records only the coordinates `u^a_I`,
> not the base point in `Space d`.

```lean
structure JetFiberData (d m k : ℕ) where
  /-- The fiber coordinates indexed by all derivative indices of order at most `k`. -/
  coord : JetCoordinates d m k
```

**An instance with no name**, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L65).

```lean
instance : CoeFun (JetFiberData d m k) (fun _ => DerivativeIndex d k → Fin m → ℝ)
```

**`ClassicalFieldTheory.Local.JetFiberData.ext`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L69).

```lean
lemma ext (V W : JetFiberData d m k) (hcoord : ∀ I a, V.coord I a = W.coord I a) : V = W
```

**`ClassicalFieldTheory.Local.JetFiberData.value`**, a def, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L82).

> The zero-th order component of a jet-fiber direction, corresponding to the field value.

```lean
def value (V : JetFiberData d m k) : EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.JetFiberData.value_apply`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L86).

```lean
lemma value_apply (V : JetFiberData d m k) (a : Fin m) :
    V.value a = V.coord 0 a
```

**An instance with no name**, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L90).

```lean
instance : Zero (JetFiberData d m k)
```

**An instance with no name**, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L93).

```lean
instance : Add (JetFiberData d m k)
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L96).

```lean
instance : SMul ℝ (JetFiberData d m k)
```

**`ClassicalFieldTheory.Local.JetFiberData.zero_coord`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L100).

```lean
lemma zero_coord (I : DerivativeIndex d k) (a : Fin m) :
    (0 : JetFiberData d m k).coord I a = 0
```

**`ClassicalFieldTheory.Local.JetFiberData.add_coord`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L104).

```lean
lemma add_coord (V W : JetFiberData d m k) (I : DerivativeIndex d k) (a : Fin m) :
    (V + W).coord I a = V.coord I a + W.coord I a
```

**`ClassicalFieldTheory.Local.JetFiberData.smul_coord`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L108).

```lean
lemma smul_coord (c : ℝ) (V : JetFiberData d m k) (I : DerivativeIndex d k) (a : Fin m) :
    (c • V).coord I a = c * V.coord I a
```

## B. Affine fiber structure on jet points

**`ClassicalFieldTheory.Local.JetPoint.addFiber`**, a def, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L123).

> Translate a jet point by a fiber-direction increment.

```lean
def addFiber (J : JetPoint d m k) (V : JetFiberData d m k) : JetPoint d m k
```

**`ClassicalFieldTheory.Local.JetPoint.lineMap`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L128).

> The affine line in jet space through `J` in the fiber direction `V`.

```lean
def lineMap (J : JetPoint d m k) (V : JetFiberData d m k) (s : ℝ) : JetPoint d m k
```

**`ClassicalFieldTheory.Local.JetPoint.addFiber_base`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L132).

```lean
lemma addFiber_base (J : JetPoint d m k) (V : JetFiberData d m k) :
    (J.addFiber V).base = J.base
```

**`ClassicalFieldTheory.Local.JetPoint.addFiber_value`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L136).

```lean
lemma addFiber_value (J : JetPoint d m k) (V : JetFiberData d m k) :
    (J.addFiber V).value = J.value + V.value
```

**`ClassicalFieldTheory.Local.JetPoint.addFiber_coord`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L142).

```lean
lemma addFiber_coord (J : JetPoint d m k) (V : JetFiberData d m k)
    (I : DerivativeIndex d k) (a : Fin m) :
    (J.addFiber V).coord I a = J.coord I a + V.coord I a
```

**`ClassicalFieldTheory.Local.JetPoint.lineMap_base`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L147).

```lean
lemma lineMap_base (J : JetPoint d m k) (V : JetFiberData d m k) (s : ℝ) :
    (J.lineMap V s).base = J.base
```

**`ClassicalFieldTheory.Local.JetPoint.lineMap_coord`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L151).

```lean
lemma lineMap_coord (J : JetPoint d m k) (V : JetFiberData d m k) (s : ℝ)
    (I : DerivativeIndex d k) (a : Fin m) :
    (J.lineMap V s).coord I a = J.coord I a + s * V.coord I a
```

## C. Fiber directions determined by fields

**`ClassicalFieldTheory.Local.jetDirectionAt`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L163).

> The jet-fiber direction determined by a field `g` at a point `x`.

```lean
noncomputable def jetDirectionAt (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) :
    JetFiberData d m k
```

**`ClassicalFieldTheory.Local.jetDirectionAt_coord`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L169).

```lean
lemma jetDirectionAt_coord (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d)
    (I : DerivativeIndex d k) (a : Fin m) :
    (jetDirectionAt k g x).coord I a = ∂^[I.1] (fun y => (g y) a) x
```

**`ClassicalFieldTheory.Local.jetDirectionAt_coord_zero`**, a lemma, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L173).

```lean
lemma jetDirectionAt_coord_zero (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (a : Fin m) :
    (jetDirectionAt k g x).coord 0 a = (g x) a
```

**`ClassicalFieldTheory.Local.jetCoordinatesAt_add_smul`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L178).

```lean
lemma jetCoordinatesAt_add_smul (k : ℕ) (f g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (s : ℝ)
    (hf : ContDiff ℝ ∞ f) (hg : ContDiff ℝ ∞ g) :
    jetCoordinatesAt k (fun y => f y + s • g y) x =
      jetCoordinatesAt k f x + s • jetCoordinatesAt k g x
```

**`ClassicalFieldTheory.Local.jetAt_add_smul`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean#L207).

```lean
lemma jetAt_add_smul (k : ℕ) (f g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (s : ℝ)
    (hf : ContDiff ℝ ∞ f) (hg : ContDiff ℝ ∞ g) :
    jetAt k (fun y => f y + s • g y) x = (jetAt k f x).lineMap (jetDirectionAt k g x) s
```

## Depends on

- [Coordinate-level jet points](jetpoint.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPointFiber.lean)
