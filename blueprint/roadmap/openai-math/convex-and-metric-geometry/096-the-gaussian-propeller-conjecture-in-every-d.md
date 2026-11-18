---
declaration: section
origin: cited
lean: OAI.GaussianPropeller.all_partitions
statement: formalized
proof: formalized
---

# 096. The Gaussian propeller conjecture in every dimension

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the sum of squared Gaussian first moments of any finite measurable partition is at most $9/(8\pi)$. In dimension at least two, three planar sectors of angle $2\pi/3$, extended orthogonally, attain the bound. Combined with the separate Unique Games theorem, this proves NP-hardness of improving the loss factor $(8\pi/9)(1-1/k)$ for identity-target kernel clustering with fixed *k* ≥ 3 on rational centered positive semidefinite inputs.

## The Gaussian propeller bound in every dimension

We prove the Gaussian propeller conjecture: for every finite measurable partition of a Euclidean space, the sum of the squared lengths of its Gaussian first moments is at most $9/(8\pi)$. For dimension at least two and at least three cells, three planar sectors of angle $2\pi/3$, extended by an orthogonal Euclidean factor, attain the bound.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/The-Gaussian-Propeller-Bound-in-Every-Dimension-September-24-2026/main.pdf); the Lean below formalizes results from it.

## The Lean formalization

The Gaussian propeller problem asks how large the sum of squared Gaussian first moments can be over a partition. The formalized result proves the sharp bound $9/(8\pi)$ for every positive dimension and every positive number of labelled cells, allowing empty cells and arbitrary masses. In dimension at least two with at least three cells, three planar sectors of angle $120^\circ$, extended in orthogonal directions, attain equality. The separate Gaussian-maxima and kernel-clustering consequences are not included.

## Lean: Gaussian propeller bound and attainment

```lean
theorem all_partitions : AllPartitions
```

Stated in [GaussianPropeller.lean, line 38](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/GaussianPropeller.lean#L38). Proved in [lean/OAI/Probability/GaussianPropeller/Main.lean, line 78](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Probability/GaussianPropeller/Main.lean#L78). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/096.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/096.md)
