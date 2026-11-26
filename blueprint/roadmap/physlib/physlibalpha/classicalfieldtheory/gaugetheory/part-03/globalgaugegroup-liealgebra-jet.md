---
declaration: module
origin: cited
lean: GlobalGaugeGroup.jetLieAlgebra, GlobalGaugeGroup.mem_jetLieAlgebra, GlobalGaugeGroup.mem_jetLieAlgebra_iff, GlobalGaugeGroup.mem_jetLieAlgebra_of, GlobalGaugeGroup.map_pderiv_mem_jetLieAlgebra, GlobalGaugeGroup.commutator_mem_jetLieAlgebra, GlobalGaugeGroup.jetLieSubalgebra, GlobalGaugeGroup.mem_jetLieSubalgebra
statement: formalized
proof: formalized
---

# The Lie algebra jets of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Jet`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean): 21 declarations (4 instances with no name), 14 with a docstring.

> The Taylor series at a point of the infinitesimal gauge transformations.

## i. Overview

> An infinitesimal gauge transformation of a global gauge group `G` with Lie algebra `𝔤` is a
> smooth map from spacetime into `𝔤`. Its jet at the base point is a matrix of formal power
> series in the spacetime coordinates, all of whose base-point derivatives `∂_s A (0)` lie in
> `𝔤`. These Lie algebra jets form a Lie algebra under the commutator, since by the Leibniz
> rule each base-point derivative of a commutator is a sum of commutators of base-point
> derivatives.
>
> Membership is checked through `mem_jetLieAlgebra_of`: a property of matrices of jets that is
> preserved by every derivative, and that places the value in `𝔤`, places every base-point
> derivative in `𝔤`.
>
> This is how conjugation `A ↦ U⁻¹ A U` by an invertible matrix of jets `U` is shown to
> preserve the Lie algebra jets, when the value of `U` lies in the group and `(∂_μ U) U⁻¹` is a
> Lie algebra jet. At the base point it is the adjoint action of the group, and the derivative
> of `U⁻¹ A U` is `U⁻¹ (∂_μ A − [(∂_μ U) U⁻¹, A]) U`, again of the same form. These are the
> facts that make the jet gauge group of
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.GaugeJetGroup` a group.
>
> Being a Lie algebra jet is a condition on each Taylor coefficient separately, since the
> base-point derivative along `s` is `s!` times the coefficient of `x^s`. So any Taylor data in
> `𝔤` give a Lie algebra jet. A matrix of jets `W` solving the linear radial system
> `E W + W = B + R W − W R`, for Lie algebra jets `B` and `R` with `R` vanishing at the base
> point, is a Lie algebra jet. Here `E = ∑_ρ x_ρ ∂_ρ` is the Euler operator, which multiplies
> the coefficient of degree `n` by `n`, so the coefficient of `W` of degree `n` is `1/(n + 1)`
> times that of `B` plus commutators of coefficients of `R` with coefficients of `W` of lower
> degree. This is how the radial transport of a Lie algebra jet is shown to be a gauge jet.

## ii. Key results

> - `GlobalGaugeGroup.jetLieAlgebra` : the Lie algebra jets, as a real subspace.
> - `GlobalGaugeGroup.mem_jetLieAlgebra_iff` : a matrix of jets is a Lie algebra jet exactly
>   when its value lies in the Lie algebra and its derivatives are Lie algebra jets.
> - `GlobalGaugeGroup.mem_jetLieAlgebra_of` : the induction principle for Lie algebra jets.
> - `GlobalGaugeGroup.jetLieSubalgebra` : the Lie algebra jets, as a Lie subalgebra.
> - `GlobalGaugeGroup.inv_mul_mul_mem_jetLieAlgebra` : conjugation by an invertible matrix of
>   jets with value in the group and `(∂_μ U) U⁻¹` a Lie algebra jet preserves the Lie algebra
>   jets.
> - `GlobalGaugeGroup.taylorMatrix_mem_jetLieAlgebra` : Taylor data in the Lie algebra give a
>   Lie algebra jet.
> - `GlobalGaugeGroup.mem_jetLieAlgebra_of_euler` : a solution of the linear radial system
>   `E W + W = B + R W − W R` with `B`, `R` Lie algebra jets is a Lie algebra jet.

## iv. References

> * None.

## A. The Lie algebra jets

**`GlobalGaugeGroup.jetLieAlgebra`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L91).

> The real subspace of matrices of jets all of whose base-point derivatives lie in the
> Lie algebra.

```lean
def jetLieAlgebra : Submodule ℝ (Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_jetLieAlgebra`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L103).

```lean
lemma mem_jetLieAlgebra {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieAlgebra ↔ ∀ s, derivValueMatrix s A ∈ G.lieAlgebra
```

**`GlobalGaugeGroup.mem_jetLieAlgebra_iff`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L108).

> A matrix of jets is a Lie algebra jet exactly when its value lies in the Lie algebra and
> its derivatives are Lie algebra jets.

```lean
lemma mem_jetLieAlgebra_iff {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieAlgebra ↔
      (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A ∈ G.lieAlgebra ∧
        ∀ μ, A.map (pderiv μ) ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.mem_jetLieAlgebra_of`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L121).

> An induction principle for Lie algebra jets. A property of matrices of jets that is
> preserved by every derivative, and that forces the value into the Lie algebra, forces
> every base-point derivative into the Lie algebra.

```lean
lemma mem_jetLieAlgebra_of {P : Matrix κ κ SpaceTimeAlgebra → Prop}
    (h0 : ∀ A, P A → (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A ∈ G.lieAlgebra)
    (hd : ∀ A, P A → ∀ μ, P (A.map (pderiv μ))) {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : P A) : A ∈ G.jetLieAlgebra
```

## B. Closure properties

**`GlobalGaugeGroup.map_pderiv_mem_jetLieAlgebra`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L136).

```lean
lemma map_pderiv_mem_jetLieAlgebra {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (μ : Fin 1 ⊕ Fin 3) : A.map (pderiv μ) ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.commutator_mem_jetLieAlgebra`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L142).

> The Lie algebra jets are closed under the commutator. By the Leibniz rule each
> base-point derivative of a commutator is a sum of commutators of base-point derivatives.

```lean
lemma commutator_mem_jetLieAlgebra {A B : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) (hB : B ∈ G.jetLieAlgebra) : A * B - B * A ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.jetLieSubalgebra`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L155).

> The Lie algebra jets, as a Lie subalgebra of matrices of jets under the commutator.

```lean
def jetLieSubalgebra : LieSubalgebra ℝ (Matrix κ κ SpaceTimeAlgebra)
```

**`GlobalGaugeGroup.mem_jetLieSubalgebra`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L162).

```lean
lemma mem_jetLieSubalgebra {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieSubalgebra ↔ A ∈ G.jetLieAlgebra
```

**An instance with no name**, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L165).

```lean
noncomputable instance : AddCommGroup G.jetLieSubalgebra
```

**An instance with no name**, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L167).

```lean
noncomputable instance : Module ℝ G.jetLieSubalgebra
```

**An instance with no name**, [line 169](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L169).

```lean
noncomputable instance : LieRing G.jetLieSubalgebra
```

**An instance with no name**, [line 171](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L171).

```lean
noncomputable instance : LieAlgebra ℝ G.jetLieSubalgebra
```

**`GlobalGaugeGroup.mapMatrix_C_mem_jetLieAlgebra`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L174).

> A constant matrix in the Lie algebra is a Lie algebra jet.

```lean
lemma mapMatrix_C_mem_jetLieAlgebra {a : Matrix κ κ ℂ} (ha : a ∈ G.lieAlgebra) :
    (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.X_smul_mem_jetLieAlgebra`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L184).

> The Lie algebra jets are closed under multiplication by a coordinate.

```lean
lemma X_smul_mem_jetLieAlgebra (μ : Fin 1 ⊕ Fin 3) {A : Matrix κ κ SpaceTimeAlgebra}
    (hA : A ∈ G.jetLieAlgebra) : (X μ : SpaceTimeAlgebra) • A ∈ G.jetLieAlgebra
```

## C. Conjugation by invertible matrices of jets

**`GlobalGaugeGroup.inv_mul_mul_mem_jetLieAlgebra`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L217).

> Conjugation `A ↦ U⁻¹ A U` preserves the Lie algebra jets, when the value of `U` lies in
> the group and `(∂_μ U) U⁻¹` is a Lie algebra jet. At the base point it is the adjoint
> action of the group, and the derivative of `U⁻¹ A U` is again of this form,
> `U⁻¹ (∂_μ A − [(∂_μ U) U⁻¹, A]) U`.

```lean
lemma inv_mul_mul_mem_jetLieAlgebra {U : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hU : unitsEval U ∈ G.group)
    (hω : ∀ μ, (U : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) *
      (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra) ∈ G.jetLieAlgebra)
    {A : Matrix κ κ SpaceTimeAlgebra} (hA : A ∈ G.jetLieAlgebra) :
    (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra) * A * U ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.map_pderiv_inv_mul_mem_jetLieAlgebra`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L241).

> The derivative of an inverse is a Lie algebra jet when the derivative of the matrix is. For
> an invertible matrix of jets `U` with value in the group and `(∂_μ U) U⁻¹` a Lie algebra jet,
> `(∂_μ U⁻¹) U = −U⁻¹ ((∂_μ U) U⁻¹) U` is a Lie algebra jet.

```lean
lemma map_pderiv_inv_mul_mem_jetLieAlgebra {U : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hU : unitsEval U ∈ G.group)
    (hω : ∀ μ, (U : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) *
      (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra) ∈ G.jetLieAlgebra) (μ : Fin 1 ⊕ Fin 3) :
    (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) * (U : Matrix κ κ SpaceTimeAlgebra)
      ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.mul_mul_inv_mem_jetLieAlgebra`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L253).

> Conjugation `A ↦ U A U⁻¹` preserves the Lie algebra jets, when the value of `U` lies in
> the group and `(∂_μ U) U⁻¹` is a Lie algebra jet.

```lean
lemma mul_mul_inv_mem_jetLieAlgebra {U : GeneralLinearGroup κ SpaceTimeAlgebra}
    (hU : unitsEval U ∈ G.group)
    (hω : ∀ μ, (U : Matrix κ κ SpaceTimeAlgebra).map (pderiv μ) *
      (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra) ∈ G.jetLieAlgebra)
    {A : Matrix κ κ SpaceTimeAlgebra} (hA : A ∈ G.jetLieAlgebra) :
    (U : Matrix κ κ SpaceTimeAlgebra) * A * (↑U⁻¹ : Matrix κ κ SpaceTimeAlgebra)
      ∈ G.jetLieAlgebra
```

## D. Taylor coefficients and the radial system

**`GlobalGaugeGroup.mem_jetLieAlgebra_iff_coeff`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L272).

> A matrix of jets is a Lie algebra jet exactly when each of its matrices of Taylor
> coefficients lies in the Lie algebra.

```lean
lemma mem_jetLieAlgebra_iff_coeff {A : Matrix κ κ SpaceTimeAlgebra} :
    A ∈ G.jetLieAlgebra ↔ ∀ p, A.map (coeff p) ∈ G.lieAlgebra
```

**`GlobalGaugeGroup.taylorMatrix_mem_jetLieAlgebra`**, a lemma, [line 287](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L287).

> The matrix of jets with base-point Taylor data in the Lie algebra is a Lie algebra jet.

```lean
lemma taylorMatrix_mem_jetLieAlgebra {c : Multiset (Fin 1 ⊕ Fin 3) → Matrix κ κ ℂ}
    (hc : ∀ s, c s ∈ G.lieAlgebra) : taylorMatrix c ∈ G.jetLieAlgebra
```

**`GlobalGaugeGroup.map_coeff_commutator_mem_lieAlgebra`**, a lemma, [line 295](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L295).

> The Taylor coefficient of `x^p` of the commutator `R W − W R` lies in the Lie algebra when
> `R` is a Lie algebra jet vanishing at the base point and the coefficients of `W` of degree
> less than that of `p` lie in the Lie algebra.

```lean
lemma map_coeff_commutator_mem_lieAlgebra {R W : Matrix κ κ SpaceTimeAlgebra}
    (hR : R ∈ G.jetLieAlgebra) (hR0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix R = 0)
    {p : (Fin 1 ⊕ Fin 3) →₀ ℕ}
    (hW : ∀ q, Finsupp.degree q < Finsupp.degree p → W.map (coeff q) ∈ G.lieAlgebra) :
    (R * W - W * R).map (coeff p) ∈ G.lieAlgebra
```

**`GlobalGaugeGroup.mem_jetLieAlgebra_of_euler`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean#L326).

> A solution of a linear radial system built from Lie algebra jets is a Lie algebra jet. The
> system is `E W + W = B + R W − W R` for a matrix of jets `W`, where `B` and `R` are Lie
> algebra jets with `R` vanishing at the base point, and `E` is the Euler operator, which
> multiplies the coefficient of degree `n` by `n`. The coefficient of `W` of degree `n` is
> `1/(n + 1)` times that of `B` plus commutators with coefficients of `W` of lower degree, and
> lies in the Lie algebra by induction on `n`.

```lean
lemma mem_jetLieAlgebra_of_euler {W B R : Matrix κ κ SpaceTimeAlgebra}
    (hB : B ∈ G.jetLieAlgebra) (hR : R ∈ G.jetLieAlgebra)
    (hR0 : (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix R = 0)
    (hW : ∑ ρ, (X ρ : SpaceTimeAlgebra) • W.map (pderiv ρ) + W = B + (R * W - W * R)) :
    W ∈ G.jetLieAlgebra
```

## Depends on

- [The Lie algebra of a global gauge group](../part-02/globalgaugegroup-liealgebra-basic.md)
- [Matrices over the jet ring](../../../spaceandtime/spacetime/spacetimealgebra-matrix.md)
- [Taylor data of matrices of jets](../../../spaceandtime/spacetime/spacetimealgebra-taylor.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/LieAlgebra/Jet.lean)
