---
declaration: module
origin: cited
lean: DimensionBasis, DimensionBasis.pi, Dimension, Dimension.exponent, Dimension.ofFunction, Dimension.ofFunction_exponent, Dimension.ext, Dimension.mul_exponent
statement: formalized
proof: formalized
---

# Dimension

The module `Physlib.Units.Dimension`, [Physlib/Units/Dimension.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean): 28 declarations (6 instances with no name), 13 with a docstring.

> In this module we define the type `Dimension` which carries the dimension
> of a physical quantity.
>
> A `Dimension B` is parameterised by a *basis* `B` of base dimensions equipped with a
> `DimensionBasis` representation. Each representation is additively equivalent to assigning an
> `Exponent` to every base dimension `b : B`. The parameterisation is purely in
> the dimensional *algebra*: `Dimension B` is a `CommGroup` for every represented basis `B`
> (multiplication adds exponents, inversion negates them), so quantities can be typed by
> dimensions over any basis. The commutative-group, `Exponent`- and `ℚ`-power structures, decidable
> equality (`DecidableEq`), the base vectors `single b`, and the change-of-basis map
> `extend` are all generic in `B`.
>
> PhysLib's default basis is `LTMCTDimensionBase` — length, time, mass, charge,
> temperature — whose projections and named generators (`L𝓭`, `T𝓭`, …) live in
> `Physlib.Units.LTMCTDimensionBase`. It is *charge*-based with five generators, so it
> is **not** the SI/ISQ base-quantity set; the ISQ set is `ISQDimensionBase`, and other
> systems (Gaussian–CGS, natural units, …) are equally expressible as `Dimension B` for
> a suitable basis `B`.

## Defining dimensions

**`DimensionBasis`**, a class, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L45).

> A choice of exponent-tuple representation for a basis `B`. Native addition on `Exponents`
> is used for dimension multiplication, while `exponentEquiv` provides the basis-generic API.

```lean
class DimensionBasis (B : Type) where
  /-- The native tuple of exponents for this basis. -/
  Exponents : Type
  /-- The additive structure on native exponent tuples. -/
  [addCommGroup : AddCommGroup Exponents]
  /-- Native exponent tuples are additively equivalent to exponent functions on the basis. -/
  exponentEquiv : Exponents ≃+ (B → Dimension.Exponent)
```

**`DimensionBasis.pi`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L58).

> The function-backed exponent representation for a basis without a specialized tuple.

```lean
def pi (B : Type) : DimensionBasis B
```

**`Dimension`**, a structure, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L67).

> A dimension over a represented basis `B`. PhysLib's default basis is
> `LTMCTDimensionBase`.

```lean
structure Dimension (B : Type) [DimensionBasis B] where
  /-- The dimension's native exponent tuple. -/
  exponents : DimensionBasis.Exponents B
```

**`Dimension.exponent`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L76).

> The exponent of a dimension at a base dimension.

```lean
def exponent (d : Dimension B) : B → Exponent
```

**`Dimension.ofFunction`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L80).

> Construct a dimension from an exponent function.

```lean
def ofFunction (f : B → Exponent) : Dimension B
```

**`Dimension.ofFunction_exponent`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L84).

```lean
lemma ofFunction_exponent (f : B → Exponent) (b : B) : (ofFunction f).exponent b = f b
```

**`Dimension.ext`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L88).

```lean
lemma ext {d1 d2 : Dimension B} (h : ∀ b, d1.exponent b = d2.exponent b) : d1 = d2
```

**An instance with no name**, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L96).

```lean
instance : Mul (Dimension B)
```

**`Dimension.mul_exponent`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L100).

```lean
lemma mul_exponent (d1 d2 : Dimension B) (b : B) :
    (d1 * d2).exponent b = d1.exponent b + d2.exponent b
```

**An instance with no name**, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L104).

```lean
instance : One (Dimension B)
```

**`Dimension.one_exponent`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L108).

```lean
lemma one_exponent (b : B) : (1 : Dimension B).exponent b = 0
```

**An instance with no name**, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L111).

```lean
instance : CommGroup (Dimension B)
```

**`Dimension.inv_exponent`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L132).

```lean
lemma inv_exponent (d : Dimension B) (b : B) : d⁻¹.exponent b = -d.exponent b
```

**`Dimension.div_exponent`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L136).

```lean
lemma div_exponent (d1 d2 : Dimension B) (b : B) :
    (d1 / d2).exponent b = d1.exponent b - d2.exponent b
```

**`Dimension.npow_exponent`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L141).

```lean
lemma npow_exponent (d : Dimension B) (n : ℕ) (b : B) :
    (d ^ n).exponent b = n • d.exponent b
```

**An instance with no name**, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L147).

```lean
instance : Pow (Dimension B) ℚ
```

**`Dimension.qpow_exponent`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L151).

```lean
lemma qpow_exponent (d : Dimension B) (q : ℚ) (b : B) :
    (d ^ q).exponent b = d.exponent b * Exponent.ofRat q
```

**An instance with no name**, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L158).

> Raising a dimension to an `Exponent` power. Unlike the `ℚ`-valued power, this preserves
> reducible arithmetic for concrete fractional exponents.

