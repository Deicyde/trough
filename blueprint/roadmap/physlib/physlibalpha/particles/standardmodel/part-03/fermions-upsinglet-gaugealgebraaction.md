---
declaration: module
origin: cited
lean: StandardModel.UpSinglet.colourEnd, StandardModel.UpSinglet.colourEnd_apply_mk, StandardModel.UpSinglet.colourEnd_add, StandardModel.UpSinglet.colourEnd_smul, StandardModel.UpSinglet.colourEnd_zero, StandardModel.UpSinglet.colourEnd_neg, StandardModel.UpSinglet.colourEnd_multiset_sum, StandardModel.UpSinglet.colourEnd_mul
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the up-type singlet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.UpSinglet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean): 21 declarations, 14 with a docstring; 7 private, not shown.

## i. Overview

> The `(3, 1)_{4}` action of the gauge algebra on the up-type singlet: the colour part of
> the algebra element acts on the colour index and the hypercharge part scales, both
> through the physicists' factor of `i`, matching the group action `u ^ 4 • U₃`
> infinitesimally. The main theorem shows this is the infinitesimal action underlying the
> jet gauge action `UpSinglet.repJetGaugeGroupI`, in the sense of
> `LocalGaugeData.IsInfinitesimalActionOf`.

## ii. Key results

> - `colourEnd` : the endomorphism of the up singlet defined by a colour matrix.
> - `gaugeAlgebraAction` : the infinitesimal `(3, 1)_{4}` action of the gauge algebra.
> - `upMatrix` : the `SpaceTimeAlgebra`-valued colour matrix of the jet gauge action.
> - `upMatrix_map_pderiv` : the derivative identity for the colour matrix.
> - `upMatrix_mul_jetActionMatrix` : the equivariance identity for the colour matrix.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.UpSinglet.colourEnd`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L63).

> The endomorphism of the up singlet defined by a `3 × 3` complex matrix acting on
> the colour index, with the Weyl factor untouched.

```lean
noncomputable def colourEnd (A : Matrix (Fin 3) (Fin 3) ℂ) :
    UpSinglet →ₗ[ℂ] UpSinglet
```

**`StandardModel.UpSinglet.colourEnd_apply_mk`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L69).

```lean
lemma colourEnd_apply_mk (A : Matrix (Fin 3) (Fin 3) ℂ) (v : UpSinglet) :
    colourEnd A v
      = valLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3)) Fermion.RightHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (valLinEquiv v))
```

**`StandardModel.UpSinglet.colourEnd_add`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L75).

```lean
lemma colourEnd_add (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A + B) = colourEnd A + colourEnd B
```

**`StandardModel.UpSinglet.colourEnd_smul`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L80).

```lean
lemma colourEnd_smul (z : ℂ) (A : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (z • A) = z • colourEnd A
```

**`StandardModel.UpSinglet.colourEnd_zero`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L85).

```lean
lemma colourEnd_zero : colourEnd 0 = 0
```

**`StandardModel.UpSinglet.colourEnd_neg`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L88).

```lean
lemma colourEnd_neg (A : Matrix (Fin 3) (Fin 3) ℂ) : colourEnd (-A) = -colourEnd A
```

**`StandardModel.UpSinglet.colourEnd_multiset_sum`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L92).

```lean
lemma colourEnd_multiset_sum (m : Multiset (Matrix (Fin 3) (Fin 3) ℂ)) :
    colourEnd m.sum = (m.map colourEnd).sum
```

**`StandardModel.UpSinglet.colourEnd_mul`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L100).

> The colour endomorphisms compose through matrix multiplication.

```lean
lemma colourEnd_mul (A B : Matrix (Fin 3) (Fin 3) ℂ) :
    colourEnd (A * B) = colourEnd A ∘ₗ colourEnd B
```

**`StandardModel.UpSinglet.actionMatrix`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L110).

> The matrix of the infinitesimal `(3, 1)_{4}` action of a gauge algebra element on
> the colour index: `i` times the colour part, shifted by `i` times `4` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 3) (Fin 3) ℂ
```

**`StandardModel.UpSinglet.gaugeAlgebraAction`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L118).

> **The infinitesimal action of the gauge algebra on the up-type singlet**: the
> derivative of the `(3, 1)_{4}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot — the form consumed by the
> covariant derivative `GaugeAlgebraRealization.covDerivIter` and by
> `LocalGaugeData.IsInfinitesimalActionOf`.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] UpSinglet →ₗ[ℂ] UpSinglet
```

## B. The colour matrix of the jet gauge action

## C. The infinitesimal action underlies the jet gauge action

