---
declaration: module
origin: cited
lean: AddZero.ulift, ULift.instStar, ULift.star_eq, ULift.instInvolutiveStar, ULift.instStarMul, ULift.starRingEnd_down, AddEquiv.ulift_apply
statement: formalized
proof: formalized
---

# Typeclass instances for `ULift`

The module `QuantumInfo.ForMathlib.ULift`, [QuantumInfo/ForMathlib/ULift.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean): 11 declarations (4 instances with no name), none with a docstring.

> This file equips `ULift` with algebraic and analytic typeclass instances lifted from the
> underlying type, including `Star`, `StarMul`, `StarRing`, `NormedField`, `DenselyNormedField`
> and `RCLike` structures, together with the corresponding `simp` lemmas relating operations on
> `ULift.{v, u} α` to operations on the underlying `α`.

**`AddZero.ulift`**, an instance, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L26).

```lean
instance AddZero.ulift {α : Type u} [AddZero α] : AddZero (ULift.{v, u} α)
```

**`ULift.instStar`**, an instance, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L28).

```lean
instance ULift.instStar {𝕜 : Type u} [Star 𝕜] : Star (ULift.{v,u} 𝕜)
```

**`ULift.star_eq`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L32).

```lean
lemma ULift.star_eq {𝕜 : Type u} [Star 𝕜] (x : ULift.{v,u} 𝕜) : star x = .up (star x.down)
```

**`ULift.instInvolutiveStar`**, an instance, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L35).

```lean
instance ULift.instInvolutiveStar {𝕜 : Type u} [InvolutiveStar 𝕜] :
    InvolutiveStar (ULift.{v,u} 𝕜)
```

**`ULift.instStarMul`**, an instance, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L39).

```lean
instance ULift.instStarMul {𝕜 : Type u} [Mul 𝕜] [StarMul 𝕜] : StarMul (ULift.{v,u} 𝕜)
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L42).

```lean
instance {𝕜 : Type u} [NonUnitalNonAssocSemiring 𝕜] [StarRing 𝕜] : StarRing (ULift.{v,u} 𝕜)
```

**`ULift.starRingEnd_down`**, a lemma, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L46).

```lean
lemma ULift.starRingEnd_down {𝕜 : Type u} (x : ULift.{v,u} 𝕜) [CommSemiring 𝕜] [StarRing 𝕜] :
    ((starRingEnd (ULift.{v, u} 𝕜)) x).down = star x.down
```

**An instance with no name**, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L50).

```lean
instance {𝕜 : Type u} [NormedField 𝕜] : NormedField (ULift.{v,u} 𝕜)
```

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L54).

```lean
instance {𝕜 : Type u} [DenselyNormedField 𝕜] : DenselyNormedField (ULift.{v,u} 𝕜)
```

**`AddEquiv.ulift_apply`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L58).

```lean
lemma AddEquiv.ulift_apply {α : Type u} [Add α] (x : ULift.{v, u} α) :
    AddEquiv.ulift.{u, v} x = x.down
```

**An instance with no name**, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean#L62).

```lean
noncomputable instance {𝕜 : Type u} [RCLike 𝕜] : RCLike (ULift.{v,u} 𝕜)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/ULift.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/ULift.lean)
