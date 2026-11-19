---
declaration: lemma
origin: cited
lean: MIPRE.Introspection.ClockArithmetic.uniformProg_closed, MIPRE.Introspection.ClockArithmetic.uniformProg_runs, MIPRE.Introspection.growingClock_budget, MIPRE.Introspection.growingClock_runs, MIPRE.Introspection.growingClock_size, MIPRE.Introspection.growingClockCompiler_apply, MIPRE.Introspection.growingClockCompiler_runs, MIPRE.Introspection.growingClock_polynomial_time, MIPRE.Introspection.growingClock_ansBound_time, MIPRE.Introspection.ClockSimulation.prog_closed, MIPRE.Introspection.ClockSimulation.prog_halts, MIPRE.Introspection.ClockSimulation.decider_accepts_iff, MIPRE.Introspection.ClockSimulation.original_decider_preserved, MIPRE.Introspection.ClockSimulation.compiler_apply, MIPRE.Introspection.ClockSimulation.compiler_binary_bounds, MIPRE.Introspection.ClockSimulation.decider_haltsWithin, MIPRE.Introspection.ClockSimulation.original_decider_ansBound_time
statement: formalized
proof: formalized
---

# Executable growing clock and original-index simulation

For each fixed exponent $k$, an actual closed program generates the unary budget $2^{(\lambda n+1)^k}$. Hardwiring $\lambda$ adds only its binary encoding size and a fixed overhead; the parameter-to-program compiler is polynomial time. For $k,\lambda,n\geq1$, generation time is polynomial in that budget and is bounded by a uniformly enlarged introspection budget. A total clocked simulator reads the clock at index $n$ and runs the original program at $2^n$. For a bounded source verifier and legal original questions and answers, the exponent-five clock preserves acceptance exactly. Its actual compiler has polynomial cost and output size in the source description size and binary parameter length. For a bounded source and positive index, the complete clock generation, reindexing, universal simulation and result check fit a uniformly enlarged introspection budget. This is the original-program simulation component, not the complete introspection predicate or its cutoff parser.

## Depends on

- [Absolute costs on the original legal answer cut](../part-02/lem-intro-ambient-runtime.md)
- [Total clocking of arbitrary typed decision programs](../part-01/lem-detype-total-clock.md)

## Proof depends on

- [Efficient s-m-n](../../computability/lem-smn.md)

## Proof

Compose the checked unary arithmetic and exponentiation programs, hardwire the binary parameter using the actual specialization compiler, and bound the cost by a fixed polynomial in the output budget. The reindexing program changes only the source index. Determinism and the legal-query runtime bound show that clocking preserves the source's accepting result. Compose the actual program constructors for compilation, and absorb the complete execution cost into a fixed polynomial of the generated budget.

## Lean

Formalized as [`MIPRE.Introspection.ClockArithmetic.uniformProg_closed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockArithmetic.uniformProg_closed), [`MIPRE.Introspection.ClockArithmetic.uniformProg_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockArithmetic.uniformProg_runs), [`MIPRE.Introspection.growingClock_budget`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClock_budget), [`MIPRE.Introspection.growingClock_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClock_runs), [`MIPRE.Introspection.growingClock_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClock_size), [`MIPRE.Introspection.growingClockCompiler_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClockCompiler_apply), [`MIPRE.Introspection.growingClockCompiler_runs`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClockCompiler_runs), [`MIPRE.Introspection.growingClock_polynomial_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClock_polynomial_time), [`MIPRE.Introspection.growingClock_ansBound_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.growingClock_ansBound_time), [`MIPRE.Introspection.ClockSimulation.prog_closed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.prog_closed), [`MIPRE.Introspection.ClockSimulation.prog_halts`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.prog_halts), [`MIPRE.Introspection.ClockSimulation.decider_accepts_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.decider_accepts_iff), [`MIPRE.Introspection.ClockSimulation.original_decider_preserved`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.original_decider_preserved), [`MIPRE.Introspection.ClockSimulation.compiler_apply`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.compiler_apply), [`MIPRE.Introspection.ClockSimulation.compiler_binary_bounds`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.compiler_binary_bounds), [`MIPRE.Introspection.ClockSimulation.decider_haltsWithin`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.decider_haltsWithin), [`MIPRE.Introspection.ClockSimulation.original_decider_ansBound_time`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Introspection.ClockSimulation.original_decider_ansBound_time).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 1858](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L1858)
