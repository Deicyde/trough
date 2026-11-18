---
declaration: module
origin: cited
lean: ProbabilisticTheory.isTraceClass_zero, ProbabilisticTheory.isTraceClass_smul, ProbabilisticTheory.isTraceClass_neg, ProbabilisticTheory.traceNorm_zero, ProbabilisticTheory.traceNorm_smul, ProbabilisticTheory.traceNorm_neg, ProbabilisticTheory.opNorm_le_traceNorm, ProbabilisticTheory.traceClassSubmodule
statement: formalized
proof: formalized
---

# The trace-class Banach space

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.TraceClass.Banach`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean): 21 declarations, 12 with a docstring.

> Trace-class operators form a Banach space under the trace norm.

## i. Overview

> The trace-class operators form a Banach space `𝒮₁(H)` under the trace norm. The trace norm dominates
> the operator norm, so an absolutely convergent series of trace-class operators converges in operator
> norm. Its limit is trace class because the trace norm is lower semicontinuous along such limits,
> which gives completeness.

## ii. Key results

> - `TraceClass` : the trace-class operators with the trace norm.
> - `opNorm_le_traceNorm` : the operator norm is at most the trace norm.
> - `isTraceClass_of_tendsto_of_traceNorm_bounded` : an operator-norm limit of trace-class operators
>   with bounded trace norms is trace class.
> - `TraceClass.instCompleteSpace` : `𝒮₁(H)` is complete.

## iv. References

> * None.

## A. Arithmetic closure of `IsTraceClass`

**`ProbabilisticTheory.isTraceClass_zero`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L56).

```lean
lemma isTraceClass_zero : IsTraceClass (0 : H →L[ℂ] H)
```

**`ProbabilisticTheory.isTraceClass_smul`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L61).

> Trace-class operators are closed under scalar multiplication.

```lean
lemma isTraceClass_smul (c : ℂ) {T : H →L[ℂ] H} (hT : IsTraceClass T) :
    IsTraceClass (c • T)
```

**`ProbabilisticTheory.isTraceClass_neg`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L80).

```lean
lemma isTraceClass_neg {T : H →L[ℂ] H} (hT : IsTraceClass T) : IsTraceClass (-T)
```

**`ProbabilisticTheory.traceNorm_zero`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L84).

```lean
lemma traceNorm_zero : traceNorm (0 : H →L[ℂ] H) isTraceClass_zero = 0
```

**`ProbabilisticTheory.traceNorm_smul`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L90).

> The trace norm is absolutely homogeneous: `‖c • T‖₁ = ‖c‖ ‖T‖₁`.

```lean
lemma traceNorm_smul (c : ℂ) {T : H →L[ℂ] H} (hT : IsTraceClass T) :
    traceNorm (c • T) (isTraceClass_smul c hT) = ‖c‖ * traceNorm T hT
```

**`ProbabilisticTheory.traceNorm_neg`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L107).

```lean
lemma traceNorm_neg {T : H →L[ℂ] H} (hT : IsTraceClass T) (hnegT : IsTraceClass (-T)) :
    traceNorm (-T) hnegT = traceNorm T hT
```

**`ProbabilisticTheory.opNorm_le_traceNorm`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L125).

> **The operator norm is at most the trace norm.** With `S = √|T|`, Parseval and Cauchy–Schwarz
> give `‖S x‖² ≤ ‖T‖₁ ‖x‖²`, and `‖T‖ = ‖S‖²`.

```lean
lemma opNorm_le_traceNorm {T : H →L[ℂ] H} (hT : IsTraceClass T) : ‖T‖ ≤ traceNorm T hT
```

## B. The trace-class submodule and Banach space

**`ProbabilisticTheory.traceClassSubmodule`**, a def, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L186).

> The trace-class operators, as a submodule of the bounded operators.

```lean
def traceClassSubmodule (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H]
    [CompleteSpace H] : Submodule ℂ (H →L[ℂ] H)
```

**`ProbabilisticTheory.TraceClass`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L195).

> **The trace-class Banach space `𝒮₁(H)`**, normed by the trace norm. It is a `def` so that the
> operator norm inherited from the ambient submodule is not found as an instance.

```lean
def TraceClass (H : Type*) [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H] :
    Type _
