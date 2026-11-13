---
declaration: section
origin: cited
lean: MetaMathlibExt.IsWordOverlap, MetaMathlibExt.IsOverlapFreeBinaryWord
statement: formalized
proof: formalized
---

# Overlap-free words

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/overlap-free-words/index.html).

## Overlaps in words

A finite word $o$ over an alphabet $\alpha$ is an overlap if
$o = xyxyx$ for some finite words $x$ and $y$ over $\alpha$ with $x$ nonempty; $y$ may be empty.

Here $x$ may have any positive length, not only length one.

Formalized by `MetaMathlibExt.IsWordOverlap`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/OverlapFreeBinaryWord.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/OverlapFreeBinaryWord.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/overlap-free-words/index.html#is-word-overlap).

## Overlap-free binary words

A finite binary word is overlap-free when none of its
contiguous factors is an overlap.

Formalized by `MetaMathlibExt.IsOverlapFreeBinaryWord`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/OverlapFreeBinaryWord.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/OverlapFreeBinaryWord.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/overlap-free-words/index.html#is-overlap-free-binary-word).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Overlap-free words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/overlap-free-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/repetitions-in-words/overlap-free-words)
