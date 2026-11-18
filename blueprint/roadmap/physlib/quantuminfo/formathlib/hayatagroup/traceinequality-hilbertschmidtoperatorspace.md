---
declaration: module
origin: cited
lean: HilbertSchmidtOperatorSpace.HSIndex, HilbertSchmidtOperatorSpace.hsOrthonormalBasis, HilbertSchmidtOperatorSpace.HSCoords, HilbertSchmidtOperatorSpace.HSCoordFun, HilbertSchmidtOperatorSpace.HSOp, HilbertSchmidtOperatorSpace.hsCoordsLinearEquiv, HilbertSchmidtOperatorSpace.matrixToFun, HilbertSchmidtOperatorSpace.matrixToCoords
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.HilbertSchmidtOperatorSpace

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.HilbertSchmidtOperatorSpace`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean): 55 declarations (14 instances with no name), 15 with a docstring; 6 private, not shown.

**`HilbertSchmidtOperatorSpace.HSIndex`**, an abbrev, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L28).

> The canonical finite index used for Hilbert-Schmidt coordinates.

```lean
abbrev HSIndex (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ]
    [FiniteDimensional ℂ ℋ]
```

**`HilbertSchmidtOperatorSpace.hsOrthonormalBasis`**, an abbrev, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L33).

> The standard orthonormal basis on a finite-dimensional Hilbert space.

```lean
noncomputable abbrev hsOrthonormalBasis :
    OrthonormalBasis (HSIndex ℋ) ℂ ℋ
```

**`HilbertSchmidtOperatorSpace.HSCoords`**, an abbrev, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L38).

> Coordinate space for Hilbert-Schmidt operators.

```lean
abbrev HSCoords (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ]
    [FiniteDimensional ℂ ℋ]
```

**`HilbertSchmidtOperatorSpace.HSCoordFun`**, an abbrev, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L43).

> The underlying coordinate function space for Hilbert-Schmidt operators.

```lean
abbrev HSCoordFun (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ]
    [FiniteDimensional ℂ ℋ]