```

**`ProbabilisticTheory.TraceClass.instAddCommGroup`**, an instance, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L201).

```lean
noncomputable instance instAddCommGroup : AddCommGroup (TraceClass H)
```

**`ProbabilisticTheory.TraceClass.instModule`**, an instance, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L204).

```lean
noncomputable instance instModule : Module ℂ (TraceClass H)
```

**`ProbabilisticTheory.TraceClass.mem_iff`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L207).

```lean
lemma mem_iff {T : H →L[ℂ] H} : T ∈ traceClassSubmodule H ↔ IsTraceClass T
```

**`ProbabilisticTheory.TraceClass.isTraceClass_coe`**, a lemma, [line 210](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L210).

> The trace-class witness carried by an element of `TraceClass H`.

```lean
lemma isTraceClass_coe (T : TraceClass H) : IsTraceClass T.1
```

**`ProbabilisticTheory.TraceClass.ofOperator`**, a def, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L213).

> The element of `TraceClass H` given by a trace-class operator.

```lean
def ofOperator (T : H →L[ℂ] H) (hT : IsTraceClass T) : TraceClass H
```

**`ProbabilisticTheory.TraceClass.ofOperator_coe`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L215).

```lean
lemma ofOperator_coe (T : H →L[ℂ] H) (hT : IsTraceClass T) :
    (ofOperator T hT).1 = T
```

**`ProbabilisticTheory.TraceClass.traceClassAddGroupNorm`**, a def, [line 221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L221).

> **The trace norm as an `AddGroupNorm`** on the trace-class submodule: nonnegativity, the
> triangle inequality (`traceNorm_add_le`), invariance under negation, and the zero-detection
> property (via `opNorm_le_traceNorm`).

```lean
noncomputable def traceClassAddGroupNorm : AddGroupNorm (TraceClass H)
```

**`ProbabilisticTheory.TraceClass.instNormedAddCommGroup`**, an instance, [line 235](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L235).

> **The trace-class Banach space's `NormedAddCommGroup` instance**, with norm `traceNorm`.

```lean
noncomputable instance instNormedAddCommGroup : NormedAddCommGroup (TraceClass H)
```

**`ProbabilisticTheory.TraceClass.norm_eq_traceNorm`**, a lemma, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L238).

```lean
lemma norm_eq_traceNorm (T : TraceClass H) :
    ‖T‖ = traceNorm T.1 (isTraceClass_coe T)
```

**`ProbabilisticTheory.TraceClass.instNormedSpace`**, an instance, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L243).

> **The trace-class Banach space's `NormedSpace ℂ` instance**: scalar multiplication scales the
> trace norm exactly, by `traceNorm_smul`.

```lean
noncomputable instance instNormedSpace : NormedSpace ℂ (TraceClass H)
```

**`ProbabilisticTheory.TraceClass.isTraceClass_of_tendsto_of_traceNorm_bounded`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L253).

> **Lower semicontinuity of the trace norm.** An operator-norm limit of trace-class operators with
> trace norms bounded by `C` is trace class, with trace norm at most `C`.

```lean
lemma isTraceClass_of_tendsto_of_traceNorm_bounded {Tn : ℕ → H →L[ℂ] H} {T : H →L[ℂ] H} {C : ℝ}
    (hTn : ∀ n, IsTraceClass (Tn n)) (hbound : ∀ n, traceNorm (Tn n) (hTn n) ≤ C)
    (htendsto : Tendsto Tn atTop (𝓝 T)) :
    ∃ hT : IsTraceClass T, traceNorm T hT ≤ C
```

**`ProbabilisticTheory.TraceClass.instCompleteSpace`**, an instance, [line 323](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean#L323).

> **The trace-class operators form a Banach space.** The partial sums of an absolutely convergent
> series converge in operator norm, and lower semicontinuity bounds the trace norm of the tails.

```lean
noncomputable instance instCompleteSpace : CompleteSpace (TraceClass H)
```

## Depends on

- [Products of Hilbert–Schmidt operators](traceclass-generalproduct.md)

## Proof depends on

- [Trace-norm estimates](traceclass-idealnorm.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/TraceClass/Banach.lean)
