---
declaration: section
origin: cited
lean: NormedSpace.goldstine_finite, MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.james_reflexivity
statement: formalized
proof: formalized
---

# James' reflexivity theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/james-reflexivity-theorem/index.html).

## Finite-coordinate Goldstine theorem

Let $X$ be a real normed space, write $X^*$ for
its dual space of continuous linear functionals and $X^{**}$ for the dual of $X^*$, and let
$T \in X^{**}$ with $\|T\| \le 1$. Then for every finite set $s \subseteq X^*$ and every real
$\varepsilon > 0$ there is $x \in X$ with $\|x\| \le 1$ such that $|z(x) - T(z)| < \varepsilon$
for every $z \in s$.

Formalized by `NormedSpace.goldstine_finite`, a theorem declared in [MathlibExt/Analysis/Normed/Module/JamesReflexivity.lean, line 681](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/JamesReflexivity.lean#L681). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/james-reflexivity-theorem/index.html#goldstine-finite).

## James' reflexivity theorem

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let $E$ be a
Banach space over $\mathbb{K}$. The canonical embedding of $E$ into its bidual $E^{**}$ is
surjective if and only if every continuous linear functional $f \colon E \to \mathbb{K}$ attains
its norm on the closed unit ball, that is, there is $x \in E$ with $\|x\| \le 1$ and
$|f(x)| = \|f\|$.

Proof: The reverse implication uses the general real James convex-block argument, with Goldstine
approximation and weak-star cluster hulls. Restriction of scalars transfers the result from real
scalars to $\mathbb{K}$.

## Sources

- R. C. James, Reflexivity and the Supremum of Linear Functionals, Ann. of Math. 66 (1957), DOI 10.2307/1970122; Bourbaki form; Lean states `RCLike` Banach case with norm-attainment equivalence for reflexivity.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.BanachSpaceWanted.james_reflexivity`, a theorem declared in [MathlibExt/Analysis/Normed/Module/JamesReflexivity.lean, line 1203](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/JamesReflexivity.lean#L1203). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/james-reflexivity-theorem/index.html#james-reflexivity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: James' reflexivity theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/james-reflexivity-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/james-reflexivity-theorem)
