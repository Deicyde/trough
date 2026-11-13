---
declaration: section
origin: cited
lean: MetaMathlibExt.firstDifference, MetaMathlibExt.firstDifferenceList
statement: formalized
proof: formalized
---

# First differences of binary words

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/first-differences-of-binary-words/index.html).

## First difference of an infinite binary word

For an infinite word $w = w_0 w_1 w_2 \cdots$
over $\mathbb{Z}/2\mathbb{Z}$, its first difference is the infinite word $\Delta w$ over
$\mathbb{Z}/2\mathbb{Z}$ with $(\Delta w)_i = w_{i+1} - w_i$ for every natural number $i$.

Formalized by `MetaMathlibExt.firstDifference`, a definition declared in [MathlibExt/Combinatorics/Words/FirstDifference.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FirstDifference.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/first-differences-of-binary-words/index.html#first-difference).

## First difference of a finite binary word

For a finite word $w = w_0 w_1 \cdots w_m$ over
$\mathbb{Z}/2\mathbb{Z}$, its first difference is the word
$(w_1 - w_0)(w_2 - w_1) \cdots (w_m - w_{m-1})$ of length $m$, computed in $\mathbb{Z}/2\mathbb{Z}$.
The first difference of the empty word is the empty word.

Formalized by `MetaMathlibExt.firstDifferenceList`, a definition declared in [MathlibExt/Combinatorics/Words/FirstDifference.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Words/FirstDifference.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/first-differences-of-binary-words/index.html#first-difference-list).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: First differences of binary words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/first-differences-of-binary-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/first-differences-of-binary-words)
