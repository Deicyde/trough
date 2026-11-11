---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.Ergodic.MultipleRecurrenceWanted.furstenberg_multipleRecurrence, MathlibExt.Dynamics.Ergodic.KrylovBogolyubovWanted.krylov_bogolyubov
statement: formalized
proof: formalized
---

# Ergodic theory: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/index.html).

Ergodic theory studies measure-preserving transformations and their statistical behaviour: ergodic averages, recurrence, mixing and the structure of measure-preserving actions.

## Furstenberg multiple recurrence theorem

Let $\mu$ be a probability measure on a measurable
space $\alpha$, let $T : \alpha \to \alpha$ be a measurable map preserving $\mu$, and let $A$ be a
measurable set with $\mu(A) > 0$. For $m \in \mathbb{N}$ write $T^{-m}(A)$ for the preimage of $A$
under the $m$-th iterate of $T$. Then for every integer $k > 0$ there is an integer $n > 0$ such
that

$$\mu\Big(\bigcap_{i=0}^{k-1} T^{-i n}(A)\Big) > 0.$$

Proof: We apply the finitary Szemerédi theorem to dense sets of return times in finite orbit
segments, using an averaging argument to obtain a positive-measure family of such segments.

## Sources

- H. Furstenberg, J. Analyse Math. 31 (1977) and Recurrence in Ergodic Theory (1981); Lean states one-transformation arithmetic-progression k-term intersection form without ergodicity hypothesis.

Formalized by `MathlibExt.Dynamics.Ergodic.MultipleRecurrenceWanted.furstenberg_multipleRecurrence`, a theorem declared in [MathlibExt/Dynamics/Ergodic/MultipleRecurrence.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/Ergodic/MultipleRecurrence.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/index.html#furstenberg-multiple-recurrence).

## Krylov–Bogolyubov theorem

Every continuous map $T : X \to X$ of a nonempty compact metric
space $X$ to itself has an invariant Borel probability measure: there is a probability measure
$\mu$ on the Borel $\sigma$-algebra of $X$ whose pushforward under $T$ equals $\mu$.

## Sources

- N. M. Krylov and N. N. Bogolyubov, Ann. Math. 38 (1937), 65-113, DOI 10.2307/1968511.

Formalized by `MathlibExt.Dynamics.Ergodic.KrylovBogolyubovWanted.krylov_bogolyubov`, a theorem declared in [MathlibExt/Dynamics/Ergodic/KrylovBogolyubov.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Dynamics/Ergodic/KrylovBogolyubov.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/index.html#krylov-bogolyubov).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ergodic theory](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/ergodic-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/ergodic-theory)
