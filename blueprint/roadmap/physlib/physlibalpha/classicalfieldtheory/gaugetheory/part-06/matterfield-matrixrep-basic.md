---
declaration: module
origin: cited
lean: LocalGaugeData.MatrixRep, LocalGaugeData.MatrixRep.pderivPi, LocalGaugeData.MatrixRep.pderivPi_apply, LocalGaugeData.MatrixRep.foldPi, LocalGaugeData.MatrixRep.foldPi_apply, LocalGaugeData.MatrixRep.foldPi_zero, LocalGaugeData.MatrixRep.pderivPi_comp_foldPi, LocalGaugeData.MatrixRep.ccPi
statement: formalized
proof: formalized
---

# Matrix representations of a jet gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.MatrixRep.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean): 64 declarations, 32 with a docstring.

## i. Overview

> A model-building table describes how a field transforms by a *matrix*: the jets of
> gauge transformations act on the internal index `ι` of the field through a matrix of
> jets `mat U`, the gauge algebra through a matrix of numbers `act c`, and the jets of the
> gauge algebra through a matrix of jets `jetAct a`. This file packages such a matrix
> representation as `LocalGaugeData.MatrixRep`, together with the two identities that make
> `act` the infinitesimal action underlying `mat`: the *derivative identity*
> `∂_μ (mat U) = -(jetAct (ω_μ U)) · mat U` in terms of the Maurer–Cartan form, and the
> *equivariance identity* `mat U · jetAct c = jetAct (Ad_U c) · mat U`.
>
> The internal index is tensored with a Lorentz representation `S`: the target space of
> the field is `S ⊗ (ι → ℂ)`, and the jets of the field are identified with
> `S ⊗ (ι → SpaceTimeAlgebra)`, on which `mat U` acts by matrix–vector multiplication. The main
> theorem, `MatrixRep.isInfinitesimalActionOf`, shows that this action of the gauge algebra
> is the infinitesimal action underlying the jet gauge action in the sense of
> `LocalGaugeData.IsInfinitesimalActionOf`, once and for all matrix representations; the
> compilation `MatrixRep.matterField` then produces a `MatterField`.

## ii. Key results

> - `LocalGaugeData.MatrixRep` : a matrix representation of the jet gauge group with its
>   infinitesimal action.
> - `MatrixRep.jetEquiv` : the identification `SpaceTimeAlgebra ⊗ (S ⊗ (ι → ℂ)) ≃ S ⊗ (ι →
>   SpaceTimeAlgebra)`.
> - `MatrixRep.repJet`, `MatrixRep.repJet_smul` : the fibrewise jet gauge action.
> - `MatrixRep.repCoeff_eq` : the base-point Taylor coefficients of the jet gauge action.
> - `MatrixRep.isInfinitesimalActionOf` : the gauge-algebra action is the infinitesimal
>   action underlying the jet gauge action.
> - `MatrixRep.matterField` : the matter field of a matrix representation.
> - `MatrixRep.matterField_gaugeLorentzCompatible` : its gauge and Lorentz actions commute,
>   acting on different tensor factors.
> - `MatrixRep.matterField_pureJetsActTrivially` : pure jets act trivially on it at the base
>   point, when their matrices have identity constant term.

## iv. References

> * None.

## A. Matrix representations

**`LocalGaugeData.MatrixRep`**, a structure, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L86).

> **A matrix representation** of the jets of gauge transformations on an internal index
> `ι`: the jets act by the matrix of jets `mat U`, the gauge algebra by the matrix `act c`,
> and the jets of the gauge algebra by the matrix of jets `jetAct a`, subject to the
> derivative identity and the equivariance identity that make `act` the infinitesimal
> action underlying `mat`.

