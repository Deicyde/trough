---
declaration: section
origin: cited
lean: PeriodPair.fundamentalParallelogram, PeriodPair.fundamentalParallelogram_zero, PeriodPair.basis_repr_omega, PeriodPair.mem_fundamentalParallelogram_iff
statement: formalized
proof: formalized
---

# Fundamental parallelograms of complex lattices

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html).

## Fundamental parallelogram

Let $\omega_1, \omega_2$ be $\mathbb{R}$-linearly independent
complex numbers and let $\alpha \in \mathbb{C}$. The fundamental parallelogram with vertex $\alpha$
is the half-open parallelogram $\alpha + P$, where $P$ is the set of $z \in \mathbb{C}$ whose two
coordinates in the $\mathbb{R}$-basis $\omega_1, \omega_2$ of $\mathbb{C}$ both lie in $[0, 1)$;
that is, $P = \{t_1 \omega_1 + t_2 \omega_2 : t_1, t_2 \in [0, 1)\}$.

Formalized by `PeriodPair.fundamentalParallelogram`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html#fundamental-parallelogram).

## Fundamental parallelogram at the origin

Let $\omega_1, \omega_2$ be $\mathbb{R}$-linearly
independent complex numbers. The fundamental parallelogram with vertex $0$ equals the set of
$z \in \mathbb{C}$ whose two coordinates in the $\mathbb{R}$-basis $\omega_1, \omega_2$ of
$\mathbb{C}$ both lie in $[0, 1)$.

Formalized by `PeriodPair.fundamentalParallelogram_zero`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html#fundamental-parallelogram-zero).

## Coordinates in the period basis

Let $\omega_1, \omega_2$ be $\mathbb{R}$-linearly
independent complex numbers, so that they form a basis of $\mathbb{C}$ over $\mathbb{R}$. For all
real numbers $t_1, t_2$, the first coordinate of $t_1 \omega_1 + t_2 \omega_2$ in this basis is
$t_1$ and the second is $t_2$.

Formalized by `PeriodPair.basis_repr_omega`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html#basis-repr-omega).

## Membership in a fundamental parallelogram

Let $\omega_1, \omega_2$ be
$\mathbb{R}$-linearly independent complex numbers and let $\alpha, z \in \mathbb{C}$. Then $z$ lies
in the fundamental parallelogram with vertex $\alpha$ if and only if there are real numbers
$t_1, t_2$ with $0 \le t_1 < 1$ and $0 \le t_2 < 1$ such that
$z = \alpha + t_1 \omega_1 + t_2 \omega_2$.

Formalized by `PeriodPair.mem_fundamentalParallelogram_iff`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/Elliptic/FundamentalParallelogram.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html#mem-fundamental-parallelogram-iff).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fundamental parallelograms of complex lattices](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elliptic-functions/fundamental-parallelograms-of-complex-lattices)
