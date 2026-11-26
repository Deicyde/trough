---
declaration: module
origin: cited
lean: GlobalGaugeGroup.evalLie, GlobalGaugeGroup.evalLie_val, GlobalGaugeGroup.ofConstantLie, GlobalGaugeGroup.ofConstantLie_val, GlobalGaugeGroup.evalLie_ofConstantLie, GlobalGaugeGroup.evalLie_surjective, GlobalGaugeGroup.derivJ, GlobalGaugeGroup.derivJ_val
statement: formalized
proof: formalized
---

# The jet operations of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.JetOperations`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean): 43 declarations, 34 with a docstring.

> The evaluation, derivatives, coordinates and adjoint actions on the jets of a global gauge group.

## i. Overview

> A global gauge group `G` has gauge jets, the invertible matrices of jets with value in the
> group and Maurer–Cartan form a Lie algebra jet, and Lie algebra jets, the matrices of jets with
> every base-point derivative in the Lie algebra. This file gives the operations on them that the
> transformation laws of gauge fields and matter fields are built from, as definitions on `G`.
> Evaluation of a Lie algebra jet at the base point `G.evalLie` and the inclusion of constants
> `G.ofConstantLie` are the entrywise constant coefficient and constant embedding. The derivative
> `G.derivJ μ` and multiplication by a coordinate `G.mulCoordJ μ` act entrywise, `G.iteratedDerivJ`
> is the iterated derivative, and the adjoint actions `G.adjointJ` of the gauge jets on the Lie
> algebra jets and `G.adjointRep` of the group on its Lie algebra are conjugation `U A U⁻¹`. The
> Maurer–Cartan form is `G.maurerCartan U μ = (∂_μ U) U⁻¹`. The laws these operations satisfy are
> identities of matrices of jets. They include the Maurer–Cartan cocycle law and structure
> equation `∂_μ ω_ν − ∂_ν ω_μ = [ω_μ, ω_ν]`, and the Leibniz rule
> `∂_μ (U A U⁻¹) = U (∂_μ A) U⁻¹ + [ω_μ, U A U⁻¹]` for the adjoint action. For a compact group
> inside the unitary group the hermitian generators of physics are `a = −i X`, with the bracket
> `i (a b − b a)` and the Maurer–Cartan form `i (∂_μ U) U⁻¹`.
>
> The jets of a global gauge group are determined by their Taylor data. A Lie algebra jet is
> determined by its base-point derivatives, and a gauge jet with vanishing Maurer–Cartan form
> is constant. Any Taylor data in `𝔤` are those of a Lie algebra jet, and any Lie algebra jet
> `A` vanishing at the base point is the radial component `∑_μ x_μ ω_μ` of the Maurer–Cartan
> form of the gauge jet solving `E U = −A U`, `U(0) = 1`. These facts are proved about gauge
> jets and Lie algebra jets in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.LieAlgebra.Jet` and
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.GlobalGaugeGroup.MaurerCartan`, and assembled
> here.

## ii. Key results

> - `GlobalGaugeGroup.evalLie`, `GlobalGaugeGroup.ofConstantLie`, `GlobalGaugeGroup.derivJ`,
>   `GlobalGaugeGroup.mulCoordJ`, `GlobalGaugeGroup.iteratedDerivJ`, `GlobalGaugeGroup.adjointJ`,
>   `GlobalGaugeGroup.adjointRep` : the operations on the jets.
> - `GlobalGaugeGroup.maurerCartan_cocycle`, `GlobalGaugeGroup.maurerCartan_structure`,
>   `GlobalGaugeGroup.derivJ_adjointJ` : the laws of the Maurer–Cartan form.
> - `GlobalGaugeGroup.ext_of_evalLie_iteratedDerivJ`,
>   `GlobalGaugeGroup.exists_evalLie_iteratedDerivJ_eq` : a Lie algebra jet is determined by its
>   base-point derivatives, and every Taylor datum is realised.

## iv. References

> * None.

## A. Evaluation and constants on Lie algebra jets

**`GlobalGaugeGroup.evalLie`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L88).

> Evaluation of a Lie algebra jet at the base point, the entrywise constant coefficient.

```lean
noncomputable def evalLie : G.jetLieSubalgebra →ₗ⁅ℝ⁆ G.lieSubalgebra
```

**`GlobalGaugeGroup.evalLie_val`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L98).

```lean
lemma evalLie_val (A : G.jetLieSubalgebra) :
    (G.evalLie A).1 = (constantCoeff : SpaceTimeAlgebra →+* ℂ).mapMatrix A.1
```

