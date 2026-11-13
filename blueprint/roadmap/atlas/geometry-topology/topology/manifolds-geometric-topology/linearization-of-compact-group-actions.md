---
declaration: section
origin: cited
lean: MathlibExt.Topology.ScottishBook183Wanted.ScottishBookProblem183Claim, MathlibExt.Topology.ScottishBook183Wanted.bogolyubov183_refuted
statement: formalized
---

# Linearization of compact group actions

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearization-of-compact-group-actions/index.html).

## Bogolyubov's linearization claim (Scottish Book Problem 183)

The claim that for every
$n \in \mathbb{N}$ and every compact, connected, locally connected topological group $G$ acting
on $\mathbb{R}^n$ with continuous action map $G \times \mathbb{R}^n \to \mathbb{R}^n$, there is a
homeomorphism $\varphi$ of $\mathbb{R}^n$ such that for every $g \in G$ there is a linear map
$L_g \colon \mathbb{R}^n \to \mathbb{R}^n$ with $\varphi(g \cdot x) = L_g(\varphi(x))$ for all
$x \in \mathbb{R}^n$.

This is Bogolyubov's problem in its original form: coordinates can be introduced in which every
transformation of the group is linear.

Formalized by `MathlibExt.Topology.ScottishBook183Wanted.ScottishBookProblem183Claim`, a definition declared in [WantedExt/Topology/ScottishBook183Wanted.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook183Wanted.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearization-of-compact-group-actions/index.html#scottish-book-problem183-claim).

## Bogolyubov's Problem 183 has a negative answer

Bogolyubov's linearization claim is false:
there are $n \in \mathbb{N}$ and a compact, connected, locally connected topological group $G$
acting continuously on $\mathbb{R}^n$ such that for no homeomorphism $\varphi$ of $\mathbb{R}^n$
is every map $\varphi \circ g \circ \varphi^{-1}$, for $g \in G$, linear.

## Sources

- N. N. Bogolyubov, Problem 183 of the Scottish Book; see the commentary in R. D. Mauldin (ed.), The Scottish Book, 2nd ed. (Birkhäuser, 2015).

Stated but not proved: `MathlibExt.Topology.ScottishBook183Wanted.bogolyubov183_refuted` is written with `theorem_wanted` in [WantedExt/Topology/ScottishBook183Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Topology/ScottishBook183Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearization-of-compact-group-actions/index.html#bogolyubov183-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linearization of compact group actions](https://deicyde.github.io/atlas-lean/roadmap/Topology/manifolds-geometric-topology/linearization-of-compact-group-actions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Topology/manifolds-geometric-topology/linearization-of-compact-group-actions)
