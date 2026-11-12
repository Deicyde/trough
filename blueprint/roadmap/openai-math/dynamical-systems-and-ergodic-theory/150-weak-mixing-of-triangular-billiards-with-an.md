---
declaration: section
origin: cited
lean: OAI.TriangularBilliards.irrational_triangle_billiard
statement: formalized
proof: formalized
---

# 150. Weak mixing of triangular billiards with an irrational angle

2 manuscripts and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to *π* is weakly mixing for normalized area times uniform direction. This strengthens ergodicity on the entire irrational-angle class, with no genericity or Diophantine restrictions.

## Weak mixing of triangular billiards with an irrational angle

We prove that the unit-speed billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to *π* is weakly mixing for normalized Liouville measure. Equivalently, the product of the flow with itself is ergodic.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Weak-mixing-of-triangular-billiards-with-an-irrational-angle-October-5-2026/weak-mixing-triangular-billiards.pdf).

## Ergodicity of triangular billiards with an irrational angle

We prove that the unit-speed billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to *π* is ergodic for normalized area times uniform angular measure. No genericity or Diophantine condition is required. The flow is considered outside the null set of trajectories that hit a vertex.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026/Ergodicity-of-triangular-billiards-with-an-irrational-angle-September-25-2026.pdf); the Lean below formalizes results from it.

## The Lean formalization

The formalization proves that the unit-speed billiard flow in every nondegenerate Euclidean triangle with at least one angle irrational relative to $\pi$ is ergodic for normalized area times uniform angular measure. It constructs the flow outside the null set of exceptional trajectories, proves uniqueness of the flight chain there, and establishes measure preservation and the flow law almost everywhere. No genericity or Diophantine condition on the irrational angle is assumed.

## Lean: Ergodicity of triangular billiards with an irrational angle

Stated in [IrrationalTriangleBilliard.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/IrrationalTriangleBilliard.lean).

```lean
theorem irrational_triangle_billiard (Q : Triangle) (hQ : Q.HasIrrationalAngle) :
    MainConclusion Q
```

Proved in [lean/OAI/Dynamics/TriangleBilliards/Main.lean, line 418](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Dynamics/TriangleBilliards/Main.lean#L418).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/150.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/150.md)
