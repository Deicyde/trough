---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.ρ, MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.B, MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.determinant, MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.theorem_1_2
statement: formalized
---

# Reverse Minkowski theorem

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html).

## Gaussian mass of a lattice

For a real number $s$ and a $\mathbb{Z}$-submodule
$\mathcal{L} \subseteq \mathbb{R}^n$, the Gaussian mass of $\mathcal{L}$ at parameter $s$ is
$\rho_s(\mathcal{L}) = \sum_{y \in \mathcal{L}} e^{-\pi \|y\|^2 / s^2}$, where $\|y\|$ is the
Euclidean norm.

The sum is taken to be $0$ when the series is not summable.

Formalized by `MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.ρ`, a definition declared in [WantedExt/NumberTheory/ReverseMinkowskiWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ReverseMinkowskiWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html#untitled).

## Basis matrix of a lattice

Let $\mathcal{L} \subseteq \mathbb{R}^n$ be a discrete
$\mathbb{Z}$-submodule of rank $m$. Its basis matrix $B(\mathcal{L})$ is the real
$n \times m$ matrix whose $j$-th column is the $j$-th vector of a fixed, arbitrarily chosen
$\mathbb{Z}$-basis of $\mathcal{L}$.

Formalized by `MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.B`, a definition declared in [WantedExt/NumberTheory/ReverseMinkowskiWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ReverseMinkowskiWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html#b).

## Determinant of a lattice

For a discrete $\mathbb{Z}$-submodule
$\mathcal{L} \subseteq \mathbb{R}^n$ with basis matrix $B = B(\mathcal{L})$ (the real matrix whose
columns form a fixed $\mathbb{Z}$-basis of $\mathcal{L}$), the determinant of $\mathcal{L}$ is
$\det(\mathcal{L}) = \sqrt{\det(B^{T} B)}$.

Formalized by `MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.determinant`, a definition declared in [WantedExt/NumberTheory/ReverseMinkowskiWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ReverseMinkowskiWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html#determinant).

## Reverse Minkowski theorem

Let $\mathcal{L} \subseteq \mathbb{R}^n$ be a full-rank lattice, that
is, a discrete subgroup of $\mathbb{R}^n$ that spans $\mathbb{R}^n$, such that every subgroup
$\mathcal{L}' \subseteq \mathcal{L}$ (a lattice of possibly lower rank) has determinant
$\det(\mathcal{L}') \ge 1$. Let $t = 10(\log n + 2)$, where $\log$ is the natural logarithm. Then
the Gaussian mass of $\mathcal{L}$ at parameter $1/t$ satisfies
$\rho_{1/t}(\mathcal{L}) = \sum_{y \in \mathcal{L}} e^{-\pi t^2 \|y\|^2} \le 3/2$, where
$\|y\|$ is the Euclidean norm.

## Sources

- O. Regev, N. Stephens-Davidowitz, `A reverse Minkowski theorem`, Annals of Math, 199 (1) 2024. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_reverse_minkowski` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.ReverseMinkowskiWanted.ReverseMinkowski.theorem_1_2` is written with `theorem_wanted` in [WantedExt/NumberTheory/ReverseMinkowskiWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ReverseMinkowskiWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html#theorem-1-2).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reverse Minkowski theorem](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/uniform-distribution-metric/reverse-minkowski-theorem)
