---
declaration: section
origin: cited
lean: MetaMathlibExt.Complexity.KeyTheorems.SharpPThresholdPSPACE.thresholdLang, MetaMathlibExt.Complexity.KeyTheorems.SharpPThresholdPSPACE.sharpP_threshold_pspace
statement: formalized
---

# Threshold languages of #P functions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/threshold-languages-of-p-functions/index.html).

## Threshold language of a counting function

For a function $f$ from bitstrings to
natural numbers, the threshold language of $f$ is the decision problem that accepts a bitstring
$y$ exactly when decoding $y$ with the canonical bitstring encoding of pairs of a bitstring and
a natural number succeeds and gives a pair $(x, k)$ with $k \le f(x)$; bitstrings that do not
decode are rejected.

Formalized by `MetaMathlibExt.Complexity.KeyTheorems.SharpPThresholdPSPACE.thresholdLang`, a definition declared in [WantedExt/Complexity/KeyTheorems/SharpPThresholdPSPACEWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SharpPThresholdPSPACEWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/threshold-languages-of-p-functions/index.html#threshold-lang).

## Threshold languages of #P functions are in PSPACE

For every function $f$ in $\#P$,
the threshold language of $f$, which accepts a bitstring exactly when it decodes, under the
canonical bitstring encoding of pairs, to a pair $(x, k)$ of a bitstring $x$ and a natural
number $k$ with $k \le f(x)$, is in PSPACE.

## Sources

- L. G. Valiant, "The complexity of enumeration and reliability problems" (1979); S. Arora and B. Barak, Computational Complexity: A Modern Approach, 2009, Theorem 9.3 (#P ⊆ PSPACE in the threshold-language form).

Stated but not proved: `MetaMathlibExt.Complexity.KeyTheorems.SharpPThresholdPSPACE.sharpP_threshold_pspace` is written with `theorem_wanted` in [WantedExt/Complexity/KeyTheorems/SharpPThresholdPSPACEWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Complexity/KeyTheorems/SharpPThresholdPSPACEWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/threshold-languages-of-p-functions/index.html#sharp-p-threshold-pspace).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Threshold languages of #P functions](https://deicyde.github.io/atlas-lean/roadmap/TheoryOfComputation/counting-complexity/threshold-languages-of-p-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/TheoryOfComputation/counting-complexity/threshold-languages-of-p-functions)
