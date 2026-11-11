---
declaration: section
origin: cited
lean: MetaMathlibExt.IsEventuallyPeriodic, MetaMathlibExt.IsEventuallyPeriodic.of_witness, MetaMathlibExt.IsEventuallyPeriodic.witness_spec, MetaMathlibExt.IsEventuallyPeriodic.of_periodic, MetaMathlibExt.IsUltimatelyPeriodic, MetaMathlibExt.IsEventuallyPeriodic.of_finite_orbit
statement: formalized
proof: formalized
---

# Eventually periodic sequences

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html).

## Eventually periodic sequences

A sequence $u : \mathbb{N} \to \alpha$ with values in a
type $\alpha$ is eventually periodic if there are natural numbers $p > 0$ (a period) and $n_0$
(a preperiod) such that $u(n + p) = u(n)$ for every natural number $n \ge n_0$.

Formalized by `MetaMathlibExt.IsEventuallyPeriodic`, a definition declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#is-eventually-periodic).

## Explicit period and preperiod give eventual periodicity

Let $\alpha$ be a type and
$u : \mathbb{N} \to \alpha$ a sequence. If there are natural numbers $p > 0$ and $n_0$ such that
$u(n + p) = u(n)$ for every natural number $n \ge n_0$, then $u$ is eventually periodic.

Formalized by `MetaMathlibExt.IsEventuallyPeriodic.of_witness`, a theorem declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#of-witness).

## Period and preperiod of an eventually periodic sequence

Let $\alpha$ be a type. If a
sequence $u : \mathbb{N} \to \alpha$ is eventually periodic, then there are natural numbers
$p > 0$ and $n_0$ such that $u(n + p) = u(n)$ for every natural number $n \ge n_0$.

Formalized by `MetaMathlibExt.IsEventuallyPeriodic.witness_spec`, a theorem declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#witness-spec).

## Periodic sequences are eventually periodic

Let $\alpha$ be a type, let
$u : \mathbb{N} \to \alpha$ be a sequence and let $p > 0$ be a natural number with
$u(n + p) = u(n)$ for every $n \in \mathbb{N}$. Then $u$ is eventually periodic.

Formalized by `MetaMathlibExt.IsEventuallyPeriodic.of_periodic`, a theorem declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#of-periodic).

## Ultimately periodic sequences

Let $\alpha$ be a type. A sequence
$u : \mathbb{N} \to \alpha$ is called ultimately periodic exactly when it is eventually periodic;
the two terms name the same notion.

Formalized by `MetaMathlibExt.IsUltimatelyPeriodic`, an abbreviation declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#is-ultimately-periodic).

## Orbits in a finite set are eventually periodic

Let $S$ be a finite set, $F : S \to S$ a
map and $r : \mathbb{N} \to S$ a sequence with $r(n + 1) = F(r(n))$ for every $n \in \mathbb{N}$.
Then $r$ is eventually periodic.

Formalized by `MetaMathlibExt.IsEventuallyPeriodic.of_finite_orbit`, a theorem declared in [MathlibExt/Dynamics/EventuallyPeriodicSequence.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/EventuallyPeriodicSequence.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html#of-finite-orbit).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Eventually periodic sequences](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/eventually-periodic-sequences)
