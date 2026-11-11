---
declaration: section
origin: cited
lean: MathlibExt.Analysis.BanachAlaogluWanted.Analysis.weakStarPolar, MathlibExt.Analysis.BanachAlaogluWanted.Analysis.banach_alaoglu_bourbaki
statement: formalized
---

# Banach–Alaoglu theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/banach-alaoglu-theorem/index.html).

## Weak-star polar

For a real topological vector space $E$ and a subset $s \subseteq E$,
the weak-star polar of $s$ is the set of continuous linear functionals $\varphi$ on $E$, viewed
as elements of the weak dual of $E$, such that $|\varphi(x)| \le 1$ for every $x \in s$.

Formalized by `MathlibExt.Analysis.BanachAlaogluWanted.Analysis.weakStarPolar`, a definition declared in [WantedExt/Analysis/BanachAlaogluWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/BanachAlaogluWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/banach-alaoglu-theorem/index.html#weak-star-polar).

## Banach–Alaoglu–Bourbaki theorem

Let $E$ be a real locally convex topological vector
space and let $U$ be a neighbourhood of $0$ in $E$. Then the weak-star polar of $U$ is compact
in the weak dual of $E$, that is, in the space of continuous linear functionals on $E$ with the
weak-star topology.

## Sources

- N. Bourbaki, Espaces vectoriels topologiques; the normed case is L. Alaoglu, Ann. of Math. 41 (1940). Listed as §137 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `banach_alaoglu_bourbaki` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.BanachAlaogluWanted.Analysis.banach_alaoglu_bourbaki` is written with `theorem_wanted` in [WantedExt/Analysis/BanachAlaogluWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/BanachAlaogluWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/banach-alaoglu-theorem/index.html#banach-alaoglu-bourbaki).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Banach–Alaoglu theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/banach-alaoglu-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/banach-alaoglu-theorem)