```lean
structure MatrixRep (jets : LocalGaugeData G₀ 𝔤 GJ 𝔤J) (ι : Type) [Fintype ι] [DecidableEq ι]
    where
  /-- The matrix of jets by which a jet of gauge transformations acts. -/
  mat : GJ → Matrix ι ι SpaceTimeAlgebra
  mat_one : mat 1 = 1
  mat_mul : ∀ U V, mat (U * V) = mat U * mat V
  /-- The matrix by which an element of the gauge algebra acts. -/
  act : 𝔤 →ₗ[ℝ] Matrix ι ι ℂ
  /-- The matrix of jets by which a jet of gauge algebra elements acts. -/
  jetAct : 𝔤J → Matrix ι ι SpaceTimeAlgebra
  jetAct_ofConstantLie : ∀ c, jetAct (jets.ofConstantLie c) = (act c).map (C : ℂ → SpaceTimeAlgebra)
  /-- The base-point Taylor coefficients of the jet action matrix are the action matrices
    of the base-point Taylor coefficients. -/
  jetAct_map_cc_foldl : ∀ (p : Multiset (Fin 1 ⊕ Fin 3)) (a : 𝔤J),
    ((jetAct a).map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv p f))
      = act (jets.evalLie (jets.iteratedDeriv p a))
  /-- The derivative identity: the formal derivative of the matrix of a gauge jet is minus
    the jet action of its Maurer–Cartan form times the matrix. -/
  mat_map_pderiv : ∀ (U : GJ) (μ : Fin 1 ⊕ Fin 3),
    (mat U).map (fun f => pderiv μ f) = -(jetAct (jets.maurerCartan U μ) * mat U)
  /-- The equivariance identity: the matrix of a gauge jet intertwines the constant jet
    action with its adjoint transform. -/
  mat_mul_jetAct : ∀ (U : GJ) (c : 𝔤),
    mat U * jetAct (jets.ofConstantLie c)
      = jetAct (jets.adjointJ U (jets.ofConstantLie c)) * mat U
```

## B. The target space and its jets

> The target space of the field is `S ⊗ (ι → ℂ)` for a Lorentz representation `S`; its jets
> `SpaceTimeAlgebra ⊗ (S ⊗ (ι → ℂ))` are identified with `S ⊗ (ι → SpaceTimeAlgebra)` by absorbing the
> jet ring into the internal index.

**`LocalGaugeData.MatrixRep.pderivPi`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L127).

> The entrywise formal derivative on `ι → SpaceTimeAlgebra`, as a `ℂ`-linear map.

```lean
noncomputable def pderivPi (μ : Fin 1 ⊕ Fin 3) : (ι → SpaceTimeAlgebra) →ₗ[ℂ]
    (ι → SpaceTimeAlgebra)
```

**`LocalGaugeData.MatrixRep.pderivPi_apply`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L133).

```lean
lemma pderivPi_apply (μ : Fin 1 ⊕ Fin 3) (w : ι → SpaceTimeAlgebra) (i : ι) :
    pderivPi μ w i = pderiv μ (w i)
```

**`LocalGaugeData.MatrixRep.foldPi`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L137).

> The entrywise iterated formal derivative on `ι → SpaceTimeAlgebra`, as a `ℂ`-linear map.

```lean
noncomputable def foldPi (x : Multiset (Fin 1 ⊕ Fin 3)) :
    (ι → SpaceTimeAlgebra) →ₗ[ℂ] (ι → SpaceTimeAlgebra)
```

**`LocalGaugeData.MatrixRep.foldPi_apply`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L145).

```lean
lemma foldPi_apply (x : Multiset (Fin 1 ⊕ Fin 3)) (w : ι → SpaceTimeAlgebra) (i : ι) :
    foldPi x w i = SpaceTimeAlgebra.iteratedPDeriv x (w i)
```

**`LocalGaugeData.MatrixRep.foldPi_zero`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L148).

```lean
lemma foldPi_zero : foldPi (ι := ι) 0 = LinearMap.id
```

**`LocalGaugeData.MatrixRep.pderivPi_comp_foldPi`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L150).

```lean
lemma pderivPi_comp_foldPi (μ : Fin 1 ⊕ Fin 3) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    pderivPi (ι := ι) μ ∘ₗ foldPi x = foldPi (μ ::ₘ x)
```

**`LocalGaugeData.MatrixRep.ccPi`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L158).

> The entrywise base-point evaluation on `ι → SpaceTimeAlgebra`, as a `ℂ`-linear map.

```lean
noncomputable def ccPi : (ι → SpaceTimeAlgebra) →ₗ[ℂ] (ι → ℂ)
```

**`LocalGaugeData.MatrixRep.ccPi_apply`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L165).

```lean
lemma ccPi_apply (w : ι → SpaceTimeAlgebra) (i : ι) : ccPi w i = constantCoeff (w i)
```