**`GlobalGaugeGroup.ofConstantLie`**, a def, [line 102](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L102).

> A constant Lie algebra element as a Lie algebra jet, the entrywise constant embedding.

```lean
noncomputable def ofConstantLie : G.lieSubalgebra →ₗ⁅ℝ⁆ G.jetLieSubalgebra
```

**`GlobalGaugeGroup.ofConstantLie_val`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L112).

```lean
lemma ofConstantLie_val (a : G.lieSubalgebra) :
    (G.ofConstantLie a).1 = (C : ℂ →+* SpaceTimeAlgebra).mapMatrix a.1
```

**`GlobalGaugeGroup.evalLie_ofConstantLie`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L117).

> Evaluating the constant Lie algebra jet of `a` at the base point gives back `a`.

```lean
lemma evalLie_ofConstantLie (a : G.lieSubalgebra) : G.evalLie (G.ofConstantLie a) = a
```

**`GlobalGaugeGroup.evalLie_surjective`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L122).

> Every Lie algebra element is the value of a Lie algebra jet, namely its constant jet.

```lean
lemma evalLie_surjective : Function.Surjective G.evalLie
```

## B. Derivatives and coordinates

**`GlobalGaugeGroup.derivJ`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L133).

> The formal derivative `∂_μ` of a Lie algebra jet in the spacetime direction `μ`, taken
> entrywise.

```lean
noncomputable def derivJ (μ : Fin 1 ⊕ Fin 3) :
    G.jetLieSubalgebra →ₗ[ℝ] G.jetLieSubalgebra
```

**`GlobalGaugeGroup.derivJ_val`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L140).

```lean
lemma derivJ_val (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    (G.derivJ μ A).1 = A.1.map (pderiv μ)
```

**`GlobalGaugeGroup.derivJ_comm`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L144).

> The formal derivatives commute.

```lean
lemma derivJ_comm (μ ν : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    G.derivJ μ (G.derivJ ν A) = G.derivJ ν (G.derivJ μ A)
```

**`GlobalGaugeGroup.derivJ_bracket`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L149).

> The Leibniz rule for the bracket of Lie algebra jets.

```lean
lemma derivJ_bracket (μ : Fin 1 ⊕ Fin 3) (A B : G.jetLieSubalgebra) :
    G.derivJ μ ⁅A, B⁆ = ⁅G.derivJ μ A, B⁆ + ⁅A, G.derivJ μ B⁆
```

**`GlobalGaugeGroup.derivJ_ofConstantLie`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L160).

> A constant Lie algebra jet has vanishing derivative.

```lean
lemma derivJ_ofConstantLie (μ : Fin 1 ⊕ Fin 3) (a : G.lieSubalgebra) :
    G.derivJ μ (G.ofConstantLie a) = 0
```

**`GlobalGaugeGroup.mulCoordJ`**, a def, [line 165](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L165).

> Multiplication of a Lie algebra jet by the spacetime coordinate `x_μ`.

```lean
noncomputable def mulCoordJ (μ : Fin 1 ⊕ Fin 3) :
    G.jetLieSubalgebra →ₗ[ℝ] G.jetLieSubalgebra
```

**`GlobalGaugeGroup.mulCoordJ_val`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L172).

```lean
lemma mulCoordJ_val (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    (G.mulCoordJ μ A).1 = (X μ : SpaceTimeAlgebra) • A.1
```

**`GlobalGaugeGroup.derivJ_mulCoordJ`**, a lemma, [line 176](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L176).

> The Leibniz rule for a coordinate, `∂_μ (x_ν A) = x_ν ∂_μ A + δ_{μν} A`.

```lean
lemma derivJ_mulCoordJ (μ ν : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    G.derivJ μ (G.mulCoordJ ν A) = G.mulCoordJ ν (G.derivJ μ A) + if μ = ν then A else 0
```

**`GlobalGaugeGroup.evalLie_mulCoordJ`**, a lemma, [line 192](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L192).

> A multiple of a coordinate vanishes at the base point.

```lean
lemma evalLie_mulCoordJ (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    G.evalLie (G.mulCoordJ μ A) = 0
```

### B.1. The iterated derivative

**`GlobalGaugeGroup.instRightCommutativeCompDerivJ`**, an instance, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L204).

> Post-composition with `derivJ` is right-commutative.

