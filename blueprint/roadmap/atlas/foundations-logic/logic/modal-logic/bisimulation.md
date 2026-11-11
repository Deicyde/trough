---
declaration: section
origin: cited
lean: Cslib.Modal.Bisimulation, Cslib.Modal.Bisimulation.satisfies_iff, Cslib.Modal.Bisimulation.Bisimilar, Cslib.Modal.Bisimulation.Bisimilar.satisfies_iff
statement: formalized
proof: formalized
---

# Bisimulation

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html).

## Modal

## Bisimulation

Let $M$ and $N$ be Kripke models over the same atoms, with sets of
worlds $W$ and $V$ and accessibility relations $R_M$ and $R_N$. A relation
$Z \subseteq W \times V$ is a bisimulation between $M$ and $N$ when, for all $w \in W$ and
$v \in V$ with $w \mathrel{Z} v$: each atom $a$ is true at $w$ in $M$ if and only if $a$ is
true at $v$ in $N$; for every $w'$ with $w \mathrel{R_M} w'$ there is $v'$ with
$v \mathrel{R_N} v'$ and $w' \mathrel{Z} v'$ (forth); and for every $v'$ with
$v \mathrel{R_N} v'$ there is $w'$ with $w \mathrel{R_M} w'$ and $w' \mathrel{Z} v'$ (back).

Formalized by `Cslib.Modal.Bisimulation`, a structure declared in [CSLibExt/Logics/Modal/Bisimulation.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Bisimulation.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html#bisimulation).

## Bisimulations preserve modal formulas

Let $Z$ be a bisimulation between Kripke models
$M$ and $N$ over the same atoms. If $Z$ relates a world $w$ of $M$ to a world $v$ of $N$, then
every modal formula $\varphi$ is satisfied at $w$ in $M$ if and only if $\varphi$ is satisfied
at $v$ in $N$.

Formalized by `Cslib.Modal.Bisimulation.satisfies_iff`, a theorem declared in [CSLibExt/Logics/Modal/Bisimulation.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Bisimulation.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html#satisfies-iff).

## Bisimilar worlds

Let $M$ and $N$ be Kripke models over the same atoms. A world $w$ of
$M$ and a world $v$ of $N$ are bisimilar if some bisimulation between $M$ and $N$ relates $w$
to $v$.

Formalized by `Cslib.Modal.Bisimulation.Bisimilar`, a definition declared in [CSLibExt/Logics/Modal/Bisimulation.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Bisimulation.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html#bisimilar).

## Bisimilar worlds are modally equivalent

If a world $w$ of a Kripke model $M$ and a world
$v$ of a Kripke model $N$ over the same atoms are bisimilar, then every modal formula $\varphi$
is satisfied at $w$ in $M$ if and only if $\varphi$ is satisfied at $v$ in $N$.

Formalized by `Cslib.Modal.Bisimulation.Bisimilar.satisfies_iff`, a theorem declared in [CSLibExt/Logics/Modal/Bisimulation.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Logics/Modal/Bisimulation.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html#satisfies-iff-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bisimulation](https://deicyde.github.io/atlas-lean/roadmap/Logic/modal-logic/bisimulation/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Logic/modal-logic/bisimulation)
