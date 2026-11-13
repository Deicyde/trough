---
declaration: section
origin: cited
lean: SymbolicDynamics.FullShift.FullShiftSpace, SymbolicDynamics.FullShift.unitShift, SymbolicDynamics.FullShift.shiftHomeomorph, SymbolicDynamics.FullShift.automorphismGroup, SymbolicDynamics.FullShift.IsOneDimensionalCA, SymbolicDynamics.FullShift.jointlyPeriodicPoints, SymbolicDynamics.FullShift.jointPeriodicCount, SymbolicDynamics.FullShift.jointPeriodicGrowthRate
statement: formalized
proof: formalized
---

# Full shift and cellular automata

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html).

## Full shift space

For $N \in \mathbb{N}$, the configuration space of the two-sided full
shift on $N$ symbols is the set $\{0, \dots, N-1\}^{\mathbb{Z}}$ of all bi-infinite sequences
$x = (x_i)_{i \in \mathbb{Z}}$ of symbols. It carries the product of the discrete topologies.

Formalized by `SymbolicDynamics.FullShift.FullShiftSpace`, an abbreviation declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#full-shift-space).

## Unit shift

The unit shift on the full shift on $N$ symbols is the map $\sigma$ from
$\{0, \dots, N-1\}^{\mathbb{Z}}$ to itself given by $(\sigma x)_i = x_{i+1}$ for all
$i \in \mathbb{Z}$, the left translation by one step.

Formalized by `SymbolicDynamics.FullShift.unitShift`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#unit-shift).

## The unit shift as a homeomorphism

The unit shift $\sigma$ of the full shift on $N$
symbols, given by $(\sigma x)_i = x_{i+1}$, is a homeomorphism of
$\{0, \dots, N-1\}^{\mathbb{Z}}$ onto itself, with inverse given by
$(\sigma^{-1} x)_i = x_{i-1}$.

Formalized by `SymbolicDynamics.FullShift.shiftHomeomorph`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#shift-homeomorph).

## Automorphism group of the full shift

The automorphism group of the full shift on $N$
symbols is the subgroup of the group of homeomorphisms of $\{0, \dots, N-1\}^{\mathbb{Z}}$ onto
itself consisting of the homeomorphisms $\varphi$ that commute with the unit shift $\sigma$,
given by $(\sigma x)_i = x_{i+1}$, that is, $\varphi \circ \sigma = \sigma \circ \varphi$.

Formalized by `SymbolicDynamics.FullShift.automorphismGroup`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#automorphism-group).

## One-dimensional cellular automaton

A map $f$ from the full shift
$\{0, \dots, N-1\}^{\mathbb{Z}}$ on $N$ symbols to itself is a one-dimensional cellular
automaton if $f$ is continuous and commutes with the unit shift $\sigma$, given by
$(\sigma x)_i = x_{i+1}$, that is, $f \circ \sigma = \sigma \circ f$.

This is the Curtis–Hedlund–Lyndon characterization of cellular automata.

Formalized by `SymbolicDynamics.FullShift.IsOneDimensionalCA`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#is-one-dimensional-ca).

## Jointly periodic points

For a map $f$ from the full shift
$\{0, \dots, N-1\}^{\mathbb{Z}}$ on $N$ symbols to itself, the jointly periodic points of $f$
are the configurations $x$ that are periodic for $f$ and periodic for the unit shift $\sigma$,
given by $(\sigma x)_i = x_{i+1}$: there are $m \ge 1$ and $n \ge 1$ with $f^m(x) = x$ and
$\sigma^n(x) = x$.

No common period for $f$ and $\sigma$ is required.

Formalized by `SymbolicDynamics.FullShift.jointlyPeriodicPoints`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#jointly-periodic-points).

## Joint periodic count

For $k \in \mathbb{N}$ and a map $f$ from the full shift
$\{0, \dots, N-1\}^{\mathbb{Z}}$ on $N$ symbols to itself, $P(f, k)$ is the number of
configurations $x$ with $\sigma^k(x) = x$, where $\sigma$ is the unit shift given by
$(\sigma x)_i = x_{i+1}$, that are also periodic for $f$, that is, $f^n(x) = x$ for some
$n \ge 1$. Here $k$ need not be the least period of $x$ under $\sigma$.

The count is the cardinality of a set, taken to be $0$ when the set is infinite, which can
happen only for $k = 0$.

Formalized by `SymbolicDynamics.FullShift.jointPeriodicCount`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#joint-periodic-count).

## Joint periodic growth rate

For a map $f$ from the full shift $S_N$ on $N$ symbols to
itself, the joint periodic growth rate is the real number

$$\nu(f, S_N) = \limsup_{k \to \infty} P(f, k)^{1/k},$$

where $k$ ranges over the positive integers and $P(f, k)$ is the joint periodic count: the
number of configurations fixed by the $k$-th power of the unit shift that are also periodic
for $f$.

Formalized by `SymbolicDynamics.FullShift.jointPeriodicGrowthRate`, a definition declared in [MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Dynamics/SymbolicDynamics/FullShift.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html#joint-periodic-growth-rate).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Full shift and cellular automata](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/full-shift-and-cellular-automata)
