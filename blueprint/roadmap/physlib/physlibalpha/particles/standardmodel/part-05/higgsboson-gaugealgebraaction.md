---
declaration: module
origin: cited
lean: StandardModel.HiggsVec.weakEnd, StandardModel.HiggsVec.weakEnd_apply, StandardModel.HiggsVec.weakEnd_add, StandardModel.HiggsVec.weakEnd_smul, StandardModel.HiggsVec.weakEnd_zero, StandardModel.HiggsVec.weakEnd_neg, StandardModel.HiggsVec.weakEnd_multiset_sum, StandardModel.HiggsVec.weakEnd_mul
statement: formalized
proof: formalized
---

# The infinitesimal gauge action on the Higgs doublet

The module `PhyslibAlpha.Particles.StandardModel.HiggsBoson.GaugeAlgebraAction`, [PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean): 19 declarations, 13 with a docstring; 7 private, not shown.

## i. Overview

> The infinitesimal `(1, 2)_{3}` action of the gauge algebra on the Higgs doublet: the
> weak part of the algebra element acts on the weak index and the hypercharge part scales,
> both through the physicists' factor of `i`, matching the group action `u ^ 3 • U₂`
> infinitesimally. The compatibility with the jet gauge action —
> `LocalGaugeData.IsInfinitesimalActionOf` — is proved at the end of this file: the
> base-point Taylor coefficients of the jet action satisfy the Maurer–Cartan Leibniz law
> and intertwine the action with the adjoint transports. The proofs work through the weak
> matrix `jetGaugeMatrix` of the jet action and the all-orders matrix Leibniz rule at the
> base point.

## ii. Key results

> - `weakEnd` : the endomorphism of the Higgs doublet defined by a `2 × 2` matrix on the
>   weak index.
> - `gaugeAlgebraAction` : the infinitesimal `(1, 2)_{3}` action of the gauge algebra.
> - `isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal action
>   underlying the jet gauge action `repJetGaugeGroupI`.

## iv. References

> * None.

## A. The action of the gauge algebra

**`StandardModel.HiggsVec.weakEnd`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L62).

> The endomorphism of the Higgs doublet defined by a `2 × 2` complex matrix acting on
> the weak index.

```lean
noncomputable def weakEnd (A : Matrix (Fin 2) (Fin 2) ℂ) :
    HiggsVec →ₗ[ℂ] HiggsVec
```

**`StandardModel.HiggsVec.weakEnd_apply`**, a lemma, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L66).

```lean
lemma weakEnd_apply (A : Matrix (Fin 2) (Fin 2) ℂ) (v : HiggsVec) :
    weakEnd A v = Matrix.toLpLinAlgEquiv 2 A v
```

**`StandardModel.HiggsVec.weakEnd_add`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L69).

```lean
lemma weakEnd_add (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A + B) = weakEnd A + weakEnd B
```

**`StandardModel.HiggsVec.weakEnd_smul`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L73).

```lean
lemma weakEnd_smul (z : ℂ) (A : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (z • A) = z • weakEnd A
```

**`StandardModel.HiggsVec.weakEnd_zero`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L77).

```lean
lemma weakEnd_zero : weakEnd 0 = 0
```

**`StandardModel.HiggsVec.weakEnd_neg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L80).

```lean
lemma weakEnd_neg (A : Matrix (Fin 2) (Fin 2) ℂ) : weakEnd (-A) = -weakEnd A
```

**`StandardModel.HiggsVec.weakEnd_multiset_sum`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L84).

```lean
lemma weakEnd_multiset_sum (m : Multiset (Matrix (Fin 2) (Fin 2) ℂ)) :
    weakEnd m.sum = (m.map weakEnd).sum
```

**`StandardModel.HiggsVec.weakEnd_mul`**, a lemma, [line 92](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L92).

> The weak endomorphisms compose through matrix multiplication.

```lean
lemma weakEnd_mul (A B : Matrix (Fin 2) (Fin 2) ℂ) :
    weakEnd (A * B) = weakEnd A ∘ₗ weakEnd B
```

**`StandardModel.HiggsVec.actionMatrix`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L100).

> The matrix of the infinitesimal `(1, 2)_{3}` action of a gauge algebra element on
> the weak index: `i` times the weak part, shifted by `i` times `3` the
> hypercharge.

```lean
noncomputable def actionMatrix (c : GaugeAlgebra) : Matrix (Fin 2) (Fin 2) ℂ
```

**`StandardModel.HiggsVec.gaugeAlgebraAction`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L108).

> **The infinitesimal action of the gauge algebra on the Higgs doublet**: the
> derivative of the `(1, 2)_{3}` action of the gauge group, real-linear in the
> algebra slot and complex-linear in the value slot — the form consumed by the
> covariant derivative `GaugeAlgebraRealization.covDerivIter` and by
> `LocalGaugeData.IsInfinitesimalActionOf`.

```lean
noncomputable def gaugeAlgebraAction :
    GaugeAlgebra →ₗ[ℝ] HiggsVec →ₗ[ℂ] HiggsVec
```

## B. The infinitesimal action underlies the jet gauge action

