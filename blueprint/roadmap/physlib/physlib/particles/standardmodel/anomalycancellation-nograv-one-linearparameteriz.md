---
declaration: module
origin: cited
lean: SM.SMNoGrav.One.linearParameters, SM.SMNoGrav.One.linearParameters.ext, SM.SMNoGrav.One.linearParameters.asCharges, SM.SMNoGrav.One.linearParameters.speciesVal, SM.SMNoGrav.One.linearParameters.toSpecies_apply_asCharges, SM.SMNoGrav.One.linearParameters.asLinear, SM.SMNoGrav.One.linearParameters.asLinear_val, SM.SMNoGrav.One.linearParameters.cubic
statement: formalized
proof: formalized
---

# Parameterizations for solutions to the linear ACCs for 1 family

The module `Physlib.Particles.StandardModel.AnomalyCancellation.NoGrav.One.LinearParameterization`, [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean): 27 declarations, 10 with a docstring.

> In this file we give two parameterizations
> - `linearParameters` of solutions to the linear ACCs for 1 family
> - `linearParametersQENeqZero` of solutions to the linear ACCs for 1 family with Q and E non-zero

## References

> * These parameterizations are based on https://arxiv.org/abs/1907.00514.
>   [ref: Lohitsiri:2019fuu]

**`SM.SMNoGrav.One.linearParameters`**, a structure, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L34).

> The parameters for a linear parameterization to the solution of the linear ACCs.

```lean
structure linearParameters where
  /-- The parameter `Q'`. -/
  Q' : ℚ
  /-- The parameter `Y`. -/
  Y : ℚ
  /-- The parameter `E'`. -/
  E' : ℚ
```

**`SM.SMNoGrav.One.linearParameters.ext`**, a lemma, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L45).

```lean
lemma ext {S T : linearParameters} (hQ : S.Q' = T.Q') (hY : S.Y = T.Y) (hE : S.E' = T.E') :
    S = T
```

**`SM.SMNoGrav.One.linearParameters.asCharges`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L51).

> The map from the linear parameters to elements of `(SMNoGrav 1).charges`.

```lean
def asCharges (S : linearParameters) : (SMNoGrav 1).Charges
```

**`SM.SMNoGrav.One.linearParameters.speciesVal`**, a lemma, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L59).

```lean
lemma speciesVal (S : linearParameters) :
    toSpeciesEquiv S.asCharges= fun i _ => S.asCharges i
```

**`SM.SMNoGrav.One.linearParameters.toSpecies_apply_asCharges`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L72).

```lean
lemma toSpecies_apply_asCharges (S : linearParameters) (i : Fin 5) :
    toSpecies i S.asCharges = fun _ => S.asCharges i
```

**`SM.SMNoGrav.One.linearParameters.asLinear`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L78).

> The map from the linear parameters to elements of `(SMNoGrav 1).LinSols`.

```lean
def asLinear (S : linearParameters) : (SMNoGrav 1).LinSols
```

**`SM.SMNoGrav.One.linearParameters.asLinear_val`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L88).

```lean
lemma asLinear_val (S : linearParameters) : S.asLinear.val = S.asCharges
```

**`SM.SMNoGrav.One.linearParameters.cubic`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L92).

```lean
lemma cubic (S : linearParameters) :
    accCube (S.asCharges) = - 54 * S.Q'^3 - 18 * S.Q' * S.Y ^ 2 + S.E'^3
```

**`SM.SMNoGrav.One.linearParameters.cubic_zero_Q'_zero`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L102).

```lean
lemma cubic_zero_Q'_zero (S : linearParameters) (hc : accCube (S.asCharges) = 0)
    (h : S.Q' = 0) : S.E' = 0
```

**`SM.SMNoGrav.One.linearParameters.cubic_zero_E'_zero`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L107).

```lean
lemma cubic_zero_E'_zero (S : linearParameters) (hc : accCube (S.asCharges) = 0)
    (h : S.E' = 0) : S.Q' = 0
```

**`SM.SMNoGrav.One.linearParameters.bijection`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L124).

> The bijection between the type of linear parameters and `(SMNoGrav 1).LinSols`.

```lean
def bijection : linearParameters ≃ (SMNoGrav 1).LinSols
```

**`SM.SMNoGrav.One.linearParameters.bijectionQEZero`**, a def, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L182).

> The bijection between the linear parameters and `(SMNoGrav 1).LinSols` in the special
> case when Q and E are both not zero.

