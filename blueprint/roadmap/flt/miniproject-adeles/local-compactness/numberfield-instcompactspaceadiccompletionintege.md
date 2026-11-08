---
declaration: theorem
origin: cited
lean: NumberField.instCompactSpaceAdicCompletionIntegers
statement: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/451
---

# NumberField.instCompactSpaceAdicCompletionIntegers

If $K$ is a number field and $v$ is a nonzero prime ideal of the integers of $K$, then the integers of $K_v$ is a compact open subgroup.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Openness should follow from the fact that the integers are $\{x : v(x)\lt v(1/\pi)\}$ where $\pi$ is a uniformizer. Compactness needs finiteness of the residue field $\mathcal{O}_K/v$.

## Lean

Stated as [`NumberField.instCompactSpaceAdicCompletionIntegers`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.instCompactSpaceAdicCompletionIntegers); the blueprint does not mark its proof formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 74](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L74)
