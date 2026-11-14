---
declaration: module
origin: cited
lean: ProbabilisticTheory.Stinespring.T, ProbabilisticTheory.Stinespring.baseFunctional, ProbabilisticTheory.Stinespring.baseFunctional_tmul, ProbabilisticTheory.Stinespring.sesquiBilinear, ProbabilisticTheory.Stinespring.tensorInner, ProbabilisticTheory.Stinespring.tensorInner_tmul, ProbabilisticTheory.Stinespring.tensorInner_conj_symm_tmul, ProbabilisticTheory.Stinespring.tensorInner_conj_symm
statement: formalized
proof: formalized
---

# Stinespring's dilation theorem

The module `PhyslibAlpha.ProbabilisticTheory.CStarAlgebra.Stinespring.Dilation`, [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean): 62 declarations (7 instances with no name), 22 with a docstring.

> Stinespring's theorem: every completely positive map has the form J a = V⋆ π(a) V.

## i. Overview

> Every completely positive map `J` from a C⋆-algebra `A` into the bounded operators on `H` has the
> form `J a = V⋆ π(a) V` for a representation `π` of `A` on a Hilbert space `K` and an operator `V : H
> → K`. The space `K` is the completion of `A ⊗ H` for the inner product `⟪a ⊗ h, b ⊗ k⟫ = ⟪h, J(a⋆ b)
> k⟫`, which is positive because `J` is completely positive, and `π` is left multiplication. For
> commutative `A` this contains Naimark's dilation of a POVM.

## ii. Key results

> - `Stinespring.Canonical.K` : the dilation space.
> - `Stinespring.Canonical.canonicalRepresentation`, `Stinespring.Canonical.embedding` : the
>   representation `π` and the operator `V`.
> - `Stinespring.Canonical.canonical_stinespring_identity` : `J a = V⋆ π(a) V`.
> - `Stinespring.exists_stinespringWitness` : **Stinespring's theorem.**

## iv. References

> * None.

**`ProbabilisticTheory.Stinespring.T`**, an abbrev, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L61).

> The tensor-product carrier `A ⊗[ℂ] H` the whole construction below lives on.

```lean
abbrev T (A H : Type*) [CStarAlgebra A] [PartialOrder A] [StarOrderedRing A]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
```

**`ProbabilisticTheory.Stinespring.baseFunctional`**, a def, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L65).

> The functional `b ⊗ k ↦ ⟪h, J(a⋆b) k⟫`, the building block of the kernel inner product.

```lean
def baseFunctional (J : A →CP (H →L[ℂ] H)) (a : A) (h : H) :
    T A H →ₗ[ℂ] ℂ
```

**`ProbabilisticTheory.Stinespring.baseFunctional_tmul`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L84).

```lean
lemma baseFunctional_tmul (J : A →CP (H →L[ℂ] H)) (a b : A) (h k : H) :
    baseFunctional J a h (b ⊗ₜ[ℂ] k) = inner ℂ h (J (star a * b) k)
```

**`ProbabilisticTheory.Stinespring.sesquiBilinear`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L89).

> `baseFunctional`, packaged as a sesquilinear map in `(a, h)`.

```lean
def sesquiBilinear (J : A →CP (H →L[ℂ] H)) :
    A →ₛₗ[starRingEnd ℂ] H →ₛₗ[starRingEnd ℂ] (T A H →ₗ[ℂ] ℂ)
```

**`ProbabilisticTheory.Stinespring.tensorInner`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L100).

> The (possibly degenerate) sesquilinear form on `T A H` induced by lifting `sesquiBilinear`
> through the tensor product.

```lean
def tensorInner (J : A →CP (H →L[ℂ] H)) :
    T A H →ₛₗ[starRingEnd ℂ] (T A H →ₗ[ℂ] ℂ)
```

**`ProbabilisticTheory.Stinespring.tensorInner_tmul`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L105).

```lean
lemma tensorInner_tmul (J : A →CP (H →L[ℂ] H)) (a b : A) (h k : H) :
    tensorInner J (a ⊗ₜ[ℂ] h) (b ⊗ₜ[ℂ] k) =
      inner ℂ h (J (star a * b) k)
```

**`ProbabilisticTheory.Stinespring.tensorInner_conj_symm_tmul`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L110).

```lean
lemma tensorInner_conj_symm_tmul (J : A →CP (H →L[ℂ] H)) (a b : A) (h k : H) :
    starRingEnd ℂ (tensorInner J (a ⊗ₜ[ℂ] h) (b ⊗ₜ[ℂ] k)) =
      tensorInner J (b ⊗ₜ[ℂ] k) (a ⊗ₜ[ℂ] h)
```

