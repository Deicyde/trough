---
declaration: module
origin: cited
lean: StandardModel.localGaugeData, StandardModel.instFreeLocalGaugeData, StandardModel.localGaugeData_eval, StandardModel.localGaugeData_ofConstant, StandardModel.localGaugeData_evalLie, StandardModel.localGaugeData_ofConstantLie, StandardModel.localGaugeData_adjoint, StandardModel.localGaugeData_deriv
statement: formalized
proof: formalized
---

# The Standard Model gauge group as local gauge data

The module `PhyslibAlpha.Particles.StandardModel.GaugeGroup.LocalGaugeData`, [PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean): 17 declarations, 8 with a docstring.

## i. Overview

> The generic theory of gauge and matter fields is stated against a supplied local-gauge-data
> package `jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J`. The Standard Model already carries all of its
> data, for the jet gauge group `JetGaugeGroupI` of `SU(3) × SU(2) × U(1)` with jet Lie algebra
> `JetGaugeAlgebra`, global group `GaugeGroupI` and gauge algebra `GaugeAlgebra`.
>
> This file packages those existing constructions as the named term
> `StandardModel.localGaugeData`, and records the rules that compute the generic interface
> back to the Standard Model definition it came from, so that the existing Standard Model
> lemmas apply to it unchanged. It is a term, not an instance: every generic construction
> receives it as an argument. Its faithfulness — Taylor determinacy of the jet gauge algebra
> and the vanishing of the Maurer–Cartan form exactly on constant jets — is a property of that
> package rather than a choice, so it is an instance.
>
> Everything the generic theory derives from a package is thereby available for the Standard
> Model: the Taylor–Leibniz theorem for the adjoint action, the truncation filtration of the
> jet gauge group by the Maurer–Cartan form, the covariance of the covariant derivative, and
> the determination of a pure jet by its symmetrized Maurer–Cartan data. Its freeness, the
> remaining power-series input to the classification of invariants, is
> `instFreeLocalGaugeData`, the generic freeness of gauge data built from factors.

## ii. Key results

> - `StandardModel.localGaugeData` : the Standard Model gauge group as local gauge data.
> - `StandardModel.instFreeLocalGaugeData` : the package is free.
> - `StandardModel.localGaugeData_eval`, `StandardModel.localGaugeData_deriv`,
>   `StandardModel.localGaugeData_maurerCartan`, `StandardModel.localGaugeData_adjointCoeff_apply`,
>   … : the generic interface computed back to the Standard Model definitions.
> - `StandardModel.instFaithfulLocalGaugeData` : the package is faithful.

## iv. References

> * None.

## A. The local-gauge-data package

> `LocalGaugeData` is an ordinary structure, so this is a named term supplied at each use site,
> not an instance found by search. The four carriers do not determine it — a truncated jet
> group over the same gauge group would be a second, equally canonical package — so nothing
> is registered globally.

**`StandardModel.localGaugeData`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L80).

> The Standard Model gauge group as local gauge data, for the jet gauge group
> `JetGaugeGroupI` and its Lie algebra `JetGaugeAlgebra` over the global group
> `GaugeGroupI` and gauge algebra `GaugeAlgebra`. It is the gauge data
> `StandardModel.Model.gaugeData` that the model table assembles from the factor list
> `[.SU 3, .SU 2, .U1]` by `LocalGaugeData.ofFactors`; the carriers of that assembly are
> `JetGaugeGroupI` and `JetGaugeAlgebra` on the nose, and each data field is definitionally
> the existing Standard Model construction (the rules of section B are all `rfl`).

```lean
noncomputable def localGaugeData :
    LocalGaugeData GaugeGroupI GaugeAlgebra JetGaugeGroupI JetGaugeAlgebra
```

**`StandardModel.instFreeLocalGaugeData`**, an instance, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L88).

> The Standard Model package is free. It is the local gauge data of the factors
> `SU(3)`, `SU(2)` and `U(1)`, each free, and freeness passes to products:
> `LocalGaugeData.instFreeOfFactors`. The symmetrized Maurer–Cartan data are therefore free
> coordinates on its pure jets, by `LocalGaugeData.symmetrizedMaurerCartanCoeff_bijective`.

```lean
instance instFreeLocalGaugeData : localGaugeData.Free
```

## B. The generic interface in Standard Model terms

> These rules point from the generic interface to the Standard Model definitions, which is
> the direction in which the existing Standard Model lemmas become applicable.

**`StandardModel.localGaugeData_eval`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L133).

```lean
lemma localGaugeData_eval : localGaugeData.eval = JetGaugeGroupI.eval
```

**`StandardModel.localGaugeData_ofConstant`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L136).

```lean
lemma localGaugeData_ofConstant : localGaugeData.ofConstant = JetGaugeGroupI.ofConstant
```

**`StandardModel.localGaugeData_evalLie`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L139).

```lean
lemma localGaugeData_evalLie : localGaugeData.evalLie = JetGaugeAlgebra.eval
```

