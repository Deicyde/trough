---
declaration: section
origin: cited
lean: MetaMathlibExt.IsUnboundedFamily, MetaMathlibExt.boundingNumber
statement: formalized
proof: formalized
---

# Bounding number

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/bounding-number/index.html).

## Unbounded family

A family $F$ of functions $\mathbb{N} \to \mathbb{N}$ is unbounded if no
function $g : \mathbb{N} \to \mathbb{N}$ bounds every member of $F$, where $g$ bounds $f$ if there
is an $N$ such that $f(n) \le g(n)$ for all $n \ge N$.

Formalized by `MetaMathlibExt.IsUnboundedFamily`, a definition declared in [MathlibExt/SetTheory/Cardinal/Characteristics.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Cardinal/Characteristics.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/bounding-number/index.html#is-unbounded-family).

## Bounding number

The bounding number $\mathfrak{b}$ is the infimum of the cardinalities of
all unbounded families of functions $\mathbb{N} \to \mathbb{N}$.

Formalized by `MetaMathlibExt.boundingNumber`, a definition declared in [MathlibExt/SetTheory/Cardinal/Characteristics.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Cardinal/Characteristics.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/bounding-number/index.html#bounding-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bounding number](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/cardinal-arithmetic/bounding-number/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/cardinal-arithmetic/bounding-number)
