---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CStarAlgebra.Bicommutant.bicommutant_finiteDimensional_matrix, MathlibExt.Analysis.VonNeumannDoubleCommutantWanted.Analysis.vonNeumann_doubleCommutant_tfae
statement: formalized
---

# Von Neumann bicommutant theorem

2 results, 1 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/von-neumann-bicommutant-theorem/index.html).

## Finite-dimensional bicommutant theorem

Let $n$ be a natural number and let $S$ be a
unital $*$-subalgebra of the algebra $M_n(\mathbb{C})$ of complex $n \times n$ matrices. Then the
commutant of the commutant of $S$ equals $S$: a matrix commutes with every matrix that commutes
with all elements of $S$ if and only if it lies in $S$.

## Sources

- John von Neumann, "Zur Algebra der Funktionaloperationen und Theorie der normalen Operatoren", Mathematische Annalen 102 (1930), 370--427, DOI 10.1007/BF01782352. This is the finite-dimensional specialization: in finite dimension every subspace is closed, so the strong-operator closure condition of the general theorem is vacuous.

Formalized by `MathlibExt.Analysis.CStarAlgebra.Bicommutant.bicommutant_finiteDimensional_matrix`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/Bicommutant.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/Bicommutant.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/von-neumann-bicommutant-theorem/index.html#bicommutant-finite-dimensional-matrix).

## Von Neumann's double commutant theorem

Let $H$ be a complex Hilbert space and let $S$ be
a unital $*$-subalgebra of the algebra of bounded linear operators on $H$. Write $S'$ for the
commutant of $S$, the set of bounded operators on $H$ that commute with every element of $S$.
The following are equivalent: $S$ equals its double commutant $S''$; $S$ is closed in the weak
operator topology; $S$ is closed in the strong operator topology, the topology of pointwise
convergence on $H$.

## Sources

- J. von Neumann, *Zur Algebra der Funktionaloperationen und Theorie der normalen Operatoren*, Math. Ann. 102 (1929) (double commutant theorem). Problem `vonneumann_double_commutant` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.Analysis.VonNeumannDoubleCommutantWanted.Analysis.vonNeumann_doubleCommutant_tfae` is written with `theorem_wanted` in [WantedExt/Analysis/VonNeumannDoubleCommutantWanted.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/VonNeumannDoubleCommutantWanted.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/von-neumann-bicommutant-theorem/index.html#von-neumann-double-commutant-tfae).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Von Neumann bicommutant theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/von-neumann-bicommutant-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras/von-neumann-bicommutant-theorem)
