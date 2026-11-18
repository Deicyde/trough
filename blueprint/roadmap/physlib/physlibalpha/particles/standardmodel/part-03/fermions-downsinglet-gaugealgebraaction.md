---
declaration: module
origin: cited
lean: StandardModel.DownSinglet.colourEnd, StandardModel.DownSinglet.colourEnd_apply_mk, StandardModel.DownSinglet.colourEnd_add, StandardModel.DownSinglet.colourEnd_smul, StandardModel.DownSinglet.colourEnd_zero, StandardModel.DownSinglet.colourEnd_neg, StandardModel.DownSinglet.colourEnd_multiset_sum, StandardModel.DownSinglet.colourEnd_mul
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the down-type singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.DownSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean): 21 declarations, 14 with a docstring; 8 private, not shown.

## i. Overview

> The infinitesimal `(3, 1)_{-2}` action of the gauge algebra on the down-type singlet,
> and the proof that it is the infinitesimal action underlying the jet gauge action
> `DownSinglet.repJetGaugeGroupI`, in the sense of
> `LocalGaugeData.IsInfinitesimalActionOf`.
>
>
> - `DownSinglet.gaugeAlgebraAction` : the infinitesimal `(3, 1)_{-2}` action.
> - `DownSinglet.isInfinitesimalActionOf` : the action underlies the jet gauge action.

## ii. Key results

> - `colourEnd` : the endomorphism of the down singlet defined by a `3 × 3` complex matrix acting on
>   the colour index, with the Weyl factor untouched
> - `colourEnd_apply_mk`
> - `colourEnd_add`
> - `colourEnd_smul`

## iv. References

> * None.

## A. The action of the gauge algebra

> The infinitesimal `(3, 1)_{-2}` action of the gauge algebra on the down-type singlet:
> the colour part of the algebra element acts on the colour index and the hypercharge
> part scales, both through the physicists' factor of `i`, matching the group action
> `(star u) ^ 2 • U₃` infinitesimally. The compatibility with the jet gauge action —
> `LocalGaugeData.IsInfinitesimalActionOf` — is proved at the end of this file.

**`StandardModel.DownSinglet.colourEnd`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L66).

> The endomorphism of the down singlet defined by a `3 × 3` complex matrix acting on
> the colour index, with the Weyl factor untouched.

```lean
noncomputable def colourEnd (A : Matrix (Fin 3) (Fin 3) ℂ) :
    DownSinglet →ₗ[ℂ] DownSinglet
```

**`StandardModel.DownSinglet.colourEnd_apply_mk`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L72).

```lean
lemma colourEnd_apply_mk (A : Matrix (Fin 3) (Fin 3) ℂ) (v : DownSinglet) :
    colourEnd A v
      = valLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3)) Fermion.RightHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (valLinEquiv v))
```

**`StandardModel.DownSinglet.colourEnd_add`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L78).

```lean
lemma colourEnd_add (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A + B) = colourEnd A + colourEnd B
```

**`StandardModel.DownSinglet.colourEnd_smul`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L83).

```lean
lemma colourEnd_smul (z : ℂ) (A : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (z • A) = z • colourEnd A
```

**`StandardModel.DownSinglet.colourEnd_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L88).

```lean
lemma colourEnd_zero : colourEnd 0 = 0
```

**`StandardModel.DownSinglet.colourEnd_neg`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L91).

```lean
lemma colourEnd_neg (A : Matrix (Fin 3) (Fin 3) ℂ) : colourEnd (-A) = -colourEnd A
```

**`StandardModel.DownSinglet.colourEnd_multiset_sum`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L95).

```lean
lemma colourEnd_multiset_sum (m : Multiset (Matrix (Fin 3) (Fin 3) ℂ)) :
    colourEnd m.sum = (m.map colourEnd).sum
```

**`StandardModel.DownSinglet.colourEnd_mul`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L103).

> The colour endomorphisms compose through matrix multiplication.

```lean
lemma colourEnd_mul (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A * B) = colourEnd A ∘ₗ colourEnd B
```

**`StandardModel.DownSinglet.actionMatrix`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L113).

> The matrix of the infinitesimal `(3, 1)_{-2}` action of a gauge algebra element on
> the colour index: `i` times the colour part, shifted by `i` times `-2` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.DownSinglet.gaugeAlgebraAction`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L121).

> **The infinitesimal action of the gauge algebra on the down-type singlet**: the
> derivative of the `(3, 1)_{-2}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot — the form consumed by the
> covariant derivative `GaugeAlgebraRealization.covDerivIter` and by
> `LocalGaugeData.IsInfinitesimalActionOf`.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] DownSinglet →ₗ[ℂ] DownSinglet
```

