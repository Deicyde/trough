---
catalog: module
lean: CompPoly.GuruswamiSudan.GSInterpParams, CompPoly.GuruswamiSudan.yWeight, CompPoly.GuruswamiSudan.degreeLt, CompPoly.GuruswamiSudan.DistinctXCoordinates, CompPoly.GuruswamiSudan.ValidInterpolationWitness, CompPoly.GuruswamiSudan.LinearKernelContext, CompPoly.GuruswamiSudan.denseLinearKernelContext, CompPoly.GuruswamiSudan.GSInterpContext, CompPoly.GuruswamiSudan.FieldRootContext, CompPoly.GuruswamiSudan.GSRootContext
statement: formalized
proof: formalized
---

# Guruswami-Sudan Backend Contexts

`CompPoly.Bivariate.GuruswamiSudan.Context`, in [CompPoly/Bivariate/GuruswamiSudan/Context.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean), by Valerii Huhnin.

> Explicit executable contexts for the CompPoly Guruswami-Sudan core. The
> contexts package replaceable operations together with the contracts used by the
> public correctness theorems.

`CompPoly.GuruswamiSudan.GSInterpParams` (structure, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L27))

> Parameters for the CompPoly interpolation step.

```lean
structure GSInterpParams where
  messageDegree : Nat
  multiplicity : Nat
  weightedDegreeBound : Nat
deriving Repr, BEq, DecidableEq
```

`CompPoly.GuruswamiSudan.yWeight` (definition, [line 34](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L34))

> The GS weighted degree uses weights `(1, messageDegree - 1)`.

```lean
def yWeight (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.degreeLt` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L38))

> `p.degree < k`, treating the zero polynomial as degree `bot`.

```lean
def degreeLt {F : Type*} [Zero F] (p : CPolynomial F) (k : Nat) : Prop
```

`CompPoly.GuruswamiSudan.DistinctXCoordinates` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L42))

> Packed input points have no duplicate `x`-coordinates.

```lean
def DistinctXCoordinates {F : Type*} (points : Array (Prod F F)) : Prop
```

`CompPoly.GuruswamiSudan.ValidInterpolationWitness` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L47))

> Semantic interpolation witness used by backend contracts and core
> completeness statements.

```lean
def ValidInterpolationWitness {F : Type*}
    [CommSemiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (points : Array (Prod F F)) (params : GSInterpParams) (Q : CBivariate F) : Prop
```

`CompPoly.GuruswamiSudan.LinearKernelContext` (structure, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L62))

> A dense homogeneous linear-kernel backend.
>
> The operation returns a nonzero kernel witness in the backend's chosen
> normalization when it can find one. Completeness is stated in the negative form
> needed by dense interpolation systems: if no witness is returned, no nonzero
> homogeneous solution exists.

```lean
structure LinearKernelContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  homogeneousWitness : DenseMatrix F → Option (Array F)
  witness_width :
    ∀ {M : DenseMatrix F} {v : Array F},
      homogeneousWitness M = some v →
        DenseMatrix.VectorWidth M v
  witness_sound :
    ∀ {M : DenseMatrix F} {v : Array F},
      DenseMatrix.WellFormed M →
        homogeneousWitness M = some v →
          DenseMatrix.IsHomogeneousSolution M v
  witness_nonzero :
    ∀ {M : DenseMatrix F} {v : Array F},
      homogeneousWitness M = some v →
        DenseMatrix.NonzeroVector v
  witness_complete :
    ∀ {M : DenseMatrix F},
      DenseMatrix.WellFormed M →
        homogeneousWitness M = none →
          ∀ v,
            DenseMatrix.VectorWidth M v →
              DenseMatrix.IsHomogeneousSolution M v →
                ¬ (DenseMatrix.NonzeroVector v)
```

`CompPoly.GuruswamiSudan.denseLinearKernelContext` (definition, [line 93](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L93))

> The dense Gaussian-elimination homogeneous-kernel backend.
>
> The executable witness is computed by the in-place reduction
> `DenseMatrix.homogeneousWitnessInPlace`, which mutates the matrix array instead of
> copying it on every row operation. It returns the same witness as the copying
> `DenseMatrix.homogeneousWitness` (`DenseMatrix.homogeneousWitnessInPlace_eq`), so the
> backend contract is discharged by the copying-kernel correctness lemmas.

```lean
def denseLinearKernelContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] :
    LinearKernelContext F
```

`CompPoly.GuruswamiSudan.GSInterpContext` (structure, [line 119](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L119))

> Guruswami-Sudan-facing interpolation backend.
>
> The backend packages the executable interpolation operation together with the
> contract fields used by callers, using the explicit context style used by
> univariate multiplication and remainder backends.

```lean
structure GSInterpContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] where
  interpolate : Array (Prod F F) → GSInterpParams → Option (CBivariate F)
  sound :
    ∀ points params Q,
      interpolate points params = some Q →
        ValidInterpolationWitness points params Q
  complete :
    ∀ points params,
      DistinctXCoordinates points →
      (exists Q, ValidInterpolationWitness points params Q) →
        exists Q, interpolate points params = some Q
```

`CompPoly.GuruswamiSudan.FieldRootContext` (structure, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L138))

> Executable root finder for univariate field polynomials.
>
> Completeness is only required for nonzero polynomials. A zero univariate
> polynomial vanishes on every field element, so an unconditional array-valued
> complete root finder would have to enumerate the whole field.

```lean
structure FieldRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  rootsInField : CPolynomial F → Array F
  sound :
    ∀ p a,
      a ∈ (rootsInField p).toList →
        CPolynomial.eval a p = 0
  complete :
    ∀ p a,
      p ≠ 0 →
      CPolynomial.eval a p = 0 →
        a ∈ (rootsInField p).toList
```

`CompPoly.GuruswamiSudan.GSRootContext` (structure, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean#L156))

> Guruswami-Sudan-facing bounded-degree root backend.
>
> Completeness is only required for nonzero bivariate input. The zero bivariate
> polynomial has every degree-bounded univariate polynomial as a root, which is not
> a finite output contract for large fields.

```lean
structure GSRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F]
    [DecidableEq F] where
  rootsYDegreeLt : CBivariate F → Nat → Array (CPolynomial F)
  sound :
    ∀ Q k p,
      p ∈ (rootsYDegreeLt Q k).toList →
        degreeLt p k ∧ CBivariate.composeY Q p = 0
  complete :
    ∀ Q k p,
      Q ≠ 0 →
      degreeLt p k →
      CBivariate.composeY Q p = 0 →
        p ∈ (rootsYDegreeLt Q k).toList
```

## Depends on

- [Partial Derivatives and Multiplicity of Computable Bivariate Polynomials](../deriv.md)
- [Guruswami-Sudan Polynomial Helpers](polynomial.md)
- [In-Place Dense Homogeneous Kernels](../../linearalgebra/dense/kernelinplace.md)

## Proof depends on

- [Dense Homogeneous-Kernel Correctness](../../linearalgebra/dense/kernelcorrectness.md)
- [In-Place Dense Kernel Correctness](../../linearalgebra/dense/kernelinplacecorrectness.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Context.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Context.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Context.json)
