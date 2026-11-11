---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.FurstenbergTopologicalWanted.Dynamics.IsMultiplyRecurrent, MathlibExt.Dynamics.FurstenbergTopologicalWanted.Dynamics.furstenberg_topological_recurrence
statement: formalized
---

# Topological multiple recurrence

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/topological-multiple-recurrence/index.html).

## Multiply recurrent point

Let $X$ be a topological space and $T \colon X \to X$ a map.
A point $x \in X$ is multiply recurrent for $T$ if for every integer $d \ge 1$ there is a
strictly increasing sequence of natural numbers $(n_k)$ such that $T^{j n_k}(x) \to x$ as
$k \to \infty$ for every integer $j$ with $1 \le j \le d$, where $T^{m}$ denotes the $m$-th
iterate of $T$.

Formalized by `MathlibExt.Dynamics.FurstenbergTopologicalWanted.Dynamics.IsMultiplyRecurrent`, a definition declared in [WantedExt/Dynamics/FurstenbergTopologicalWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/FurstenbergTopologicalWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/topological-multiple-recurrence/index.html#is-multiply-recurrent).

## Furstenberg–Weiss multiple recurrence for a single homeomorphism

Every homeomorphism
$T$ of a nonempty compact metric space $X$ has a multiply recurrent point: there is a point
$x \in X$ such that for every integer $d \ge 1$ there is a strictly increasing sequence of
natural numbers $(n_k)$ with $T^{j n_k}(x) \to x$ as $k \to \infty$ for every integer $j$ with
$1 \le j \le d$, where $T^{m}$ denotes the $m$-th iterate of $T$.

## Sources

- H. Furstenberg and B. Weiss, *Topological dynamics and combinatorial number theory*, Journal d'Analyse Mathématique 34 (1978), 61-85. Listed as §56 (main theorem) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `furstenberg_topological` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.FurstenbergTopologicalWanted.Dynamics.furstenberg_topological_recurrence` is written with `theorem_wanted` in [WantedExt/Dynamics/FurstenbergTopologicalWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Dynamics/FurstenbergTopologicalWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/topological-multiple-recurrence/index.html#furstenberg-topological-recurrence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Topological multiple recurrence](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/topological-symbolic-dynamics/topological-multiple-recurrence/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Dynamics/topological-symbolic-dynamics/topological-multiple-recurrence)
