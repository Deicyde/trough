---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: IsAlgebraic.exists_smul_eq_mul
---

# IsAlgebraic.exists\_smul\_eq\_mul

If $R/S$ is an algebraic extension of integral domains, then any fraction $a/b$ with $a,b\in R$ can be written as $c/d$ with $c\in R$ and $d\in S$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

If $f\in S[X]$ satisfies $f(b)=0$, then $f(0)\in S$ is a multiple of $b$. If $f(0)=bx\in S$, then $a/b=(ax)/(bx)$ as desired.

## Lean

Formalized as [`IsAlgebraic.exists_smul_eq_mul`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsAlgebraic.exists_smul_eq_mul).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 305](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/FrobeniusProject.tex#L305)
