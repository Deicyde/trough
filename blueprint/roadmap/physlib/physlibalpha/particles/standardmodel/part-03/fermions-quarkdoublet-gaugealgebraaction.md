---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet.colourWeakValLinEquiv, StandardModel.QuarkDoublet.colourWeakEnd, StandardModel.QuarkDoublet.colourWeakEnd_apply_mk, StandardModel.QuarkDoublet.colourWeakEnd_add, StandardModel.QuarkDoublet.colourWeakEnd_smul, StandardModel.QuarkDoublet.colourWeakEnd_zero, StandardModel.QuarkDoublet.colourWeakEnd_neg, StandardModel.QuarkDoublet.colourWeakEnd_multiset_sum
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the quark doublet

The module `PhyslibAlpha.Particles.StandardModel.Fermions.QuarkDoublet.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean): 21 declarations, 14 with a docstring; 7 private, not shown.

## i. Overview

> The `(3, 2)_{1}` action of the gauge algebra on the quark doublet: the colour and weak
> parts of the algebra element act on the combined colour–weak index through the Kronecker
> sum, and the hypercharge part scales, all through the physicists' factor of `i`, matching
> the group action `u • (U₃ ⊗ₖ U₂)` infinitesimally. The main theorem shows this is the
> infinitesimal action underlying the jet gauge action `QuarkDoublet.repJetGaugeGroupI`,
> in the sense of `LocalGaugeData.IsInfinitesimalActionOf`.

## ii. Key results

> - `colourWeakEnd` : the endomorphism of the quark doublet defined by a colour–weak
>   matrix.
> - `gaugeAlgebraAction` : the infinitesimal `(3, 2)_{1}` action of the gauge algebra.
> - `jetGaugeMatrix_map_pderiv` : the derivative identity for the colour–weak matrix.
> - `jetGaugeMatrix_mul_jetActionMatrix` : the equivariance identity for the colour–weak
>   matrix.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.QuarkDoublet.colourWeakValLinEquiv`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L65).

> The identification of the quark doublet with a left-handed Weyl spinor tensored with
> a colour–weak vector over the combined index `Fin 3 × Fin 2`: the `ℂ`-level analogue
> of `jetValLinEquiv`.

```lean
noncomputable def colourWeakValLinEquiv :
    QuarkDoublet ≃ₗ[ℂ] Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3 × Fin 2)
```

**`StandardModel.QuarkDoublet.colourWeakEnd`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L74).

> The endomorphism of the quark doublet defined by a complex matrix over the
> combined colour–weak index, with the Weyl factor untouched.

```lean
noncomputable def colourWeakEnd (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    QuarkDoublet →ₗ[ℂ] QuarkDoublet
```

**`StandardModel.QuarkDoublet.colourWeakEnd_apply_mk`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L80).

```lean
lemma colourWeakEnd_apply_mk (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ)
    (v : QuarkDoublet) :
    colourWeakEnd A v
      = colourWeakValLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace ℂ (Fin 3 × Fin 2))
            Fermion.LeftHandedWeyl
            (Matrix.toLpLinAlgEquiv 2 A) (colourWeakValLinEquiv v))
```

**`StandardModel.QuarkDoublet.colourWeakEnd_add`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L88).

```lean
lemma colourWeakEnd_add (A B : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (A + B) = colourWeakEnd A + colourWeakEnd B
```

**`StandardModel.QuarkDoublet.colourWeakEnd_smul`**, a lemma, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L93).

```lean
lemma colourWeakEnd_smul (z : ℂ) (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (z • A) = z • colourWeakEnd A
```

**`StandardModel.QuarkDoublet.colourWeakEnd_zero`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L98).

```lean
lemma colourWeakEnd_zero : colourWeakEnd 0 = 0
```

**`StandardModel.QuarkDoublet.colourWeakEnd_neg`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L101).

```lean
lemma colourWeakEnd_neg (A : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (-A) = -colourWeakEnd A
```

**`StandardModel.QuarkDoublet.colourWeakEnd_multiset_sum`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L106).

```lean
lemma colourWeakEnd_multiset_sum
    (m : Multiset (Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ)) :
    colourWeakEnd m.sum = (m.map colourWeakEnd).sum
```

**`StandardModel.QuarkDoublet.colourWeakEnd_mul`**, a lemma, [line 115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L115).

> The colour–weak endomorphisms compose through matrix multiplication.

```lean
lemma colourWeakEnd_mul (A B : Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ) :
    colourWeakEnd (A * B) = colourWeakEnd A ∘ₗ colourWeakEnd B
```

**`StandardModel.QuarkDoublet.actionMatrix`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L125).

> The matrix of the infinitesimal `(3, 2)_{1}` action of a gauge algebra element on
> the combined colour–weak index: `i` times the Kronecker sum of the colour and weak
> parts, shifted by `i` times the hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) :
    Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) ℂ
