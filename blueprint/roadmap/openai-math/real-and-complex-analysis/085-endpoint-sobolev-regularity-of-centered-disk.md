---
declaration: section
origin: cited
lean: OAI.SignedDisk.CenteredDiskEndpoint.main_signed_finite_band, OAI.CenteredDiskEndpoint.main_endpoint
statement: formalized
proof: formalized
---

# 085. Endpoint Sobolev regularity of centered disk averages

1 manuscript and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the planar centered-disk case of the Hajłasz–Onninen maximal-function regularity problem. For every real $f\in W^{1,1}(\mathbb R^2)$, the centered disk maximal function satisfies $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ with an absolute constant. It belongs locally to $W^{1,1}$ and has a globally integrable weak gradient.

## An Endpoint Gradient Bound for the Centered Disk Maximal Operator

We prove the endpoint gradient bound $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ for every real-valued $f\in W^{1,1}(\mathbb R^2)$, where $Mf(x)$ is the supremum of the averages of $|f|$ over disks centered at *x*, and *C* is an absolute constant. The maximal function belongs to $W^{1,1}_{\mathrm{loc}}(\mathbb R^2)$ and has a globally integrable weak gradient. This gives a positive resolution of the planar centered-disk case of the endpoint question of Hajłasz and Onninen.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/An-Endpoint-Gradient-Bound-for-the-Centered-Disk-Maximal-Operator-September-26-2026/article.pdf); the Lean below formalizes results from it.

## The Lean formalization

The centered disk maximal operator takes the supremum of averages of $|f|$ over disks centered at each point. The formalization proves that every real $f\in W^{1,1}(\mathbb R^2)$ has a maximal function that is finite almost everywhere, belongs to $W^{1,1}_{\mathrm{loc}}$, and has a globally integrable weak gradient satisfying $\|\nabla Mf\|_1\le C\|\nabla f\|_1$ for one absolute constant $C$.

The earlier signed finite-band estimate for smooth compactly supported functions is also retained. The general endpoint statement covers the Sobolev setting of the paper; a BV extension is outside these statements.

## Lean: Signed finite-band disk-maximal gradient bound

```lean
theorem main_signed_finite_band : SignedFiniteBandStatement
```

Stated in [SignedFiniteBand.lean, line 45](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/SignedFiniteBand.lean#L45). Proved in [lean/OAI/Analysis/SignedDisk/Main.lean, line 296](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/SignedDisk/Main.lean#L296). formalization.yaml lists it as one of the repository's main results.

## Lean: Endpoint gradient bound for the centered disk maximal operator

```lean
theorem main_endpoint : EndpointStatement
```

Stated in [DiskMaximal.lean, line 56](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/DiskMaximal.lean#L56). Proved in [lean/OAI/Analysis/DiskMaximal/Main.lean, line 144](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/DiskMaximal/Main.lean#L144).

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/085.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/085.md)
