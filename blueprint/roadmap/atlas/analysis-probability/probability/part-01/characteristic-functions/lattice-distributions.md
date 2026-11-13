---
declaration: section
origin: cited
lean: MathlibExt.Probability.CharFunLattice.IsLatticeRV, MathlibExt.Probability.CharFunLattice.charFun_eq_one_iff_measure_eq_one_of_lattice, MathlibExt.Probability.CharFunLattice.IsLatticeRV.exists_lattice_support
statement: formalized
proof: formalized
---

# Lattice distributions

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/lattice-distributions/index.html).

## Lattice random variable

A measure $\mu$ on $\mathbb{R}$ with characteristic function
$\varphi(t) = \int e^{itx} \, d\mu(x)$ is a lattice random variable if $\varphi(l) = 1$ for some
real $l \ne 0$ and $\varphi(t) \ne 1$ for some real $t$.

For a probability measure, the second condition says that $\mu$ is not the point mass at $0$.

Formalized by `MathlibExt.Probability.CharFunLattice.IsLatticeRV`, a definition declared in [MathlibExt/Probability/CharFunLattice.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CharFunLattice.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/lattice-distributions/index.html#is-lattice-rv).

## A characteristic function equal to one detects lattice support

Let $\mu$ be a
probability measure on $\mathbb{R}$ with characteristic function
$\varphi(t) = \int e^{itx} \, d\mu(x)$, and let $l \ne 0$ be real. Then $\varphi(l) = 1$ if and
only if $\mu$ gives mass $1$ to the lattice $\{(2\pi / l) k : k \in \mathbb{Z}\}$.

Forward direction: $\operatorname{Re} \varphi(l) = \int \cos(lx) \, d\mu(x) = 1$ forces
$\int (1 - \cos(lx)) \, d\mu(x) = 0$, hence $\cos(lx) = 1$ almost everywhere, hence
$lx \in 2\pi\mathbb{Z}$ almost everywhere. Backward direction: on the lattice the integrand
$e^{ilx}$ is identically $1$.

Formalized by `MathlibExt.Probability.CharFunLattice.charFun_eq_one_iff_measure_eq_one_of_lattice`, a theorem declared in [MathlibExt/Probability/CharFunLattice.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CharFunLattice.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/lattice-distributions/index.html#char-fun-eq-one-iff-measure-eq-one-of-la).

## Lattice random variables are supported on a lattice

Let $\mu$ be a probability measure
on $\mathbb{R}$ that is a lattice random variable. Then there is a real number $h \ne 0$ such
that $\mu$ gives mass $1$ to the lattice $\{hk : k \in \mathbb{Z}\}$.

One can take $h = 2\pi / l$ for a nonzero frequency $l$ at which the characteristic function of
$\mu$ equals $1$. The condition that the characteristic function is not identically $1$ is not
needed.

Formalized by `MathlibExt.Probability.CharFunLattice.IsLatticeRV.exists_lattice_support`, a theorem declared in [MathlibExt/Probability/CharFunLattice.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/CharFunLattice.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/lattice-distributions/index.html#exists-lattice-support).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lattice distributions](https://deicyde.github.io/atlas-lean/roadmap/Probability/characteristic-functions/lattice-distributions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/characteristic-functions/lattice-distributions)
