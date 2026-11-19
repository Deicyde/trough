---
declaration: def
origin: cited
lean: TauCeti.blaschkeFactor
statement: formalized
---

# TauCeti.blaschkeFactor

The boundary-compatible Blaschke factor with parameter `a`: it is
`z ↦ (z - a) / (1 - conj a * z)` when `‖a‖ < 1` and the constant `-a` otherwise.  For `‖a‖ = 1`
this constant is the removable extension of the same rational expression
(see `TauCeti.blaschkeFactor_eq_div`).  Parameters of norm greater than one are not intended.

```lean
TauCeti.blaschkeFactor (a z : ℂ) : ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.blaschkeFactor`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.html#TauCeti.blaschkeFactor).

## Sources

- [Tau Ceti documentation: `TauCeti.blaschkeFactor`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.html#TauCeti.blaschkeFactor)
- [Source of `TauCeti.blaschkeFactor` in TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/BlaschkeProduct.lean#L68)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions, part II](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ConformalMappingPartII/STATUS.md)
