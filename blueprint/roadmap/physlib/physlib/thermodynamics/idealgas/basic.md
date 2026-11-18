---
declaration: module
origin: cited
lean: adiabatic_relation_log, adiabatic_relation_UaUbVaVb, entropy
statement: formalized
proof: formalized
---

# Ideal gas: basic entropy and adiabatic relations

The module `Physlib.Thermodynamics.IdealGas.Basic`, [Physlib/Thermodynamics/IdealGas/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/IdealGas/Basic.lean): 3 declarations, 3 with a docstring, 2 listed as significant.

> In this module we formalize a simple thermodynamic model of a monophase
> ideal gas. We:
>
> * Define the entropy
>     S(U,V,N) = N s₀ + N R (c \log(U/U₀) + \log(V/V₀) - (c+1)\log(N/N₀)),
> * Prove equivalent formulations of the adiabatic relation for two states
>   (U\_a, V\_a) and (U\_b, V\_b) at fixed N:
>
>   1. c \log(U\_a/U\_b) + \log(V\_a/V\_b) = 0,
>   2. (U\_a/U\_b)^c (V\_a/V\_b) = 1,
>   3. U\_a^c V\_a = U\_b^c V\_b (the latter follows from (2)).

**`entropy`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/IdealGas/Basic.lean#L34).

> Entropy of a monophase ideal gas:
> S(U,V,N) = N s0 + N R (c log(U/U0) + log(V/V0) - (c+1) log(N/N0)).

```lean
def entropy
    (c R s0 U0 V0 N0 : ℝ) (U V N : ℝ) : ℝ
```

**`adiabatic_relation_log`**, a theorem, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/IdealGas/Basic.lean#L46). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Adiabatic relation in logarithmic form:
> If S(Ua,Va,N) = S(Ub,Vb,N) with N fixed,
> then c * log (Ua/Ub) + log (Va/Vb) = 0.

```lean
theorem adiabatic_relation_log
    {s0 U0 V0 N0 c R : ℝ}
    {Ua Ub Va Vb N : ℝ}
    (hUa : 0 < Ua) (hUb : 0 < Ub)
    (hVa : 0 < Va) (hVb : 0 < Vb)
    (hN : 0 < N)
    (hU0 : 0 < U0) (hV0 : 0 < V0)
    (hR : 0 < R)
    (hS :
      entropy c R s0 U0 V0 N0 Ua Va N =
      entropy c R s0 U0 V0 N0 Ub Vb N) :
    c * log (Ua / Ub) + log (Va / Vb) = 0
```

**`adiabatic_relation_UaUbVaVb`**, a theorem, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/IdealGas/Basic.lean#L75). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Adiabatic relation in product form:
> If S(Ua,Va,N) = S(Ub,Vb,N) with N fixed,
> then (Ua/Ub)^c * (Va/Vb) = 1.

```lean
theorem adiabatic_relation_UaUbVaVb
    {s0 U0 V0 N0 c R : ℝ}
    {Ua Ub Va Vb N : ℝ}
    (hUa : 0 < Ua) (hUb : 0 < Ub)
    (hVa : 0 < Va) (hVb : 0 < Vb)
    (hN : 0 < N)
    (hU0 : 0 < U0) (hV0 : 0 < V0)
    (hR : 0 < R)
    (hS :
      entropy c R s0 U0 V0 N0 Ua Va N =
      entropy c R s0 U0 V0 N0 Ub Vb N) :
    (Real.rpow (Ua / Ub) c) * (Va / Vb) = 1
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Thermodynamics/IdealGas/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Thermodynamics/IdealGas/Basic.lean)
