---
declaration: section
origin: cited
lean: MathlibExt.Dynamics.EinsiedlerKatokLindenstraussWanted.Dynamics.EinsiedlerKatokLindenstrauss.distToNearestInt, MathlibExt.Dynamics.EinsiedlerKatokLindenstraussWanted.Dynamics.EinsiedlerKatokLindenstrauss.einsiedler_katok_lindenstrauss
statement: formalized
---

# Littlewood conjecture

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/littlewood-conjecture/index.html).

## Distance to the nearest integer

For a real number $x$, this is $|x - r|$, where $r$
is the integer nearest to $x$ (halves rounded up); equivalently, it is the minimum of
$|x - n|$ over all integers $n$.

Formalized by `MathlibExt.Dynamics.EinsiedlerKatokLindenstraussWanted.Dynamics.EinsiedlerKatokLindenstrauss.distToNearestInt`, a definition declared in [WantedExt/Dynamics/EinsiedlerKatokLindenstraussWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/EinsiedlerKatokLindenstraussWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/littlewood-conjecture/index.html#dist-to-nearest-int).

## Einsiedler–Katok–Lindenstrauss theorem

For a real number $x$, write $\lVert x \rVert$
for the distance from $x$ to the nearest integer. The set of pairs $(\alpha, \beta)$ of real
numbers with $\liminf_{n \to \infty} n \cdot \lVert n\alpha \rVert \cdot \lVert n\beta \rVert > 0$,
the lower limit taken over natural numbers $n$, has Hausdorff dimension $0$ in $\mathbb{R}^2$.

## Sources

-. Problem `einsiedler_katok_lindenstrauss` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Dynamics.EinsiedlerKatokLindenstraussWanted.Dynamics.EinsiedlerKatokLindenstrauss.einsiedler_katok_lindenstrauss` is written with `theorem_wanted` in [WantedExt/Dynamics/EinsiedlerKatokLindenstraussWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Dynamics/EinsiedlerKatokLindenstraussWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/littlewood-conjecture/index.html#einsiedler-katok-lindenstrauss).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Littlewood conjecture](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/littlewood-conjecture/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/littlewood-conjecture)