**`ProbabilisticTheory.Stinespring.tensorInner_conj_symm`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L127).

```lean
lemma tensorInner_conj_symm (J : A →CP (H →L[ℂ] H)) (x y : T A H) :
    starRingEnd ℂ (tensorInner J x y) = tensorInner J y x
```

**`ProbabilisticTheory.Stinespring.tensorInner_nonneg`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L143).

```lean
lemma tensorInner_nonneg (J : A →CP (H →L[ℂ] H)) (x : T A H) :
    0 ≤ tensorInner J x x
```

**`ProbabilisticTheory.Stinespring.tensorCore`**, a def, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L155).

> `tensorInner`, packaged as a `PreInnerProductSpace.Core` on `T A H`.

```lean
def tensorCore (J : A →CP (H →L[ℂ] H)) :
    PreInnerProductSpace.Core ℂ (T A H)
```

**`ProbabilisticTheory.Stinespring.leftMul`**, a def, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L175).

> Left multiplication by `a` on the algebra factor of `T A H`.

```lean
def leftMul (a : A) : T A H →ₗ[ℂ] T A H
```

**`ProbabilisticTheory.Stinespring.leftMul_tmul`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L179).

```lean
lemma leftMul_tmul (a b : A) (h : H) :
    leftMul a (b ⊗ₜ[ℂ] h) = (a * b) ⊗ₜ[ℂ] h
```

**`ProbabilisticTheory.Stinespring.tensorInner_leftMul`**, a lemma, [line 183](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L183).

```lean
lemma tensorInner_leftMul (J : A →CP (H →L[ℂ] H)) (a : A) (x y : T A H) :
    tensorInner J (leftMul a x) y = tensorInner J x (leftMul (star a) y)
```

**`ProbabilisticTheory.Stinespring.leftMul_mul`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L196).

```lean
lemma leftMul_mul (a b : A) (x : T A H) :
    leftMul (a * b) x = leftMul a (leftMul b x)
```

**`ProbabilisticTheory.Stinespring.leftMul_add`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L204).

```lean
lemma leftMul_add (a b : A) (x : T A H) :
    leftMul (a + b) x = leftMul a x + leftMul b x
```

**`ProbabilisticTheory.Stinespring.leftMul_smul`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L214).

```lean
lemma leftMul_smul (r : ℂ) (a : A) (x : T A H) :
    leftMul (r • a) x = r • leftMul a x
```

**`ProbabilisticTheory.Stinespring.leftMul_one`**, a lemma, [line 224](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L224).

```lean
lemma leftMul_one (x : T A H) : leftMul (1 : A) x = x
```

**`ProbabilisticTheory.Stinespring.leftMul_norm_sub`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L231).

```lean
lemma leftMul_norm_sub (a : A) (x : T A H) :
    leftMul ((‖a‖ ^ 2 : ℝ) • (1 : A) - star a * a) x =
      (‖a‖ ^ 2 : ℂ) • x - leftMul (star a * a) x
```

**`ProbabilisticTheory.Stinespring.tensorInner_leftMul_selfadjoint`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L246).

```lean
lemma tensorInner_leftMul_selfadjoint (J : A →CP (H →L[ℂ] H)) {q : A} (hq : star q = q)
    (x : T A H) :
    tensorInner J (leftMul q x) x = tensorInner J x (leftMul q x)
```

**`ProbabilisticTheory.Stinespring.tensorInner_leftMul_nonneg`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L251).

```lean
lemma tensorInner_leftMul_nonneg (J : A →CP (H →L[ℂ] H)) {q : A} (hq : 0 ≤ q)
    (x : T A H) : 0 ≤ tensorInner J (leftMul q x) x
```

## A. The seminorm and pre-Hilbert structures induced by the kernel

**`ProbabilisticTheory.Stinespring.tensorSeminormed`**, a def, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L274).

> The seminormed-group structure `T A H` inherits from `tensorCore`'s (possibly degenerate)
> inner product.

```lean
def tensorSeminormed (J : A →CP (H →L[ℂ] H)) :
    SeminormedAddCommGroup (T A H)
```

**`ProbabilisticTheory.Stinespring.tensorInnerProductSpace`**, a def, [line 282](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L282).

> The inner product space structure on `T A H`, with respect to `tensorSeminormed`, coming
> from `tensorCore`.

