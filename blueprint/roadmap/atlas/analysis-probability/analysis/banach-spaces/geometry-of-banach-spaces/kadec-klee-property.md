---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_of_forall_tendsto_and_tendsto_norm, MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_of_tendsto_weakSpace_and_tendsto_norm, MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_iff_forall_tendsto_and_tendsto_norm, MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_iff_tendsto_weakSpace_and_tendsto_norm
statement: formalized
proof: formalized
---

# Kadec–Klee property

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html).

## Kadec–Klee property, all-functionals form

Let $E$ be a uniformly convex real normed
space, let $(u_n)$ be a sequence in $E$ and let $x \in E$. If $f(u_n) \to f(x)$ for every
continuous linear functional $f \colon E \to \mathbb{R}$ and $\|u_n\| \to \|x\|$, then
$u_n \to x$ in norm.

Formalized by `MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_of_forall_tendsto_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Module/KadecKlee.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/KadecKlee.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html#tendsto-of-forall-tendsto-and-tendsto-no).

## Kadec–Klee property, weak-topology form

Let $E$ be a uniformly convex real normed
space, let $(u_n)$ be a sequence in $E$ and let $x \in E$. If $u_n \to x$ in the weak topology
of $E$ (the topology induced by the continuous linear functionals $E \to \mathbb{R}$) and
$\|u_n\| \to \|x\|$, then $u_n \to x$ in norm.

Formalized by `MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_of_tendsto_weakSpace_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Module/KadecKlee.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/KadecKlee.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html#tendsto-of-tendsto-weak-space-and-tendst).

## Kadec–Klee iff, all-functionals form

Let $E$ be a uniformly convex real normed space,
let $(u_n)$ be a sequence in $E$ and let $x \in E$. Then $u_n \to x$ in norm if and only if
$f(u_n) \to f(x)$ for every continuous linear functional $f \colon E \to \mathbb{R}$ and
$\|u_n\| \to \|x\|$.

Formalized by `MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_iff_forall_tendsto_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Module/KadecKlee.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/KadecKlee.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html#tendsto-iff-forall-tendsto-and-tendsto-n).

## Kadec–Klee iff, weak-topology form

Let $E$ be a uniformly convex real normed space,
let $(u_n)$ be a sequence in $E$ and let $x \in E$. Then $u_n \to x$ in norm if and only if
$u_n \to x$ in the weak topology of $E$ (the topology induced by the continuous linear
functionals $E \to \mathbb{R}$) and $\|u_n\| \to \|x\|$.

Formalized by `MathlibExt.Analysis.Normed.Module.KadecKlee.tendsto_iff_tendsto_weakSpace_and_tendsto_norm`, a theorem declared in [MathlibExt/Analysis/Normed/Module/KadecKlee.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Module/KadecKlee.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html#tendsto-iff-tendsto-weak-space-and-tends).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kadec–Klee property](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/geometry-of-banach-spaces/kadec-klee-property)
