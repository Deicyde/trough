---
declaration: corollary
origin: cited
lean: flt
statement: formalized
---

# FLT

Fermat's Last Theorem is true. In other words, there are no positive integers $a,b,c$ and natural $n\geq3$ such that $a^n+b^n=c^n$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [FermatLastTheorem.of\_p\_ge\_5](../reduction-to-ngeq5-and-prime/fermatlasttheorem-of-p-ge-5.md)
- [FreyPackage.false](freypackage-false.md)
- [FreyPackage.of\_not\_FermatLastTheorem\_p\_ge\_5](../frey-packages/freypackage-of-not-fermatlasttheorem-p-ge-5.md)

## Proof

Assume there is a there is a counterexample $a^n+b^n=c^n$. By Corollary [Corollary FermatLastTheorem.of\_p\_ge\_5](../reduction-to-ngeq5-and-prime/fermatlasttheorem-of-p-ge-5.md) we may assume that there is also a counterexample $a^p+b^p=c^p$ with $p\geq 5$ and prime. Then there is a Frey package $(a,b,c,p)$ by [Lemma FreyPackage.of\_not\_FermatLastTheorem\_p\_ge\_5](../frey-packages/freypackage-of-not-fermatlasttheorem-p-ge-5.md), contradicting Corollary [Corollary FreyPackage.false](freypackage-false.md).

## Lean

Formalized as [`flt`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/flt).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/ch02reductions.tex, line 221](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/ch02reductions.tex#L221)
