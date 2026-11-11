---
declaration: section
origin: cited
lean: MetaMathlibExt.IsMeasurable, MetaMathlibExt.IsWeaklyCompact
statement: formalized
proof: formalized
---

# Large cardinals: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/index.html).

Cardinals with strong closure or reflection properties, such as inaccessible, Mahlo, weakly compact and measurable cardinals, whose existence cannot be proved in ZFC.

## Measurable cardinal

A cardinal κ is *measurable* if κ > ℵ₀ and there is a
set I with |I| = κ carrying an ultrafilter U on I which is

1. *κ-complete*: for every family 𝒮 ⊆ U with |𝒮| < κ we have ⋂ 𝒮 ∈ U; and
1. *nonprincipal*: every cofinite subset of I belongs to U --- equivalently, since U is an
   ultrafilter, no finite subset of I belongs to U.

Formalized by `MetaMathlibExt.IsMeasurable`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/Measurable.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/Measurable.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/index.html#measurable-cardinal).

## Weakly compact cardinal

A cardinal $\kappa$ is *weakly compact* if $\aleph_0 < \kappa$
and $\kappa \to (\kappa)^2_2$: for every set $I$ of cardinality $\kappa$ and every colouring $c$
of the finite subsets of $I$ with two colours, there are a subset $H \subseteq I$ of cardinality
$\kappa$ and a colour $k$ such that $c(s) = k$ for every two-element subset $s \subseteq H$.

Formalized by `MetaMathlibExt.IsWeaklyCompact`, a definition declared in [MathlibExt/SetTheory/Cardinal/LargeCardinal/WeaklyCompact.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/SetTheory/Cardinal/LargeCardinal/WeaklyCompact.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/index.html#is-weakly-compact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large cardinals](https://deicyde.github.io/atlas-lean/roadmap/SetTheory/large-cardinals/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/SetTheory/large-cardinals)