```lean
def tensorInnerProductSpace (J : A →CP (H →L[ℂ] H)) :
    @InnerProductSpace ℂ (T A H) inferInstance (tensorSeminormed J)
```

**`ProbabilisticTheory.Stinespring.leftMul_norm_le`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L310).

```lean
lemma leftMul_norm_le (a : A) (J : A →CP (H →L[ℂ] H)) (x : T A H) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    ‖leftMul a x‖ ≤ ‖a‖ * ‖x‖
```

**`ProbabilisticTheory.Stinespring.uniformContinuous_add`**, a lemma, [line 371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L371).

```lean
lemma uniformContinuous_add (J : A →CP (H →L[ℂ] H)) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : PseudoMetricSpace (T A H) := SeminormedAddCommGroup.toPseudoMetricSpace
    UniformContinuous fun p : T A H × T A H => p.1 + p.2
```

**`ProbabilisticTheory.Stinespring.uniformContinuous_neg`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L388).

```lean
lemma uniformContinuous_neg (J : A →CP (H →L[ℂ] H)) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : PseudoMetricSpace (T A H) := SeminormedAddCommGroup.toPseudoMetricSpace
    UniformContinuous fun x : T A H => -x
```

**`ProbabilisticTheory.Stinespring.leftMulCLM`**, a def, [line 405](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L405).

> `leftMul a`, bundled as a continuous linear map for the kernel seminorm.

```lean
def leftMulCLM (J : A →CP (H →L[ℂ] H)) (a : A) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : InnerProductSpace ℂ (T A H) := tensorInnerProductSpace J
    T A H →L[ℂ] T A H
```

**`ProbabilisticTheory.Stinespring.leftMulCLM_apply`**, a lemma, [line 413](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L413).

```lean
lemma leftMulCLM_apply (J : A →CP (H →L[ℂ] H)) (a : A) (x : T A H) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : InnerProductSpace ℂ (T A H) := tensorInnerProductSpace J
    leftMulCLM J a x = leftMul a x
```

**`ProbabilisticTheory.Stinespring.leftMulCompletion`**, a def, [line 422](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L422).

> The continuous extension of `leftMulCLM` to the completion of `T A H`.

```lean
def leftMulCompletion (J : A →CP (H →L[ℂ] H)) (a : A) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : PseudoMetricSpace (T A H) := SeminormedAddCommGroup.toPseudoMetricSpace
    letI : InnerProductSpace ℂ (T A H) := tensorInnerProductSpace J
    letI : NormedSpace ℂ (T A H) := (tensorInnerProductSpace J).toNormedSpace
    UniformSpace.Completion (T A H) →L[ℂ] UniformSpace.Completion (T A H)
```

**`ProbabilisticTheory.Stinespring.leftMulCompletion_coe`**, a lemma, [line 440](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L440).

```lean
lemma leftMulCompletion_coe (J : A →CP (H →L[ℂ] H)) (a : A) (x : T A H) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : PseudoMetricSpace (T A H) := SeminormedAddCommGroup.toPseudoMetricSpace
    letI : InnerProductSpace ℂ (T A H) := tensorInnerProductSpace J
    leftMulCompletion J a (x : UniformSpace.Completion (T A H)) = leftMulCLM J a x
```

**`ProbabilisticTheory.Stinespring.leftMulCompletion_mul`**, a lemma, [line 458](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L458).

```lean
lemma leftMulCompletion_mul (J : A →CP (H →L[ℂ] H)) (a b : A) :
    letI : SeminormedAddCommGroup (T A H) := tensorSeminormed J
    letI : PseudoMetricSpace (T A H) := SeminormedAddCommGroup.toPseudoMetricSpace
    letI : InnerProductSpace ℂ (T A H) := tensorInnerProductSpace J
    letI : NormedSpace ℂ (T A H) := (tensorInnerProductSpace J).toNormedSpace
    leftMulCompletion J (a * b) =
      (leftMulCompletion J a).comp (leftMulCompletion J b)
```

## B. The canonical CP-dependent Hilbert space

> The CP kernel changes the norm, so its pre-Hilbert space is made a type synonym. This is the same
> pattern used by Mathlib's own scalar GNS construction (`PositiveLinearMap.PreGNS`): the synonym
> lets the tensor product retain its original module structure while carrying a CP-dependent
> seminorm and inner product.

**`ProbabilisticTheory.Stinespring.Canonical.Pre`**, a def, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L502).

> A type synonym for `T A H` carrying the CP-kernel-dependent seminorm and inner product,
> kept separate so the tensor product retains its own module structure.

