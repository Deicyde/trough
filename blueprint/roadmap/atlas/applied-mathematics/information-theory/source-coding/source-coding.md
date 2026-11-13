---
declaration: section
origin: cited
lean: MathlibExt.InformationTheory.KraftMcMillan.kraft_mcmillan_lengths
statement: formalized
proof: formalized
---

# Source coding: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/index.html).

Lossless compression of information sources by variable-length codes, including prefix codes, the Kraft–McMillan inequality and Shannon's source coding bounds.

## Kraft's inequality for prefix codes

Let $\alpha$ be a finite set of source symbols,
let $\beta$ be a finite alphabet with $D \ge 2$ letters, and let $l : \alpha \to \mathbb{N}$.
There is a prefix-free code assigning to each $a \in \alpha$ a word over $\beta$ of length
$l(a)$ if and only if $\sum_{a \in \alpha} D^{-l(a)} \le 1$.

Formalized by `MathlibExt.InformationTheory.KraftMcMillan.kraft_mcmillan_lengths`, a theorem declared in [MathlibExt/InformationTheory/KraftMcMillan.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/InformationTheory/KraftMcMillan.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/index.html#kraft-mcmillan-lengths).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Source coding](https://deicyde.github.io/atlas-lean/roadmap/InformationTheory/source-coding/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/InformationTheory/source-coding)
