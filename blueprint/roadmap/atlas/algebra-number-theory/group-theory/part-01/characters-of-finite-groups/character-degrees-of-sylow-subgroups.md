---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.irreducibleDegrees, MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.maxPPartExponent, MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.sylowCharacterDegreeExponentBounded, MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.sylowCharacterDegreeExponentBounded_holds
statement: formalized
---

# Character degrees of Sylow subgroups

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html).

## Irreducible complex representation degrees

For a group $G$, the set of natural numbers $d$
such that $G$ has an irreducible complex representation of finite dimension $d$; for a finite
group these are the degrees $\chi(1)$ of its irreducible characters.

Formalized by `MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.irreducibleDegrees`, a definition declared in [WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html#irreducible-degrees).

## Largest $p$-adic exponent of the irreducible degrees

For a natural number $p$ and a group
$G$, $e_p(G)$ is the supremum in $\mathbb{N}$ of the exponents of $p$ in the prime factorizations
of the dimensions of the finite-dimensional irreducible complex representations of $G$, where the
supremum of an empty or unbounded set is $0$. For a prime $p$ and a finite group $G$, it is the
largest $e$ such that $p^e$ divides the degree $\chi(1)$ of some irreducible character $\chi$ of
$G$.

Formalized by `MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.maxPPartExponent`, a definition declared in [WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html#max-ppart-exponent).

## Kourovka Problem 15.62 ($p$-parts of character degrees of Sylow subgroups)

The statement,
asked by A. Moretó, that there is a function $f \colon \mathbb{N} \to \mathbb{N}$ such that
$e_p(P) \le f(e_p(G))$ for every prime $p$, every finite group $G$ and every Sylow $p$-subgroup $P$
of $G$, where $e_p(H)$ is the largest exponent of $p$ dividing an irreducible character degree of
$H$.

Formalized by `MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.sylowCharacterDegreeExponentBounded`, a definition declared in [WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html#sylow-character-degree-exponent-bounded).

## Character degrees of Sylow subgroups are bounded in terms of those of the group

There is a
function $f \colon \mathbb{N} \to \mathbb{N}$ such that for every prime $p$, every finite group
$G$ and every Sylow $p$-subgroup $P$ of $G$, $e_p(P) \le f(e_p(G))$, where $e_p(H)$ is the
largest exponent of $p$ dividing an irreducible character degree of $H$.

One function works for all primes, since Yang and Qian's bound $|G : F(G)|_p \le p^{k e_p(G)}$,
with $F(G)$ the Fitting subgroup of $G$, has an absolute constant $k$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Archive of Solved Problems, Problem 15.62 (A. Moretó); resolution: Yong Yang and Guohua Qian, Adv. Math. 328 (2018), 356-366, abstract (|G : F(G)|_p ≤ p^(k e_p(G)) for a constant k, F(G) the Fitting subgroup, which settles Moretó's conjecture that e_p(P) = log_p b(P), b(P) the largest character degree of P, is bounded by a function of e_p(G)); Kourovka Archive, Problem 15.62 (answer: Yes, it is true); the solvable case is due to A. Moretó and T. R. Wolf, Adv. Math. 184 (2004), 18-36.

Stated but not proved: `MathlibExt.GroupTheory.SylowCharacterDegreePPartKourovka15Problem62Wanted.sylowCharacterDegreeExponentBounded_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/SylowCharacterDegreePPartKourovka15Problem62Wanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html#sylow-character-degree-exponent-bounded-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Character degrees of Sylow subgroups](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/characters-of-finite-groups/character-degrees-of-sylow-subgroups)
