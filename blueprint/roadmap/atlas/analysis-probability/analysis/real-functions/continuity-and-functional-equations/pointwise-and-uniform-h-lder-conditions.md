---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Calculus.ScottishBook83Wanted.ScottishBookProblem83Claim, MathlibExt.Analysis.Calculus.ScottishBook83Wanted.auerbach83_refuted
statement: formalized
---

# Pointwise and uniform Hölder conditions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/pointwise-and-uniform-h-lder-conditions/index.html).

## Auerbach's Hölder condition problem (Scottish Book 83)

Auerbach's Problem 83 from the Scottish Book: if a continuous
function `f` satisfies, at every point `x`, that the difference
quotients `|f (x + h) - f x| / |h| ^ a` stay below a constant `M` for
all sufficiently small nonzero `h` — that is, if the limsup of the
quotients as `h → 0` is `< M`, with `0 < a < 1` — does `f` then satisfy
a Hölder condition of exponent `a`?

Formalized by `MathlibExt.Analysis.Calculus.ScottishBook83Wanted.ScottishBookProblem83Claim`, a definition declared in [WantedExt/Analysis/Calculus/ScottishBook83Wanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/ScottishBook83Wanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/pointwise-and-uniform-h-lder-conditions/index.html#scottish-book-problem83-claim).

## Pointwise difference-quotient bounds do not imply Hölder continuity

Auerbach's Problem 83 is false: the pointwise limsup condition does
not imply a Hölder condition. Source: H. Auerbach, Problem 83 of the
Scottish Book; typescript Ad 83 records the negative answer, with
Marcinkiewicz's counterexample: a triangular function on intervals
`1 / n - xₙ`, `1 / n + xₙ` with height `1 / n` and suitably small
half-widths `xₙ`, whose difference quotients are small near every
point but which is not globally Hölder.

Stated but not proved: `MathlibExt.Analysis.Calculus.ScottishBook83Wanted.auerbach83_refuted` is written with `theorem_wanted` in [WantedExt/Analysis/Calculus/ScottishBook83Wanted.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/Calculus/ScottishBook83Wanted.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/pointwise-and-uniform-h-lder-conditions/index.html#auerbach83-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pointwise and uniform Hölder conditions](https://deicyde.github.io/atlas-lean/roadmap/Analysis/real-functions/continuity-and-functional-equations/pointwise-and-uniform-h-lder-conditions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/real-functions/continuity-and-functional-equations/pointwise-and-uniform-h-lder-conditions)