```lean
instance instRightCommutativeCompDerivJ : RightCommutative
    (fun (D : G.jetLieSubalgebra →ₗ[ℝ] G.jetLieSubalgebra) (μ : Fin 1 ⊕ Fin 3) =>
      D.comp (G.derivJ μ))
```

**`GlobalGaugeGroup.iteratedDerivJ`**, a def, [line 211](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L211).

> The iterated formal derivative on the Lie algebra jets, the product of `derivJ` over a
> multiset of directions.

```lean
noncomputable def iteratedDerivJ (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    G.jetLieSubalgebra →ₗ[ℝ] G.jetLieSubalgebra
```

**`GlobalGaugeGroup.iteratedDerivJ_zero`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L216).

```lean
lemma iteratedDerivJ_zero :
    G.iteratedDerivJ (0 : Multiset (Fin 1 ⊕ Fin 3)) = LinearMap.id
```

**`GlobalGaugeGroup.iteratedDerivJ_cons`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L220).

```lean
lemma iteratedDerivJ_cons (μ : Fin 1 ⊕ Fin 3) (μs : Multiset (Fin 1 ⊕ Fin 3)) :
    G.iteratedDerivJ (μ ::ₘ μs) = (G.derivJ μ).comp (G.iteratedDerivJ μs)
```

**`GlobalGaugeGroup.iteratedDerivJ_add`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L235).

> The iterated derivative is additive in the multiset.

```lean
lemma iteratedDerivJ_add (s t : Multiset (Fin 1 ⊕ Fin 3)) :
    G.iteratedDerivJ (s + t) = (G.iteratedDerivJ s).comp (G.iteratedDerivJ t)
```

**`GlobalGaugeGroup.iteratedDerivJ_singleton`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L243).

```lean
lemma iteratedDerivJ_singleton (μ : Fin 1 ⊕ Fin 3) :
    G.iteratedDerivJ ({μ} : Multiset (Fin 1 ⊕ Fin 3)) = G.derivJ μ
```

**`GlobalGaugeGroup.iteratedDerivJ_cons_eq_comp_derivJ`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L249).

> The first derivative in a multiset may be taken first rather than last.

```lean
lemma iteratedDerivJ_cons_eq_comp_derivJ (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3)) :
    G.iteratedDerivJ (μ ::ₘ s) = (G.iteratedDerivJ s).comp (G.derivJ μ)
```

**`GlobalGaugeGroup.iteratedDerivJ_bracket`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L256).

> The iterated Leibniz rule for the bracket.

```lean
lemma iteratedDerivJ_bracket (s : Multiset (Fin 1 ⊕ Fin 3)) (a b : G.jetLieSubalgebra) :
    G.iteratedDerivJ s ⁅a, b⁆ =
      (s.antidiagonal.map fun p => ⁅G.iteratedDerivJ p.1 a, G.iteratedDerivJ p.2 b⁆).sum
```

**`GlobalGaugeGroup.iteratedDerivJ_val`**, a lemma, [line 275](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L275).

> The iterated derivative is the entrywise iterated formal derivative.

```lean
lemma iteratedDerivJ_val (s : Multiset (Fin 1 ⊕ Fin 3)) (A : G.jetLieSubalgebra) :
    (G.iteratedDerivJ s A).1 = A.1.map fun f => iteratedPDeriv s f
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_val`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L290).

> The base-point value of the iterated derivative of a Lie algebra jet is its base-point
> derivative.

```lean
lemma evalLie_iteratedDerivJ_val (s : Multiset (Fin 1 ⊕ Fin 3)) (A : G.jetLieSubalgebra) :
    (G.evalLie (G.iteratedDerivJ s A)).1 = derivValueMatrix s A.1
```

**`GlobalGaugeGroup.iteratedDerivJ_ofConstantLie_of_ne_zero`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L296).

> Every iterated derivative of a constant Lie algebra jet vanishes.

```lean
lemma iteratedDerivJ_ofConstantLie_of_ne_zero {p : Multiset (Fin 1 ⊕ Fin 3)} (hp : p ≠ 0)
    (a : G.lieSubalgebra) : G.iteratedDerivJ p (G.ofConstantLie a) = 0
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_mulCoordJ`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L307).

> The base-point value of an iterated derivative of a multiple of a coordinate.

```lean
lemma evalLie_iteratedDerivJ_mulCoordJ (μ : Fin 1 ⊕ Fin 3) (s : Multiset (Fin 1 ⊕ Fin 3))
    (a : G.jetLieSubalgebra) :
    G.evalLie (G.iteratedDerivJ s (G.mulCoordJ μ a)) =
      s.count μ • G.evalLie (G.iteratedDerivJ (s.erase μ) a)
```