```

**`HilbertSchmidtOperatorSpace.HSOp`**, a def, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L48).

> The operator space `L ℋ`, viewed later with the Hilbert-Schmidt structure.

```lean
def HSOp (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ] : Type u
```

**An instance with no name**, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L51).

```lean
instance : AddCommGroup (HSOp ℋ)
```

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L56).

```lean
instance : Module ℂ (HSOp ℋ)
```

**An instance with no name**, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L60).

```lean
instance : Star (HSOp ℋ)
```

**An instance with no name**, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L64).

```lean
instance : Mul (HSOp ℋ)
```

**An instance with no name**, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L68).

```lean
instance : One (HSOp ℋ)
```

**An instance with no name**, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L72).

```lean
instance : Inhabited (HSOp ℋ)
```

**An instance with no name**, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L76).

```lean
instance : Zero (HSOp ℋ)
```

**An instance with no name**, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L81).

```lean
instance : FiniteDimensional ℂ (HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.hsCoordsLinearEquiv`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L85).

```lean
noncomputable def hsCoordsLinearEquiv :
    HSCoords ℋ ≃ₗ[ℂ] (HSCoordFun ℋ)
```

**`HilbertSchmidtOperatorSpace.matrixToFun`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L90).

```lean
def matrixToFun :
    Matrix (HSIndex ℋ) (HSIndex ℋ) ℂ ≃ₗ[ℂ] HSCoordFun ℋ
```

**`HilbertSchmidtOperatorSpace.matrixToCoords`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L107).

```lean
noncomputable def matrixToCoords :
    Matrix (HSIndex ℋ) (HSIndex ℋ) ℂ ≃ₗ[ℂ] HSCoords ℋ
```

**`HilbertSchmidtOperatorSpace.hsLinearMapEquiv`**, a def, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L112).

> Forget continuity and identify continuous linear operators with linear endomorphisms.

```lean
noncomputable def hsLinearMapEquiv :
    HSOp ℋ ≃ₗ[ℂ] (ℋ →ₗ[ℂ] ℋ)
```

**`HilbertSchmidtOperatorSpace.toHSCoordsLinearEquiv`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L117).

> Hilbert-Schmidt coordinates on `L ℋ`.

```lean
noncomputable def toHSCoordsLinearEquiv :
    HSOp ℋ ≃ₗ[ℂ] HSCoords ℋ
```

**`HilbertSchmidtOperatorSpace.toHSCoordsLinearEquiv_apply_apply`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L125).

```lean
lemma toHSCoordsLinearEquiv_apply_apply
    (T : HSOp ℋ) (i j : HSIndex ℋ) :
    toHSCoordsLinearEquiv (ℋ := ℋ) T (i, j) =
      LinearMap.toMatrix (hsOrthonormalBasis (ℋ := ℋ)).toBasis
        (hsOrthonormalBasis (ℋ := ℋ)).toBasis
        ((hsLinearMapEquiv (ℋ := ℋ)) T) i j
```

**An instance with no name**, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L145).

```lean
instance : NormedAddCommGroup (HSOp ℋ)
```

**An instance with no name**, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L149).

```lean
instance : NormedSpace ℂ (HSOp ℋ)
```

**An instance with no name**, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L152).

```lean
instance : Inner ℂ (HSOp ℋ)
```

**An instance with no name**, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L155).

```lean
instance : InnerProductSpace ℂ (HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.toHSCoordsLinearIsometryEquiv`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L184).

> Hilbert-Schmidt coordinates as a linear isometry.

```lean
noncomputable def toHSCoordsLinearIsometryEquiv :
    HSOp ℋ ≃ₗᵢ[ℂ] HSCoords ℋ
```

**An instance with no name**, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L193).

```lean
instance : CompleteSpace (HSOp ℋ)
```

**An instance with no name**, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L201).

```lean
instance : ContinuousSMul ℂ (HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.ofOp`**, an abbrev, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L206).

> Reinterpret an operator as an element of the Hilbert-Schmidt operator space.

```lean
abbrev ofOp (T : L ℋ) : HSOp ℋ
```

**`HilbertSchmidtOperatorSpace.toOp`**, an abbrev, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L209).

> Forget the Hilbert-Schmidt structure and recover the underlying operator.

```lean
abbrev toOp (T : HSOp ℋ) : L ℋ
```

**`HilbertSchmidtOperatorSpace.leftMulHS`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L212).

> Left multiplication on the Hilbert-Schmidt operator space.

```lean
noncomputable def leftMulHS (A : L ℋ) : HSOp ℋ →L[ℂ] HSOp ℋ
```

**`HilbertSchmidtOperatorSpace.rightMulHS`**, a def, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L219).

> Right multiplication on the Hilbert-Schmidt operator space.

```lean
noncomputable def rightMulHS (B : L ℋ) : HSOp ℋ →L[ℂ] HSOp ℋ
```

**`HilbertSchmidtOperatorSpace.leftMulHS_apply`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L226).

```lean
lemma leftMulHS_apply (A : L ℋ) (T : HSOp ℋ) :
    toOp (leftMulHS (ℋ := ℋ) A T) = A * toOp T
```

**`HilbertSchmidtOperatorSpace.rightMulHS_apply`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L230).

```lean
lemma rightMulHS_apply (B : L ℋ) (T : HSOp ℋ) :
    toOp (rightMulHS (ℋ := ℋ) B T) = toOp T * B
```

**`HilbertSchmidtOperatorSpace.leftMulHS_mul`**, a lemma, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L235).

```lean
lemma leftMulHS_mul (A B : L ℋ) :
    leftMulHS (ℋ := ℋ) (A * B) = leftMulHS (ℋ := ℋ) A * leftMulHS (ℋ := ℋ) B
```

**`HilbertSchmidtOperatorSpace.rightMulHS_mul`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L242).

```lean
lemma rightMulHS_mul (A B : L ℋ) :
    rightMulHS (ℋ := ℋ) (A * B) = rightMulHS (ℋ := ℋ) B * rightMulHS (ℋ := ℋ) A
```

**`HilbertSchmidtOperatorSpace.leftMulHS_one`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L248).

```lean
lemma leftMulHS_one :
    leftMulHS (ℋ := ℋ) (1 : L ℋ) = (1 : L (HSOp ℋ))
```

**`HilbertSchmidtOperatorSpace.rightMulHS_one`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L254).

```lean
lemma rightMulHS_one :
    rightMulHS (ℋ := ℋ) (1 : L ℋ) = (1 : L (HSOp ℋ))
```

**`HilbertSchmidtOperatorSpace.leftMulHS_rightMulHS_commute`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L261).

```lean
lemma leftMulHS_rightMulHS_commute (A B : L ℋ) :
    Commute (leftMulHS (ℋ := ℋ) A) (rightMulHS (ℋ := ℋ) B)
```

**`HilbertSchmidtOperatorSpace.hsInner_eq_trace`**, a lemma, [line 340](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L340).

```lean
lemma hsInner_eq_trace (X Y : L ℋ) :
    inner ℂ (ofOp X) (ofOp Y) = LinearMap.trace ℂ ℋ ((star X * Y).toLinearMap)
```

**`HilbertSchmidtOperatorSpace.re_hsInner_eq_traceRe`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L355).

```lean
lemma re_hsInner_eq_traceRe (X Y : L ℋ) :
    Complex.re (inner ℂ (ofOp X) (ofOp Y)) =
      Complex.re (LinearMap.trace ℂ ℋ ((star X * Y).toLinearMap))
```

**`HilbertSchmidtOperatorSpace.leftMulHS_star`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L360).

```lean
lemma leftMulHS_star (A : L ℋ) :
    star (leftMulHS (ℋ := ℋ) A) = leftMulHS (ℋ := ℋ) (star A)
```

**`HilbertSchmidtOperatorSpace.leftMulHS_real_smul_one`**, a lemma, [line 373](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L373).

```lean
lemma leftMulHS_real_smul_one (r : ℝ) :
    leftMulHS (ℋ := ℋ) (r • (1 : L ℋ)) = r • (1 : L (HSOp ℋ))
```

**`HilbertSchmidtOperatorSpace.rightMulHS_real_smul_one`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L380).

```lean
lemma rightMulHS_real_smul_one (r : ℝ) :
    rightMulHS (ℋ := ℋ) (r • (1 : L ℋ)) = r • (1 : L (HSOp ℋ))
```

**`HilbertSchmidtOperatorSpace.leftMulHS_nonneg`**, a lemma, [line 386](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L386).

```lean
lemma leftMulHS_nonneg {A : L ℋ} (hA0 : 0 ≤ A) :
    0 ≤ leftMulHS (ℋ := ℋ) A
```

**`HilbertSchmidtOperatorSpace.leftMulHS_le_leftMulHS`**, a lemma, [line 431](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L431).

```lean
lemma leftMulHS_le_leftMulHS {A B : L ℋ} (hAB : A ≤ B) :
    leftMulHS (ℋ := ℋ) A ≤ leftMulHS (ℋ := ℋ) B
```

**`HilbertSchmidtOperatorSpace.leftMulHS_pdSet`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L441).

```lean
lemma leftMulHS_pdSet [ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint] [Nontrivial (L ℋ)]
    {A : L ℋ} (hA : A ∈ GeneralizedPerspectiveFunction.pdSet (ℋ := ℋ)) :
    leftMulHS (ℋ := ℋ) A ∈ GeneralizedPerspectiveFunction.pdSet (ℋ := HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.rightMulHS_star`**, a lemma, [line 462](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L462).

```lean
lemma rightMulHS_star (A : L ℋ) :
    star (rightMulHS (ℋ := ℋ) A) = rightMulHS (ℋ := ℋ) (star A)
```

**`HilbertSchmidtOperatorSpace.leftMulHSStarAlgHom`**, a def, [line 479](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L479).

> Left multiplication as a real `⋆`-algebra homomorphism on the Hilbert-Schmidt operator space.

```lean
noncomputable def leftMulHSStarAlgHom : L ℋ →⋆ₐ[ℝ] L (HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.rightMulHSStarAlgHom`**, a def, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L494).

> Right multiplication as a real `⋆`-algebra homomorphism out of the opposite algebra.

```lean
noncomputable def rightMulHSStarAlgHom : (L ℋ)ᵐᵒᵖ →⋆ₐ[ℝ] L (HSOp ℋ)
```

**`HilbertSchmidtOperatorSpace.rightMulHSStarAlgHom_apply`**, a lemma, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L516).

```lean
lemma rightMulHSStarAlgHom_apply (A : (L ℋ)ᵐᵒᵖ) :
    rightMulHSStarAlgHom (ℋ := ℋ) A = rightMulHS (ℋ := ℋ) (MulOpposite.unop A)
```

**`HilbertSchmidtOperatorSpace.opStarHSStarAlgHom`**, a def, [line 521](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L521).

> The `⋆`-algebra hom sending `A` to `op (star A)`. On selfadjoint operators this is just `op`.

```lean
noncomputable def opStarHSStarAlgHom : L ℋ →⋆ₐ[ℝ] (L ℋ)ᵐᵒᵖ
```

**`HilbertSchmidtOperatorSpace.op_isSelfAdjoint`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L551).

```lean
lemma op_isSelfAdjoint (A : L ℋ) (hA : IsSelfAdjoint A) :
    IsSelfAdjoint (MulOpposite.op A : (L ℋ)ᵐᵒᵖ)
```

**`HilbertSchmidtOperatorSpace.spectrum_op_eq`**, a lemma, [line 592](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L592).

```lean
lemma spectrum_op_eq [ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint] [Nontrivial (L ℋ)]
    (A : L ℋ) (hA : IsSelfAdjoint A) :
    spectrum ℝ (MulOpposite.op A : (L ℋ)ᵐᵒᵖ) = spectrum ℝ A
```

**`HilbertSchmidtOperatorSpace.cfc_op_eq_op_cfc`**, a lemma, [line 599](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L599).

```lean
lemma cfc_op_eq_op_cfc [ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint]
    [ContinuousFunctionalCalculus ℝ ((L ℋ)ᵐᵒᵖ) IsSelfAdjoint] [Nontrivial (L ℋ)]
    (f : ℝ → ℝ) (A : L ℋ) (hA : IsSelfAdjoint A)
    (hf : ContinuousOn f (spectrum ℝ A)) :
    cfc (R := ℝ) (A := (L ℋ)ᵐᵒᵖ) (p := IsSelfAdjoint) f (MulOpposite.op A) =
      MulOpposite.op (cfcR f A)
```

**`HilbertSchmidtOperatorSpace.leftMulHS_cfcR`**, a lemma, [line 623](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L623).

```lean
lemma leftMulHS_cfcR [ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint] [Nontrivial (L ℋ)]
    (f : ℝ → ℝ) (A : L ℋ) (hA : IsSelfAdjoint A)
    (hf : ContinuousOn f (spectrum ℝ A)) :
    leftMulHS (ℋ := ℋ) (cfcR f A) =
      cfcR (ℋ := HSOp ℋ) f (leftMulHS (ℋ := ℋ) A)
```

**`HilbertSchmidtOperatorSpace.rightMulHS_cfcR`**, a lemma, [line 637](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean#L637).

```lean
lemma rightMulHS_cfcR [ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint]
    [ContinuousFunctionalCalculus ℝ ((L ℋ)ᵐᵒᵖ) IsSelfAdjoint] [Nontrivial (L ℋ)]
    (f : ℝ → ℝ) (A : L ℋ) (hA : IsSelfAdjoint A)
    (hf : ContinuousOn f (spectrum ℝ A)) :
    rightMulHS (ℋ := ℋ) (cfcR f A) =
      cfcR (ℋ := HSOp ℋ) f (rightMulHS (ℋ := ℋ) A)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.GeneralizedPerspectiveFunction](traceinequality-generalizedperspectivefunction.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/HilbertSchmidtOperatorSpace.lean)
