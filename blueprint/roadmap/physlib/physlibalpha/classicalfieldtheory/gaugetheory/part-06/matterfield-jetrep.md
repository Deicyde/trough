---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField.EndJet, GlobalGaugeGroup.MatterField.lieAlgebraRepFun_congr, GlobalGaugeGroup.MatterField.jetLieAlgebraRepFun, GlobalGaugeGroup.MatterField.jetDerivValue_jetLieAlgebraRepFun, GlobalGaugeGroup.MatterField.jetLieAlgebraRep, GlobalGaugeGroup.MatterField.jetDerivValue_jetLieAlgebraRep, GlobalGaugeGroup.MatterField.jetLieAlgebraRep_ofConstantLie, GlobalGaugeGroup.MatterField.jetDeriv_jetLieAlgebraRep
statement: formalized
proof: formalized
---

# The jet representation of a matter field

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetRep`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean): 23 declarations, 19 with a docstring.

> The continuous representation `ρ : G → GL(V)` of a matter field, extended to the jets
> of gauge transformations and to the Lie algebra jets.

## i. Overview

> A matter field `M` transforms under the representation `ρ = M.rep` of the global
> gauge group `G` on its target space `V`. A gauge transformation `U(x)` acts on it through
> `ρ(U(x))`, a function valued in the linear maps on `V`. Its jets are the jets of
> `V →L[ℂ] V`-valued functions, `M.EndJet = SpaceTimeAlgebra ⊗[ℂ] (V →L[ℂ] V)`, an algebra. On
> jets, a gauge jet `U` acts through the jet `ρ(U)` of `x ↦ ρ(U(x))`, and a Lie algebra jet `A`
> through the jet `dρ(A)` of `x ↦ dρ(A(x))`, with `dρ` the Lie algebra representation of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.DerivRep`.
>
> The jet action is built from the Lie algebra action and the Maurer–Cartan form, and not by
> applying `ρ` to the power series entries of `U`, because `ρ` is only defined on the group `G`
> itself. A jet is formal, so there is no group element `U(x)` to which `ρ` could be applied
> and no formula for the jet of `ρ(U(x))` in terms of the entries of `U`. What is available is
> the Lie algebra representation `dρ`, which acts on the Lie algebra jets, and the Maurer–Cartan
> form `ω_μ = (∂_μ U) U⁻¹`, which carries a gauge jet into them. The derivative of `ρ(U(x))` is
> `dρ(ω_μ) ρ(U(x))`, so the jet is recovered as the unique solution of this equation with the
> right base-point value.
>
> The jet `dρ(A)` is defined by its base-point derivatives, those of `A` with `dρ` applied, each
> lying in the Lie algebra. It commutes with the derivatives, sends constant jets to constant
> jets and preserves the commutator, the base-point derivatives of a commutator being sums of
> commutators of base-point derivatives.
>
> The jet `ρ(U)` is characterised by its value `ρ(U(0))` and the derivative identity
> `∂_μ ρ(U) = dρ(ω_μ) ρ(U)`, with `ω_μ = (∂_μ U) U⁻¹` the Maurer–Cartan form. The flatness of
> the Maurer–Cartan form, `∂_μ ω_ν − ∂_ν ω_μ = [ω_μ, ω_ν]`, carries over to `dρ(ω_μ)`, so the
> derivative identity has a unique solution with any prescribed value, by the theory of flat
> families of jets in `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Jet`.
> Uniqueness then gives `ρ(U V) = ρ(U) ρ(V)` and the equivariance
> `dρ(U A U⁻¹) ρ(U) = ρ(U) dρ(A)`.

## ii. Key results

> - `GlobalGaugeGroup.MatterField.EndJet` : the jets of linear maps on the target space.
> - `GlobalGaugeGroup.MatterField.jetLieAlgebraRep` : the jet `dρ(A)` of a Lie algebra
>   jet.
> - `GlobalGaugeGroup.MatterField.jetRep` : the jet `ρ(U)` of a gauge jet, as a
>   homomorphism.
> - `GlobalGaugeGroup.MatterField.jetDeriv_jetRep` : the derivative identity
>   `∂_μ ρ(U) = dρ(ω_μ) ρ(U)`.
> - `GlobalGaugeGroup.MatterField.jetLieAlgebraRep_adjoint_mul_jetRep` : the equivariance
>   `dρ(U A U⁻¹) ρ(U) = ρ(U) dρ(A)`.

## iv. References

> * B. C. Hall, *Lie Groups, Lie Algebras, and Representations*, 2nd ed., Springer (2015).

## A. The Lie algebra representation on Lie algebra jets

**`GlobalGaugeGroup.MatterField.EndJet`**, an abbrev, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L99).

> The jets of linear maps on the target space, an algebra.

```lean
abbrev EndJet : Type
```

**`GlobalGaugeGroup.MatterField.lieAlgebraRepFun_congr`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L102).

> `dρ` depends on a generator only through its matrix.

