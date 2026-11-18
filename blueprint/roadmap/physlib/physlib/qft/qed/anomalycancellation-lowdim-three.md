---
declaration: module
origin: cited
lean: PureU1.Three.cube_for_linSol', PureU1.Three.cube_for_linSol, PureU1.Three.three_sol_zero, PureU1.Three.solOfLinear, PureU1.Three.solOfLinear_surjects
statement: formalized
proof: formalized
---

# The Pure U(1) case with 3 fermion

The module `Physlib.QFT.QED.AnomalyCancellation.LowDim.Three`, [Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean): 5 declarations, 1 with a docstring.

> We show that S is a solution only if one of its charges is zero.
> We define a surjective map from `LinSols` with a charge equal to zero to `Sols`.

**`PureU1.Three.cube_for_linSol'`**, a lemma, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean#L27).

```lean
lemma cube_for_linSol' (S : (PureU1 3).LinSols) :
    3 * S.val (0 : Fin 3) * S.val (1 : Fin 3) * S.val (2 : Fin 3) = 0 ↔
    (PureU1 3).cubicACC S.val = 0
```

**`PureU1.Three.cube_for_linSol`**, a lemma, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean#L38).

```lean
lemma cube_for_linSol (S : (PureU1 3).LinSols) :
    (S.val (0 : Fin 3) = 0 ∨ S.val (1 : Fin 3) = 0 ∨ S.val (2 : Fin 3) = 0) ↔
    (PureU1 3).cubicACC S.val = 0
```

**`PureU1.Three.three_sol_zero`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean#L44).

```lean
lemma three_sol_zero (S : (PureU1 3).Sols) : S.val (0 : Fin 3) = 0 ∨ S.val (1 : Fin 3) = 0
    ∨ S.val (2 : Fin 3) = 0
```

**`PureU1.Three.solOfLinear`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean#L48).

> Given a `LinSol` with a charge equal to zero a `Sol`.

```lean
def solOfLinear (S : (PureU1 3).LinSols)
    (hS : S.val (0 : Fin 3) = 0 ∨ S.val (1 : Fin 3) = 0 ∨ S.val (2 : Fin 3) = 0) :
    (PureU1 3).Sols
```

**`PureU1.Three.solOfLinear_surjects`**, a lemma, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean#L54).

```lean
lemma solOfLinear_surjects (S : (PureU1 3).Sols) :
    ∃ (T : (PureU1 3).LinSols) (hT : T.val (0 : Fin 3) = 0 ∨ T.val (1 : Fin 3) = 0
    ∨ T.val (2 : Fin 3) = 0), solOfLinear T hT = S
```

## Depends on

- [Anomaly cancellation of a theory with a pure U(1)-gauge group](anomalycancellation-basic.md)

## Sources

- [Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/QED/AnomalyCancellation/LowDim/Three.lean)
