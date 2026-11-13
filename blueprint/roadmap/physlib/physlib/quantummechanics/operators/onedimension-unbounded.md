---
declaration: module
origin: cited
lean: QuantumMechanics.OneDimension.UnboundedOperator, QuantumMechanics.OneDimension.UnboundedOperator.ofSelfCLM, QuantumMechanics.OneDimension.UnboundedOperator.ofSelfCLM_apply, QuantumMechanics.OneDimension.UnboundedOperator.IsGeneralizedEigenvector, QuantumMechanics.OneDimension.UnboundedOperator.isGeneralizedEigenvector_ofSelfCLM_iff, QuantumMechanics.OneDimension.UnboundedOperator.IsSymmetric
statement: formalized
proof: formalized
---

# Unbounded operators

The module `Physlib.QuantumMechanics.Operators.OneDimension.Unbounded`, [Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean): 7 declarations (1 instance with no name), 4 with a docstring.

## Note

> It is likely one day the material in this file will be moved to or appear
> in another form within Mathlib.

**`QuantumMechanics.OneDimension.UnboundedOperator`**, a def, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L32).

> An unbounded operator on the one-dimensional Hilbert space,
> corresponds to a subobject `ι : S →L[ℂ] HilbertSpace` of the Hilbert
> space along with the operator `op : S →L[ℂ] HilbertSpace`

```lean
def UnboundedOperator {S : Type} [AddCommGroup S] [Module ℂ S]
    [TopologicalSpace S] (ι : S →L[ℂ] HilbertSpace)
    (_ : Function.Injective ι)
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L42).

```lean
instance : CoeFun (UnboundedOperator ι hι) (fun _ => S → HilbertSpace)
```

**`QuantumMechanics.OneDimension.UnboundedOperator.ofSelfCLM`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L46).

> An unbounded operator created from a continuous linear map ` S →L[ℂ] S`.

```lean
def ofSelfCLM (Op : S →L[ℂ] S) : UnboundedOperator ι hι
```

**`QuantumMechanics.OneDimension.UnboundedOperator.ofSelfCLM_apply`**, a lemma, [line 49](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L49).

```lean
lemma ofSelfCLM_apply (Op : S →L[ℂ] S) (ψ : S) :
    ofSelfCLM (hι := hι) Op ψ = ι (Op ψ)
```

**`QuantumMechanics.OneDimension.UnboundedOperator.IsGeneralizedEigenvector`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L54).

> A map `F : S →L[ℂ] ℂ` is a generalized eigenvector of an unbounded operator `U`
> on `S` if there is an eigenvalue `c` such that for all `ψ`, `F (U ψ) = c ⬝ F ψ`

```lean
def IsGeneralizedEigenvector (F : S →L[ℂ] ℂ) (c : ℂ) : Prop
```

**`QuantumMechanics.OneDimension.UnboundedOperator.isGeneralizedEigenvector_ofSelfCLM_iff`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L57).

```lean
lemma isGeneralizedEigenvector_ofSelfCLM_iff {Op : S →L[ℂ] S}
    (F : S →L[ℂ] ℂ) (c : ℂ) :
    IsGeneralizedEigenvector (ofSelfCLM (hι := hι) Op) F c ↔
    ∀ ψ : S, F (Op ψ) = c • F ψ
```

**`QuantumMechanics.OneDimension.UnboundedOperator.IsSymmetric`**, a def, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean#L70).

> The condition for an unbounded operator to be *symmetric* (equivalently, formally
> self-adjoint): `⟪U ψ1, ι ψ2⟫ = ⟪ι ψ1, U ψ2⟫` for all `ψ1 ψ2`. This is the Hermitian
> pairing on the underlying space `S`; on its own it does **not** imply genuine
> self-adjointness (`A† = A`, including equality of domains), which for an unbounded
> operator on a proper dense core is strictly stronger.

```lean
def IsSymmetric : Prop
```

## Depends on

- [Hilbert space for one dimension quantum mechanics](../hilbertspaces/onedimension-basic.md)

## Sources

- [Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Operators/OneDimension/Unbounded.lean)
