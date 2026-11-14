---
declaration: definition
origin: cited
lean: IsRegularPrime
statement: formalized
---

# regular-prime

An odd prime $p$ is *regular* when $p$ does not divide the class number of the $p$th cyclotomic field:

$$
p \nmid h\bigl(\mathbb{Q}(\zeta_p)\bigr).
$$

Otherwise $p$ is *irregular*. (In the formalisation the condition is phrased as coprimality of $p$ with the cardinality of the class group of $\mathbb{Q}(\zeta_p)$, which is equivalent because $p$ is prime.)

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`IsRegularPrime`](https://riccardobrasca.github.io/KummerCriterion/docs/find/#doc/IsRegularPrime).

## Sources

- [Kummer's criterion blueprint: subsections/introduction.tex, line 45](https://github.com/riccardobrasca/KummerCriterion/blob/b96b2cde81e799bfe8364b6dd469abafd9a26bdf/blueprint/src/subsections/introduction.tex#L45)
