---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Module.MazurLemma.mem_closure_convexHull_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.MazurLemma.mem_closure_convexHull_range_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.MazurLemma.exists_finite_convex_combination_norm_sub_lt_of_tendsto_weakSpace, MathlibExt.Analysis.Normed.Module.MazurLemma.exists_finite_convex_combination_norm_sub_lt_of_forall_tendsto
statement: formalized
proof: formalized
---

# Mazur's lemma

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html).

## Mazur's lemma, hull form

Let $E$ be a normed space over $\mathbb{K}$, where $\mathbb{K}$
is $\mathbb{R}$ or $\mathbb{C}$, regarded also as a real vector space by restricting scalars. If
a sequence $(u_n)_{n \in \mathbb{N}}$ in $E$ converges to $x \in E$ in the weak topology of $E$
(the topology induced by the continuous $\mathbb{K}$-linear functionals on $E$), then for every
$N \in \mathbb{N}$ the point $x$ lies in the norm closure of the real convex hull of the tail
$\{u_n : n \ge N\}$.

Formalized by `MathlibExt.Analysis.Normed.Module.MazurLemma.mem_closure_convexHull_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/MazurLemma.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/MazurLemma.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html#mem-closure-convex-hull-of-tendsto-weak).

## Mazur's lemma, hull form for the whole sequence

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, regarded also as a real vector
space by restricting scalars. If a sequence $(u_n)_{n \in \mathbb{N}}$ in $E$ converges to
$x \in E$ in the weak topology of $E$ (the topology induced by the continuous $\mathbb{K}$-linear
functionals on $E$), then $x$ lies in the norm closure of the real convex hull of the set
$\{u_n : n \in \mathbb{N}\}$.

Formalized by `MathlibExt.Analysis.Normed.Module.MazurLemma.mem_closure_convexHull_range_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/MazurLemma.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/MazurLemma.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html#mem-closure-convex-hull-range-of-tendsto).

## Mazur's lemma, explicit finite convex combinations

Let $E$ be a normed space over
$\mathbb{K}$, where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, regarded also as a real vector
space by restricting scalars. If a sequence $(u_n)_{n \in \mathbb{N}}$ in $E$ converges to
$x \in E$ in the weak topology of $E$ (the topology induced by the continuous $\mathbb{K}$-linear
functionals on $E$), then for every $N \in \mathbb{N}$ and every real $\varepsilon > 0$ there are
a finite index set $I$, real weights $w_i \ge 0$ with $\sum_{i \in I} w_i = 1$ and natural
numbers $n_i \ge N$ for $i \in I$ such that
$\left\| \sum_{i \in I} w_i u_{n_i} - x \right\| < \varepsilon$.

Formalized by `MathlibExt.Analysis.Normed.Module.MazurLemma.exists_finite_convex_combination_norm_sub_lt_of_tendsto_weakSpace`, a theorem declared in [MathlibExt/Analysis/Normed/Module/MazurLemma.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/MazurLemma.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html#exists-finite-convex-combination-norm-su).

## Mazur's lemma in the textbook phrasing

Let $E$ be a normed space over $\mathbb{K}$,
where $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, regarded also as a real vector space by
restricting scalars. Let $(u_n)_{n \in \mathbb{N}}$ be a sequence in $E$ and $x \in E$ such that
$f(u_n) \to f(x)$ for every continuous $\mathbb{K}$-linear functional $f \colon E \to \mathbb{K}$.
Then for every $N \in \mathbb{N}$ and every real $\varepsilon > 0$ there are a finite index set
$I$, real weights $w_i \ge 0$ with $\sum_{i \in I} w_i = 1$ and natural numbers $n_i \ge N$ for
$i \in I$ such that $\left\| \sum_{i \in I} w_i u_{n_i} - x \right\| < \varepsilon$.

Formalized by `MathlibExt.Analysis.Normed.Module.MazurLemma.exists_finite_convex_combination_norm_sub_lt_of_forall_tendsto`, a theorem declared in [MathlibExt/Analysis/Normed/Module/MazurLemma.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Normed/Module/MazurLemma.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html#exists-finite-convex-combination-norm-su-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Mazur's lemma](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/duality-and-weak-topologies/mazur-s-lemma)
