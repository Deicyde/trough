---
declaration: section
origin: cited
lean: MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.Tantibar, MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.Mandelbar, MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.mandelbar_not_path_connected
statement: formalized
---

# Tricorn

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/tricorn/index.html).

## The antiholomorphic quadratic map

For $c \in \mathbb{C}$, the map
$T_c : \mathbb{C} \to \mathbb{C}$ is $T_c(z) = \bar z^2 + c$, where $\bar z$ is the complex
conjugate of $z$.

Formalized by `MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.Tantibar`, a definition declared in [WantedExt/Analysis/MandelbarWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbarWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/tricorn/index.html#tantibar).

## The Mandelbar set (tricorn)

The Mandelbar set is the set of $c \in \mathbb{C}$ for which
the orbit of $0$ under the map $T_c(z) = \bar z^2 + c$ is bounded: there is a real number $M$
with $|T_c^n(0)| \le M$ for all $n \ge 0$, where $T_c^n$ is the $n$-th iterate of $T_c$ and
$T_c^0$ is the identity.

This set is the connectedness locus of the family $z \mapsto \bar z^2 + c$.

Formalized by `MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.Mandelbar`, a definition declared in [WantedExt/Analysis/MandelbarWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbarWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/tricorn/index.html#mandelbar).

## The Mandelbar set is not path-connected

The Mandelbar set (tricorn), the set of
$c \in \mathbb{C}$ for which the orbit of $0$ under $z \mapsto \bar z^2 + c$ is bounded, is not
path-connected.

This is the degree-2 case of the Hubbard–Schleicher theorem that multicorns are not
path-connected.

## Sources

- John H. Hubbard and Dierk Schleicher, *Multicorns are not Path Connected*, arXiv:1209.1753 (2012); published in *Frontiers in Complex Dynamics* (Princeton University Press, 2014), pp. 73-102. Listed as §62 (additional statement 2) in O. Knill, *Some Fundamental Theorems in Mathematics* (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `mandelbar_not_path_connected` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.MandelbarWanted.ComplexAnalysis.mandelbar_not_path_connected` is written with `theorem_wanted` in [WantedExt/Analysis/MandelbarWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Analysis/MandelbarWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/tricorn/index.html#mandelbar-not-path-connected).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tricorn](https://deicyde.github.io/atlas-lean/roadmap/Dynamics/complex-dynamics/tricorn/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Dynamics/complex-dynamics/tricorn)