```lean
lemma lieAlgebraRepFun_congr {X Y : G.lieAlgebra} (h : (X : Matrix κ κ ℂ) = Y) :
    lieAlgebraRepFun M X = lieAlgebraRepFun M Y
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRepFun`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L108).

> The jet `dρ(A)` of a Lie algebra jet `A`, whose base-point derivative along `s` is `dρ` of
> that of `A`.

```lean
noncomputable def jetLieAlgebraRepFun (A : G.jetLieSubalgebra) : M.EndJet
```

**`GlobalGaugeGroup.MatterField.jetDerivValue_jetLieAlgebraRepFun`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L112).

```lean
lemma jetDerivValue_jetLieAlgebraRepFun (A : G.jetLieSubalgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    jetDerivValue s (jetLieAlgebraRepFun M A) =
      lieAlgebraRepFun M ⟨derivValueMatrix s A.1, A.2 s⟩
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRep`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L118).

> The jet `dρ(A)` of a Lie algebra jet, as a real-linear map.

```lean
noncomputable def jetLieAlgebraRep : G.jetLieSubalgebra →ₗ[ℝ] M.EndJet
```

**`GlobalGaugeGroup.MatterField.jetDerivValue_jetLieAlgebraRep`**, a lemma, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L130).

```lean
lemma jetDerivValue_jetLieAlgebraRep (A : G.jetLieSubalgebra) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    jetDerivValue s (jetLieAlgebraRep M A) = lieAlgebraRepFun M ⟨derivValueMatrix s A.1, A.2 s⟩
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRep_ofConstantLie`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L135).

> The jet `dρ(A)` of a constant Lie algebra jet `A = a` is the constant jet `dρ(a)`.

```lean
lemma jetLieAlgebraRep_ofConstantLie (a : G.lieSubalgebra) :
    jetLieAlgebraRep M (G.ofConstantLie a) = jetOfConstant (lieAlgebraRep M a)
```

**`GlobalGaugeGroup.MatterField.jetDeriv_jetLieAlgebraRep`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L151).

> The jet `dρ(A)` commutes with the formal derivatives, `∂_μ dρ(A) = dρ(∂_μ A)`.

```lean
lemma jetDeriv_jetLieAlgebraRep (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    jetDeriv μ (jetLieAlgebraRep M A) = jetLieAlgebraRep M (G.derivJ μ A)
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRep_lie`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L159).

> The jet `dρ` on Lie algebra jets preserves the commutator. The base-point derivatives of
> a commutator are sums of commutators of base-point derivatives, each preserved by `dρ`.

```lean
lemma jetLieAlgebraRep_lie (A B : G.jetLieSubalgebra) :
    jetLieAlgebraRep M ⁅A, B⁆ =
      jetLieAlgebraRep M A * jetLieAlgebraRep M B -
        jetLieAlgebraRep M B * jetLieAlgebraRep M A
```

## B. The jet of a representation along a gauge jet

### B.1. The flat family `dρ(ω)`

**`GlobalGaugeGroup.MatterField.jetDeriv_jetLieAlgebraRep_maurerCartan_sub`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L194).

> The structure equation for `dρ(ω)`, `∂_μ dρ(ω_ν) − ∂_ν dρ(ω_μ) = [dρ(ω_μ), dρ(ω_ν)]`,
> so the family `dρ(ω_μ)` is flat.

```lean
lemma jetDeriv_jetLieAlgebraRep_maurerCartan_sub (U : G.gaugeJetGroup) (μ ν : Fin 1 ⊕ Fin 3) :
    jetDeriv μ (jetLieAlgebraRep M (G.maurerCartan U ν)) -
        jetDeriv ν (jetLieAlgebraRep M (G.maurerCartan U μ)) =
      jetLieAlgebraRep M (G.maurerCartan U μ) * jetLieAlgebraRep M (G.maurerCartan U ν) -
        jetLieAlgebraRep M (G.maurerCartan U ν) * jetLieAlgebraRep M (G.maurerCartan U μ)
```

### B.2. The jet of the representation along a gauge jet

**`GlobalGaugeGroup.MatterField.jetRepFun`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L212).

> The jet `ρ(U)` of the representation along a gauge jet `U`, the solution of the
> derivative identity `∂_μ ρ(U) = dρ(ω_μ) ρ(U)` with value `ρ(U(0))`, which exists since the
> family `dρ(ω_μ)` is flat.

```lean
noncomputable def jetRepFun (U : G.gaugeJetGroup) : M.EndJet
```

**`GlobalGaugeGroup.MatterField.jetEval_jetRepFun`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L218).

> The value of `ρ(U)` at the base point is `ρ(U(0))`.

```lean
lemma jetEval_jetRepFun (U : G.gaugeJetGroup) :
    jetEval (jetRepFun M U) = ((M.rep (G.evalGaugeJet U) : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V)
```

**`GlobalGaugeGroup.MatterField.jetDeriv_jetRepFun`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L224).

> The derivative identity `∂_μ ρ(U) = dρ(ω_μ) ρ(U)`.

