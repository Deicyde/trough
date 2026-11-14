---
declaration: module
origin: cited
lean: HermitianMat.trace_eq_trace, HermitianMat.trace_eq_trace_trivial, HermitianMat.trace_eq_trace_rc, HermitianMat.trace, HermitianMat.trace_smul, HermitianMat.trace_zero, HermitianMat.trace_add, HermitianMat.traceAddMonoidHom
statement: formalized
proof: formalized
---

# Trace of Hermitian Matrices

The module `QuantumInfo.ForMathlib.HermitianMat.Trace`, [QuantumInfo/ForMathlib/HermitianMat/Trace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean): 39 declarations, 5 with a docstring, 3 listed as significant.

> While the trace of a Hermitian matrix is, in informal math, typically just "the same as" a trace of
> a matrix that happens to be Hermitian - it is a real number, not a complex number. Or more generally,
> it is a self-adjoint element of the base `StarAddMonoid`.
>
> Working directly with `Matrix.trace` then means that there would be constant casts between rings,
> chasing imaginary parts and inequalities and so on. By defining `HermitianMat.trace` as its own
> operation, we encapsulate the mess and give a clean interface.
>
> The `IsMaximalSelfAdjoint` class is used so that (for example) for matrices over ℤ or ℝ,
> `HermitianMat.trace` works as well and is in fact defeq to `Matrix.trace`. For ℂ or `RCLike`,
> it uses the real part.

**`HermitianMat.trace`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L39).

> The trace of the matrix. This requires a `IsMaximalSelfAdjoint R α` instance, and then maps from
> `HermitianMat n α` to `R`. This means that the trace of (say) a `HermitianMat n ℤ` gives values in ℤ,
> but that the trace of a `HermitianMat n ℂ` gives values in ℝ. The fact that traces are "automatically"
> real reduces coercions down the line.

```lean
def trace (A : HermitianMat n α) : R
```

**`HermitianMat.trace_eq_trace`**, a theorem, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L43). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `HermitianMat.trace` reduces to `Matrix.trace` in the algebra.

```lean
theorem trace_eq_trace (A : HermitianMat n α) : algebraMap R α A.trace = Matrix.trace A.mat
```

**`HermitianMat.trace_smul`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L50).

```lean
lemma trace_smul (A : HermitianMat n α) (r : R) : (r • A).trace = r * A.trace
```

**`HermitianMat.trace_zero`**, a lemma, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L58).

```lean
lemma trace_zero : (0 : HermitianMat n α).trace = 0
```

**`HermitianMat.trace_add`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L62).

```lean
lemma trace_add (A B : HermitianMat n α) : (A + B).trace = A.trace + B.trace
```

**`HermitianMat.traceAddMonoidHom`**, a def, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L67).

> `trace` bundled as an `AddMonoidHom`.

```lean
def traceAddMonoidHom : HermitianMat n α →+ R
```

**`HermitianMat.trace_listSum`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L73).

```lean
lemma trace_listSum (l : List (HermitianMat n α)) : l.sum.trace = (l.map trace).sum
```

**`HermitianMat.trace_multisetSum`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L77).

```lean
lemma trace_multisetSum (l : Multiset (HermitianMat n α)) : l.sum.trace = (l.map trace).sum
```

**`HermitianMat.trace_sum`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L81).

```lean
lemma trace_sum {ι : Type*} (s : Finset ι) (f : ι → HermitianMat n α) :
    (∑ i ∈ s, f i).trace = ∑ i ∈ s, (f i).trace
```

**`HermitianMat.trace_neg`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L90).

```lean
lemma trace_neg (A : HermitianMat n α) : (-A).trace = -A.trace
```

**`HermitianMat.trace_sub`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L94).

```lean
lemma trace_sub (A B : HermitianMat n α) : (A - B).trace = A.trace - B.trace
```

**`Matrix.IsHermitian.isSelfAdjoint_trace`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L103).

```lean
lemma _root_.Matrix.IsHermitian.isSelfAdjoint_trace {A : Matrix n n α} (hA : A.IsHermitian) :
    IsSelfAdjoint A.trace
```

**`HermitianMat.trace_kronecker`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L110).

```lean
lemma trace_kronecker [FaithfulSMul R α] : (A ⊗ₖ B).trace = A.trace * B.trace
```

**`HermitianMat.trace_eq_trace_trivial`**, a theorem, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L128). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `HermitianMat.trace` reduces to `Matrix.trace` when the elements are a `TrivialStar`.

```lean
theorem trace_eq_trace_trivial (A : HermitianMat n ℝ) : A.trace = A.mat.trace
```

**`HermitianMat.trace_eq_re_trace`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L138).

