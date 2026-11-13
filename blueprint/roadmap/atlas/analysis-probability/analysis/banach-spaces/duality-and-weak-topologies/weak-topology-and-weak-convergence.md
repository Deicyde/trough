---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Module.WeakConvergence.bddAbove_norm_range_of_forall_tendsto, MathlibExt.Analysis.Normed.Module.WeakConvergence.norm_le_liminf_norm_of_forall_tendsto, MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_apply_of_forall_tendsto, MathlibExt.Analysis.Normed.Module.WeakConvergence.forall_tendsto_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_weakSpace_of_forall_tendsto, MathlibExt.Analysis.Normed.Module.WeakConvergence.bddAbove_norm_range_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.WeakConvergence.norm_le_liminf_norm_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_weakSpace_apply_of_tendsto_weakSpace
statement: formalized
proof: formalized
---

# Weak topology and weak convergence

18 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html).

## Weakly convergent sequences are norm-bounded

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in $E$
and let $x \in E$. If $f(u_n) \to f(x)$ as $n \to \infty$ for every continuous linear
functional $f \colon E \to \mathbb{K}$, then the norms are bounded above: there is a real
number $C$ with $\|u_n\| \le C$ for all $n$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.bddAbove_norm_range_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#bdd-above-norm-range-of-forall-tendsto).

## Weak lower semicontinuity of the norm

Let $E$ be a normed space over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in $E$
and let $x \in E$. If $f(u_n) \to f(x)$ as $n \to \infty$ for every continuous linear
functional $f \colon E \to \mathbb{K}$, that is, $u_n$ converges weakly to $x$, then
$\|x\| \le \liminf_{n \to \infty} \|u_n\|$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.norm_le_liminf_norm_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#norm-le-liminf-norm-of-forall-tendsto).

## Bounded operators preserve weak convergence

Let $E$ and $F$ be normed spaces over
$\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T \colon E \to F$ be a continuous linear map,
let $(u_n)_{n \in \mathbb{N}}$ be a sequence in $E$ and let $x \in E$. If $f(u_n) \to f(x)$ for
every continuous linear functional $f \colon E \to \mathbb{K}$, then $g(T u_n) \to g(T x)$ for
every continuous linear functional $g \colon F \to \mathbb{K}$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_apply_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#tendsto-apply-of-forall-tendsto).

## Weak convergence gives convergence under every functional

Let $E$ be a normed space
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in
$E$ and let $x \in E$. If $u_n \to x$ in the weak topology of $E$ (the topology induced by all
continuous linear functionals $E \to \mathbb{K}$), then $f(u_n) \to f(x)$ as $n \to \infty$ for
every continuous linear functional $f \colon E \to \mathbb{K}$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.forall_tendsto_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 115](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L115). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#forall-tendsto-of-tendsto-weak-space).

## Convergence under every functional gives weak convergence

Let $E$ be a normed space
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in
$E$ and let $x \in E$. If $f(u_n) \to f(x)$ as $n \to \infty$ for every continuous linear
functional $f \colon E \to \mathbb{K}$, then $u_n \to x$ in the weak topology of $E$ (the
topology induced by all continuous linear functionals $E \to \mathbb{K}$).

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_weakSpace_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#tendsto-weak-space-of-forall-tendsto).

## Weakly convergent sequences are norm-bounded (weak topology form)

Let $E$ be a
normed space over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be
a sequence in $E$ and let $x \in E$. If $u_n \to x$ in the weak topology of $E$ (the topology
induced by all continuous linear functionals $E \to \mathbb{K}$), then there is a real number
$C$ with $\|u_n\| \le C$ for all $n$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.bddAbove_norm_range_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#bdd-above-norm-range-of-tendsto-weak-spa).

## Weak lower semicontinuity of the norm (weak topology form)

