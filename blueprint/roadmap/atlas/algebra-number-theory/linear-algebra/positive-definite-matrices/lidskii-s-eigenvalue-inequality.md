---
declaration: section
origin: cited
lean: MathlibExt.LinearAlgebra.LidskiiInequalityWanted.LinearAlgebra.lidskii_inequality, MathlibExt.LinearAlgebra.LidskiiWanted.LinearAlgebra.lidskii_last
statement: formalized
---

# Lidskii's eigenvalue inequality

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/lidskii-s-eigenvalue-inequality/index.html).

## Lidskii's inequality

Let $A$ and $B$ be Hermitian complex square matrices indexed by a
finite set with $N$ elements. List the eigenvalues of $A$, of $B$ and of $B - A$, each with
multiplicity and in decreasing order, as $\alpha_1 \ge \dots \ge \alpha_N$,
$\beta_1 \ge \dots \ge \beta_N$ and $\gamma_1 \ge \dots \ge \gamma_N$. Then for every real
$p \ge 1$,

$$\sum_{j=1}^N |\alpha_j - \beta_j|^p \le \sum_{j=1}^N |\gamma_j|^p.$$

## Sources

- V. B. Lidskii, On the proper values of a sum and product of symmetric matrices, Dokl. Akad. Nauk SSSR 75 (1950), 769-772. Listed as an additional statement of §99 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `lidskii_inequality` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.LinearAlgebra.LidskiiInequalityWanted.LinearAlgebra.lidskii_inequality` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/LidskiiInequalityWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/LidskiiInequalityWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/lidskii-s-eigenvalue-inequality/index.html#lidskii-inequality).

## Lidskii–Last theorem

Let $A$ and $B$ be Hermitian complex square matrices indexed by a
finite set with $N$ elements, and list the eigenvalues of $A$ and of $B$, each with multiplicity
and in decreasing order, as $\alpha_1 \ge \dots \ge \alpha_N$ and $\beta_1 \ge \dots \ge \beta_N$.
Then

$$\sum_{j=1}^N |\alpha_j - \beta_j| \le \sum_{i,j} |A_{ij} - B_{ij}|.$$

## Sources

- V. B. Lidskii (1950); the entrywise ℓ¹ form is due to Y. Last (around 1993). Listed as §99 in O. Knill, Some Fundamental Theorems in Mathematics (https://people.math.harvard.edu/~knill/graphgeometry/papers/fundamental.pdf). Problem `lidskii_last` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.LinearAlgebra.LidskiiWanted.LinearAlgebra.lidskii_last` is written with `theorem_wanted` in [WantedExt/LinearAlgebra/LidskiiWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/LinearAlgebra/LidskiiWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/lidskii-s-eigenvalue-inequality/index.html#lidskii-last).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Lidskii's eigenvalue inequality](https://deicyde.github.io/atlas-lean/roadmap/LinearAlgebra/positive-definite-matrices/lidskii-s-eigenvalue-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/LinearAlgebra/positive-definite-matrices/lidskii-s-eigenvalue-inequality)
