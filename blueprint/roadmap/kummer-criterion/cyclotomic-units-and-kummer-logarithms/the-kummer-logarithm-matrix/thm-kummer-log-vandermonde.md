---
declaration: theorem
origin: cited
lean: KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_eq_diagonal_mul_vandermonde
statement: formalized
proof: formalized
---

# kummer-log-vandermonde

The Kummer logarithm matrix factors as

$$
M = D \cdot V,
$$

where $D$ is the diagonal matrix of Bernoulli factors (the $j$th diagonal entry being a unit multiple of the reduction of $B_{2j}/2j$) and $V$ is a Vandermonde-type matrix built from Teichmüller values.

## Depends on

- [concreteKummerLogMatrix](def-concretekummerlogmatrix.md)

## Proof

Expand the completed logarithm of each generator in the Dwork basis and compute the coefficients. Each entry of $M$ splits as a product of a factor depending only on the row $j$ — the Bernoulli factor — and a factor of the form $\eta_a^{\,2j}$ depending on the column through a Teichmüller node $\eta_a$. Collecting the row factors into a diagonal matrix exhibits the remaining matrix as a Vandermonde matrix in the nodes $\eta_a^2$.

## Lean

Formalized as [`KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_eq_diagonal_mul_vandermonde`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.CyclotomicUnits.concreteKummerLogMatrix_eq_diagonal_mul_vandermonde).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 227](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L227)