**`StandardModel.localGaugeData_ofConstantLie`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L142).

```lean
lemma localGaugeData_ofConstantLie :
    localGaugeData.ofConstantLie = JetGaugeAlgebra.ofConstant
```

**`StandardModel.localGaugeData_adjoint`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L146).

```lean
lemma localGaugeData_adjoint : localGaugeData.adjoint = GaugeAlgebra.adjoint
```

**`StandardModel.localGaugeData_deriv`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L149).

```lean
lemma localGaugeData_deriv (μ : Fin 1 ⊕ Fin 3) :
    localGaugeData.deriv μ = JetGaugeAlgebra.deriv μ
```

**`StandardModel.localGaugeData_iteratedDeriv`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L155).

> The generic iterated derivative is the Standard Model iterated derivative, both being
> the same fold of `JetGaugeAlgebra.deriv` over the multiset of directions.

```lean
lemma localGaugeData_iteratedDeriv (s : Multiset (Fin 1 ⊕ Fin 3)) :
    localGaugeData.iteratedDeriv s = JetGaugeAlgebra.iteratedDeriv s
```

**`StandardModel.localGaugeData_mulCoord`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L159).

```lean
lemma localGaugeData_mulCoord (μ : Fin 1 ⊕ Fin 3) :
    localGaugeData.mulCoord μ = JetGaugeAlgebra.coord μ
```

**`StandardModel.localGaugeData_adjointJ`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L163).

```lean
lemma localGaugeData_adjointJ : localGaugeData.adjointJ = JetGaugeAlgebra.adjoint
```

**`StandardModel.localGaugeData_maurerCartan`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L166).

```lean
lemma localGaugeData_maurerCartan : localGaugeData.maurerCartan = maurerCartanForm
```

**`StandardModel.localGaugeData_adjointCoeff_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L170).

> The adjoint Taylor coefficients of the package, written out in Standard Model terms.

```lean
lemma localGaugeData_adjointCoeff_apply (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3))
    (a : GaugeAlgebra) :
    localGaugeData.adjointCoeff U x a =
      JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv x
        (JetGaugeAlgebra.adjointMap U (JetGaugeAlgebra.ofConstant a)))
```

**`StandardModel.localGaugeData_adjointCoeff_toSU3Matrix`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L177).

> The `su(3)` component of the adjoint Taylor coefficients.

```lean
lemma localGaugeData_adjointCoeff_toSU3Matrix (U : JetGaugeGroupI)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (b : GaugeAlgebra) :
    (localGaugeData.adjointCoeff U p b).toSU3Matrix
      = ((U.1.1 * b.toSU3Matrix.map (MvPowerSeries.C : ℂ → SpaceTimeAlgebra) *
          star U.1.1).map fun f =>
          MvPowerSeries.constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
```

**`StandardModel.localGaugeData_adjointCoeff_toSU2Matrix`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L187).

> The `su(2)` component of the adjoint Taylor coefficients.

```lean
lemma localGaugeData_adjointCoeff_toSU2Matrix (U : JetGaugeGroupI)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (b : GaugeAlgebra) :
    (localGaugeData.adjointCoeff U p b).toSU2Matrix
      = ((U.2.1.1 * b.toSU2Matrix.map (MvPowerSeries.C : ℂ → SpaceTimeAlgebra) * star U.2.1.1).map
          fun f => MvPowerSeries.constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
```

**`StandardModel.localGaugeData_adjointCoeff_toU1Value`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L196).

> The `u(1)` component of the adjoint Taylor coefficients.

```lean
lemma localGaugeData_adjointCoeff_toU1Value (U : JetGaugeGroupI)
    (p : Multiset (Fin 1 ⊕ Fin 3)) (b : GaugeAlgebra) :
    (localGaugeData.adjointCoeff U p b).toU1Value
      = MvPowerSeries.constantCoeff
          (SpaceTimeAlgebra.iteratedPDeriv p (MvPowerSeries.C b.toU1Value))
```

## C. Faithfulness

**`StandardModel.instFaithfulLocalGaugeData`**, an instance, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean#L217).

> The Standard Model package is faithful: an element of the jet gauge algebra is
> determined by the base-point values of its iterated derivatives, and a jet whose
> Maurer–Cartan form vanishes is the constant jet of its value. Both are statements about
> power series, proved from the matrix definitions in
> `JetGaugeAlgebra.ext_of_eval_iteratedDeriv` and `maurerCartanForm_eq_zero_iff_ofConstant`.
> Unlike the package itself this is a property of it and not a choice, so it is an
> instance.

```lean
instance instFaithfulLocalGaugeData : localGaugeData.Faithful
```

## Depends on

- [The Standard Model](../part-01/basic.md)
- [The Maurer–Cartan forms of the jet gauge group](../part-05/gaugegroup-maurercartan-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/GaugeGroup/LocalGaugeData.lean)
