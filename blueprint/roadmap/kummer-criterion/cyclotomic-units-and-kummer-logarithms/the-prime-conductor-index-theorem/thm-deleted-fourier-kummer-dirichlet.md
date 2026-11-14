---
declaration: theorem
origin: cited
lean: KummerCriterion.kummerDirichletDeterminant_of_deletedFourier
statement: formalized
proof: formalized
---

# deleted-fourier-kummer-dirichlet

The deleted-Fourier determinant identity supplies the Kummer–Dirichlet determinant hypothesis required by the Sinnott index pipeline: the regulator-type determinant of the cyclotomic-unit family is, up to an explicit nonzero factor, a product of the character sums $\sum_a \chi(a) \log|1-e^{2\pi i a/p}|$ over the even nontrivial characters.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The logarithmic embeddings of the cyclotomic units form a matrix whose group-theoretic structure (rows and columns indexed by a cyclic group) is diagonalised by the discrete Fourier transform with one character deleted. Composing the resulting determinant identity with the regulator identity for the cyclotomic-unit family produces exactly the Kummer–Dirichlet determinant needed downstream.

## Lean

Formalized as [`KummerCriterion.kummerDirichletDeterminant_of_deletedFourier`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/KummerCriterion.kummerDirichletDeterminant_of_deletedFourier).

## Sources

- [Kummer's criterion blueprint: subsections/cyclotomic-units.tex, line 406](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/cyclotomic-units.tex#L406)
