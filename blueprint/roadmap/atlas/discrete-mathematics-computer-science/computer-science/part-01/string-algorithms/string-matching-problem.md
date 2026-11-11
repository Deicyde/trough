---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.StringMatching.MatchAt, Cslib.Algorithms.Lean.StringMatching.matchAt_iff, Cslib.Algorithms.Lean.StringMatching.exists_matchAt_iff_isInfix
statement: formalized
proof: formalized
---

# String matching problem

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-problem/index.html).

## Pattern match at an offset

For lists $p$ (the pattern) and $t$ (the text) over a type
$\alpha$ and a natural number $k$, the pattern $p$ matches the text $t$ at the zero-based offset
$k$ when $k$ is at most the length of $t$ and $p$ is a prefix of the list obtained from $t$ by
dropping its first $k$ entries.

The explicit bound on $k$ excludes offsets beyond the end of the text for an empty pattern.

Formalized by `Cslib.Algorithms.Lean.StringMatching.MatchAt`, a definition declared in [CSLibExt/Algorithms/Lean/StringMatching/Basic.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/Basic.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-problem/index.html#match-at).

## Characterization of a match at an offset

For lists $p$ and $t$ and a natural number $k$,
the pattern $p$ matches the text $t$ at the zero-based offset $k$ if and only if $k$ is at most
the length of $t$ and $p$ is a prefix of the list obtained from $t$ by dropping its first $k$
entries.

Formalized by `Cslib.Algorithms.Lean.StringMatching.matchAt_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Basic.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/Basic.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-problem/index.html#match-at-iff).

## A pattern occurs in a text iff it matches at some offset

For lists $p$ and $t$, there
is an offset $k$ such that the pattern $p$ matches the text $t$ at $k$ if and only if $p$ is an
infix of $t$, that is, $t$ is the concatenation of some list $u$, then $p$, then some list $v$.

Formalized by `Cslib.Algorithms.Lean.StringMatching.exists_matchAt_iff_isInfix`, a theorem declared in [CSLibExt/Algorithms/Lean/StringMatching/Basic.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/StringMatching/Basic.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-problem/index.html#exists-match-at-iff-is-infix).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: String matching problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/string-algorithms/string-matching-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/string-algorithms/string-matching-problem)