**`LocalGaugeData.MatrixRep.C_mul_eq_smul`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L168).

> A constant jet times a jet is the scalar multiple.

```lean
lemma C_mul_eq_smul (z : ℂ) (f : SpaceTimeAlgebra) : (C z : SpaceTimeAlgebra) * f = z • f
```

**`LocalGaugeData.MatrixRep.ccPi_foldPi_mulVec`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L177).

> The base-point evaluation of the iterated derivative of a matrix–vector product with
> constant entries is the matrix–vector product of the base-point coefficients.

```lean
lemma ccPi_foldPi_mulVec (x : Multiset (Fin 1 ⊕ Fin 3)) (A : Matrix ι ι SpaceTimeAlgebra)
    (v : ι → ℂ) :
    ccPi (foldPi x (A.mulVec fun k => (C (v k) : SpaceTimeAlgebra)))
      = (A.map fun f => constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f)).mulVec v
```

### B.1. The target space

> The target space `V` of the field is any complex vector space identified, through `e`,
> with `S ⊗ (ι → ℂ)` for a Lorentz representation `S`. Keeping `V` abstract (rather than
> taking `V = S ⊗ (ι → ℂ)` itself) keeps the real-scalar structure on `V` the canonical
> `Module.complexToReal`, and lets the concrete target spaces of a model serve as `V`.

**`LocalGaugeData.MatrixRep.jetEquiv`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L204).

> The jets of a `V`-valued field as `S ⊗ (ι → SpaceTimeAlgebra)`, through the identification
> `e : V ≃ S ⊗ (ι → ℂ)`: the jet ring is absorbed into the internal index.

```lean
noncomputable def jetEquiv (e : V ≃ₗ[ℂ] S ⊗[ℂ] (ι → ℂ)) :
    SpaceTimeAlgebra ⊗[ℂ] V ≃ₗ[ℂ] S ⊗[ℂ] (ι → SpaceTimeAlgebra)
```

**`LocalGaugeData.MatrixRep.jetEquiv_tmul`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L213).

```lean
lemma jetEquiv_tmul (f : SpaceTimeAlgebra) (s : S) (v : ι → ℂ) :
    jetEquiv e (f ⊗ₜ[ℂ] e.symm (s ⊗ₜ[ℂ] v)) = s ⊗ₜ[ℂ] (fun i => v i • f)
```

**`LocalGaugeData.MatrixRep.induction_on`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L219).

> Induction on the jets of a `V`-valued field through the identification `e`.

```lean
lemma induction_on {P : SpaceTimeAlgebra ⊗[ℂ] V → Prop} (z : SpaceTimeAlgebra ⊗[ℂ] V)
    (tmul : ∀ (f : SpaceTimeAlgebra) (s : S) (v : ι → ℂ), P (f ⊗ₜ[ℂ] e.symm (s ⊗ₜ[ℂ] v)))
    (add : ∀ a b, P a → P b → P (a + b)) : P z
```

**`LocalGaugeData.MatrixRep.jetEquiv_jetDeriv`**, a lemma, [line 232](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L232).

> The identification of jets intertwines the formal derivative with the entrywise
> derivative.

```lean
lemma jetEquiv_jetDeriv (μ : Fin 1 ⊕ Fin 3) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEquiv e (jetDeriv μ z) = LinearMap.lTensor S (pderivPi μ) (jetEquiv e z)
```

**`LocalGaugeData.MatrixRep.jetEquiv_jetIteratedDeriv`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L244).

> The identification of jets intertwines the iterated formal derivative with the
> entrywise iterated derivative.

```lean
lemma jetEquiv_jetIteratedDeriv (x : Multiset (Fin 1 ⊕ Fin 3)) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEquiv e (jetIteratedDeriv x z) = LinearMap.lTensor S (foldPi x) (jetEquiv e z)
```

**`LocalGaugeData.MatrixRep.jetEval_eq`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L254).

> The base-point evaluation of a jet through the identification.

```lean
lemma jetEval_eq (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEval z = e.symm (LinearMap.lTensor S ccPi (jetEquiv e z))
```

**`LocalGaugeData.MatrixRep.jetEquiv_smul`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L265).

> Multiplication by a scalar jet through the identification.

