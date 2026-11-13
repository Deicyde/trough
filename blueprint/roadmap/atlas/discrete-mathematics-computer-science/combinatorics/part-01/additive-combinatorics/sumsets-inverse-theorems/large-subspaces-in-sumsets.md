---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.AlmostSubspaceInSumsetWanted.conjecture, MathlibExt.Combinatorics.AlmostSubspaceInSumsetWanted.conjecture_holds
statement: formalized
---

# Large subspaces in sumsets

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/large-subspaces-in-sumsets/index.html).

## Almost-subspace-in-$A + A$ conjecture

The statement that there are real constants $C > 0$
and $E > 0$ such that for every $n \in \mathbb{N}$, every set $A \subseteq \mathbb{F}_2^n$ and all
real numbers $\alpha$ and $\varepsilon$ with $\alpha > 0$, $0 < \varepsilon < 1$ and
$|A| / 2^n = \alpha$, there is an additive subgroup $V$ of $\mathbb{F}_2^n$ whose codimension
$\log_2(2^n / |V|)$ is at most $C \, (\log(\varepsilon^{-1} \alpha^{-1}) + 1)^E$ and which
satisfies $|V \cap (A + A)| \ge (1 - \varepsilon) |V|$. Here $A + A = \{a + b : a, b \in A\}$ and
$\log$ is the natural logarithm; the constants $C$ and $E$ express the source's codimension bound
$\log^{O(1)}(\varepsilon^{-1} \alpha^{-1})$.

## Sources

- cites [AIM-COMBINATORICS-0031], aim-combinatorics-notes.json notes[30].

Formalized by `MathlibExt.Combinatorics.AlmostSubspaceInSumsetWanted.conjecture`, a definition declared in [WantedExt/Combinatorics/AlmostSubspaceInSumsetWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AlmostSubspaceInSumsetWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/large-subspaces-in-sumsets/index.html#conjecture).

## A subspace almost inside $A + A$ (Kelley–Meka)

There are real constants $C > 0$ and
$E > 0$ such that for every $n \in \mathbb{N}$, every set $A \subseteq \mathbb{F}_2^n$ and all real
numbers $\alpha$ and $\varepsilon$ with $\alpha > 0$, $0 < \varepsilon < 1$ and
$|A| / 2^n = \alpha$, there is an additive subgroup $V$ of $\mathbb{F}_2^n$ whose codimension
$\log_2(2^n / |V|)$ is at most $C \, (\log(\varepsilon^{-1} \alpha^{-1}) + 1)^E$ and which
satisfies $|V \cap (A + A)| \ge (1 - \varepsilon) |V|$. Here $A + A = \{a + b : a, b \in A\}$ and
$\log$ is the natural logarithm.

Kelley and Meka (Lemma 1.5 of arXiv:2302.05537) show that, over a finite field $\mathbb{F}_q$,
every set $A \subseteq \mathbb{F}_q^n$ of density at least $2^{-d}$ and every error parameter
$\tau$ admit a set $A' \subseteq A$ whose affine span $V + \theta$ has codimension
$O(d^5 \log(1/\tau)^4)$ and $|A' + A'| \ge (1 - \tau)|V + \theta|$, answering the question of
Hatami, Hosseini and Lovett. Over $\mathbb{F}_2$ the sumset $A' + A'$ lies in the subspace $V$,
which gives the statement. Bloom and Sisask improve this codimension bound (arXiv:2309.02353,
Theorem 3).

## Sources

- Zander Kelley and Raghu Meka, Strong bounds for 3-progressions, FOCS 2023, arXiv:2302.05537, https://arxiv.org/abs/2302.05537.

Stated but not proved: `MathlibExt.Combinatorics.AlmostSubspaceInSumsetWanted.conjecture_holds` is written with `theorem_wanted` in [WantedExt/Combinatorics/AlmostSubspaceInSumsetWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/AlmostSubspaceInSumsetWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/large-subspaces-in-sumsets/index.html#conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Large subspaces in sumsets](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/large-subspaces-in-sumsets/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/additive-combinatorics/sumsets-inverse-theorems/large-subspaces-in-sumsets)
