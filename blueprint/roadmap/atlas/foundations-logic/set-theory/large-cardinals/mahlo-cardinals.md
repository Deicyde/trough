---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMahlo, MetaMathlibExt.IsWeaklyMahlo
statement: formalized
proof: formalized
---

# Mahlo cardinals

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/mahlo-cardinals/index.html).

## Mahlo cardinal

A cardinal κ is *Mahlo* if κ is inaccessible and the set {  λ < κ : λ  is inaccessible  } of
inaccessibles below κ is stationary in κ.

Formalized by `MetaMathlibExt.IsMahlo`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Mahlo.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Cardinal/LargeCardinal/Mahlo.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/mahlo-cardinals/index.html#mahlo-cardinal).

## Weakly Mahlo cardinal

A cardinal κ is *weakly Mahlo* if κ is weakly inaccessible and {  λ < κ : λ  is a regular
cardinal  } is stationary in κ.

Formalized by `MetaMathlibExt.IsWeaklyMahlo`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Mahlo.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/SetTheory/Cardinal/LargeCardinal/Mahlo.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/mahlo-cardinals/index.html#weakly-mahlo-cardinal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mahlo cardinals](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/mahlo-cardinals/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/SetTheory/large-cardinals/mahlo-cardinals)