```lean
lemma jetDeriv_jetRepFun (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv μ (jetRepFun M U) = jetLieAlgebraRep M (G.maurerCartan U μ) * jetRepFun M U
```

**`GlobalGaugeGroup.MatterField.eq_jetRepFun`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L230).

> The jet `ρ(U)` is the only jet with value `ρ(U(0))` satisfying the derivative identity.

```lean
lemma eq_jetRepFun {U : G.gaugeJetGroup} {Y : M.EndJet}
    (hY : ∀ μ, jetDeriv μ Y = jetLieAlgebraRep M (G.maurerCartan U μ) * Y)
    (hY0 : jetEval Y = ((M.rep (G.evalGaugeJet U) : (M.V →L[ℂ] M.V)ˣ) : M.V →L[ℂ] M.V)) :
    Y = jetRepFun M U
```

**`GlobalGaugeGroup.MatterField.jetRepFun_one`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L236).

```lean
lemma jetRepFun_one : jetRepFun M 1 = 1
```

### B.3. Equivariance and multiplicativity

**`GlobalGaugeGroup.MatterField.jetDeriv_jetLieAlgebraRep_adjointJ`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L249).

> The derivative of `dρ(U A U⁻¹)` is `dρ(U (∂_μ A) U⁻¹) + [dρ(ω_μ), dρ(U A U⁻¹)]`.

```lean
lemma jetDeriv_jetLieAlgebraRep_adjointJ (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra)
    (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv μ (jetLieAlgebraRep M (G.adjointJ U A)) =
      jetLieAlgebraRep M (G.adjointJ U (G.derivJ μ A)) +
        (jetLieAlgebraRep M (G.maurerCartan U μ) *
            jetLieAlgebraRep M (G.adjointJ U A) -
          jetLieAlgebraRep M (G.adjointJ U A) *
            jetLieAlgebraRep M (G.maurerCartan U μ))
```

**`GlobalGaugeGroup.MatterField.jetEval_adjointDefect`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L261).

> The equivariance defect `dρ(U A U⁻¹) ρ(U) − ρ(U) dρ(A)` vanishes at the base point, by
> `dρ(g X g⁻¹) = ρ(g) dρ(X) ρ(g)⁻¹`.

```lean
lemma jetEval_adjointDefect (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    jetEval (jetLieAlgebraRep M (G.adjointJ U A) * jetRepFun M U -
        jetRepFun M U * jetLieAlgebraRep M A) = 0
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRep_adjoint_mul_jetRepFun`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L277).

> The equivariance `dρ(U A U⁻¹) ρ(U) = ρ(U) dρ(A)`. The defect vanishes at the base point
> and its derivative is the defect of the derivative plus `dρ(ω_μ)` times the defect, so it
> vanishes.

```lean
lemma jetLieAlgebraRep_adjoint_mul_jetRepFun (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    jetLieAlgebraRep M (G.adjointJ U A) * jetRepFun M U =
      jetRepFun M U * jetLieAlgebraRep M A
```

**`GlobalGaugeGroup.MatterField.jetRepFun_mul`**, a lemma, [line 291](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L291).

> The jet of a representation is multiplicative, `ρ(U V) = ρ(U) ρ(V)`.

```lean
lemma jetRepFun_mul (U V : G.gaugeJetGroup) :
    jetRepFun M (U * V) = jetRepFun M U * jetRepFun M V
```

### B.4. The jet representation

**`GlobalGaugeGroup.MatterField.jetRep`**, a def, [line 310](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L310).

> The jet representation `U ↦ ρ(U)` of the jet gauge group.

```lean
noncomputable def jetRep : G.gaugeJetGroup →* M.EndJet
```

**`GlobalGaugeGroup.MatterField.jetRep_apply`**, a lemma, [line 316](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L316).

```lean
lemma jetRep_apply (U : G.gaugeJetGroup) : jetRep M U = jetRepFun M U
```

**`GlobalGaugeGroup.MatterField.jetDeriv_jetRep`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L319).

> The derivative identity `∂_μ ρ(U) = dρ(ω_μ) ρ(U)` of the jet representation.

```lean
lemma jetDeriv_jetRep (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    jetDeriv μ (jetRep M U) = jetLieAlgebraRep M (G.maurerCartan U μ) * jetRep M U
```

**`GlobalGaugeGroup.MatterField.jetLieAlgebraRep_adjoint_mul_jetRep`**, a lemma, [line 324](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean#L324).

> The equivariance `dρ(U A U⁻¹) ρ(U) = ρ(U) dρ(A)` of the jet representation.

```lean
lemma jetLieAlgebraRep_adjoint_mul_jetRep (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    jetLieAlgebraRep M (G.adjointJ U A) * jetRep M U =
      jetRep M U * jetLieAlgebraRep M A
```

## Depends on

- [The jet operations of a global gauge group](../part-02/globalgaugegroup-jetoperations.md)
- [`V`-valued jets](../part-04/localfieldalgebra-jet.md)
- [The derivative of a representation of a global gauge group](matterfield-derivrep.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/JetRep.lean)