> The `(3, 1)_{4}` action of the gauge algebra is the infinitesimal action underlying the
> jet gauge action, in the sense of `LocalGaugeData.IsInfinitesimalActionOf`: the base-point
> Taylor coefficients of the jet action satisfy the Maurer–Cartan Leibniz law and
> intertwine the action with the adjoint transports. The proofs work through the colour
> matrix of the jet action and the all-orders matrix Leibniz rule at the base point.

**`StandardModel.UpSinglet.jetActionMatrix`**, a def, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L163).

> The jet-valued matrix of the infinitesimal `(3, 1)_{4}` action of a jet of gauge
> algebra elements: the jet analogue of `actionMatrix`.

```lean
noncomputable def jetActionMatrix (a : JetGaugeAlgebra) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra
```

**`StandardModel.UpSinglet.jetActionMatrix_map_cc_foldl`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L168).

> The base-point Taylor coefficients of the jet action matrix are the action matrices
> of the base-point Taylor coefficients.

```lean
lemma jetActionMatrix_map_cc_foldl (p : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    ((jetActionMatrix a).map fun f =>
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = actionMatrix (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv p a))
```

**`StandardModel.UpSinglet.upMatrix`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L189).

> The `SpaceTimeAlgebra`-valued colour matrix of the jet gauge action on the up singlet: the
> colour matrix of the gauge jet carrying the `4` hypercharge phase.

```lean
noncomputable def upMatrix (U : JetGaugeGroupI) : Matrix (Fin 3) (Fin 3) SpaceTimeAlgebra
```

**`StandardModel.UpSinglet.repJetGaugeGroupI_eq_upMatrix`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L193).

```lean
lemma repJetGaugeGroupI_eq_upMatrix (U : JetGaugeGroupI)
    (z : SpaceTimeAlgebra ⊗[ℂ] UpSinglet) :
    repJetGaugeGroupI U z
      = jetValLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3))
            Fermion.RightHandedWeyl
            ((Matrix.toLpLinAlgEquiv 2 (upMatrix U)).restrictScalars ℂ)
            (jetValLinEquiv z))
```

**`StandardModel.UpSinglet.upMatrix_map_pderiv`**, a lemma, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L323).

> **The derivative identity** for the colour matrix of the jet gauge action: the
> formal derivative of the colour matrix is minus the jet action matrix of the
> Maurer–Cartan form times the colour matrix.

```lean
lemma upMatrix_map_pderiv (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (upMatrix U).map (fun f => pderiv μ f)
      = -(jetActionMatrix (maurerCartanForm U μ) * upMatrix U)
```

**`StandardModel.UpSinglet.upMatrix_mul_jetActionMatrix`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L378).

> **The equivariance identity** for the colour matrix of the jet gauge action: the
> colour matrix intertwines the constant jet action matrix with its adjoint
> transform.

```lean
lemma upMatrix_mul_jetActionMatrix (U : JetGaugeGroupI) (c : GaugeAlgebra) :
    upMatrix U * jetActionMatrix (JetGaugeAlgebra.ofConstant c)
      = jetActionMatrix (JetGaugeAlgebra.adjointMap U (JetGaugeAlgebra.ofConstant c))
        * upMatrix U
```

**`StandardModel.UpSinglet.repCoeff_eq`**, a lemma, [line 396](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L396).

> **The base-point Taylor coefficients of the jet gauge action** on the up-type
> singlet are the colour endomorphisms of the base-point Taylor coefficients of the
> colour matrix.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = colourEnd ((upMatrix U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

**`StandardModel.UpSinglet.colourEnd_one`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L460).

> The colour endomorphism of the identity matrix is the identity.

```lean
lemma colourEnd_one : colourEnd 1 = LinearMap.id
```

**`StandardModel.UpSinglet.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 467](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L467).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

**`StandardModel.UpSinglet.isInfinitesimalActionOf`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L489).

> **The `(3, 1)_{4}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the up-type singlet**: its base-point Taylor
> coefficients obey the Maurer–Cartan Leibniz law and intertwine the action with the
> adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## D. The gauge action commutes with the Lorentz action

**`StandardModel.UpSinglet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 604](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean#L604).

> The infinitesimal gauge action on the up-type singlet acts on the colour factor, the
> Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : UpSinglet) :
    UpSinglet.gaugeAlgebraAction c (UpSinglet.repLorentzGroup Λ v) =
      UpSinglet.repLorentzGroup Λ (UpSinglet.gaugeAlgebraAction c v)
```

## Depends on

- [Up-type singlets (PhyslibAlpha)](fermions-upsinglet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/UpSinglet/GaugeAlgebraAction.lean)
