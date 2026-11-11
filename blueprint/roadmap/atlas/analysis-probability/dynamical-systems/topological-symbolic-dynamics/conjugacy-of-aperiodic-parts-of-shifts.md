---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.AMR43Problem1Wanted.X, MathlibExt.Dynamics.AMR43Problem1Wanted.YAmb, MathlibExt.Dynamics.AMR43Problem1Wanted.Y, MathlibExt.Dynamics.AMR43Problem1Wanted.AperiodicX, MathlibExt.Dynamics.AMR43Problem1Wanted.AperiodicY, MathlibExt.Dynamics.AMR43Problem1Wanted.shiftXRes, MathlibExt.Dynamics.AMR43Problem1Wanted.shiftYRes, MathlibExt.Dynamics.AMR43Problem1Wanted.conjecture
statement: formalized
---

# Conjugacy of aperiodic parts of shifts

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html).

## The full 2-shift

$X$ is the space of all two-sided sequences
$x = (x_i)_{i \in \mathbb{Z}}$ with every $x_i \in \{0, 1\}$, carrying the product topology.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.X`, an abbreviation declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#x).

## The full 3-shift

The space of all two-sided sequences $y = (y_i)_{i \in \mathbb{Z}}$
with every $y_i \in \{0, 1, 2\}$, carrying the product topology. It is the ambient space of the
proper 3-colouring shift.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.YAmb`, an abbreviation declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#yamb).

## The proper 3-colouring shift

$Y$ is the set of sequences $y = (y_i)_{i \in \mathbb{Z}}$
in the full 3-shift (so every $y_i \in \{0, 1, 2\}$) such that $y_i \ne y_{i+1}$ for every
$i \in \mathbb{Z}$.

It is a mixing shift of finite type.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.Y`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#y).

## Aperiodic part of the full 2-shift

Let $\sigma$ be the left shift on the full 2-shift
$X$, given by $(\sigma x)_i = x_{i+1}$. The aperiodic part of $X$ is the set of all $x \in X$
that are not periodic for $\sigma$, that is, with $\sigma^n x \ne x$ for every $n \ge 1$.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.AperiodicX`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#aperiodic-x).

## Aperiodic part of the 3-colouring shift

Let $\sigma$ be the left shift on the full
3-shift, given by $(\sigma y)_i = y_{i+1}$. The aperiodic part of the proper 3-colouring shift
$Y$ is the set of all $y \in Y$ that are not periodic for $\sigma$, that is, with
$\sigma^n y \ne y$ for every $n \ge 1$.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.AperiodicY`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#aperiodic-y).

## Shift on the aperiodic part of the full 2-shift

The left shift $\sigma$, given by
$(\sigma x)_i = x_{i+1}$, maps the aperiodic part of the full 2-shift $X$ into itself; this is
the self-map of the aperiodic part of $X$ obtained by restricting $\sigma$ to it.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.shiftXRes`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#shift-xres).

## Shift on the aperiodic part of the 3-colouring shift

The left shift $\sigma$, given by
$(\sigma y)_i = y_{i+1}$, maps the aperiodic part of the proper 3-colouring shift $Y$ into
itself; this is the self-map of the aperiodic part of $Y$ obtained by restricting $\sigma$
to it.

## Sources

- [AMR-043-0001].

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.shiftYRes`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#shift-yres).

## Hochman's aperiodic conjugacy question

Let $X$ be the full 2-shift and $Y$ the proper
3-colouring shift, write $X \setminus \mathrm{Per}(X)$ and $Y \setminus \mathrm{Per}(Y)$ for
their aperiodic parts with the subspace topologies, and let $\sigma$ be the left shift
$(\sigma z)_i = z_{i+1}$ on each. The statement is that there is a homeomorphism
$e \colon X \setminus \mathrm{Per}(X) \to Y \setminus \mathrm{Per}(Y)$ with
$e(\sigma a) = \sigma(e(a))$ for every $a \in X \setminus \mathrm{Per}(X)$, that is, the two
aperiodic parts are topologically conjugate.

## Sources

- [AMR-043-0001] Hochman problem 1.

Formalized by `MathlibExt.Dynamics.AMR43Problem1Wanted.conjecture`, a definition declared in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#conjecture).

## The aperiodic parts of the full 2-shift and the 3-colouring shift are not conjugate

Let $X$ be the full 2-shift, $Y$ the proper 3-colouring shift, and $\sigma$ the left shift on
each. There is no homeomorphism $e$ from the aperiodic part of $X$ onto the aperiodic part of
$Y$, each with the subspace topology, such that $e(\sigma a) = \sigma(e(a))$ for every $a$ in the
aperiodic part of $X$; that is, Hochman's aperiodic conjugacy question has a negative answer.

Salo proves that every conjugacy between infinite transitive shifts of finite type minus
periodic points extends to a conjugacy of the shifts of finite type; since the full 2-shift
has fixed points and the proper 3-colouring shift has none, the aperiodic parts are not
conjugate.

## Sources

- Ville Salo, Conjugacy of transitive SFTs minus periodic points, Proc. London Math. Soc. (accepted; arXiv v3 2023), arXiv:2104.09860, https://arxiv.org/abs/2104.09860.

Stated but not proved: `MathlibExt.Dynamics.AMR43Problem1Wanted.conjecture_refuted` is written with `theorem_wanted` in [WantedExt/Dynamics/AMR43Problem1Wanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/AMR43Problem1Wanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html#conjecture-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Conjugacy of aperiodic parts of shifts](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/conjugacy-of-aperiodic-parts-of-shifts)