```lean
instance : Pow (Dimension B) Exponent
```

**`Dimension.epow_exponent`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L162).

```lean
lemma epow_exponent (d : Dimension B) (c : Exponent) (b : B) :
    (d ^ c).exponent b = d.exponent b * c
```

**An instance with no name**, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L167).

> Decidable equality of dimensions over a finite basis `B`.

```lean
instance [Fintype B] : DecidableEq (Dimension B)
```

**`Dimension.single`**, a def, [line 173](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L173).

> The base-dimension vector for `b : B`: exponent `1` at `b`, `0` elsewhere. This
> is the generic analogue of the named generators `L𝓭`, `T𝓭`, …

```lean
def single [DecidableEq B] (b : B) : Dimension B
```

**`Dimension.single_exponent`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L176).

```lean
lemma single_exponent [DecidableEq B] (b b' : B) :
    (single b).exponent b' = if b' = b then 1 else 0
```

**`Dimension.extend`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L184).

> Change of basis along a map `f : B → B'` of base dimensions: reindex a dimension
> over `B` into one over `B'` by placing each exponent at its image. For an embedding
> `f` (injective) this preserves every exponent (`extend_exponent_apply`), so a
> dimension in one system re-expresses faithfully in an extending one.

```lean
def extend {B' : Type} [DimensionBasis B'] [Fintype B] [DecidableEq B']
    (f : B → B') (d : Dimension B) : Dimension B'
```

**`Dimension.extend_exponent_apply`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L189).

```lean
lemma extend_exponent_apply {B' : Type} [DimensionBasis B'] [Fintype B] [DecidableEq B']
    {f : B → B'} (hf : Function.Injective f) (d : Dimension B) (b : B) :
    (extend f d).exponent (f b) = d.exponent b
```

## Dimension-preserving maps between bases

> A cross-basis map of dimensions is only admissible if it preserves the dimensional
> *algebra*. We record the two truth-preserving directions as bundled data:
>
> * an `Embedding B B'` is an **injective** `MonoidHom (Dimension B) (Dimension B')` — a
>   faithful, dimension-preserving inclusion of one basis into another; and
> * a `Projection B' B` is a **surjective** `MonoidHom (Dimension B') (Dimension B)` — a
>   truth-preserving *reduction* of a richer basis onto a coarser one.
>
> Being a `MonoidHom` is what makes either map dimension-preserving (it respects
> products, inverses and rational powers); the injectivity / surjectivity side condition
> distinguishes the two directions. Cross-basis dimension maps should be produced as one
> of these, so that dimension-preservation holds by construction — a bare relabelling
> that sends a base dimension to an inequivalent one is *not* expressible as either.

**`Dimension.extendHom`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L217).

> `extend f` packaged as a monoid homomorphism of dimensions.

```lean
def extendHom {B' : Type} [DimensionBasis B'] [Fintype B] [DecidableEq B'] (f : B → B') :
    Dimension B →* Dimension B'
```

**`Dimension.Embedding`**, a structure, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L233).

> A **dimension embedding** `B ↪ B'`: an injective monoid homomorphism of
> dimensions. As a `MonoidHom` it is dimension-preserving (it respects products,
> inverses and rational powers); injectivity makes it a faithful inclusion of the basis
> `B` into `B'`. Cross-basis dimension injections are produced as `Embedding`s so that
> dimension-preservation holds by construction.

```lean
structure Embedding (B B' : Type) [DimensionBasis B] [DimensionBasis B'] where
  /-- The underlying dimension-preserving homomorphism. -/
  toHom : Dimension B →* Dimension B'
  /-- The homomorphism is injective (a faithful embedding). -/
  inj : Function.Injective toHom
```

**`Dimension.Projection`**, a structure, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L243).

> A **dimension projection** `B' ↠ B`: a surjective monoid homomorphism of
> dimensions. As a `MonoidHom` it is truth-preserving, but it is lossy — it reduces a
> richer basis `B'` onto a coarser basis `B`, collapsing the base dimensions that `B`
> does not track.

```lean
structure Projection (B' B : Type) [DimensionBasis B'] [DimensionBasis B] where
  /-- The underlying dimension-preserving homomorphism. -/
  toHom : Dimension B' →* Dimension B
  /-- The homomorphism is surjective (the reduction hits every dimension of `B`). -/
  surj : Function.Surjective toHom
```

**`Dimension.Embedding.ofBasis`**, a def, [line 252](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean#L252).

> An injective *basis* map `f : B → B'` induces a dimension embedding, via `extend`.
> This is the label-level case: it sends each base dimension of `B` to a base dimension
> of `B'`, so it is automatically dimension-preserving and faithful.

```lean
def Embedding.ofBasis {B B' : Type} [DimensionBasis B] [DimensionBasis B']
    [Fintype B] [DecidableEq B']
    (f : B → B') (hf : Function.Injective f) : Embedding B B'
```

## Depends on

- [Reducible rational arithmetic for dimension exponents](exponent.md)

## Sources

- [Physlib/Units/Dimension.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Dimension.lean)