## C. The adjoint actions

**`GlobalGaugeGroup.adjointJ`**, a def, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L328).

> The adjoint action `A ↦ U A U⁻¹` of the gauge jets on the Lie algebra jets.

```lean
noncomputable def adjointJ : Representation ℝ G.gaugeJetGroup G.jetLieSubalgebra
```

**`GlobalGaugeGroup.adjointJ_val`**, a lemma, [line 338](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L338).

```lean
lemma adjointJ_val (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    (G.adjointJ U A).1 = U.1.1 * A.1 * (U.1⁻¹).1
```

**`GlobalGaugeGroup.adjointRep`**, a def, [line 342](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L342).

> The adjoint action `a ↦ g a g⁻¹` of the group on its Lie algebra.

```lean
noncomputable def adjointRep : Representation ℝ G.group G.lieSubalgebra
```

**`GlobalGaugeGroup.adjointRep_val`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L353).

```lean
lemma adjointRep_val (g : G.group) (a : G.lieSubalgebra) :
    (G.adjointRep g a).1 = g.1.1 * a.1 * (g.1⁻¹).1
```

**`GlobalGaugeGroup.adjointJ_bracket`**, a lemma, [line 357](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L357).

> The adjoint action of a gauge jet is by Lie algebra automorphisms.

```lean
lemma adjointJ_bracket (U : G.gaugeJetGroup) (A B : G.jetLieSubalgebra) :
    G.adjointJ U ⁅A, B⁆ = ⁅G.adjointJ U A, G.adjointJ U B⁆
```

**`GlobalGaugeGroup.evalLie_adjointJ`**, a lemma, [line 370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L370).

> At the base point the adjoint action of a gauge jet is the adjoint action of its value.

```lean
lemma evalLie_adjointJ (U : G.gaugeJetGroup) (A : G.jetLieSubalgebra) :
    G.evalLie (G.adjointJ U A) = G.adjointRep (G.evalGaugeJet U) (G.evalLie A)
```

**`GlobalGaugeGroup.evalLie_adjointJ_ofConstantLie`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L381).

> At the base point, the adjoint action of a gauge jet on a constant is the adjoint action of
> its value.

```lean
lemma evalLie_adjointJ_ofConstantLie (U : G.gaugeJetGroup) (a : G.lieSubalgebra) :
    G.evalLie (G.adjointJ U (G.ofConstantLie a)) = G.adjointRep (G.evalGaugeJet U) a
```

## D. The Maurer–Cartan form

**`GlobalGaugeGroup.maurerCartan_cocycle`**, a lemma, [line 393](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L393).

> The Maurer–Cartan form is a cocycle for the adjoint action,
> `ω_μ(U V) = ω_μ(U) + U ω_μ(V) U⁻¹`.

```lean
lemma maurerCartan_cocycle (U V : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    G.maurerCartan (U * V) μ = G.maurerCartan U μ + G.adjointJ U (G.maurerCartan V μ)
```

**`GlobalGaugeGroup.maurerCartan_structure`**, a lemma, [line 399](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L399).

> The Maurer–Cartan structure equation `∂_μ ω_ν − ∂_ν ω_μ = [ω_μ, ω_ν]` in the Lie algebra
> jets.

```lean
lemma maurerCartan_structure (U : G.gaugeJetGroup) (μ ν : Fin 1 ⊕ Fin 3) :
    G.derivJ μ (G.maurerCartan U ν) - G.derivJ ν (G.maurerCartan U μ) =
      ⁅G.maurerCartan U μ, G.maurerCartan U ν⁆
```

**`GlobalGaugeGroup.derivJ_adjointJ`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L406).

> The Leibniz rule for the adjoint action,
> `∂_μ (U A U⁻¹) = U (∂_μ A) U⁻¹ + [ω_μ, U A U⁻¹]`.

```lean
lemma derivJ_adjointJ (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) (A : G.jetLieSubalgebra) :
    G.derivJ μ (G.adjointJ U A) =
      G.adjointJ U (G.derivJ μ A) + ⁅G.maurerCartan U μ, G.adjointJ U A⁆
```

### D.1. First consequences of the laws

**`GlobalGaugeGroup.maurerCartan_inv_adjointJ`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L431).

