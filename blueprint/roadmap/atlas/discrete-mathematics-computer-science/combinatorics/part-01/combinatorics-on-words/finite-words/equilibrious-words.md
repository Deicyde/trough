---
declaration: section
origin: cited
lean: MetaMathlibExt.IsEquilibriousWord, MetaMathlibExt.isEquilibriousWord_reverse
statement: formalized
proof: formalized
---

# Equilibrious words

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/equilibrious-words/index.html).

## Equilibrious binary words

A finite word $u$ over the binary alphabet $\{0, 1\}$ is
equilibrious when the letters $0$ and $1$ occur the same number of times in $u$.

The letters $a$ and $b$ of the source alphabet $\Sigma = \{a, b\}$ are represented by $0$ and $1$.

## Sources

- <https://cs.uwaterloo.ca/journals/JIS/VOL28/Coons/coons6.tex>, lines 543–575.

Formalized by `MetaMathlibExt.IsEquilibriousWord`, a definition declared in [MathlibExt/Combinatorics/Words/EquilibriousWord.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/EquilibriousWord.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/equilibrious-words/index.html#is-equilibrious-word).

## Reversal preserves equilibrious words

A finite word $u$ over the binary alphabet
$\{0, 1\}$ is equilibrious if and only if its reversal is equilibrious.

Formalized by `MetaMathlibExt.isEquilibriousWord_reverse`, a theorem declared in [MathlibExt/Combinatorics/Words/EquilibriousWord.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/EquilibriousWord.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/equilibrious-words/index.html#is-equilibrious-word-reverse).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Equilibrious words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/equilibrious-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/equilibrious-words)
