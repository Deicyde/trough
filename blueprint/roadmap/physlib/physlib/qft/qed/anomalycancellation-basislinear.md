---
declaration: module
origin: cited
lean: PureU1.BasisLinear.asCharges, PureU1.BasisLinear.asCharges_eq_castSucc, PureU1.BasisLinear.asCharges_ne_castSucc, PureU1.BasisLinear.asLinSols, PureU1.BasisLinear.sum_of_vectors, PureU1.BasisLinear.coordinateMap, PureU1.BasisLinear.asBasis, PureU1.BasisLinear.finrank_AnomalyFreeLinear
statement: formalized
proof: formalized
---

# Basis of `LinSols`

The module `Physlib.QFT.QED.AnomalyCancellation.BasisLinear`, [Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean): 9 declarations (1 instance with no name), 6 with a docstring.

> We give a basis of vector space `LinSols`, and find the rank thereof.

**`PureU1.BasisLinear.asCharges`**, a def, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L29).

> The basis elements as charges, defined to have a `1` in the `j`th position and a `-1` in the
> last position.

```lean
def asCharges (j : Fin n) : (PureU1 n.succ).Charges
```

**`PureU1.BasisLinear.asCharges_eq_castSucc`**, a lemma, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L37).

```lean
lemma asCharges_eq_castSucc (j : Fin n) :
    asCharges j (Fin.castSucc j) = 1
```

**`PureU1.BasisLinear.asCharges_ne_castSucc`**, a lemma, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L42).

```lean
lemma asCharges_ne_castSucc {k j : Fin n} (h : k ≠ j) :
    asCharges k j.castSucc = 0
```

**`PureU1.BasisLinear.asLinSols`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L50).

> The basis elements as `LinSols`.

```lean
def asLinSols (j : Fin n) : (PureU1 n.succ).LinSols
```

**`PureU1.BasisLinear.sum_of_vectors`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L70).

```lean
lemma sum_of_vectors {n : ℕ} (f : Fin k → (PureU1 n).LinSols) (j : Fin n) :
    (∑ i : Fin k, (f i)).1 j = (∑ i : Fin k, (f i).1 j)
```

**`PureU1.BasisLinear.coordinateMap`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L77).

> The coordinate map for the basis.

```lean
def coordinateMap : (PureU1 n.succ).LinSols ≃ₗ[ℚ] Fin n →₀ ℚ
```

**`PureU1.BasisLinear.asBasis`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L116).

> The basis of `LinSols`.

```lean
def asBasis : Basis (Fin n) ℚ ((PureU1 n.succ).LinSols)
```

**An instance with no name**, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L120).

> The module over `ℚ` defined by linear solutions to the pure `U(1)` ACCs is finite.

```lean
instance : Module.Finite ℚ ((PureU1 n.succ).LinSols)
```

**`PureU1.BasisLinear.finrank_AnomalyFreeLinear`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean#L124).

> The module of solutions to the linear pure-U(1) acc has rank equal to `n`.

```lean
lemma finrank_AnomalyFreeLinear :
    Module.finrank ℚ (((PureU1 n.succ).LinSols)) = n
```

## Depends on

- [Anomaly cancellation of a theory with a pure U(1)-gauge group](anomalycancellation-basic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/BasisLinear.lean)