```lean
lemma jetEquiv_smul (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    jetEquiv e (χ • z)
      = LinearMap.lTensor S
          ((LinearMap.lsmul SpaceTimeAlgebra (ι → SpaceTimeAlgebra) χ).restrictScalars ℂ)
          (jetEquiv e z)
```

**`LocalGaugeData.MatrixRep.jetEquiv_jetOfConstant`**, a lemma, [line 279](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L279).

> A jet of a constant through the identification.

```lean
lemma jetEquiv_jetOfConstant (s : S) (v : ι → ℂ) :
    jetEquiv e (jetOfConstant (e.symm (s ⊗ₜ[ℂ] v))) = s ⊗ₜ[ℂ] (fun i => C (v i))
```

## C. Endomorphisms from matrices

**`LocalGaugeData.MatrixRep.valEndAlgHom`**, a def, [line 295](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L295).

> The endomorphism of the target space `V ≃ S ⊗ (ι → ℂ)` defined by a complex matrix on
> the internal index, as an algebra map.

```lean
noncomputable def valEndAlgHom : Matrix ι ι ℂ →ₐ[ℂ] Module.End ℂ V
```

**`LocalGaugeData.MatrixRep.valEnd`**, a def, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L302).

> The endomorphism of the target space `V ≃ S ⊗ (ι → ℂ)` defined by a complex matrix on
> the internal index, with the Lorentz factor untouched.

```lean
noncomputable def valEnd (B : Matrix ι ι ℂ) : V →ₗ[ℂ] V
```

**`LocalGaugeData.MatrixRep.valEnd_apply`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L304).

```lean
lemma valEnd_apply (B : Matrix ι ι ℂ) (d : V) :
    valEnd e B d = e.symm (LinearMap.lTensor S (Matrix.toLin' B) (e d))
```

**`LocalGaugeData.MatrixRep.valEnd_apply_symm_tmul`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L307).

```lean
lemma valEnd_apply_symm_tmul (B : Matrix ι ι ℂ) (s : S) (v : ι → ℂ) :
    valEnd e B (e.symm (s ⊗ₜ[ℂ] v)) = e.symm (s ⊗ₜ[ℂ] (B.mulVec v))
```

**`LocalGaugeData.MatrixRep.valEnd_add`**, a lemma, [line 311](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L311).

```lean
lemma valEnd_add (A B : Matrix ι ι ℂ) : valEnd e (A + B) = valEnd e A + valEnd e B
```

**`LocalGaugeData.MatrixRep.valEnd_smul`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L314).

```lean
lemma valEnd_smul (z : ℂ) (A : Matrix ι ι ℂ) : valEnd e (z • A) = z • valEnd e A
```

**`LocalGaugeData.MatrixRep.valEnd_zero`**, a lemma, [line 317](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L317).

```lean
lemma valEnd_zero : valEnd e (0 : Matrix ι ι ℂ) = 0
```

**`LocalGaugeData.MatrixRep.valEnd_neg`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L319).

```lean
lemma valEnd_neg (A : Matrix ι ι ℂ) : valEnd e (-A) = -valEnd e A
```

**`LocalGaugeData.MatrixRep.valEnd_multiset_sum`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L322).

```lean
lemma valEnd_multiset_sum (m : Multiset (Matrix ι ι ℂ)) :
    valEnd e m.sum = (m.map (valEnd e)).sum
```

**`LocalGaugeData.MatrixRep.valEnd_mul`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L326).

```lean
lemma valEnd_mul (A B : Matrix ι ι ℂ) : valEnd e (A * B) = valEnd e A ∘ₗ valEnd e B
```

**`LocalGaugeData.MatrixRep.valEnd_one`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L329).

```lean
lemma valEnd_one : valEnd e (1 : Matrix ι ι ℂ) = LinearMap.id
```

**`LocalGaugeData.MatrixRep.jetEnd`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L334).

> The endomorphism of `S ⊗ (ι → SpaceTimeAlgebra)` defined by a matrix of jets on the internal
> index.

```lean
noncomputable def jetEnd (A : Matrix ι ι SpaceTimeAlgebra) :
    S ⊗[ℂ] (ι → SpaceTimeAlgebra) →ₗ[ℂ] S ⊗[ℂ] (ι → SpaceTimeAlgebra)
```