## B. The infinitesimal action underlies the jet gauge action

> The `(3, 1)_{-2}` action of the gauge algebra is the infinitesimal action underlying the
> jet gauge action, in the sense of `LocalGaugeData.IsInfinitesimalActionOf`: the base-point
> Taylor coefficients of the jet action satisfy the Maurer–Cartan Leibniz law and
> intertwine the action with the adjoint transports. The proofs work through the colour
> matrix of the jet action and the all-orders matrix Leibniz rule at the base point.

**`StandardModel.DownSinglet.jetActionMatrix`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L170).

> The jet-valued matrix of the infinitesimal `(3, 1)_{-2}` action of a jet of gauge
> algebra elements: the jet analogue of `actionMatrix`.

```lean
noncomputable def jetActionMatrix (a : JetGaugeAlgebra) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra
```

**`StandardModel.DownSinglet.jetActionMatrix_map_cc_foldl`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L175).

> The base-point Taylor coefficients of the jet action matrix are the action matrices
> of the base-point Taylor coefficients.

```lean
lemma jetActionMatrix_map_cc_foldl (p : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    ((jetActionMatrix a).map fun f =>
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = actionMatrix (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv p a))
```

**`StandardModel.DownSinglet.downMatrix`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L195).

> The `SpaceTimeAlgebra`-valued colour matrix of the jet gauge action on the down singlet: the
> colour matrix of the gauge jet carrying the `-2` hypercharge phase.

```lean
noncomputable def downMatrix (U : JetGaugeGroupI) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra
```

**`StandardModel.DownSinglet.repJetGaugeGroupI_eq_downMatrix`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L199).

```lean
lemma repJetGaugeGroupI_eq_downMatrix (U : JetGaugeGroupI)
    (z : SpaceTimeAlgebra ⊗[ℂ] DownSinglet) :
    repJetGaugeGroupI U z
      = jetValLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3))
            Fermion.RightHandedWeyl
            ((Matrix.toLpLinAlgEquiv 2 (downMatrix U)).restrictScalars ℂ)
            (jetValLinEquiv z))
```

**`StandardModel.DownSinglet.downMatrix_map_pderiv`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L329).

> **The derivative identity** for the colour matrix of the jet gauge action: the
> formal derivative of the colour matrix is minus the jet action matrix of the
> Maurer–Cartan form times the colour matrix.

```lean
lemma downMatrix_map_pderiv (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (downMatrix U).map (fun f => pderiv μ f)
      = -(jetActionMatrix (maurerCartanForm U μ) * downMatrix U)
```

**`StandardModel.DownSinglet.downMatrix_mul_jetActionMatrix`**, a lemma, [line 392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L392).

> **The equivariance identity** for the colour matrix of the jet gauge action: the
> colour matrix intertwines the constant jet action matrix with its adjoint
> transform.

```lean
lemma downMatrix_mul_jetActionMatrix (U : JetGaugeGroupI) (c : GaugeAlgebra) :
    downMatrix U * jetActionMatrix (JetGaugeAlgebra.ofConstant c)
      = jetActionMatrix (JetGaugeAlgebra.adjointMap U (JetGaugeAlgebra.ofConstant c))
        * downMatrix U
```

**`StandardModel.DownSinglet.repCoeff_eq`**, a lemma, [line 410](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L410).

> **The base-point Taylor coefficients of the jet gauge action** on the down-type
> singlet are the colour endomorphisms of the base-point Taylor coefficients of the
> colour matrix.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = colourEnd ((downMatrix U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

**`StandardModel.DownSinglet.colourEnd_one`**, a lemma, [line 471](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L471).

> The colour endomorphism of the identity matrix is the identity.

```lean
lemma colourEnd_one : colourEnd 1 = LinearMap.id
```

**`StandardModel.DownSinglet.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 478](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L478).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

**`StandardModel.DownSinglet.isInfinitesimalActionOf`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L502).

> **The `(3, 1)_{-2}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the down-type singlet**: its base-point Taylor
> coefficients obey the Maurer–Cartan Leibniz law and intertwine the action with the
> adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.DownSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 617](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean#L617).

> The infinitesimal gauge action on the down-type singlet acts on the colour factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : DownSinglet) :
    DownSinglet.gaugeAlgebraAction c (DownSinglet.repLorentzGroup Λ v) =
      DownSinglet.repLorentzGroup Λ (DownSinglet.gaugeAlgebraAction c v)
```

## Depends on

- [Down-type singlets (PhyslibAlpha)](fermions-downsinglet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/DownSinglet/GaugeAlgebraAction.lean)
