---
declaration: section
origin: cited
lean: CharacterTheory.irred_dim_dvd_card, MathlibExt.GroupTheory.MaschkeDecomposition.maschke_decomposition
statement: formalized
proof: formalized
---

# Representations of finite groups: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/index.html).

Ordinary representation theory of finite groups over algebraically closed fields of characteristic zero: characters, irreducibility, Schur's lemma, multiplicities and the Wedderburn decomposition of the group algebra.

## Dimension of an irreducible representation divides the group order

If `ρ` is an irreducible representation of a finite group `G` over an
algebraically closed field `k` of characteristic zero, then
`dim_k ρ ∣ |G|`. In particular, over `ℂ`, every irreducible degree divides
the order of the group.

Formalized by `CharacterTheory.irred_dim_dvd_card`, a theorem declared in [MathlibExt/RepresentationTheory/IrreducibleDimension.lean, line 314](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RepresentationTheory/IrreducibleDimension.lean#L314). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/index.html#irred-dim-dvd-card).

## Maschke's theorem

Every finite-dimensional complex representation $\sigma$ of a finite
group is equivalent to the direct sum of a finite family of irreducible subrepresentations of
$\sigma$.

Formalized by `MathlibExt.GroupTheory.MaschkeDecomposition.maschke_decomposition`, a theorem declared in [MathlibExt/GroupTheory/MaschkeDecomposition.lean, line 219](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/MaschkeDecomposition.lean#L219). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/index.html#maschke-decomposition).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Representations of finite groups](https://deicyde.github.io/atlas-lean/roadmap/RepresentationTheory/finite-group-representations/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RepresentationTheory/finite-group-representations)