**`LocalGaugeData.MatrixRep.jetEnd_eq_lTensor`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L340).

```lean
lemma jetEnd_eq_lTensor (A : Matrix ι ι SpaceTimeAlgebra) :
    jetEnd S A = LinearMap.lTensor S
      ((Matrix.toLinAlgEquiv' A : Module.End SpaceTimeAlgebra
          (ι → SpaceTimeAlgebra)).restrictScalars ℂ)
```

**`LocalGaugeData.MatrixRep.jetEnd_tmul`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L345).

```lean
lemma jetEnd_tmul (A : Matrix ι ι SpaceTimeAlgebra) (s : S) (w : ι → SpaceTimeAlgebra) :
    jetEnd S A (s ⊗ₜ[ℂ] w) = s ⊗ₜ[ℂ] (A.mulVec w)
```

**`LocalGaugeData.MatrixRep.jetEnd_one`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L350).

```lean
lemma jetEnd_one : jetEnd S (1 : Matrix ι ι SpaceTimeAlgebra) = LinearMap.id
```

**`LocalGaugeData.MatrixRep.jetEnd_mul`**, a lemma, [line 356](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L356).

```lean
lemma jetEnd_mul (A B : Matrix ι ι SpaceTimeAlgebra) : jetEnd S (A * B) =
    jetEnd S A ∘ₗ jetEnd S B
```

**`LocalGaugeData.MatrixRep.matEnd`**, a def, [line 370](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L370).

> The endomorphism of the jets `SpaceTimeAlgebra ⊗ V` of the field defined by a matrix of jets
> on the internal index, through `jetEquiv`.

```lean
noncomputable def matEnd
    (A : Matrix ι ι SpaceTimeAlgebra) : SpaceTimeAlgebra ⊗[ℂ] V →ₗ[ℂ] SpaceTimeAlgebra ⊗[ℂ] V
```

**`LocalGaugeData.MatrixRep.matEnd_apply`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L374).

```lean
lemma matEnd_apply (A : Matrix ι ι SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    matEnd e A z = (jetEquiv e).symm (jetEnd S A (jetEquiv e z))
```

**`LocalGaugeData.MatrixRep.matEnd_one`**, a lemma, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L377).

```lean
lemma matEnd_one : matEnd e (1 : Matrix ι ι SpaceTimeAlgebra) = LinearMap.id
```

**`LocalGaugeData.MatrixRep.matEnd_mul`**, a lemma, [line 382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L382).

```lean
lemma matEnd_mul (A B : Matrix ι ι SpaceTimeAlgebra) :
    matEnd e (A * B) = matEnd e A ∘ₗ matEnd e B
```

**`LocalGaugeData.MatrixRep.matEnd_smul`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L390).

> The matrix endomorphisms are fibrewise: they commute with multiplication by scalar
> jets.

```lean
lemma matEnd_smul (A : Matrix ι ι SpaceTimeAlgebra) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    matEnd e A (χ • z) = χ • matEnd e A z
```

## D. The jet gauge action

**`LocalGaugeData.MatrixRep.repJet`**, a def, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L413).

> **The jet gauge action** of a matrix representation on the jets of a `V`-valued
> field: the matrix of jets acts on the internal index by matrix–vector multiplication,
> with the Lorentz factor untouched.

```lean
noncomputable def repJet : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] V)
```

**`LocalGaugeData.MatrixRep.repJet_apply`**, a lemma, [line 418](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L418).

```lean
lemma repJet_apply (U : GJ) : R.repJet e U = matEnd e (R.mat U)
```

**`LocalGaugeData.MatrixRep.repJet_smul`**, a lemma, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L422).

> **The jet gauge action is fibrewise**: it commutes with multiplication by scalar
> jets.

```lean
lemma repJet_smul (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] V) :
    R.repJet e U (χ • z) = χ • R.repJet e U z
```

**`LocalGaugeData.MatrixRep.repAlgebra`**, a def, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L429).

> **The action of the gauge algebra** of a matrix representation on the target space
> `V ≃ S ⊗ (ι → ℂ)`: the action matrix acts on the internal index, real-linearly in the
> algebra slot and complex-linearly in the value slot.

```lean
noncomputable def repAlgebra : 𝔤 →ₗ[ℝ] V →ₗ[ℂ] V
```

