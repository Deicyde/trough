---
declaration: module
origin: cited
lean: LieHom.holPart, LieHom.antiholPart, LieHom.holPart_add_antiholPart, LieHom.holPart_add, LieHom.antiholPart_add, LieHom.map_ofReal_smul, LieHom.map_smul_complex, LieHom.map_I_smul_I_smul
statement: formalized
proof: formalized
---

# Holomorphic and antiholomorphic parts of a real Lie algebra homomorphism

The module `PhyslibAlpha.Mathematics.RepresentationTheory.Sl2.HolomorphicPart`, [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean): 13 declarations, 13 with a docstring.

> A real Lie algebra homomorphism between complex algebras splits into a complex-linear and a
> complex-antilinear part, which commute.

## i. Overview

> Let `D : A →ₗ⁅ℝ⁆ B` be a real Lie algebra homomorphism between complex associative algebras. It
> need not be complex linear, as for the derivative of a representation of `SL(2, ℂ)` regarded as a
> real Lie group. Its holomorphic and antiholomorphic parts
> `D_L X = (D X - i D (i X)) / 2` and `D_R X = (D X + i D (i X)) / 2` add up to `D`. The first is
> complex linear and the second complex antilinear (B), each preserves brackets, and the two
> commute (C). So `D` is the sum of two commuting complex representations.

## ii. Key results

> - `LieHom.holPart`, `LieHom.antiholPart` : the holomorphic and antiholomorphic parts.
> - `LieHom.holPart_add_antiholPart` : the two parts add up to the homomorphism.
> - `LieHom.holPart_lie`, `LieHom.antiholPart_lie` : each part preserves brackets.
> - `LieHom.holPart_lie_antiholPart` : the two parts commute.

## iv. References

> - B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. The definitions

**`LieHom.holPart`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L64).

> The holomorphic part `X ↦ (D X - i D (i X)) / 2` of a real Lie algebra homomorphism between
> complex associative algebras.

```lean
noncomputable def holPart (X : A) : B
```

**`LieHom.antiholPart`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L68).

> The antiholomorphic part `X ↦ (D X + i D (i X)) / 2` of a real Lie algebra homomorphism
> between complex associative algebras.

```lean
noncomputable def antiholPart (X : A) : B
```

**`LieHom.holPart_add_antiholPart`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L71).

> The homomorphism is the sum of its holomorphic and antiholomorphic parts.

```lean
lemma holPart_add_antiholPart (X : A) : D.holPart X + D.antiholPart X = D X
```

**`LieHom.holPart_add`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L76).

> The holomorphic part is additive.

```lean
lemma holPart_add (X Y : A) : D.holPart (X + Y) = D.holPart X + D.holPart Y
```

**`LieHom.antiholPart_add`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L81).

> The antiholomorphic part is additive.

```lean
lemma antiholPart_add (X Y : A) :
    D.antiholPart (X + Y) = D.antiholPart X + D.antiholPart Y
```

## B. Complex multiples

**`LieHom.map_ofReal_smul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L93).

> A real Lie algebra homomorphism commutes with real multiples written as complex ones.

```lean
lemma map_ofReal_smul (r : ℝ) (X : A) : D ((r : ℂ) • X) = (r : ℂ) • D X
```

**`LieHom.map_smul_complex`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L98).

> A complex multiple `c X` is mapped to `Re c • D X + Im c • D (i X)`.

```lean
lemma map_smul_complex (c : ℂ) (X : A) :
    D (c • X) = (c.re : ℂ) • D X + (c.im : ℂ) • D (I • X)
```

**`LieHom.map_I_smul_I_smul`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L104).

> Multiplying twice by `i` negates the image.

```lean
lemma map_I_smul_I_smul (X : A) : D (I • I • X) = - D X
```

**`LieHom.holPart_smul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L108).

> The holomorphic part is complex linear.

```lean
lemma holPart_smul (c : ℂ) (X : A) : D.holPart (c • X) = c • D.holPart X
```

**`LieHom.antiholPart_smul`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L117).

> The antiholomorphic part is complex antilinear.

```lean
lemma antiholPart_smul (c : ℂ) (X : A) :
    D.antiholPart (c • X) = starRingEnd ℂ c • D.antiholPart X
```

## C. Brackets

**`LieHom.holPart_lie`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L133).

> The holomorphic part preserves brackets.

```lean
lemma holPart_lie (X Y : A) : ⁅D.holPart X, D.holPart Y⁆ = D.holPart ⁅X, Y⁆
```

**`LieHom.antiholPart_lie`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L139).

> The antiholomorphic part preserves brackets.

```lean
lemma antiholPart_lie (X Y : A) :
    ⁅D.antiholPart X, D.antiholPart Y⁆ = D.antiholPart ⁅X, Y⁆
```

**`LieHom.holPart_lie_antiholPart`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean#L146).

> The holomorphic and antiholomorphic parts commute with each other.

```lean
lemma holPart_lie_antiholPart (X Y : A) : ⁅D.holPart X, D.antiholPart Y⁆ = 0
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/RepresentationTheory/Sl2/HolomorphicPart.lean)
