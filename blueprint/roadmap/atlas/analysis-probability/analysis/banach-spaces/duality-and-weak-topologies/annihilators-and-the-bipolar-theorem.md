---
declaration: section
origin: cited
lean: Submodule.topologicalAnnihilator, Submodule.topologicalCoannihilator, Submodule.mem_topologicalAnnihilator, Submodule.mem_topologicalCoannihilator, Submodule.topologicalAnnihilator_anti, Submodule.topologicalCoannihilator_anti, Submodule.topologicalAnnihilator_bot, Submodule.topologicalAnnihilator_top
statement: formalized
proof: formalized
---

# Annihilators and the bipolar theorem

19 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html).

## Topological annihilator

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with continuous dual $E^*$. The topological annihilator of a subspace $S$ of $E$
is the subspace of $E^*$ consisting of the continuous linear functionals $f$ with $f(x) = 0$
for all $x \in S$.

Formalized by `Submodule.topologicalAnnihilator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator).

## Topological coannihilator

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$, with continuous dual $E^*$. The topological coannihilator of a subspace $\Phi$ of
$E^*$ is the subspace of $E$ consisting of the vectors $x$ with $f(x) = 0$ for all
$f \in \Phi$.

Formalized by `Submodule.topologicalCoannihilator`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-coannihilator).

## Membership in the topological annihilator

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $S$ be a subspace of $E$, and let
$f : E \to \mathbb{K}$ be a continuous linear functional. Then $f$ lies in the topological
annihilator of $S$ if and only if $f(x) = 0$ for every $x \in S$.

Formalized by `Submodule.mem_topologicalAnnihilator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#mem-topological-annihilator).

## Membership in the topological coannihilator

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, let $\Phi$ be a subspace of the continuous dual
of $E$, and let $x \in E$. Then $x$ lies in the topological coannihilator of $\Phi$ if and only if
$f(x) = 0$ for every $f \in \Phi$.

Formalized by `Submodule.mem_topologicalCoannihilator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#mem-topological-coannihilator).

## The topological annihilator reverses inclusion

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $S \subseteq T$ be
subspaces of $E$. Then the topological annihilator of $T$ is contained in the topological
annihilator of $S$.

Formalized by `Submodule.topologicalAnnihilator_anti`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-anti).

## The topological coannihilator is antitone

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with continuous dual $E^*$. If $\Phi \subseteq \Psi$
are subspaces of $E^*$, then the topological coannihilator of $\Psi$ is contained in the
topological coannihilator of $\Phi$.

Formalized by `Submodule.topologicalCoannihilator_anti`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 110](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L110). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-coannihilator-anti).

## Topological annihilator of the zero subspace

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$. The topological annihilator of the zero subspace
of $E$ is the whole continuous dual of $E$.

Formalized by `Submodule.topologicalAnnihilator_bot`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-bot).

## Topological annihilator of the whole space

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with continuous dual $E^*$. The topological
annihilator of $E$, viewed as a subspace of itself, is the zero subspace of $E^*$: a continuous
linear functional vanishing everywhere on $E$ is zero.

Formalized by `Submodule.topologicalAnnihilator_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-top).

## Topological coannihilator of the zero subspace

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with continuous dual $E^*$. The topological
coannihilator of the zero subspace of $E^*$ is all of $E$.

Formalized by `Submodule.topologicalCoannihilator_bot`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-coannihilator-bot).

## Topological coannihilator of the whole dual

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with continuous dual $E^*$. The topological
coannihilator of $E^*$ itself is the zero subspace of $E$: a vector killed by every continuous
linear functional is zero.

The proof uses the Hahn–Banach norming functional.

Formalized by `Submodule.topologicalCoannihilator_top`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-coannihilator-top).

## A subspace lies in its double annihilator

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$. Every subspace $S$ of $E$ is contained in the
topological coannihilator of the topological annihilator of $S$.

Formalized by `Submodule.le_topologicalCoannihilator_topologicalAnnihilator`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#le-topological-coannihilator-topological).

## Topological annihilator of the closure

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$. For every subspace $S$ of $E$, the topological
annihilator of the topological closure $\overline{S}$ equals the topological annihilator of
$S$: a continuous linear functional vanishing on $S$ vanishes on $\overline{S}$.

Formalized by `Submodule.topologicalAnnihilator_topologicalClosure`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 184](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L184). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-topological-clos).

## Separation

Let $E$ be a normed space over $\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$
or $\mathbb{C}$, let $S$ be a subspace of $E$, and let $x \in E$ lie outside the topological
closure of $S$. Then some continuous linear functional $f$ in the topological annihilator of $S$
satisfies $f(x) \neq 0$.

Formalized by `Submodule.exists_mem_topologicalAnnihilator_apply_ne_zero`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#exists-mem-topological-annihilator-apply).

## Separation, normalized

Let $E$ be a normed space over $\mathbb{K}$, where $\mathbb{K}$ is
$\mathbb{R}$ or $\mathbb{C}$, let $S$ be a subspace of $E$, and let $x \in E$ lie outside the
topological closure of $S$. Then some continuous linear functional $f$ in the topological
annihilator of $S$ satisfies $f(x) = 1$.

Formalized by `Submodule.exists_mem_topologicalAnnihilator_apply_eq_one`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#exists-mem-topological-annihilator-apply-2).

## Bipolar theorem

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$
and let $S$ be a subspace of $E$. The topological coannihilator of the topological annihilator
of $S$, that is, the subspace of vectors of $E$ killed by every continuous linear functional
vanishing on $S$, is the topological closure of $S$.

Formalized by `Submodule.topologicalAnnihilator_topologicalCoannihilator_eq_topologicalClosure`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-topological-coan).

## Density criterion via the annihilator

Let $E$ be a normed space over $\mathbb{K}$, where
$\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $S$ be a subspace of $E$. The topological
annihilator of $S$ is the zero subspace of the continuous dual of $E$ if and only if $S$ is dense
in $E$.

Formalized by `Submodule.topologicalAnnihilator_eq_bot_iff_dense`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-eq-bot-iff-dense).

## The annihilator determines the closure

Let $E$ be a normed space over $\mathbb{K}$, where
$\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $S$ and $T$ be subspaces of $E$. Then $S$ and
$T$ have the same topological annihilator if and only if they have the same topological
closure.

Formalized by `Submodule.topologicalAnnihilator_eq_iff_topologicalClosure_eq`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 253](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L253). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-eq-iff-topologic).

## Topological annihilator of a sum of subspaces

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, and let $S$ and $T$ be subspaces of $E$. The
topological annihilator of $S + T$ is the intersection of the topological annihilators of $S$
and $T$.

Formalized by `Submodule.topologicalAnnihilator_sup`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 266](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L266). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-annihilator-sup).

## Topological coannihilator of a sum of subspaces

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, with continuous dual $E^*$. For subspaces $\Phi$
and $\Psi$ of $E^*$, the topological coannihilator of their supremum $\Phi + \Psi$ is the
intersection of the topological coannihilators of $\Phi$ and $\Psi$.

Formalized by `Submodule.topologicalCoannihilator_sup`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/TopologicalAnnihilator.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html#topological-coannihilator-sup).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Annihilators and the bipolar theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/annihilators-and-the-bipolar-theorem)
