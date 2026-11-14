---
declaration: module
origin: cited
lean: Physlib.Distribution.norm_iteratedFDeriv_ofRealCLM, Physlib.Distribution.powOneMul, Physlib.Distribution.powOneMul_apply
statement: formalized
proof: formalized
---

# Physlib.Mathematics.Distribution.PowMul

The module `Physlib.Mathematics.Distribution.PowMul`, [Physlib/Mathematics/Distribution/PowMul.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/PowMul.lean): 3 declarations, 1 with a docstring.

## The multiple of a Schwartz map by `x`

> In this module we define the continuous linear map from the Schwartz space
> `𝓢(ℝ, 𝕜)` to itself which takes a Schwartz map `η` to the Schwartz map `x * η`.

**`Physlib.Distribution.norm_iteratedFDeriv_ofRealCLM`**, a lemma, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/PowMul.lean#L31).

```lean
lemma norm_iteratedFDeriv_ofRealCLM {x} (i : ℕ) :
    ‖iteratedFDeriv ℝ i (RCLike.ofRealCLM (K := 𝕜)) x‖ =
      if i = 0 then |x| else if i = 1 then 1 else 0
```

**`Physlib.Distribution.powOneMul`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/PowMul.lean#L48).

> The continuous linear map `𝓢(ℝ, 𝕜) →L[𝕜] 𝓢(ℝ, 𝕜)` taking a Schwartz map
> `η` to `x * η`.

```lean
def powOneMul : 𝓢(ℝ, 𝕜) →L[𝕜] 𝓢(ℝ, 𝕜)
```

**`Physlib.Distribution.powOneMul_apply`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/PowMul.lean#L136).

```lean
lemma powOneMul_apply (ψ : 𝓢(ℝ, 𝕜)) (x : ℝ) :
    powOneMul 𝕜 ψ x = x * ψ x
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/Distribution/PowMul.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Mathematics/Distribution/PowMul.lean)