```lean
lemma trace_eq_re_trace (A : HermitianMat n 𝕜) : A.trace = RCLike.re A.mat.trace
```

**`HermitianMat.trace_one`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L142).

```lean
lemma trace_one [DecidableEq n] : (1 : HermitianMat n 𝕜).trace = Fintype.card n
```

**`HermitianMat.trace_eq_trace_rc`**, a theorem, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L147). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> `HermitianMat.trace` reduces to `Matrix.trace` when the elements are `RCLike`.

```lean
theorem trace_eq_trace_rc (A : HermitianMat n 𝕜) : A.trace = A.mat.trace
```

**`HermitianMat.trace_diagonal`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L152).

```lean
lemma trace_diagonal {T : Type*} [Fintype T] [DecidableEq T] (f : T → ℝ) :
    (diagonal 𝕜 f).trace = ∑ i, f i
```

**`HermitianMat.sum_eigenvalues_eq_trace`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L157).

```lean
lemma sum_eigenvalues_eq_trace [DecidableEq n] (A : HermitianMat n 𝕜) :
    ∑ i, A.H.eigenvalues i = A.trace
```

**`HermitianMat.trace_eq_zero_iff`**, a lemma, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L164).

```lean
lemma trace_eq_zero_iff (A : HermitianMat n 𝕜) : A.trace = 0 ↔ A.mat.trace = 0
```

**`HermitianMat.trace_eq_one_iff`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L168).

```lean
lemma trace_eq_one_iff (A : HermitianMat n 𝕜) : A.trace = 1 ↔ A.mat.trace = 1
```

**`HermitianMat.trace_reindex`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L174).

```lean
lemma trace_reindex (A : HermitianMat n 𝕜) (e : n ≃ m) :
    (A.reindex e).trace = A.trace
```

**`HermitianMat.continuous_trace`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L179).

```lean
lemma continuous_trace : Continuous (HermitianMat.trace (α := 𝕜) (n := n))
```

**`HermitianMat.traceLeft`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L189).

```lean
def traceLeft (A : HermitianMat (m × n) α) : HermitianMat n α
```

**`HermitianMat.traceRight`**, a def, [line 192](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L192).

```lean
def traceRight (A : HermitianMat (m × n) α) : HermitianMat m α
```

**`HermitianMat.traceLeft_mat`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L198).

```lean
lemma traceLeft_mat : A.traceLeft.mat = A.mat.traceLeft
```

**`HermitianMat.traceLeft_add`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L202).

```lean
lemma traceLeft_add : (A + B).traceLeft = A.traceLeft + B.traceLeft
```

**`HermitianMat.traceLeft_neg`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L206).

```lean
lemma traceLeft_neg : (-A).traceLeft = -A.traceLeft
```

**`HermitianMat.traceLeft_sub`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L210).

```lean
lemma traceLeft_sub : (A - B).traceLeft = A.traceLeft - B.traceLeft
```

**`HermitianMat.traceRight_mat`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L216).

```lean
lemma traceRight_mat :
    (traceRight A).mat = A.mat.traceRight
```

**`HermitianMat.traceRight_add`**, a lemma, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L221).

```lean
lemma traceRight_add : (A + B).traceRight = A.traceRight + B.traceRight
```

**`HermitianMat.traceRight_neg`**, a lemma, [line 225](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L225).

```lean
lemma traceRight_neg : (-A).traceRight = -A.traceRight
```

**`HermitianMat.traceRight_sub`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L229).

```lean
lemma traceRight_sub : (A - B).traceRight = A.traceRight - B.traceRight
```

**`HermitianMat.traceLeft_smul`**, a lemma, [line 240](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L240).

```lean
lemma traceLeft_smul (r : ℝ) : (r • A).traceLeft = r • A.traceLeft
```

**`HermitianMat.traceRight_smul`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L245).

```lean
lemma traceRight_smul (r : ℝ) : (r • A).traceRight = r • A.traceRight
```

**`HermitianMat.traceLeft_trace`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L249).

```lean
lemma traceLeft_trace : A.traceLeft.trace = A.trace
```

**`HermitianMat.traceRight_trace`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L253).

```lean
lemma traceRight_trace : A.traceRight.trace = A.trace
```

**`HermitianMat.traceLeft_kron`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L263).

```lean
lemma traceLeft_kron [Fintype m] : (A ⊗ₖ B).traceLeft = A.trace • B
```

**`HermitianMat.traceRight_kron`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean#L269).

```lean
lemma traceRight_kron [Fintype n] : (A ⊗ₖ B).traceRight = B.trace • A
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.Reindex](reindex.md)
- [Maximal self-adjoint subrings](../ismaximalselfadjoint.md)
- [QuantumInfo.ForMathlib.Matrix](../matrix.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Trace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Trace.lean)
