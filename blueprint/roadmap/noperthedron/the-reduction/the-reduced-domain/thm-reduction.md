---
declaration: theorem
origin: cited
lean: Cayley.reduction
statement: formalized
proof: formalized
---

# Reduction

If $\operatorname{\mathbf{P}}$ is Rupert, then there is a reduced $(u, v, j, r)$ such that $\bigl(s(u, v),\ s(u, v)\, Q_j(r)\bigr)$ is a Rupert pair.

## Depends on

- [exists_rup_pair](../../rupert-pairs/shadows-and-the-separation-criterion/lem-exists-rup-pair.md)
- [step_outer](../step-a-the-outer-view/lem-step-outer.md)
- [step_orbit](../step-b-the-relative-rotation/lem-step-orbit.md)
- [step_chart](../step-c-the-chart/lem-step-chart.md)
- [reduced](def-reduced.md)

## Proof

Lemma [exists_rup_pair](../../rupert-pairs/shadows-and-the-separation-criterion/lem-exists-rup-pair.md) gives a Rupert pair in $SO(3)$. Apply Step A (Lemma [step_outer](../step-a-the-outer-view/lem-step-outer.md)), then Step B (Lemma [step_orbit](../step-b-the-relative-rotation/lem-step-orbit.md)) to the relative rotation, then Step C (Lemma [step_chart](../step-c-the-chart/lem-step-chart.md)) to the orbit-maximal $Q$. Step C does not change $Q$, so the orbit condition persists.

## Lean

Formalized as [`Cayley.reduction`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.reduction).

## Sources

- [Noperthedron blueprint: chapters/reduction.tex, line 238](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/reduction.tex#L238)
