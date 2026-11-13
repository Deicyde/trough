---
declaration: section
origin: cited
lean: MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.IsCoupling, MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.primalValues, MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.DualFeasible, MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.kantorovich_duality_compact
statement: formalized
proof: formalized
---

# Kantorovich duality

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html).

## Coupling of two probability measures

Let $\mu$ and $\nu$ be probability measures on
measurable spaces $X$ and $Y$. A probability measure $\pi$ on $X \times Y$ is a coupling of
$\mu$ and $\nu$ when its marginals are $\mu$ and $\nu$, that is, when the pushforward of $\pi$
under the projection $X \times Y \to X$ is $\mu$ and the pushforward of $\pi$ under the
projection $X \times Y \to Y$ is $\nu$.

Formalized by `MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.IsCoupling`, a definition declared in [MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html#is-coupling).

## Values of the transport cost over couplings

Let $\mu$ and $\nu$ be probability measures
on measurable spaces $X$ and $Y$, and let $c : X \times Y \to \mathbb{R}$. The primal values of
$c$ for $\mu$ and $\nu$ form the set of real numbers $\int c \, d\pi$, where $\pi$ ranges over
the couplings of $\mu$ and $\nu$.

Here $\int c \, d\pi$ is the Bochner integral, which is $0$ when $c$ is not $\pi$-integrable.

Formalized by `MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.primalValues`, a definition declared in [MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html#primal-values).

## Dual feasible pair of potentials

Let $X$ and $Y$ be topological spaces and let
$c : X \times Y \to \mathbb{R}$. A pair of functions $\varphi : X \to \mathbb{R}$ and
$\psi : Y \to \mathbb{R}$ is dual feasible for the cost $c$ when $\varphi$ and $\psi$ are
continuous and $\varphi(x) + \psi(y) \le c(x, y)$ for all $x \in X$ and $y \in Y$.

Formalized by `MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.DualFeasible`, a definition declared in [MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html#dual-feasible).

## Kantorovich duality on compact metric spaces

Let $X$ and $Y$ be nonempty compact metric
spaces, each carrying its Borel $\sigma$-algebra, let $\mu$ and $\nu$ be probability measures on
$X$ and $Y$, and let $c : X \times Y \to \mathbb{R}$ be continuous. Then the infimum of
$\int c \, d\pi$ over all couplings $\pi$ of $\mu$ and $\nu$ equals the supremum of
$\int \varphi \, d\mu + \int \psi \, d\nu$ over all pairs of continuous functions
$\varphi : X \to \mathbb{R}$ and $\psi : Y \to \mathbb{R}$ such that
$\varphi(x) + \psi(y) \le c(x, y)$ for all $x \in X$ and $y \in Y$.

## Sources

- L. V. Kantorovich, On the Translocation of Masses (1942); English transl. J. Math. Sci. 133 (2006), 1381-1382, DOI 10.1007/S10958-006-0049-2; modern ref C. Villani, Topics in Optimal Transportation (2003).

Formalized by `MathlibExt.MeasureTheory.OptimalTransport.KantorovichWanted.kantorovich_duality_compact`, a theorem declared in [MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean, line 1039](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/MeasureTheory/OptimalTransport/Kantorovich.lean#L1039). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html#kantorovich-duality-compact).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kantorovich duality](https://deicyde.github.io/atlas-lean/roadmap/MeasureTheory/optimal-transport/kantorovich-duality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/MeasureTheory/optimal-transport/kantorovich-duality)