> The `(1, 2)_{3}` action of the gauge algebra is the infinitesimal action underlying the
> jet gauge action, in the sense of `LocalGaugeData.IsInfinitesimalActionOf`: the base-point
> Taylor coefficients of the jet action satisfy the Maurer–Cartan Leibniz law and
> intertwine the action with the adjoint transports. The proofs work through the weak
> matrix of the jet action and the all-orders matrix Leibniz rule at the base point.

**`StandardModel.HiggsVec.jetActionMatrix`**, a def, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L151).

> The jet-valued matrix of the infinitesimal `(1, 2)_{3}` action of a jet of gauge
> algebra elements: the jet analogue of `actionMatrix`.

```lean
noncomputable def jetActionMatrix (a : JetGaugeAlgebra) : Matrix (Fin 2) (Fin 2) SpaceTimeAlgebra
```

**`StandardModel.HiggsVec.jetActionMatrix_map_cc_foldl`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L156).

> The base-point Taylor coefficients of the jet action matrix are the action matrices
> of the base-point Taylor coefficients.

```lean
lemma jetActionMatrix_map_cc_foldl (p : Multiset (Fin 1 ⊕ Fin 3)) (a : JetGaugeAlgebra) :
    ((jetActionMatrix a).map fun f =>
        constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = actionMatrix (JetGaugeAlgebra.eval (JetGaugeAlgebra.iteratedDeriv p a))
```

**`StandardModel.HiggsVec.jetGaugeMatrix_map_pderiv`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L270).

> **The derivative identity** for the weak matrix of the jet gauge action: the
> formal derivative of the weak matrix is minus the jet action matrix of the
> Maurer–Cartan form times the weak matrix.

```lean
lemma jetGaugeMatrix_map_pderiv (U : JetGaugeGroupI) (μ : Fin 1 ⊕ Fin 3) :
    (jetGaugeMatrix U).map (fun f => pderiv μ f)
      = -(jetActionMatrix (maurerCartanForm U μ) * jetGaugeMatrix U)
```

**`StandardModel.HiggsVec.jetGaugeMatrix_mul_jetActionMatrix`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L329).

> **The equivariance identity** for the weak matrix of the jet gauge action: the
> weak matrix intertwines the constant jet action matrix with its adjoint
> transform.

```lean
lemma jetGaugeMatrix_mul_jetActionMatrix (U : JetGaugeGroupI) (c : GaugeAlgebra) :
    jetGaugeMatrix U * jetActionMatrix (JetGaugeAlgebra.ofConstant c)
      = jetActionMatrix (JetGaugeAlgebra.adjointMap U (JetGaugeAlgebra.ofConstant c))
        * jetGaugeMatrix U
```

**`StandardModel.HiggsVec.repCoeff_eq`**, a lemma, [line 351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L351).

> **The base-point Taylor coefficients of the jet gauge action** on the Higgs
> doublet are the weak endomorphisms of the base-point Taylor coefficients of the
> weak matrix.

```lean
lemma repCoeff_eq (U : JetGaugeGroupI) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U x
      = weakEnd ((jetGaugeMatrix U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

**`StandardModel.HiggsVec.weakEnd_one`**, a lemma, [line 385](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L385).

> The weak endomorphism of the identity matrix is the identity.

```lean
lemma weakEnd_one : weakEnd 1 = LinearMap.id
```

**`StandardModel.HiggsVec.repCoeff_zero_of_eval_eq_one`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L390).

> At the base point, a gauge jet with trivial value acts trivially: the zeroth
> Taylor coefficient of the jet gauge action is the identity.

```lean
lemma repCoeff_zero_of_eval_eq_one {U : JetGaugeGroupI} (hU : U.eval = 1) :
    GaugeAlgebraRealization.repCoeff repJetGaugeGroupI U 0 = LinearMap.id
```

**`StandardModel.HiggsVec.isInfinitesimalActionOf`**, a lemma, [line 412](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L412).

> **The `(1, 2)_{3}` action of the gauge algebra is the infinitesimal action
> underlying the jet gauge action on the Higgs doublet**: its base-point Taylor
> coefficients obey the Maurer–Cartan Leibniz law and intertwine the action with the
> adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    localGaugeData.IsInfinitesimalActionOf gaugeAlgebraAction repJetGaugeGroupI
```

## C. The gauge action commutes with the Lorentz action

**`StandardModel.HiggsVec.gaugeAlgebraAction_comm_repLorentz`**, a lemma, [line 527](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean#L527).

> The infinitesimal gauge action on the Higgs commutes with the Lorentz action, which is
> trivial.

```lean
lemma gaugeAlgebraAction_comm_repLorentz (c : GaugeAlgebra) (Λ : SL(2,ℂ)) (v : HiggsVec) :
    HiggsVec.gaugeAlgebraAction c ((Representation.trivial ℂ SL(2,ℂ) HiggsVec) Λ v) =
      (Representation.trivial ℂ SL(2,ℂ) HiggsVec) Λ (HiggsVec.gaugeAlgebraAction c v)
```

## Depends on

- [The Standard Model gauge group as local gauge data](../part-04/gaugegroup-localgaugedata.md)
- [The jet algebra of the Higgs field (Basic)](higgsboson-jetalgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Particles/StandardModel/HiggsBoson/GaugeAlgebraAction.lean)
