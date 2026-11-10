---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.discrete
statement: formalized
---

# NumberField.AdeleRing.discrete

The additive subgroup $K$ of $\mathbb{A}_K$ is discrete.

## Depends on

- [NumberField.AdeleRing.zero_discrete](numberfield-adelering-zero-discrete.md)

## Proof

If $x\in K$ and $U$ is the open subset in the previous lemma, then it's easily checked that $K\cap U=\{0\}$ implies $K\cap (U+x)=\{x\}$, and $U+x$ is open.

## Lean

Stated as [`NumberField.AdeleRing.discrete`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.discrete); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 1000](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L1000)
