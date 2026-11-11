---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.HahnBanachOneStepExtension.hahn_banach_one_step_extension_bound, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.norm_mkQL_apply, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.norm_mkQL_le, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_apply_eq_infDist, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_norm_one, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_of_notMem, MathlibExt.Analysis.Normed.Module.DualDistanceFormula.infDist_eq_sSup_norm_apply, MathlibExt.Analysis.FunctionalAnalysis.ScottishBook64Wanted.convexBodiesSeparatedByHyperplane
statement: formalized
---

# Hahn–Banach theorem

8 results, 7 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html).

## One-step Hahn–Banach extension

Let $E$ be a seminormed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $M$ be a subspace of $E$, let $C \ge 0$ be a real
number, and let $f \colon M \to \mathbb{K}$ be a continuous linear functional with
$\|f(m)\| \le C\|m\|$ for all $m \in M$. If $x_0 \in E$ does not lie in $M$, then $M$ is strictly
contained in $M' = M + \mathbb{K} x_0$, and there is a continuous linear functional
$g \colon M' \to \mathbb{K}$ that agrees with $f$ on $M$ and satisfies $\|g(v)\| \le C\|v\|$ for all
$v \in M'$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.HahnBanachOneStepExtension.hahn_banach_one_step_extension_bound`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/HahnBanachOneStepExtension.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/HahnBanachOneStepExtension.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#hahn-banach-one-step-extension-bound).

## Quotient seminorm equals distance to the subspace

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of
$E$, and give $E/S$ the quotient seminorm. Then for every $x \in E$ the class $q(x)$ of $x$ under
the quotient map $q \colon E \to E/S$ satisfies $\|q(x)\| = d(x, S)$, where
$d(x, S) = \inf_{s \in S} \|x - s\|$ is the distance from $x$ to $S$.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.norm_mkQL_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#norm-mk-ql-apply).

## The quotient map has norm at most one

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of $E$, and give
$E/S$ the quotient seminorm. Then the quotient map $q \colon E \to E/S$, a continuous linear map,
has operator norm $\|q\| \le 1$.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.norm_mkQL_le`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#norm-mk-ql-le).

## Hahn–Banach distance formula, attainment form

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of
$E$, not necessarily closed, and let $x \in E$. Then there is a continuous linear functional
$f \colon E \to \mathbb{K}$ with $\|f\| \le 1$ that vanishes on $S$ and satisfies
$f(x) = d(x, S)$, where $d(x, S) = \inf_{s \in S} \|x - s\|$ is the distance from $x$ to $S$.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_apply_eq_infDist`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#exists-annihilating-apply-eq-inf-dist).

## Norm-one annihilating functional at positive distance

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of
$E$, and let $x \in E$ have positive distance $d(x, S) = \inf_{s \in S} \|x - s\| > 0$ from $S$.
Then there is a continuous linear functional $f \colon E \to \mathbb{K}$ with $\|f\| = 1$ that
vanishes on $S$ and satisfies $f(x) = d(x, S)$.

A functional with $\|f\| \le 1$ that vanishes on $S$ and satisfies $f(x) = d(x, S)$ has norm
exactly $1$: for $s \in S$ we have $d(x, S) = |f(x - s)| \le \|f\| \, \|x - s\|$, and $s$ can be
chosen with $\|x - s\|$ arbitrarily close to $d(x, S) > 0$.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_norm_one`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#exists-annihilating-norm-one).

## Norm-one annihilating functional outside a closed subspace

Let $E$ be a normed space
over $\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a closed linear
subspace of $E$ and let $x \in E$ with $x \notin S$. Then there is a continuous linear functional
$f \colon E \to \mathbb{K}$ with $\|f\| = 1$ that vanishes on $S$ and satisfies
$f(x) = d(x, S)$, where $d(x, S) = \inf_{s \in S} \|x - s\|$ is the distance from $x$ to $S$.

Since $S$ is closed and $x \notin S$, the distance $d(x, S)$ is positive.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.exists_annihilating_of_notMem`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#exists-annihilating-of-not-mem).

## Hahn–Banach distance formula

Let $E$ be a normed space over $\mathbb{K}$, where
$\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a linear subspace of $E$, not
necessarily closed, and let $x \in E$. Then the distance $d(x, S) = \inf_{s \in S} \|x - s\|$
from $x$ to $S$ equals the supremum of $|f(x)|$ over all continuous linear functionals
$f \colon E \to \mathbb{K}$ with $\|f\| \le 1$ that vanish on $S$.

The supremum is attained, by the attainment form of the distance formula.

Formalized by `MathlibExt.Analysis.Normed.Module.DualDistanceFormula.infDist_eq_sSup_norm_apply`, a theorem declared in [MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/DualDistanceFormula.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#inf-dist-eq-s-sup-norm-apply).

## Separation of convex bodies at positive distance

Let $E$ be a real Banach space and let
$A, B \subseteq E$ be convex bodies, that is, convex, closed and bounded sets with nonempty
interior. If there is $\varepsilon > 0$ with $\operatorname{dist}(a, b) \ge \varepsilon$ for all
$a \in A$ and $b \in B$, then there are a nonzero continuous linear functional
$F : E \to \mathbb{R}$ and a constant $c \in \mathbb{R}$ with $F(a) \le c$ for all $a \in A$
and $c \le F(b)$ for all $b \in B$.

## Sources

- S. Mazur, Problem 64 of the Scottish Book; the theorem is true, as recorded in the typescript Ad 64 (Eidelheit, January 11, 1936), which gives the stronger statement that separation holds even for non-disjoint bodies with no common interior points. The positive-distance case follows from standard Hahn–Banach separation.

Stated but not proved: `MathlibExt.Analysis.FunctionalAnalysis.ScottishBook64Wanted.convexBodiesSeparatedByHyperplane` is written with `theorem_wanted` in [WantedExt/Analysis/FunctionalAnalysis/ScottishBook64Wanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/FunctionalAnalysis/ScottishBook64Wanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html#convex-bodies-separated-by-hyperplane).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hahn–Banach theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/hahn-banach-theorem)
