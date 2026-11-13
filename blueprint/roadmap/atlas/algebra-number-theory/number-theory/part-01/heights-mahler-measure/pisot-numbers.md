---
declaration: section
origin: cited
lean: MetaMathlibExt.IsPisotNumber, MetaMathlibExt.IsUniquePisotRoot
statement: formalized
proof: formalized
---

# Pisot numbers

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/pisot-numbers/index.html).

## Pisot number

A Pisot number is a real algebraic integer greater than one whose other complex
conjugates all have norm less than one.

Formalized by `MetaMathlibExt.IsPisotNumber`, a definition declared in [MathlibExt/NumberTheory/PisotNumber.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PisotNumber.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/pisot-numbers/index.html#is-pisot-number).

## Unique Pisot root of a polynomial

Let $P$ be a polynomial with real coefficients and $r$ a
real number. Then $r$ is the unique Pisot root of $P$ when $r$ is a Pisot number with $P(r) = 0$
and every Pisot number $s$ with $P(s) = 0$ equals $r$.

Formalized by `MetaMathlibExt.IsUniquePisotRoot`, a definition declared in [MathlibExt/NumberTheory/PisotRoot.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PisotRoot.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/pisot-numbers/index.html#is-unique-pisot-root).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pisot numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/heights-mahler-measure/pisot-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/heights-mahler-measure/pisot-numbers)
