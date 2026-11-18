---
declaration: theorem
origin: cited
lean: Erdos1017.uniform_asymptotic_proved, Graphon.exists_cutNormDiff_limit_of_summable
statement: formalized
proof: formalized
---

# Erdős Problem 1017: clique partitions of graphs of given size

[plasma-ai/erdos-1017](https://github.com/plasma-ai/erdos-1017) at commit [cdac1d10](https://github.com/plasma-ai/erdos-1017/tree/cdac1d10ae8d69428ce17f9762e1f83303615a78), 2026-11-11.

> This Lean 4 project concerns [Erdős Problem 1017](https://www.erdosproblems.com/1017), as cataloged by Thomas F. Bloom. Let `f(n, k)` be the least number such that the edges of every graph with `n` vertices and `k` edges can be partitioned into at most `f(n, k)` cliques, a single edge counting as a clique. Erdős, Goodman and Pósa proved `f(n, k) ≤ ⌊n²/4⌋`, which the complete balanced bipartite graph attains. Erdős asked whether this bound can be sharpened when `k > n²/4`, and Bloom's catalog asks for an estimate of `f(n, k)` there.

*Quoted from [README.md](https://github.com/plasma-ai/erdos-1017/blob/cdac1d10ae8d69428ce17f9762e1f83303615a78/README.md), Apache-2.0.*

## Depends on

Its headline statements name no Mathlib concept or declaration mapped elsewhere on this site.

## Proof depends on

- [Regularity lemma](../../../combinatorics/graph-theory/regularity-lemma.md)
- [Bernoulli law](../../../probability-theory/random-variables-and-their-laws/bernoulli-law.md)
- [Conditional probability](../../../probability-theory/definitions-in-probability-theory/conditional-probability.md)
- [$L^p$ space](../../measures-and-integral-calculus/part-01/l-p-space.md)
- [Probability measure](../../../probability-theory/definitions-in-probability-theory/probability-measure.md)
- [Moment of a random variable](../../../probability-theory/random-variables-and-their-laws/moment-of-a-random-variable.md)
- [Metric space](../../../topology/metric-spaces/metric-space.md)
- [Tychonoff's theorem](../../../../thousand-plus/geometry-and-topology/54-general-topology/tychonoffs-theorem.md)

## Main results

Its Lean names are the theorems its README names in code:

- [`Erdos1017.uniform_asymptotic_proved`](https://github.com/plasma-ai/erdos-1017/blob/cdac1d10ae8d69428ce17f9762e1f83303615a78/Erdos1017/FinalAssembly.lean#L31) (theorem)
- [`Graphon.exists_cutNormDiff_limit_of_summable`](https://github.com/plasma-ai/erdos-1017/blob/cdac1d10ae8d69428ce17f9762e1f83303615a78/vendor/Graphon/Graphon/Compactness.lean#L1402) (theorem)

No file its headlines import, directly or not (1464 files), holds `sorry`, `admit` or an axiom.

## Project

- Lean v4.35.0-rc4, Mathlib at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).
- 1,467 .lean files; its Lean libraries `Graphon`, `Erdos1017`, `Challenge`, `Solution` hold 1,466, declaring 32,235 names, with `sorry` in 1 file and 0 axioms, read without Lean.
- Its own CI at this commit: passing.
- License: Apache-2.0 ([LICENSE](https://github.com/plasma-ai/erdos-1017/blob/cdac1d10ae8d69428ce17f9762e1f83303615a78/LICENSE)).

## Builds on

- Mathlib, at [1f414401](https://github.com/leanprover-community/mathlib4/tree/1f414401f69059aa7eead47b53ee40bd38455eeb).

## Placement

Of its imports of Mathlib modules in an overview area, 212 of 438 are in Analysis, 1.8 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Analysis (212 of 438 imports, 1.8×), Topology (49 of 438 imports, 1.5×), General algebra (71 of 438 imports, 0.5×). *Proof depends on* names 8 of the 62 Mathlib concepts its files name, those named most often relative to the other projects.

## Sources

- [plasma-ai/erdos-1017 at cdac1d10](https://github.com/plasma-ai/erdos-1017/tree/cdac1d10ae8d69428ce17f9762e1f83303615a78)
