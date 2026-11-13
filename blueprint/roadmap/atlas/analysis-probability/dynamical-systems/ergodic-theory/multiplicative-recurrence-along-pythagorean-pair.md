---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.MultStructureRecurrenceWanted.conjecture, MathlibExt.Dynamics.MultStructureRecurrenceWanted.conjecture_holds
statement: formalized
---

# Multiplicative recurrence along Pythagorean pairs

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/multiplicative-recurrence-along-pythagorean-pair/index.html).

## Pythagorean-pair recurrence problem (AMR-047-0034)

The proposition that for every
probability space $(X, \mu)$ and every family $(T_a)_{a \ge 1}$, indexed by the positive integers,
of measurable bijections of $X$ with measurable inverses that preserve $\mu$, such that $T_1$ is
the identity and $T_{ab} = T_a \circ T_b$ for all positive integers $a, b$, every measurable set
$A \subseteq X$ with $\mu(A) > 0$ admits positive integers $m > n$ with

$$\mu\bigl(T_{2mn}(A) \cap T_{(m-n)(m+n)}(A)\bigr) > 0.$$

Formalized by `MathlibExt.Dynamics.MultStructureRecurrenceWanted.conjecture`, a definition declared in [WantedExt/Dynamics/MultStructureRecurrenceWanted.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/MultStructureRecurrenceWanted.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/multiplicative-recurrence-along-pythagorean-pair/index.html#conjecture).

## Multiplicative recurrence along Pythagorean pairs

Let $(X, \mu)$ be a probability space
and let $(T_a)_{a \ge 1}$, indexed by the positive integers, be measurable bijections of $X$ with
measurable inverses that preserve $\mu$, such that $T_1$ is the identity and
$T_{ab} = T_a \circ T_b$ for all positive integers $a, b$. Then for every measurable set
$A \subseteq X$ with $\mu(A) > 0$ there exist positive integers $m > n$ such that

$$\mu\bigl(T_{2mn}(A) \cap T_{(m-n)(m+n)}(A)\bigr) > 0.$$

Resolved true: Resolved by Frantzikinakis-Klurman-Moreira, Partition Regularity of Pythagorean
Pairs (arXiv:2309.10636), Theorem 2.1(i): applied with coefficients 1 and 2 to the inverse
family, it yields the two forward-image indices of AMR-047-0034. The statement is retained as a
resolved target. Source: Frantzikinakis, Klurman, Moreira, Partition Regularity of Pythagorean
Pairs, arXiv:2309.10636, Theorem 2.1(i), https://arxiv.org/abs/2309.10636. Moved from
`OpenConjectures/Dynamics/MultStructureRecurrence`.

Stated but not proved: `MathlibExt.Dynamics.MultStructureRecurrenceWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Dynamics/MultStructureRecurrenceWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/MultStructureRecurrenceWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/multiplicative-recurrence-along-pythagorean-pair/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multiplicative recurrence along Pythagorean pairs](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/multiplicative-recurrence-along-pythagorean-pair/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/ergodic-theory/multiplicative-recurrence-along-pythagorean-pair)