```

**`StandardModel.QuarkDoublet.gaugeAlgebraAction`**, a def, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L136).

> **The infinitesimal action of the gauge algebra on the quark doublet**: the
> derivative of the `(3, 2)_{1}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot — the form consumed by the
> covariant derivative `GaugeAlgebraRealization.covDerivIter` and by
> `LocalGaugeData.IsInfinitesimalActionOf`.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] QuarkDoublet →ₗ[ℂ] QuarkDoublet
```

## B. The colour–weak matrix of the jet gauge action

## C. The infinitesimal action underlies the jet gauge action

> The `(3, 2)_{1}` action of the gauge algebra is the infinitesimal action underlying the
> jet gauge action, in the sense of `LocalGaugeData.IsInfinitesimalActionOf`: the base-point
> Taylor coefficients of the jet action satisfy the Maurer–Cartan Leibniz law and
> intertwine the action with the adjoint transports. The proofs work through the
> colour–weak matrix `jetGaugeMatrix` of the jet action and the all-orders matrix Leibniz
> rule at the base point.

**`StandardModel.QuarkDoublet.jetActionMatrix`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L188).

> The jet-valued matrix of the infinitesimal `(3, 2)_{1}` action of a jet of gauge
> algebra elements: the jet analogue of `actionMatrix`.

```lean
noncomputable def jetActionMatrix (a : JetGaugeAlgebra) :
    Matrix (Fin 3 × Fin 2) (Fin 3 × Fin 2) SpaceTimeAlgebra
```

**`StandardModel.QuarkDoublet.jetActionMatrix_map_cc_foldl`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L196).

> The base-point Taylor coefficients of the jet action matrix are the action matrices
> of the base-point Taylor coefficients.

```lean
lemma jetActionMatrix_map_cc_foldl (p : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    ((jetActionMatrix a).map fun f =>
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = actionMatrix (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv p a))
```

**`StandardModel.QuarkDoublet.repJetGaugeGroupI_eq_jetGaugeMatrix`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L227).

```lean
lemma repJetGaugeGroupI_eq_jetGaugeMatrix (U : JetGaugeGroupI)
    (z : SpaceTimeAlgebra ⊗[ℂ] QuarkDoublet) :
    repJetGaugeGroupI U z
      = jetValLinEquiv.symm
          (Module.End.lTensorAlgHom ℂ (EuclideanSpace SpaceTimeAlgebra (Fin 3 × Fin 2))
            Fermion.LeftHandedWeyl
            ((Matrix.toLpLinAlgEquiv 2 (jetGaugeMatrix U)).restrictScalars ℂ)
            (jetValLinEquiv z))
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix_map_pderiv`**, a lemma, [line 394](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L394).

> **The derivative identity** for the colour–weak matrix of the jet gauge action: the
> formal derivative of the colour–weak matrix is minus the jet action matrix of the
> Maurer–Cartan form times the colour–weak matrix.

```lean
lemma jetGaugeMatrix_map_pderiv (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (jetGaugeMatrix U).map (fun f => pderiv μ f)
      = -(jetActionMatrix (maurerCartanForm U μ) * jetGaugeMatrix U)
```

**`StandardModel.QuarkDoublet.jetGaugeMatrix_mul_jetActionMatrix`**, a lemma, [line 457](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L457).

> **The equivariance identity** for the colour–weak matrix of the jet gauge action:
> the colour–weak matrix intertwines the constant jet action matrix with its adjoint
> transform.

```lean
lemma jetGaugeMatrix_mul_jetActionMatrix (U : JetGaugeGroupI) (c : GaugeAlgebra) :
    jetGaugeMatrix U * jetActionMatrix (JetGaugeAlgebra.ofConstant c)
      = jetActionMatrix (JetGaugeAlgebra.adjointMap U (JetGaugeAlgebra.ofConstant c))
        * jetGaugeMatrix U
```

**`StandardModel.QuarkDoublet.repCoeff_eq`**, a lemma, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L479).

> **The base-point Taylor coefficients of the jet gauge action** on the quark
> doublet are the colour–weak endomorphisms of the base-point Taylor coefficients of
> the colour–weak matrix.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = colourWeakEnd ((jetGaugeMatrix U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

**`StandardModel.QuarkDoublet.colourWeakEnd_one`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L566).

> The colour–weak endomorphism of the identity matrix is the identity.

```lean
lemma colourWeakEnd_one : colourWeakEnd 1 = LinearMap.id
```

**`StandardModel.QuarkDoublet.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 573](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L573).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

**`StandardModel.QuarkDoublet.isInfinitesimalActionOf`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L603).

> **The `(3, 2)_{1}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the quark doublet**: its base-point Taylor
> coefficients obey the Maurer–Cartan Leibniz law and intertwine the action with the
> adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## D. The gauge action commutes with the Lorentz action

**`StandardModel.QuarkDoublet.gaugeAlgebraAction_comm_repLorentzGroup`**, a lemma, [line 727](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean#L727).

> The infinitesimal gauge action on the quark doublet acts on the combined colour–weak
> factor, the Lorentz action on the Weyl factor, so the two commute.

```lean
lemma gaugeAlgebraAction_comm_repLorentzGroup (c : GaugeAlgebra) (Λ : SL(2,ℂ))
    (v : QuarkDoublet) :
    QuarkDoublet.gaugeAlgebraAction c (QuarkDoublet.repLorentzGroup Λ v) =
      QuarkDoublet.repLorentzGroup Λ (QuarkDoublet.gaugeAlgebraAction c v)
```

## Depends on

- [The type corresponding to quark doublets (PhyslibAlpha)](fermions-quarkdoublet-basic.md)
- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)

## Proof depends on

- [Commuting tensor-factor endomorphisms](../../../mathematics/part-01/tensorproductcomm.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/Fermions/QuarkDoublet/GaugeAlgebraAction.lean)
