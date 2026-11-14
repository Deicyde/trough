---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.TailoredVerifier.IsBounded.two_le, MIPRE.Tailored.Intro.InputRuns.clamp, MIPRE.Tailored.Intro.InputRuns.clamp_bounded, MIPRE.Tailored.Intro.InputRuns.clamp_size, MIPRE.Tailored.Intro.InputRuns.runLen, MIPRE.Tailored.Intro.InputRuns.runLp, MIPRE.Tailored.Intro.InputRuns.runLen_eq, MIPRE.Tailored.Intro.InputRuns.runLp_eq, MIPRE.Tailored.Intro.InputRuns.lenDefined, MIPRE.Tailored.Intro.InputRuns.lenRun, MIPRE.Tailored.Intro.InputRuns.lpRun, MIPRE.Tailored.Intro.InputRuns.lenRun_clamp, MIPRE.Tailored.Intro.InputRuns.lpRun_clamp, MIPRE.Tailored.Intro.InputRuns.ansBound_mono, MIPRE.Tailored.Intro.InputRuns.len_clock_le, MIPRE.Tailored.Intro.InputRuns.lp_clock_le, MIPRE.Tailored.Intro.InputRuns.lenRun_seven, MIPRE.Tailored.Intro.InputRuns.lpRun_seven
statement: formalized
proof: formalized
---

# The input's programs, run on a clamped description

Clamp the descriptions of a tailored verifier's three programs to size $\lambda$: a $\lambda$-bounded verifier keeps them, and the clamp has size linear in $\lambda$. Run the answer-length calculator and the linear-constraints processor of the clamped description through a clocked universal machine. With a clock at least the time bound of $\lambda$-boundedness at index $m \geq 2$ — at $m = 2^n$, the introspection verifier's own clock $2^{(\lambda n + 1)^5}$, for arguments of length at most $(2^n)^\lambda$ — the runs output the input's lengths and its constraints.

## Depends on

- [Tailored normal form verifier; II:1758](../part-01/def-tailored-verifier.md)
- [$\lambda$-bounded tailored verifiers, and budgets; II:1800](../part-01/def-tailored-bounded.md)
- [Total clocking of arbitrary typed decision programs](../../structure-of-the-proof/part-01/lem-detype-total-clock.md)
- [Absolute costs on the original legal answer cut](../../structure-of-the-proof/part-02/lem-intro-ambient-runtime.md)

## Proof

A bounded program halts within its bound, so the clocked run is the run; a bounded calculator halts at every question, so the constraints are what the processor outputs.

## Lean

Formalized as [`MIPRE.Tailored.TailoredVerifier.IsBounded.two_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.TailoredVerifier.IsBounded.two_le), [`MIPRE.Tailored.Intro.InputRuns.clamp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.clamp), [`MIPRE.Tailored.Intro.InputRuns.clamp_bounded`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.clamp_bounded), [`MIPRE.Tailored.Intro.InputRuns.clamp_size`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.clamp_size), [`MIPRE.Tailored.Intro.InputRuns.runLen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.runLen), [`MIPRE.Tailored.Intro.InputRuns.runLp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.runLp), [`MIPRE.Tailored.Intro.InputRuns.runLen_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.runLen_eq), [`MIPRE.Tailored.Intro.InputRuns.runLp_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.runLp_eq), [`MIPRE.Tailored.Intro.InputRuns.lenDefined`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lenDefined), [`MIPRE.Tailored.Intro.InputRuns.lenRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lenRun), [`MIPRE.Tailored.Intro.InputRuns.lpRun`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lpRun), [`MIPRE.Tailored.Intro.InputRuns.lenRun_clamp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lenRun_clamp), [`MIPRE.Tailored.Intro.InputRuns.lpRun_clamp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lpRun_clamp), [`MIPRE.Tailored.Intro.InputRuns.ansBound_mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.ansBound_mono), [`MIPRE.Tailored.Intro.InputRuns.len_clock_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.len_clock_le), [`MIPRE.Tailored.Intro.InputRuns.lp_clock_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lp_clock_le), [`MIPRE.Tailored.Intro.InputRuns.lenRun_seven`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lenRun_seven), [`MIPRE.Tailored.Intro.InputRuns.lpRun_seven`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Intro.InputRuns.lpRun_seven).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 2026](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L2026)