**`LocalGaugeData.MatrixRep.repAlgebra_apply`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L438).

```lean
lemma repAlgebra_apply (c : 𝔤) : R.repAlgebra e c = valEnd e (R.act c)
```

## E. The base-point Taylor coefficients

**`LocalGaugeData.MatrixRep.repCoeff_eq`**, a lemma, [line 448](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L448).

> **The base-point Taylor coefficients of the jet gauge action** are the endomorphisms
> of the base-point Taylor coefficients of the matrix of jets.

```lean
lemma repCoeff_eq (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff (R.repJet e) U x
      = valEnd e ((R.mat U).map fun f =>
          constantCoeff (SpaceTimeAlgebra.iteratedPDeriv x f))
```

## F. The infinitesimal action underlies the jet gauge action

**`LocalGaugeData.MatrixRep.isInfinitesimalActionOf`**, a lemma, [line 475](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L475).

> **The action of the gauge algebra of a matrix representation is the infinitesimal
> action underlying its jet gauge action**: the base-point Taylor coefficients obey the
> Maurer–Cartan Leibniz law and intertwine the action with the adjoint transports.

```lean
lemma isInfinitesimalActionOf :
    jets.IsInfinitesimalActionOf (R.repAlgebra e) (R.repJet e)
```

## G. The matter field

**`LocalGaugeData.MatrixRep.repLorentz`**, a def, [line 549](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L549).

> The Lorentz action on the target space `V ≃ S ⊗ (ι → ℂ)`: the given action on the
> Lorentz factor `S`, transported through `e`.

```lean
noncomputable def repLorentz (ρ : Representation ℂ SL(2,ℂ) S) :
    Representation ℂ SL(2,ℂ) V
```

### G.1. The global action

> A matrix representation of jets restricts to the jets of constant gauge transformations;
> the constant terms of their matrices are the matrices of a representation of the global
> gauge group on the target space. When the matrices of constant jets are constant, the jet
> action on a constant jet is this global action on the value factor.

**`LocalGaugeData.MatrixRep.repGlobal`**, a def, [line 569](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L569).

> **The global gauge action** of a matrix representation of jets: a global gauge
> transformation acts by the constant term of the matrix of its constant jet.

```lean
noncomputable def repGlobal : Representation ℂ G₀ V
```

**`LocalGaugeData.MatrixRep.repGlobal_apply`**, a lemma, [line 581](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L581).

```lean
lemma repGlobal_apply (g : G₀) :
    R.repGlobal e g = valEnd e
        ((R.mat (jets.ofConstant g)).map (constantCoeff : SpaceTimeAlgebra → ℂ))
```

**`LocalGaugeData.MatrixRep.repGlobal_apply_symm_tmul`**, a lemma, [line 588](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L588).

> The global action on a pure tensor: the constant term of the matrix acts on the
> internal index.

```lean
lemma repGlobal_apply_symm_tmul (g : G₀) (s : S) (v : ι → ℂ) :
    R.repGlobal e g (e.symm (s ⊗ₜ[ℂ] v))
      = e.symm (s ⊗ₜ[ℂ]
          ((R.mat (jets.ofConstant g)).map (constantCoeff : SpaceTimeAlgebra → ℂ)).mulVec v)
```

**`LocalGaugeData.MatrixRep.map_C_mulVec_smul`**, a lemma, [line 597](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L597).

> A matrix of constant jets acts on a scalar jet times a constant vector through its
> constant matrix.

```lean
lemma map_C_mulVec_smul (B : Matrix ι ι ℂ) (v : ι → ℂ) (χ : SpaceTimeAlgebra) :
    (B.map (C : ℂ → SpaceTimeAlgebra)).mulVec (fun i => v i • χ) = fun i => (B.mulVec v) i • χ
```

**`LocalGaugeData.MatrixRep.repJet_ofConstant`**, a lemma, [line 605](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L605).

> **On jets of constant gauge transformations the jet action is the global action** on
> the value factor, provided the matrices of constant jets are constant.

```lean
lemma repJet_ofConstant
    (hconst : ∀ g, R.mat (jets.ofConstant g)
      = ((R.mat (jets.ofConstant g)).map (constantCoeff : SpaceTimeAlgebra → ℂ)).map
          (C : ℂ → SpaceTimeAlgebra))
    (g : G₀) :
    R.repJet e (jets.ofConstant g) = TensorProduct.map LinearMap.id (R.repGlobal e g)
```

