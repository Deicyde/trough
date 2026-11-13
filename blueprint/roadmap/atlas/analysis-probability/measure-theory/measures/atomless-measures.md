---
declaration: section
origin: cited
lean: MeasureTheory.IsAtomless, MeasureTheory.isAtomless_restrict, MeasureTheory.isAtomless_exists_subset_measure_eq
statement: formalized
proof: formalized
---

# Atomless measures

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/atomless-measures/index.html).

## Atomless measure

A measure $\mu$ on a measurable space is atomless when every
measurable set $s$ with $\mu(s) > 0$ contains a measurable subset $t \subseteq s$ with
$0 < \mu(t) < \mu(s)$.

Formalized by `MeasureTheory.IsAtomless`, a definition declared in [MathlibExt/MeasureTheory/Measure/Atomless.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/Atomless.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/atomless-measures/index.html#is-atomless).

## Restriction of an atomless measure

The restriction of an atomless measure to a
measurable set is atomless.

Formalized by `MeasureTheory.isAtomless_restrict`, a theorem declared in [MathlibExt/MeasureTheory/Measure/Atomless.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/Atomless.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/atomless-measures/index.html#is-atomless-restrict).

## Sierpiński's theorem on atomless measures

Let $\mu$ be a finite atomless measure. For
every measurable set $s$ and every $t \in [0, \infty]$ with $t \le \mu(s)$, there is a measurable
set $u \subseteq s$ with $\mu(u) = t$.

Formalized by `MeasureTheory.isAtomless_exists_subset_measure_eq`, a theorem declared in [MathlibExt/MeasureTheory/Measure/Atomless.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/Measure/Atomless.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/atomless-measures/index.html#is-atomless-exists-subset-measure-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Atomless measures](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/measures/atomless-measures/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/measures/atomless-measures)