Let $E$ be a normed space
over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in
$E$ and let $x \in E$. If $u_n \to x$ in the weak topology of $E$ (the topology induced by all
continuous linear functionals $E \to \mathbb{K}$), then
$\|x\| \le \liminf_{n \to \infty} \|u_n\|$.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.norm_le_liminf_norm_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#norm-le-liminf-norm-of-tendsto-weak-spac).

## Bounded operators preserve weak convergence (weak topology form)

Let $E$ and $F$ be
normed spaces over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, let $T \colon E \to F$ be a
continuous linear map, let $(u_n)_{n \in \mathbb{N}}$ be a sequence in $E$ and let $x \in E$.
If $u_n \to x$ in the weak topology of $E$, then $T u_n \to T x$ in the weak topology of $F$;
here the weak topology of a space is the one induced by its continuous linear functionals.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakConvergence.tendsto_weakSpace_apply_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakConvergence.lean, line 147](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakConvergence.lean#L147). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#tendsto-weak-space-apply-of-tendsto-weak).

## Finitely many functionals have a common nonzero kernel vector

Finitely many continuous linear functionals on an infinite-dimensional
normed space have a common nonzero kernel vector.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.exists_ne_zero_forall_dual_apply_eq_zero`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#exists-ne-zero-forall-dual-apply-eq-zero).

## Weakly open sets contain lines through each point

Every nonempty weakly open set contains a whole line through each of its
points: if `U` is weakly open and `x ∈ U`, then `x + t • v ∈ U` for all scalars
`t` and some nonzero `v` (a common kernel vector of the finitely many
functionals constraining a basic weak neighbourhood of `x`).

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.exists_line_subset_of_isOpen`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#exists-line-subset-of-is-open).

## Weakly open sets are unbounded in infinite dimensions

Every nonempty weakly open set in an infinite-dimensional normed space is
unbounded in norm.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.exists_norm_gt_of_isOpen`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#exists-norm-gt-of-is-open).

## Open unit ball is not weakly open in infinite dimensions

The open unit ball is not weakly open in infinite dimensions.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.not_isOpen_image_ball`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#not-is-open-image-ball).

## Unit sphere is not weakly open in infinite dimensions

The unit sphere is not weakly open in infinite dimensions.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.not_isOpen_image_sphere`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 187](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L187). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#not-is-open-image-sphere).

## Weak closure of the unit sphere is the closed unit ball

In an infinite-dimensional normed space, the weak closure of the unit
sphere is the closed unit ball.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.closure_image_sphere_eq_image_closedBall`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#closure-image-sphere-eq-image-closed-bal).

## Unit sphere is not weakly closed in infinite dimensions

The unit sphere is not weakly closed in infinite dimensions: its weak
closure is the whole closed unit ball.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.not_isClosed_image_sphere`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#not-is-closed-image-sphere).

## Unit sphere is not weakly compact in infinite dimensions

The unit sphere is not weakly compact in infinite dimensions.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.not_isCompact_image_sphere`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 303](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L303). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#not-is-compact-image-sphere).

## Weak topology equals norm topology in finite dimensions

In finite dimensions the identity map from the norm topology to the weak
topology is an open map: the weak topology agrees with the norm topology.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.isOpenMap_toWeakSpaceCLM_of_finiteDimensional`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#is-open-map-to-weak-space-clm-of-finite).

## Weak topology is strictly coarser in infinite dimensions

In infinite dimensions the identity map from the norm topology to the weak
topology is not an open map: the open unit ball is norm-open but not
weakly open.

Formalized by `MathlibExt.Analysis.Normed.Module.WeakTopologyInfiniteDimensional.not_isOpenMap_toWeakSpaceCLM_of_infiniteDimensional`, a theorem declared in [MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean, line 323](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/WeakTopologyInfiniteDimensional.lean#L323). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html#not-is-open-map-to-weak-space-clm-of-inf).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Weak topology and weak convergence](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/weak-topology-and-weak-convergence)