```lean
def Pre (_J : A →CP (H →L[ℂ] H))
```

**An instance with no name**, [line 504](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L504).

```lean
instance (J : A →CP (H →L[ℂ] H)) : AddCommGroup (Pre J)
```

**An instance with no name**, [line 507](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L507).

```lean
instance (J : A →CP (H →L[ℂ] H)) : Module ℂ (Pre J)
```

**An instance with no name**, [line 510](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L510).

```lean
instance (J : A →CP (H →L[ℂ] H)) : SeminormedAddCommGroup (Pre J)
```

**An instance with no name**, [line 513](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L513).

```lean
instance (J : A →CP (H →L[ℂ] H)) : InnerProductSpace ℂ (Pre J)
```

**An instance with no name**, [line 516](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L516).

```lean
instance (J : A →CP (H →L[ℂ] H)) : IsUniformAddGroup (Pre J)
```

**An instance with no name**, [line 519](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L519).

```lean
instance (J : A →CP (H →L[ℂ] H)) : IsBoundedSMul ℂ (Pre J)
```

**An instance with no name**, [line 522](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L522).

```lean
instance (J : A →CP (H →L[ℂ] H)) : UniformContinuousConstSMul ℂ (Pre J)
```

**`ProbabilisticTheory.Stinespring.Canonical.K`**, an abbrev, [line 526](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L526).

> The completion of `Pre J`: the canonical Stinespring Hilbert space attached to `J`.

```lean
abbrev K (J : A →CP (H →L[ℂ] H))
```

**`ProbabilisticTheory.Stinespring.Canonical.preLeftMul`**, a def, [line 529](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L529).

> `leftMul a`, viewed as an operator on `Pre J`.

```lean
def preLeftMul (J : A →CP (H →L[ℂ] H)) (a : A) :
    Pre J →ₗ[ℂ] Pre J
```

**`ProbabilisticTheory.Stinespring.Canonical.preLeftMul_apply`**, a lemma, [line 533](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L533).

```lean
lemma preLeftMul_apply (J : A →CP (H →L[ℂ] H)) (a : A) (x : Pre J) :
    preLeftMul J a x = leftMul a x
```

**`ProbabilisticTheory.Stinespring.Canonical.preLeftMulCLM`**, a def, [line 537](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L537).

> `preLeftMul`, bundled as a continuous linear map.

```lean
def preLeftMulCLM (J : A →CP (H →L[ℂ] H)) (a : A) :
    Pre J →L[ℂ] Pre J
```

**`ProbabilisticTheory.Stinespring.Canonical.preLeftMulCLM_apply`**, a lemma, [line 542](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L542).

```lean
lemma preLeftMulCLM_apply (J : A →CP (H →L[ℂ] H)) (a : A) (x : Pre J) :
    preLeftMulCLM J a x = preLeftMul J a x
```

**`ProbabilisticTheory.Stinespring.Canonical.completion_leftMul_norm_le`**, a lemma, [line 545](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L545).

```lean
lemma completion_leftMul_norm_le (J : A →CP (H →L[ℂ] H)) (a : A) (x : K J) :
    ‖(preLeftMulCLM J a).completion x‖ ≤ ‖a‖ * ‖x‖
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK`**, a def, [line 557](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L557).

> The continuous extension of `preLeftMulCLM` to the completion `K J`.

```lean
def leftMulK (J : A →CP (H →L[ℂ] H)) (a : A) : K J →L[ℂ] K J
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_coe`**, a lemma, [line 562](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L562).

```lean
lemma leftMulK_coe (J : A →CP (H →L[ℂ] H)) (a : A) (x : Pre J) :
    leftMulK J a (x : K J) = preLeftMulCLM J a x
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_mul`**, a lemma, [line 566](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L566).

```lean
lemma leftMulK_mul (J : A →CP (H →L[ℂ] H)) (a b : A) :
    leftMulK J (a * b) = (leftMulK J a).comp (leftMulK J b)
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_one`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L579).

```lean
lemma leftMulK_one (J : A →CP (H →L[ℂ] H)) :
    leftMulK J (1 : A) = ContinuousLinearMap.id ℂ (K J)
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_add`**, a lemma, [line 593](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L593).

```lean
lemma leftMulK_add (J : A →CP (H →L[ℂ] H)) (a b : A) :
    leftMulK J (a + b) = leftMulK J a + leftMulK J b
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_smul`**, a lemma, [line 608](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L608).

```lean
lemma leftMulK_smul (J : A →CP (H →L[ℂ] H)) (r : ℂ) (a : A) :
    leftMulK J (r • a) = r • leftMulK J a
```