```lean
def bijectionQEZero : {S : linearParameters // S.Q' ≠ 0 ∧ S.E' ≠ 0} ≃
    {S : (SMNoGrav 1).LinSols // Q S.val (0 : Fin 1) ≠ 0 ∧ E S.val (0 : Fin 1) ≠ 0}
```

**`SM.SMNoGrav.One.linearParameters.grav`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L189).

```lean
lemma grav (S : linearParameters) :
    accGrav S.asCharges = 0 ↔ S.E' = 6 * S.Q'
```

**`SM.SMNoGrav.One.linearParametersQENeqZero`**, a structure, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L204).

> The parameters for solutions to the linear ACCs with the condition that Q and E are
> non-zero.

```lean
structure linearParametersQENeqZero where
  /-- The parameter `x`. -/
  x : ℚ
  /-- The parameter `v`. -/
  v : ℚ
  /-- The parameter `w`. -/
  w : ℚ
  hx : x ≠ 0
  hvw : v + w ≠ 0
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.ext`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L217).

```lean
lemma ext {S T : linearParametersQENeqZero} (hx : S.x = T.x) (hv : S.v = T.v)
    (hw : S.w = T.w) : S = T
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.toLinearParameters`**, a def, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L224).

> A map from `linearParametersQENeqZero` to `linearParameters`.

```lean
def toLinearParameters (S : linearParametersQENeqZero) :
    {S : linearParameters // S.Q' ≠ 0 ∧ S.E' ≠ 0}
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.tolinearParametersQNeqZero`**, a def, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L237).

> A map from `linearParameters` to `linearParametersQENeqZero` in the special case when
> `Q'` and `E'` of the linear parameters are non-zero.

```lean
def tolinearParametersQNeqZero (S : {S : linearParameters // S.Q' ≠ 0 ∧ S.E' ≠ 0}) :
    linearParametersQENeqZero
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.bijectionLinearParameters`**, a def, [line 250](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L250).

> A bijection between the type `linearParametersQENeqZero` and linear parameters
> with `Q'` and `E'` non-zero.

```lean
def bijectionLinearParameters :
    linearParametersQENeqZero ≃ {S : linearParameters // S.Q' ≠ 0 ∧ S.E' ≠ 0}
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.bijection`**, a def, [line 285](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L285).

> The bijection between `linearParametersQENeqZero` and `LinSols` with `Q` and `E` non-zero.

```lean
def bijection : linearParametersQENeqZero ≃
    {S : (SMNoGrav 1).LinSols // Q S.val (0 : Fin 1) ≠ 0 ∧ E S.val (0 : Fin 1) ≠ 0}
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.bijection_coe_val`**, a lemma, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L289).

```lean
lemma bijection_coe_val (S : linearParametersQENeqZero) :
    (bijection S).1.val = (bijectionLinearParameters S : linearParameters).asCharges
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.cubic`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L292).

```lean
lemma cubic (S : linearParametersQENeqZero) :
    accCube (bijection S).1.val = 0 ↔ S.v ^ 3 + S.w ^ 3 = -1
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.cubic_v_or_w_zero`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L308).

```lean
lemma cubic_v_or_w_zero (S : linearParametersQENeqZero) (h : accCube (bijection S).1.val = 0) :
    S.v = 0 ∨ S.w = 0
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.cubic_v_zero`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L319).

```lean
lemma cubic_v_zero (S : linearParametersQENeqZero) (h : accCube (bijection S).1.val = 0)
    (hv : S.v = 0) : S.w = -1
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.cube_w_zero`**, a lemma, [line 337](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L337).

```lean
lemma cube_w_zero (S : linearParametersQENeqZero) (h : accCube (bijection S).1.val = 0)
    (hw : S.w = 0) : S.v = -1
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.cube_w_v`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L355).

```lean
lemma cube_w_v (S : linearParametersQENeqZero) (h : accCube (bijection S).1.val = 0) :
    (S.v = -1 ∧ S.w = 0) ∨ (S.v = 0 ∧ S.w = -1)
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.grav`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L362).

```lean
lemma grav (S : linearParametersQENeqZero) : accGrav (bijection S).1.val = 0 ↔ S.v + S.w = -1
```

**`SM.SMNoGrav.One.linearParametersQENeqZero.grav_of_cubic`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean#L374).

```lean
lemma grav_of_cubic (S : linearParametersQENeqZero) (h : accCube (bijection S).1.val = 0) :
    accGrav (bijection S).1.val = 0
```

## Depends on

- [Anomaly Cancellation in the Standard Model without Gravity](anomalycancellation-nograv-basic.md)

## Sources

- [Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/AnomalyCancellation/NoGrav/One/LinearParameterization.lean)
