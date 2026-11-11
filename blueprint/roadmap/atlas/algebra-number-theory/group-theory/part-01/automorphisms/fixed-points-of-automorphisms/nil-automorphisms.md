---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.delta, MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.IsNilAutomorphism, MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.IsEAutomorphism, MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.eAutomorphismIsNil, MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.eAutomorphismIsNil_refuted
statement: formalized
---

# Nil-automorphisms

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html).

## The commutator of an element with an automorphism

For an automorphism $\varphi$ of a
group $G$ and $x \in G$, $\delta_\varphi(x) = x^{-1} \varphi(x)$. This is the commutator
$[x, \varphi]$ in the Kourovka convention $[x, y] = x^{-1} y^{-1} x y$, with $\varphi$ acting as
$x \mapsto \varphi(x)$; the iterates $\delta_\varphi^n(x)$ are the iterated commutators
$[x, {}_n \varphi]$, with $[x, {}_0 \varphi] = x$.

Formalized by `MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.delta`, a definition declared in [WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html#delta).

## Nil-automorphisms

An automorphism $\varphi$ of a group $G$ is a nil-automorphism if for
every $a \in G$ there is $n \ge 0$ with $\delta_\varphi^n(a) = 1$, where
$\delta_\varphi(x) = x^{-1} \varphi(x)$; that is, some iterated commutator $[a, {}_n \varphi]$ is
trivial.

Formalized by `MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.IsNilAutomorphism`, a definition declared in [WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html#is-nil-automorphism).

## $e$-automorphisms

An automorphism $\varphi$ of a group $G$ is an $e$-automorphism if for
any two subgroups $A$ and $B$ of $G$ with $\varphi(A) = A$, $\varphi(B) = B$ and
$A \not\subseteq B$, some $a \in A \setminus B$ has $[a, \varphi] = a^{-1} \varphi(a) \in B$.

Formalized by `MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.IsEAutomorphism`, a definition declared in [WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html#is-eautomorphism).

## Vilyatser's question on $e$-automorphisms (Kourovka 11.23)

The proposition that every
$e$-automorphism $\varphi$ of a group $G$ is a nil-automorphism of $G$.

Formalized by `MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.eAutomorphismIsNil`, a definition declared in [WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html#e-automorphism-is-nil).

## An $e$-automorphism need not be a nil-automorphism

Vilyatser's assertion in Kourovka
Problem 11.23 is false: there are a group $G$ and an automorphism $\varphi$ of $G$ that is an
$e$-automorphism (for any subgroups $A$ and $B$ of $G$ with $\varphi(A) = A$, $\varphi(B) = B$ and
$A \not\subseteq B$, some $a \in A \setminus B$ has $a^{-1} \varphi(a) \in B$) but not a
nil-automorphism: writing $\delta(x) = x^{-1} \varphi(x)$, some $a \in G$ has $\delta^n(a) \ne 1$
for every $n \ge 0$.

Muliarchyk shows that the cyclic shift of order four on the fourth direct power of the first
Grigorchuk group is such an automorphism, using Bartholdi's characterization of the Engel elements
of the Grigorchuk group; the preprint states that the work was carried out with assistance from
ChatGPT. The Kourovka Notebook (21st issue) marks 11.23 solved, "No, not every".

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 11.23 (V. G. Vilyatser); resolution: K. Muliarchyk, An e-automorphism that is not a nil-automorphism, preprint (2026), main theorem: the cyclic shift `(g₀, g₁, g₂, g₃) ↦ (g₁, g₂, g₃, g₀)` on `Γ⁴`, `Γ` the first Grigorchuk group, is an `e`-automorphism of order four and not a nil-automorphism; the Kourovka Notebook (21st issue) marks 11.23 solved, https://kourovkanotebookorg.wordpress.com/wp-content/uploads/2026/09/kourovka_11_23_solution.pdf.

Stated but not proved: `MathlibExt.GroupTheory.EAutomorphismNilAutomorphismKourovka11Problem23Wanted.eAutomorphismIsNil_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/EAutomorphismNilAutomorphismKourovka11Problem23Wanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html#e-automorphism-is-nil-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Nil-automorphisms](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/automorphisms/fixed-points-of-automorphisms/nil-automorphisms)
