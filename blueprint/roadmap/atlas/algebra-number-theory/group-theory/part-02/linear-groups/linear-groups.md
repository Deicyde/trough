---
declaration: section
origin: cited
lean: MetaMathlibExt.generalLinearGroup_exponent_eq_lcm_eq_cyclotomicProduct, MathlibExt.GroupTheory.JordanLinearGroupsWanted.jordan_linear_groups, MathlibExt.GroupTheory.LinearGroupFinitenessWanted.malcev_residuallyFinite, MathlibExt.GroupTheory.LinearGroupFinitenessWanted.selberg_finiteIndex_torsionFree, MathlibExt.GroupTheory.StableSeriesShared.HasStableSeries
statement: formalized
proof: formalized
---

# Linear groups: its own results

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html).

Groups of matrices over fields and rings: SL2, PGL2 and SU(2) and their conjugacy and subgroups (Dickson's classification), Jordan, Malcev and Selberg theorems, transvections, eigenvalues of elements of prime order, and linearity of specific groups.

## Exponent of the general linear group over a prime field

Let $p$ be a prime and let
$m \ge 1$. The exponent of the group $\mathrm{GL}_m(\mathbb{F}_p)$ of invertible $m \times m$
matrices over $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$ is

$$p^{\lceil \log_p m \rceil} \cdot \operatorname{lcm}(p - 1, p^2 - 1, \dots, p^m - 1),$$

and this number equals $p^{\lceil \log_p m \rceil} \prod_{k=1}^{m} \Phi_k(p)$, where $\Phi_k$
denotes the $k$-th cyclotomic polynomial.

## Sources

- Eugene Karolinsky and Dmytro Seliutin, *Carmichael Numbers for GL(m)*, Journal of Integer Sequences 23 (2020), Article 20.10.6, <https://cs.uwaterloo.ca/journals/JIS/VOL23/Karolinsky/kar2.tex>, Theorem `fermat_matr` (quoting J. B. Marshall, *On the extension of Fermat's theorem to matrices of order n*, Proc. Edinb. Math. Soc. 6 (1939), and I. Niven, *Fermat's theorem for matrices*, Duke Math. J. 15 (1948)), lines 139-144; the lcm/cyclotomic identity is the paper's Proposition, lines 113-118.

Formalized by `MetaMathlibExt.generalLinearGroup_exponent_eq_lcm_eq_cyclotomicProduct`, a theorem declared in [MathlibExt/GroupTheory/GeneralLinearGroupExponent.lean, line 543](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/GeneralLinearGroupExponent.lean#L543). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html#general-linear-group-exponent-eq-lcm-eq).

## Jordan's theorem on finite linear groups

For every natural number $n$ there is a natural
number $J$ such that every finite subgroup $G$ of $\mathrm{GL}_n(\mathbb{C})$ contains an abelian
subgroup $A$ that is normal in $G$ and has index $[G : A] \le J$.

## Sources

- C. Jordan, J. Reine Angew. Math. 84 (1878); Lean states complex GL_n specialization `GL_n(ℂ)` while general theorem holds over any char-zero field with bound depending only on n.

Formalized by `MathlibExt.GroupTheory.JordanLinearGroupsWanted.jordan_linear_groups`, a theorem declared in [MathlibExt/GroupTheory/JordanLinearGroups.lean, line 1202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/JordanLinearGroups.lean#L1202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html#jordan-linear-groups).

## Malcev's theorem on linear groups

Let $K$ be a field and $n$ a natural number. Every finitely
generated subgroup of the general linear group $\mathrm{GL}_n(K)$ is residually finite.

## Sources

- A. I. Malcev, Mat. Sb. 8 (1940) 405–422; Wehrfritz, Infinite Linear Groups; Lean states subgroup `G ≤ GL_n(K)` with `Group.FG G`.

Formalized by `MathlibExt.GroupTheory.LinearGroupFinitenessWanted.malcev_residuallyFinite`, a theorem declared in [MathlibExt/GroupTheory/LinearGroupFiniteness.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/LinearGroupFiniteness.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html#malcev-residually-finite).

## Selberg's lemma

Let $K$ be a field of characteristic zero and let $n$ be a natural number.
Every finitely generated subgroup $G$ of $\mathrm{GL}_n(K)$ has a subgroup $H$ of finite index in
$G$ that is torsion-free: the identity is the only element of finite order in $H$.

## Sources

- A. Selberg, Contributions to Function Theory (1960) Selberg's lemma; Alperin, Proc. AMS 1969; Lean states char-zero case with H not required normal.

Formalized by `MathlibExt.GroupTheory.LinearGroupFinitenessWanted.selberg_finiteIndex_torsionFree`, a theorem declared in [MathlibExt/GroupTheory/SelbergFiniteIndexTorsionFree.lean, line 590](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/GroupTheory/SelbergFiniteIndexTorsionFree.lean#L590). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html#selberg-finite-index-torsion-free).

## Stable sets of linear automorphisms

Let $V$ be a vector space over a field $K$. A set $S$
of $K$-linear automorphisms of $V$ is stable when there are a natural number $m$ and subspaces
$0 = W_0 \le W_1 \le \cdots \le W_m = V$ of $V$ such that $g(w) - w \in W_i$ for every $i < m$,
every $g \in S$ and every $w \in W_{i+1}$.

Formalized by `MathlibExt.GroupTheory.StableSeriesShared.HasStableSeries`, a definition declared in [WantedExt/GroupTheory/StableSeriesShared.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/GroupTheory/StableSeriesShared.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html#has-stable-series).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Linear groups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/linear-groups/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/GroupTheory/linear-groups)
