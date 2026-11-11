---
declaration: section
origin: cited
lean: MathlibExt.Analysis.CStarAlgebra.KaplanskyDensityWanted.toBounded, MathlibExt.Analysis.CStarAlgebra.KaplanskyDensityWanted.kaplansky_density_theorem
statement: formalized
proof: formalized
---

# Kaplansky density theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kaplansky-density-theorem/index.html).

## Strong-operator operators as bounded operators

For a complex Hilbert space $H$, this
sends a bounded linear operator on $H$, viewed in the space of operators with the strong operator
topology (pointwise convergence on $H$), to the same operator viewed in $B(H)$ with the operator
norm. It is the identity on underlying maps.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KaplanskyDensityWanted.toBounded`, an abbreviation declared in [MathlibExt/Analysis/CStarAlgebra/KaplanskyDensity.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/KaplanskyDensity.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kaplansky-density-theorem/index.html#to-bounded).

## Kaplansky density theorem

Let $H$ be a complex Hilbert space and let $S$ be a unital
$*$-subalgebra of the algebra $B(H)$ of bounded operators on $H$, with operator norm $\|\cdot\|$.
Take closures in the strong operator topology on $B(H)$, the topology of pointwise convergence on
$H$, and write $\overline{S}$ for the strong closure of $S$. Then the strong closure of the unit
ball $\{x \in S : \|x\| \le 1\}$ of $S$ equals the unit ball $\{y \in \overline{S} : \|y\| \le 1\}$
of $\overline{S}$.

## Sources

- Kaplansky density theorem, I. Kaplansky, Pacific J. Math. 1 (1951), 227–232; see Takesaki, Theory of Operator Algebras I, Density Theorem and Kadison–Ringrose Vol I; Lean is SOT-closure equality of unit balls via toBounded conversion, full infinite-dimensional form.

Formalized by `MathlibExt.Analysis.CStarAlgebra.KaplanskyDensityWanted.kaplansky_density_theorem`, a theorem declared in [MathlibExt/Analysis/CStarAlgebra/KaplanskyDensity.lean, line 1708](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/CStarAlgebra/KaplanskyDensity.lean#L1708). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kaplansky-density-theorem/index.html#kaplansky-density-theorem).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kaplansky density theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-algebras/kaplansky-density-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-algebras/kaplansky-density-theorem)
