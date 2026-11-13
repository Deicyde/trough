---
declaration: section
origin: cited
lean: MathlibExt.Probability.Percolation.RSWCriticalBondWanted.criticalBondMeasure, MathlibExt.Probability.Percolation.RSWCriticalBondWanted.rsw_box_crossing_lower, MathlibExt.Probability.Percolation.RSWCriticalBondWanted.rsw_box_crossing_two_sided
statement: formalized
---

# Russo–Seymour–Welsh bounds for critical bond percolation on ℤ²

3 results, 1 proved and 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per/index.html).

## Critical bond percolation measure on the square lattice

The critical bond percolation measure `ℙ_{1/2}` on `{0, 1}^{Sym2 ℤ²}`: every coordinate is
open independently with probability `1/2`.

Formalized by `MathlibExt.Probability.Percolation.RSWCriticalBondWanted.criticalBondMeasure`, an abbreviation declared in [WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per/index.html#critical-bond-measure).

## Russo–Seymour–Welsh theorem

**Russo–Seymour–Welsh theorem** (lower bound) for critical bond percolation on `ℤ²`: for
every `α > 0` there is `c > 0` with `ℙ_{1/2}(open left–right crossing of [0, ⌊αn⌋] × [0, n]) ≥ c`
for every `n`.

## Sources

- L. Russo, *A note on percolation*, Z. Wahrsch. Verw. Gebiete 43 (1978); P. D. Seymour and D. J. A. Welsh, *Percolation probabilities on the square lattice*, Ann. Discrete Math. 3 (1978); G. Grimmett, *Percolation*, 2nd ed. (1999), §11.7.

Stated but not proved: `MathlibExt.Probability.Percolation.RSWCriticalBondWanted.rsw_box_crossing_lower` is written with `theorem_wanted` in [WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per/index.html#rsw-box-crossing-lower).

## Russo–Seymour–Welsh theorem

**Russo–Seymour–Welsh theorem** (two-sided form) for critical bond percolation on `ℤ²`: for
every `α > 0` there is `c > 0` with
`c ≤ ℙ_{1/2}(open left–right crossing of [0, ⌊αn⌋] × [0, n]) ≤ 1 - c` for every `n` with
`αn ≥ 1`. The upper bound follows from the lower bound for the dual crossing.

## Sources

- L. Russo, *A note on percolation*, Z. Wahrsch. Verw. Gebiete 43 (1978); P. D. Seymour and D. J. A. Welsh, *Percolation probabilities on the square lattice*, Ann. Discrete Math. 3 (1978); G. Grimmett, *Percolation*, 2nd ed. (1999), §11.7.

Stated but not proved: `MathlibExt.Probability.Percolation.RSWCriticalBondWanted.rsw_box_crossing_two_sided` is written with `theorem_wanted` in [WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/Percolation/RSWCriticalBondWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per/index.html#rsw-box-crossing-two-sided).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Russo–Seymour–Welsh bounds for critical bond percolation on ℤ²](https://deicyde.github.io/atlas-lean/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/percolation/crossings/russo-seymour-welsh-theory/russo-seymour-welsh-bounds-for-critical-bond-per)