> The Maurer–Cartan form of an inverse, `ω_μ(U⁻¹) = − Ad_{U⁻¹} ω_μ(U)`, the cocycle law
> applied to `U⁻¹ U = 1`.

```lean
lemma maurerCartan_inv_adjointJ (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    G.maurerCartan U⁻¹ μ = -G.adjointJ U⁻¹ (G.maurerCartan U μ)
```

**`GlobalGaugeGroup.derivJ_adjointJ_ofConstantLie`**, a lemma, [line 439](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L439).

> One derivative of the adjoint action on a constant is the bracket with the Maurer–Cartan
> form, the Leibniz rule `derivJ_adjointJ` with the constant's derivative killed.

```lean
lemma derivJ_adjointJ_ofConstantLie (U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3)
    (a : G.lieSubalgebra) :
    G.derivJ μ (G.adjointJ U (G.ofConstantLie a)) =
      ⁅G.maurerCartan U μ, G.adjointJ U (G.ofConstantLie a)⁆
```

**`GlobalGaugeGroup.maurerCartan_conj`**, a lemma, [line 447](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L447).

> The Maurer–Cartan form of a conjugate, by the cocycle law, the conjugating jet
> contributes its own form and its transport by the conjugate.

```lean
lemma maurerCartan_conj (g U : G.gaugeJetGroup) (μ : Fin 1 ⊕ Fin 3) :
    G.maurerCartan (g * U * g⁻¹) μ =
      G.maurerCartan g μ + G.adjointJ g (G.maurerCartan U μ)
        - G.adjointJ (g * U * g⁻¹) (G.maurerCartan g μ)
```

**`GlobalGaugeGroup.evalLie_iteratedDerivJ_bracket_congr`**, a lemma, [line 460](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L460).

> The base-point Taylor data of a bracket is determined by that of its arguments.
> If the base-point values of the iterated derivatives of `a` and `b` along sub-multisets
> of `w` agree with those of `a'` and `b'`, then so do those of the brackets, the iterated
> Leibniz rule expands the bracket over the antidiagonal of `w`, whose parts are all
> sub-multisets of `w`.

```lean
lemma evalLie_iteratedDerivJ_bracket_congr (w : Multiset (Fin 1 ⊕ Fin 3))
    (a b a' b' : G.jetLieSubalgebra)
    (ha : ∀ p ≤ w, G.evalLie (G.iteratedDerivJ p a) = G.evalLie (G.iteratedDerivJ p a'))
    (hb : ∀ p ≤ w, G.evalLie (G.iteratedDerivJ p b) = G.evalLie (G.iteratedDerivJ p b')) :
    G.evalLie (G.iteratedDerivJ w ⁅a, b⁆) = G.evalLie (G.iteratedDerivJ w ⁅a', b'⁆)
```

## E. Determination by Taylor data

> A Lie algebra jet is determined by its base-point derivatives, a gauge jet with vanishing
> Maurer–Cartan form is constant
> (`GlobalGaugeGroup.eq_gaugeJetOfConstant_of_maurerCartan_eq_zero`), every family of Taylor data
> in the Lie algebra is that of a Lie algebra jet, and every Lie algebra jet vanishing at the base
> point is the radial component of the Maurer–Cartan form of a gauge jet with value one
> (`GlobalGaugeGroup.exists_sum_X_smul_maurerCartan_eq`).

**`GlobalGaugeGroup.ext_of_evalLie_iteratedDerivJ`**, a lemma, [line 486](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L486).

> A Lie algebra jet is determined by the base-point values of its iterated derivatives.

```lean
lemma ext_of_evalLie_iteratedDerivJ {A B : G.jetLieSubalgebra}
    (h : ∀ s, G.evalLie (G.iteratedDerivJ s A) = G.evalLie (G.iteratedDerivJ s B)) : A = B
```

**`GlobalGaugeGroup.exists_evalLie_iteratedDerivJ_eq`**, a lemma, [line 493](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean#L493).

> Every family of Taylor data in the Lie algebra is the family of base-point values of the
> iterated derivatives of a Lie algebra jet.

```lean
lemma exists_evalLie_iteratedDerivJ_eq (c : Multiset (Fin 1 ⊕ Fin 3) → G.lieSubalgebra) :
    ∃ A : G.jetLieSubalgebra, ∀ s, G.evalLie (G.iteratedDerivJ s A) = c s
```

## Depends on

- [The Maurer–Cartan form on the jet gauge group](globalgaugegroup-maurercartan.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/GlobalGaugeGroup/JetOperations.lean)
