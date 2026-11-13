---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.totientLeAutOrder, MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.autOrderEqTotientImpliesCyclic, MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.totientLeAutOrder_refuted, MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.autOrderEqTotientImpliesCyclic_refuted, MathlibExt.GroupTheory.AutomorphismGroupPrimePowerKourovka18Problem82Wanted.autOrderPrimePowerBound, MathlibExt.GroupTheory.AutomorphismGroupPrimePowerKourovka18Problem82Wanted.autOrderPrimePowerBound_holds, MathlibExt.GroupTheory.PGroupOrderDividesAutKourovka12Problem77Wanted.pGroupOrderDividesAutOrder, MathlibExt.GroupTheory.PGroupOrderDividesAutKourovka12Problem77Wanted.pGroupOrderDividesAutOrder_refuted
statement: formalized
---

# Orders of automorphism groups

8 results, 4 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html).

## Deaconescu's totient lower bound conjecture (Kourovka 15.43(a))

The statement that every
finite group $G$ satisfies $\varphi(|G|) \le |\mathrm{Aut}(G)|$, where $\varphi$ is Euler's totient
function and $\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Formalized by `MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.totientLeAutOrder`, a definition declared in [WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#totient-le-aut-order).

## Deaconescu's cyclicity conjecture (Kourovka 15.43(b))

The statement that every finite group
$G$ with $|\mathrm{Aut}(G)| = \varphi(|G|)$ is cyclic, where $\varphi$ is Euler's totient function
and $\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Formalized by `MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.autOrderEqTotientImpliesCyclic`, a definition declared in [WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#aut-order-eq-totient-implies-cyclic).

## Deaconescu's totient lower bound conjecture fails (Kourovka 15.43(a))

Not every finite group
$G$ satisfies $\varphi(|G|) \le |\mathrm{Aut}(G)|$: there is a finite group $G$ with
$|\mathrm{Aut}(G)| < \varphi(|G|)$, where $\varphi$ is Euler's totient function and
$\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Bray and Wilson prove more than is stated here: the ratio $|\mathrm{Aut}(G)| / \varphi(|G|)$ can be
made arbitrarily small.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.43 (M. Deaconescu); resolution: J. N. Bray and R. A. Wilson, On the orders of automorphism groups of finite groups, Bull. London Math. Soc. 37 (2005), no. 3, 381-385, main results (groups with |Aut G| < φ(|G|), infinitely many non-cyclic groups with |Aut G| = φ(|G|), and |Aut G|/φ(|G|) arbitrarily small); Kourovka Archive, Problem 15.43 (both answers negative), https://webspace.maths.qmul.ac.uk/j.n.bray/web/Publ/AutG/.

Stated but not proved: `MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.totientLeAutOrder_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#totient-le-aut-order-refuted).

## Deaconescu's cyclicity conjecture fails (Kourovka 15.43(b))

Not every finite group $G$ with
$|\mathrm{Aut}(G)| = \varphi(|G|)$ is cyclic: there is a non-cyclic finite group $G$ with
$|\mathrm{Aut}(G)| = \varphi(|G|)$, where $\varphi$ is Euler's totient function and
$\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Bray and Wilson prove more than is stated here: there are infinitely many such non-cyclic groups.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.43 (M. Deaconescu); resolution: J. N. Bray and R. A. Wilson, On the orders of automorphism groups of finite groups, Bull. London Math. Soc. 37 (2005), no. 3, 381-385, main results (groups with |Aut G| < φ(|G|), infinitely many non-cyclic groups with |Aut G| = φ(|G|), and |Aut G|/φ(|G|) arbitrarily small); Kourovka Archive, Problem 15.43 (both answers negative), https://webspace.maths.qmul.ac.uk/j.n.bray/web/Publ/AutG/.

Stated but not proved: `MathlibExt.GroupTheory.AutomorphismGroupOrderTotientKourovka15Problem43Wanted.autOrderEqTotientImpliesCyclic_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupOrderTotientKourovka15Problem43Wanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#aut-order-eq-totient-implies-cyclic-refu).

## Patne's prime-power divisibility problem (Kourovka 18.82)

The statement that there is a
function $f : \mathbb{N} \to \mathbb{N}$ such that for every $n \in \mathbb{N}$, every prime $p$ and
every finite group $G$, if $p^{f(n)}$ divides $|G|$ then $p^n$ divides $|\mathrm{Aut}(G)|$, where
$\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Formalized by `MathlibExt.GroupTheory.AutomorphismGroupPrimePowerKourovka18Problem82Wanted.autOrderPrimePowerBound`, a definition declared in [WantedExt/GroupTheory/AutomorphismGroupPrimePowerKourovka18Problem82Wanted.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupPrimePowerKourovka18Problem82Wanted.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#aut-order-prime-power-bound).

## Green's theorem on prime powers dividing the order of the automorphism group (Kourovka 18.82)

There is a function $f : \mathbb{N} \to \mathbb{N}$, the same for all primes, such that for every
$n \in \mathbb{N}$, every prime $p$ and every finite group $G$, if $p^{f(n)}$ divides $|G|$ then
$p^n$ divides $|\mathrm{Aut}(G)|$, where $\mathrm{Aut}(G)$ is the group of automorphisms of $G$.

Ledermann and Neumann (1956) first proved this with a function depending on $p$; J. A. Green (1956)
obtained a function independent of $p$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 18.82 (R. M. Patne); resolution: J. A. Green, Proc. Roy. Soc. London Ser. A 237 (1956), 574-581 (improving W. Ledermann and B. H. Neumann, Proc. Roy. Soc. London Ser. A 235 (1956), 235-246), Kourovka Archive, Problem 18.82: Yes, there is, https://arxiv.org/abs/1401.0300v49.

Stated but not proved: `MathlibExt.GroupTheory.AutomorphismGroupPrimePowerKourovka18Problem82Wanted.autOrderPrimePowerBound_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/AutomorphismGroupPrimePowerKourovka18Problem82Wanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/AutomorphismGroupPrimePowerKourovka18Problem82Wanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#aut-order-prime-power-bound-holds).

## Divisibility conjecture for orders of automorphism groups of $p$-groups (Kourovka 12.77)

The statement that there is a prime $p$ such that for every finite non-cyclic $p$-group $P$ of
order greater than $p^2$, the order of $P$ divides the order of its automorphism group
$\mathrm{Aut}(P)$.

The source asks this for every prime $p$; stating it for some prime makes its refutation assert a
counterexample for every prime.

Formalized by `MathlibExt.GroupTheory.PGroupOrderDividesAutKourovka12Problem77Wanted.pGroupOrderDividesAutOrder`, a definition declared in [WantedExt/GroupTheory/PGroupOrderDividesAutKourovka12Problem77Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PGroupOrderDividesAutKourovka12Problem77Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#p-group-order-divides-aut-order).

## Orders of $p$-groups need not divide orders of their automorphism groups

For every prime $p$
there is a finite non-cyclic $p$-group $P$ of order greater than $p^2$ whose order does not divide
the order of its automorphism group $\mathrm{Aut}(P)$.

González-Sánchez and Jaikin-Zapirain construct, for each prime $p$, finite $p$-groups $G_i$ with
$|\mathrm{Aut}(G_i)| / |G_i| \to 0$; they are non-abelian, hence non-cyclic of order greater than
$p^2$, and eventually $|\mathrm{Aut}(G_i)| < |G_i|$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 12.77 (well-known problem; A. I. Starostin); resolution: J. González-Sánchez and A. Jaikin-Zapirain, Finite p-groups with small automorphism group, Forum Math. Sigma 3 (2015), Paper No. e7, main theorem (abstract): for each prime p, finite p-groups G_i with |Aut(G_i)|/|G_i| → 0; Kourovka Archive, Problem 12.77.

Stated but not proved: `MathlibExt.GroupTheory.PGroupOrderDividesAutKourovka12Problem77Wanted.pGroupOrderDividesAutOrder_refuted` is written with `theorem_wanted` in [WantedExt/GroupTheory/PGroupOrderDividesAutKourovka12Problem77Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/PGroupOrderDividesAutKourovka12Problem77Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html#p-group-order-divides-aut-order-refuted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orders of automorphism groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/automorphisms/automorphism-groups/orders-of-automorphism-groups)
