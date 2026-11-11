---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.GolombRulersWanted.golombRulerLengths, MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength, MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_three_to_eleven, MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_twentySeven, MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_twentyEight
statement: formalized
---

# Golomb rulers

5 results, 2 proved and 3 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html).

## Golomb ruler lengths

For a natural number $m$, the set of Golomb ruler lengths with $m$
marks consists of the natural numbers $L$ for which there is a finite Sidon set $S$ of natural
numbers with $S \subseteq \{0, 1, \dots, L\}$, exactly $m$ elements, and $L \in S$. A mark at
$0$ is not required.

For finite sets of integers the Sidon condition is equivalent to all positive pairwise
differences being distinct.

Formalized by `MathlibExt.Combinatorics.GolombRulersWanted.golombRulerLengths`, a definition declared in [WantedExt/Combinatorics/GolombRulersWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GolombRulersWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html#golomb-ruler-lengths).

## Optimal Golomb ruler length

For $m \ge 1$, the optimal Golomb ruler length $G(m)$ is
the infimum in $\mathbb{N}$ of the set of Golomb ruler lengths with $m$ marks, that is, of the
natural numbers $L$ such that some $m$-element Sidon set of natural numbers contained in
$\{0, 1, \dots, L\}$ contains $L$; for $m = 0$ we set $G(0) = 0$.

For $m \ge 2$ this is OEIS A003022, the length of a shortest Golomb ruler with $m$ marks.

Formalized by `MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength`, a definition declared in [WantedExt/Combinatorics/GolombRulersWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GolombRulersWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html#optimal-golomb-length).

## Optimal Golomb rulers with 3 to 11 marks

The optimal Golomb ruler lengths with
$m = 3, 4, \dots, 11$ marks are, in order, $3, 6, 11, 17, 25, 34, 44, 55, 72$.

## Sources

- exhaustive searches; OEIS A003022; listed in leansolving/SqueezeBench `SqueezeBench/Problems/Golomb/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_three_to_eleven` is written with `theorem_wanted` in [WantedExt/Combinatorics/GolombRulersWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GolombRulersWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html#optimal-golomb-length-three-to-eleven).

## Optimal 27-mark Golomb ruler

The optimal Golomb ruler length with $27$ marks is $553$.

## Sources

- distributed.net OGR-27 exhaustive search, completed 2014; OEIS A003022; listed in SqueezeBench `SqueezeBench/Problems/Golomb/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_twentySeven` is written with `theorem_wanted` in [WantedExt/Combinatorics/GolombRulersWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GolombRulersWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html#optimal-golomb-length-twenty-seven).

## Optimal 28-mark Golomb ruler

The optimal Golomb ruler length with $28$ marks is $585$.

## Sources

- distributed.net OGR-28 exhaustive search, completed 2022; OEIS A003022; listed in SqueezeBench `SqueezeBench/Problems/Golomb/README.md`.

Stated but not proved: `MathlibExt.Combinatorics.GolombRulersWanted.optimalGolombLength_twentyEight` is written with `theorem_wanted` in [WantedExt/Combinatorics/GolombRulersWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/GolombRulersWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html#optimal-golomb-length-twenty-eight).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Golomb rulers](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/additive-combinatorics/sidon-sets-difference-sets/golomb-rulers)
