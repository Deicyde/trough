---
declaration: section
origin: cited
lean: MathlibExt.Topology.Algebra.BirkhoffKakutani.birkhoff_kakutani_metrization, IsLocallyConstant.exists_isOpen_one_mem_forall_mul_eq_of_hasCompactSupport
statement: formalized
proof: formalized
---

# Topological groups: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/index.html).

Groups carrying a compatible topology: metrizability, profinite groups and profinite completions, and functions on locally compact groups.

## Birkhoff–Kakutani metrization theorem

Every Hausdorff first-countable topological group is
metrizable.

## Sources

- G. Birkhoff, Compositio Math. 3 (1936), 427-430; S. Kakutani, Proc. Imp. Acad. Tokyo 12 (1936), 4-7, DOI 10.3792/PIA/1195580206.

Formalized by `MathlibExt.Topology.Algebra.BirkhoffKakutani.birkhoff_kakutani_metrization`, a theorem declared in [MathlibExt/Topology/Algebra/BirkhoffKakutani.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/Algebra/BirkhoffKakutani.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/index.html#birkhoff-kakutani-metrization).

## Locally constant compactly supported functions have uniform stabilizers

A locally constant compactly supported function on a topological group is
invariant under left and right multiplication by elements of some open
neighborhood of `1`.

Formalized by `IsLocallyConstant.exists_isOpen_one_mem_forall_mul_eq_of_hasCompactSupport`, a theorem declared in [MathlibExt/Topology/LocallyConstant.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Topology/LocallyConstant.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/index.html#exists-is-open-one-mem-forall-mul-eq-of).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topological groups](https://deicyde.github.io/atlas-lean/roadmap/Topology/topological-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Topology/topological-groups)
