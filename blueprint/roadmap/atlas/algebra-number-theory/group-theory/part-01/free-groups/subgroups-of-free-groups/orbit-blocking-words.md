---
declaration: section
origin: cited
lean: MathlibExt.GroupTheory.OrbitBlockingWordKourovka20Problem88Wanted.existsOrbitBlockingWord, MathlibExt.GroupTheory.OrbitBlockingWordKourovka20Problem88Wanted.existsOrbitBlockingWord_holds
statement: formalized
---

# Orbit-blocking words

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/orbit-blocking-words/index.html).

## Kourovka Problem 20.88 (statement)

The statement that for every $r \ge 1$ and every
element $u$ of the free group $F_r$ on $r$ generators there is $v \in F_r$ such that, for every
automorphism $\varphi$ of $F_r$ for which the reduced word of $\varphi(u)$ is cyclically reduced,
the reduced word of $v$ is not a subword (a contiguous factor) of the reduced word of $\varphi(u)$.

Formalized by `MathlibExt.GroupTheory.OrbitBlockingWordKourovka20Problem88Wanted.existsOrbitBlockingWord`, a definition declared in [WantedExt/GroupTheory/OrbitBlockingWordKourovka20Problem88Wanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OrbitBlockingWordKourovka20Problem88Wanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/orbit-blocking-words/index.html#exists-orbit-blocking-word).

## Orbit-blocking words exist (Kourovka Problem 20.88)

For every $r \ge 1$ and every element $u$
of the free group $F_r$ on $r$ generators there is $v \in F_r$ such that, for every automorphism
$\varphi$ of $F_r$ for which the reduced word of $\varphi(u)$ is cyclically reduced, the reduced
word of $v$ is not a subword (a contiguous factor) of the reduced word of $\varphi(u)$.

## Sources

- E. I. Khukhro and V. D. Mazurov (eds.), Unsolved Problems in Group Theory: The Kourovka Notebook, 21st issue, arXiv:1401.0300v49 (2026), Problem 20.88 (V. Shpilrain); resolution: L. Koch-Hyde, S. O'Connor, É. Olive and V. Shpilrain, Orbit-blocking words in free groups, preprint, arXiv:2505.00477 (2025), Theorem 6.1 and Section 6: for every w ∈ F_r there are w-orbit-blocking words, i.e. words v that are not subwords of the cyclic reduction of φ(w) for any automorphism φ (built from primitivity-blocking words such as x₁² ⋯ x_r² x₁); Kourovka Notebook (21st issue), Problem 20.88: Yes, it is true, https://arxiv.org/abs/2505.00477.

Stated but not proved: `MathlibExt.GroupTheory.OrbitBlockingWordKourovka20Problem88Wanted.existsOrbitBlockingWord_holds` is written with `theorem_wanted` in [WantedExt/GroupTheory/OrbitBlockingWordKourovka20Problem88Wanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/GroupTheory/OrbitBlockingWordKourovka20Problem88Wanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/orbit-blocking-words/index.html#exists-orbit-blocking-word-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Orbit-blocking words](https://deicyde.github.io/atlas-lean/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/orbit-blocking-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/GroupTheory/free-groups/subgroups-of-free-groups/orbit-blocking-words)