**`ProbabilisticTheory.Stinespring.Canonical.leftMulK_star`**, a lemma, [line 624](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L624).

```lean
lemma leftMulK_star (J : A →CP (H →L[ℂ] H)) (a : A) :
    leftMulK J (star a) = (leftMulK J a).adjoint
```

**`ProbabilisticTheory.Stinespring.Canonical.preEmbedding`**, a def, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L641).

> The canonical embedding `H → Pre J`, `h ↦ 1 ⊗ h`.

```lean
def preEmbedding (J : A →CP (H →L[ℂ] H)) : H →ₗ[ℂ] Pre J
```

**`ProbabilisticTheory.Stinespring.Canonical.preEmbedding_apply`**, a lemma, [line 645](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L645).

```lean
lemma preEmbedding_apply (J : A →CP (H →L[ℂ] H)) (h : H) :
    preEmbedding J h = (1 : A) ⊗ₜ[ℂ] h
```

**`ProbabilisticTheory.Stinespring.Canonical.preEmbedding_norm_sq`**, a lemma, [line 648](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L648).

```lean
lemma preEmbedding_norm_sq (J : A →CP (H →L[ℂ] H)) (h : H) :
    ‖preEmbedding J h‖ ^ 2 = RCLike.re (inner ℂ h (J (1 : A) h))
```

**`ProbabilisticTheory.Stinespring.Canonical.preEmbedding_norm_le`**, a lemma, [line 655](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L655).

```lean
lemma preEmbedding_norm_le (J : A →CP (H →L[ℂ] H)) (h : H) :
    ‖preEmbedding J h‖ ≤ Real.sqrt ‖J (1 : A)‖ * ‖h‖
```

**`ProbabilisticTheory.Stinespring.Canonical.preEmbeddingCLM`**, a def, [line 674](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L674).

> `preEmbedding`, bundled as a continuous linear map.

```lean
def preEmbeddingCLM (J : A →CP (H →L[ℂ] H)) : H →L[ℂ] Pre J
```

**`ProbabilisticTheory.Stinespring.Canonical.embedding`**, a def, [line 678](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L678).

> The canonical embedding `H → K J` into the completed Stinespring space.

```lean
def embedding (J : A →CP (H →L[ℂ] H)) : H →L[ℂ] K J
```

**`ProbabilisticTheory.Stinespring.Canonical.embedding_apply`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L682).

```lean
lemma embedding_apply (J : A →CP (H →L[ℂ] H)) (h : H) :
    embedding J h = (preEmbedding J h : K J)
```

**`ProbabilisticTheory.Stinespring.Canonical.canonicalRepresentation`**, a def, [line 687](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L687).

> The representation of `A` on `K J` by (extended) left multiplication.

```lean
def canonicalRepresentation (J : A →CP (H →L[ℂ] H)) :
    A →⋆ₐ[ℂ] (K J →L[ℂ] K J)
```

**`ProbabilisticTheory.Stinespring.Canonical.canonical_stinespring_identity`**, a lemma, [line 708](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L708).

> **Stinespring's dilation identity**: `J a = V⋆ π(a) V`, where `π` is `canonicalRepresentation`
> and `V` is `embedding`.

```lean
lemma canonical_stinespring_identity (J : A →CP (H →L[ℂ] H)) (a : A) :
    J a = ContinuousLinearMap.adjoint (embedding J) ∘L
      (canonicalRepresentation J a) ∘L embedding J
```

**`ProbabilisticTheory.Stinespring.Canonical.canonicalWitness`**, a def, [line 731](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L731).

> The canonical Stinespring witness assembled from `canonicalRepresentation` and
> `embedding`.

```lean
def canonicalWitness (J : A →CP (H →L[ℂ] H)) :
    StinespringWitness A H (K J) J
```

**`ProbabilisticTheory.Stinespring.exists_stinespringWitness`**, a lemma, [line 742](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean#L742).

> **Stinespring's dilation theorem.** Every completely positive map `J` into the bounded operators
> on `H` is `J a = V⋆ π(a) V` for a representation `π` on some Hilbert space `K` and an operator `V :
> H → K`.

```lean
lemma exists_stinespringWitness (J : A →CP (H →L[ℂ] H)) :
    Nonempty (StinespringWitness A H (Canonical.K J) J)
```

## Depends on

- [Completely positive maps as positive kernels](stinespring-kernel.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/CStarAlgebra/Stinespring/Dilation.lean)
