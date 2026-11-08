---
declaration: theorem
origin: cited
lean: NoSmallSubgroups.of_isOpenMap
statement: formalized
proof: formalized
---

# No small subgroups under open homomorphisms

Let `G` be a topological
group, `H` a group with a topology, and `f : G →* H` an open homomorphism
whose kernel has the discrete topology induced from `G`. If `G` has no small
subgroups, then so does `H`; neither continuity of `f`, continuous operations
on `H`, nor surjectivity is required. If `f` is also continuous at the identity,
`G` has no small subgroups if and only if `H` does. See
[`NoSmallSubgroups.of_isOpenMap`](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean)
and [`MonoidHom.noSmallSubgroups_iff_of_isOpenMap`](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean).

*Quoted from the headline results in [README.md](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/README.md#headline-results) of [FormalFrontier/group-theory](https://github.com/FormalFrontier/group-theory) at commit [cad97f1a](https://github.com/FormalFrontier/group-theory/tree/cad97f1a1920e3c68d41ec2d689cde51231b5a31), Apache-2.0.*

## Depends on

No dependencies are recorded: this chapter reads the libraries' source text without running Lean, which edges between declarations need.

## Lean

- `NoSmallSubgroups.of_isOpenMap` (theorem), declared in [GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean, line 42](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean#L42).

Read from the source at commit [cad97f1a](https://github.com/FormalFrontier/group-theory/tree/cad97f1a1920e3c68d41ec2d689cde51231b5a31), without running Lean.

## Sources

- [group-theory at cad97f1a: README, headline results](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/README.md#headline-results)
- [Source of `NoSmallSubgroups.of_isOpenMap` in GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean](https://github.com/FormalFrontier/group-theory/blob/cad97f1a1920e3c68d41ec2d689cde51231b5a31/GroupTheory/Topology/Algebra/Group/NoSmallSubgroups/OpenMap.lean#L42)