**`LocalGaugeData.MatrixRep.matterField`**, a def, [line 630](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L630).

> **The matter field of a matrix representation**: the target space `V ≃ S ⊗ (ι → ℂ)`
> with the Lorentz action on `S`, the jet gauge action of the matrix representation, and
> the given mass weight and declared statistics.

```lean
noncomputable def matterField (ρ : Representation ℂ SL(2,ℂ) S) (w : ℕ) (σ : FieldStatistic) :
    MatterField jets
```

**`LocalGaugeData.MatrixRep.matterField_V`**, a lemma, [line 644](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L644).

```lean
lemma matterField_V : (R.matterField e ρ w σ).V = V
```

**`LocalGaugeData.MatrixRep.matterField_repLorentz`**, a lemma, [line 647](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L647).

```lean
lemma matterField_repLorentz : (R.matterField e ρ w σ).repLorentz = repLorentz e ρ
```

**`LocalGaugeData.MatrixRep.matterField_repJet`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L650).

```lean
lemma matterField_repJet : (R.matterField e ρ w σ).repJet = R.repJet e
```

**`LocalGaugeData.MatrixRep.matterField_repAlgebra`**, a lemma, [line 653](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L653).

```lean
lemma matterField_repAlgebra : (R.matterField e ρ w σ).repAlgebra = R.repAlgebra e
```

**`LocalGaugeData.MatrixRep.matterField_massWeight`**, a lemma, [line 656](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L656).

```lean
lemma matterField_massWeight : (R.matterField e ρ w σ).massWeight = w
```

**`LocalGaugeData.MatrixRep.matterField_statistic`**, a lemma, [line 659](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L659).

```lean
lemma matterField_statistic : (R.matterField e ρ w σ).statistic = σ
```

**`LocalGaugeData.MatrixRep.repLorentz_apply_symm_tmul`**, a lemma, [line 662](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L662).

```lean
lemma repLorentz_apply_symm_tmul (Λ : SL(2,ℂ)) (s : S) (v : ι → ℂ) :
    repLorentz e ρ Λ (e.symm (s ⊗ₜ[ℂ] v)) = e.symm (ρ Λ s ⊗ₜ[ℂ] v)
```

**`LocalGaugeData.MatrixRep.repAlgebra_comm_repLorentz`**, a lemma, [line 669](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L669).

> The gauge algebra acts on the internal index and the Lorentz group on the Lorentz
> factor, so the two actions commute.

```lean
lemma repAlgebra_comm_repLorentz (c : 𝔤) (Λ : SL(2,ℂ)) (v : V) :
    R.repAlgebra e c (repLorentz e ρ Λ v) = repLorentz e ρ Λ (R.repAlgebra e c v)
```

**`LocalGaugeData.MatrixRep.matterField_gaugeLorentzCompatible`**, a lemma, [line 681](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L681).

> The matter field of a matrix representation satisfies `MatterField.GaugeLorentzCompatible`,
> for every matrix representation and Lorentz factor: the two actions live on different
> tensor factors.

```lean
lemma matterField_gaugeLorentzCompatible :
    (R.matterField e ρ w σ).GaugeLorentzCompatible
```

**`LocalGaugeData.MatrixRep.matterField_pureJetsActTrivially`**, a lemma, [line 689](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean#L689).

> The matter field of a matrix representation satisfies `MatterField.PureJetsActTrivially`
> as soon as the matrix of every jet with trivial value has identity constant term. This
> hypothesis is not a consequence of the axioms of `MatrixRep`, which fix the constant term
> of `mat` on pure jets only up to a scalar character.

```lean
lemma matterField_pureJetsActTrivially
    (hmat : ∀ {W : GJ}, jets.eval W = 1 → (R.mat W).map
        (constantCoeff : SpaceTimeAlgebra → ℂ) = 1) :
    (R.matterField e ρ w σ).PureJetsActTrivially
```

## Depends on

- [Matter fields of a gauge theory](../part-05/matterfield-basic.md)

## Proof depends on

- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/MatrixRep/Basic.lean)
