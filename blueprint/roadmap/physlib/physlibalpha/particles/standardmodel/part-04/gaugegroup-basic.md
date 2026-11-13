---
declaration: module
origin: cited
lean: StandardModel.cubeRootOfUnity, StandardModel.cubeRootOfUnity_isPrimitiveRoot, StandardModel.cubeRootOfUnity_pow_three, StandardModel.cubeRootOfUnity_ne_zero, StandardModel.cubeRootOfUnity_pow_mod, StandardModel.cubeRootOfUnity_mul_star
statement: formalized
proof: formalized
---

# A primitive cube root of unity

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.Basic`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean): 6 declarations, 6 with a docstring.

> The root of unity `ω = exp (2 π i / 3)`, which both non-abelian factors of the gauge group see.

## i. Overview

> `Physlib.Particles.StandardModel.GaugeGroup.Basic` carries the gauge group `GaugeGroupI` of
> the Standard Model and its discrete quotients. One scalar recurs throughout the structure of its
> non-abelian factors: the primitive cube root of unity `ω = exp (2 π i / 3)`. The element
> `ω • 1` generates the centre of `SU(3)`, the cyclic colour permutation has eigenvalues the
> powers of `ω`, and `diag(ω, ω²)` lies in `SU(2)`. Collected here are the facts about `ω` those
> uses need: that it is a primitive cube root of unity, that it cubes to one, that it is nonzero
> and of modulus one, and that its powers only see the exponent modulo three.

## ii. Key results

> - `StandardModel.cubeRootOfUnity` : the primitive cube root of unity `ω = exp (2 π i / 3)`.
> - `StandardModel.cubeRootOfUnity_isPrimitiveRoot` : it is a primitive cube root of unity.
> - `StandardModel.cubeRootOfUnity_pow_three`, `StandardModel.cubeRootOfUnity_pow_mod` : it cubes
>   to one, so its powers only see the exponent modulo three.
> - `StandardModel.cubeRootOfUnity_ne_zero`, `StandardModel.cubeRootOfUnity_mul_star` : it is
>   nonzero and of modulus one.

## iv. References

> The gauge group and its quotients are in `Physlib.Particles.StandardModel.GaugeGroup.Basic`.

## A. A primitive cube root of unity

> `ω = exp (2 π i / 3)` appears in both non-abelian factors: `ω • 1` generates the centre of
> `SU(3)`, the cyclic colour permutation has eigenvalues the powers of `ω`, and `diag(ω, ω²)`
> lies in `SU(2)`.

**`StandardModel.cubeRootOfUnity`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L62).

> The primitive cube root of unity `ω = exp (2 π i / 3)`.

```lean
noncomputable def cubeRootOfUnity : ℂ
```

**`StandardModel.cubeRootOfUnity_isPrimitiveRoot`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L65).

> `ω` is a primitive cube root of unity.

```lean
lemma cubeRootOfUnity_isPrimitiveRoot : IsPrimitiveRoot cubeRootOfUnity 3
```

**`StandardModel.cubeRootOfUnity_pow_three`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L70).

> `ω` cubes to one.

```lean
lemma cubeRootOfUnity_pow_three : cubeRootOfUnity ^ 3 = 1
```

**`StandardModel.cubeRootOfUnity_ne_zero`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L74).

> `ω` is nonzero, being a value of the complex exponential.

```lean
lemma cubeRootOfUnity_ne_zero : cubeRootOfUnity ≠ 0
```

**`StandardModel.cubeRootOfUnity_pow_mod`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L77).

> Powers of `ω` only see the exponent modulo three.

```lean
lemma cubeRootOfUnity_pow_mod (m : ℕ) :
    cubeRootOfUnity ^ (m % 3) = cubeRootOfUnity ^ m
```

**`StandardModel.cubeRootOfUnity_mul_star`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean#L83).

> `ω` has modulus one.

```lean
lemma cubeRootOfUnity_mul_star : cubeRootOfUnity * star cubeRootOfUnity = 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/Basic.lean)
