---
declaration: def
origin: cited
lean: TauCeti.gamma0CuspOrbitEquiv
statement: formalized
---

# The cusps of `Γ₀(N)`

are in bijection with the pairs `(g, x)` of a divisor `g` of `N`
and a unit `x` modulo `gcd(g, N / g)`. The cusp `γ • ∞` corresponds to the label of `γ`
(`gamma0CuspOrbitEquiv_cuspOrbitOfSL2Z`).

```lean
TauCeti.gamma0CuspOrbitEquiv (N : ℕ) [NeZero N] :
  (Subgroup.map sl2zToPSL2R (CongruenceSubgroup.Gamma0 N)).CuspOrbit ≃
    (g : ↥N.divisors) × (ZMod ((↑g).gcd (N / ↑g)))ˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.gamma0CuspOrbitEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Cusp/Count.html#TauCeti.gamma0CuspOrbitEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.gamma0CuspOrbitEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Cusp/Count.html#TauCeti.gamma0CuspOrbitEquiv)
- [Source of `TauCeti.gamma0CuspOrbitEquiv` in TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Cusp/Count.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/CongruenceSubgroups/Cusp/Count.lean#L222)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularForms/STATUS.md)
