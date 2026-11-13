---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceLeft, MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceRight, MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceLeft_of_trace_eq_one, MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceRight_of_trace_eq_one, MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceLeft_vecMulVec_star, MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceRight_vecMulVec_star, MathlibExt.LinearAlgebra.Matrix.PartialTrace.posSemidef_partialTraceLeft, MathlibExt.LinearAlgebra.Matrix.PartialTrace.posSemidef_partialTraceRight
statement: formalized
proof: formalized
---

# Partial trace

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html).

## Partial trace over the first factor

The partial trace over the first factor: `∑ i, A (i, j) (i, j')`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceLeft`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#partial-trace-left).

## Partial trace over the second factor

The partial trace over the second factor: `∑ j, A (i, j) (i', j)`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceRight`, a definition declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#partial-trace-right).

## Left partial trace of a density matrix has trace one

The partial trace of a density matrix has trace `1`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceLeft_of_trace_eq_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#trace-partial-trace-left-of-trace-eq-one).

## Right partial trace of a density matrix has trace one

The partial trace of a density matrix has trace `1`.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceRight_of_trace_eq_one`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#trace-partial-trace-right-of-trace-eq-on).

## Left partial trace of a rank-one matrix

The partial trace of a rank-one positive semidefinite matrix is the sum
of the rank-one positive semidefinite matrices of its slices.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceLeft_vecMulVec_star`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 191](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L191). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#partial-trace-left-vec-mul-vec-star).

## Right partial trace of a rank-one matrix

The partial trace of a rank-one positive semidefinite matrix is the sum
of the rank-one positive semidefinite matrices of its slices.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.partialTraceRight_vecMulVec_star`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#partial-trace-right-vec-mul-vec-star).

## Left partial trace preserves positive semidefiniteness

The partial trace over the first factor preserves positive semidefiniteness.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.posSemidef_partialTraceLeft`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#pos-semidef-partial-trace-left).

## Right partial trace preserves positive semidefiniteness

The partial trace over the second factor preserves positive semidefiniteness.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.posSemidef_partialTraceRight`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#pos-semidef-partial-trace-right).

## Left partial trace is adjoint to identity amplification

The partial trace over the first factor is adjoint to amplification by
the identity, in the trace pairing.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceLeft_mul`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#trace-partial-trace-left-mul).

## Right partial trace is adjoint to identity amplification

The partial trace over the second factor is adjoint to amplification by
the identity, in the trace pairing.

Formalized by `MathlibExt.LinearAlgebra.Matrix.PartialTrace.trace_partialTraceRight_mul`, a theorem declared in [MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/LinearAlgebra/Matrix/PartialTrace.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html#trace-partial-trace-right-mul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Partial trace](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/linear-maps-and-duality/partial-trace)
