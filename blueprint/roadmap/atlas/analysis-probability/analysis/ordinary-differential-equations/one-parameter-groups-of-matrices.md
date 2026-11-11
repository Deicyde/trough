---
declaration: section
origin: cited
lean: OneParameterGroup.IsOneParameterGroup, OneParameterGroup.IsOneParameterGroupIn, OneParameterGroup.IsOneParameterGroup.toGL, OneParameterGroup.IsOneParameterGroup.coe_toGL, OneParameterGroup.one_param_subgroup_form, OneParameterGroup.isOneParameterGroup_exp_smul
statement: formalized
proof: formalized
---

# One-parameter groups of matrices

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html).

## One-parameter group of complex matrices

For $m \in \mathbb{N}$, a map
$\varphi \colon \mathbb{R} \to M_m(\mathbb{C})$ into the complex $m \times m$ matrices is a
one-parameter group when $\varphi(0)$ is the identity matrix $I$,
$\varphi(s + t) = \varphi(s)\,\varphi(t)$ for all real $s$ and $t$, and $\varphi$ is
differentiable.

Such a map takes values in $\mathrm{GL}_m(\mathbb{C})$, since $\varphi(t)\,\varphi(-t) = I$.

Formalized by `OneParameterGroup.IsOneParameterGroup`, a structure declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#is-one-parameter-group).

## One-parameter group in a subgroup of the general linear group

Let $m \in \mathbb{N}$
and let $G$ be a subgroup of $\mathrm{GL}_m(\mathbb{C})$. A map
$\varphi \colon \mathbb{R} \to \mathrm{GL}_m(\mathbb{C})$ is a one-parameter group in $G$ when
the matrix-valued map $t \mapsto \varphi(t)$ is a one-parameter group and $\varphi(t) \in G$ for
every real $t$.

Formalized by `OneParameterGroup.IsOneParameterGroupIn`, a structure declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#is-one-parameter-group-in).

## The lift of a one-parameter group to the general linear group

Let $m \in \mathbb{N}$ and
let $\varphi \colon \mathbb{R} \to M_m(\mathbb{C})$ be a one-parameter group of complex
$m \times m$ matrices. For every real $t$ the matrix $\varphi(t)$ is invertible with inverse
$\varphi(-t)$; this gives the element of $\mathrm{GL}_m(\mathbb{C})$ with matrix $\varphi(t)$
and inverse $\varphi(-t)$.

Formalized by `OneParameterGroup.IsOneParameterGroup.toGL`, a definition declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#to-gl).

## Underlying matrix of the lift of a one-parameter group

Let $m \in \mathbb{N}$ and let
$\varphi \colon \mathbb{R} \to M_m(\mathbb{C})$ be a one-parameter group of complex $m \times m$
matrices. For every real $t$, the element of $\mathrm{GL}_m(\mathbb{C})$ assigned to $t$ by the
lift of $\varphi$ has underlying matrix $\varphi(t)$.

Formalized by `OneParameterGroup.IsOneParameterGroup.coe_toGL`, a theorem declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#coe-to-gl).

## One-parameter groups of matrices are exponentials

Let $m \in \mathbb{N}$. If
$\varphi \colon \mathbb{R} \to M_m(\mathbb{C})$ is a one-parameter group of complex $m \times m$
matrices, then there is a unique matrix $A \in M_m(\mathbb{C})$ such that
$\varphi(t) = \exp(tA)$ for every real $t$.

Formalized by `OneParameterGroup.one_param_subgroup_form`, a theorem declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 103](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L103). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#one-param-subgroup-form).

## Exponential curves are one-parameter groups

For every $m \in \mathbb{N}$ and every
complex $m \times m$ matrix $A$, the map $t \mapsto \exp(tA)$ from $\mathbb{R}$ to the complex
$m \times m$ matrices is a one-parameter group.

Formalized by `OneParameterGroup.isOneParameterGroup_exp_smul`, a theorem declared in [MathlibExt/Analysis/ODE/OneParameterGroup.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/ODE/OneParameterGroup.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html#is-one-parameter-group-exp-smul).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: One-parameter groups of matrices](https://deicyde.github.io/atlas-lean/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/ordinary-differential-equations/one-parameter-groups-of-matrices)
