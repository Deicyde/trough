---
declaration: theorem
origin: cited
lean: NumberField.AdeleRing.zero_discrete
statement: formalized
---

# NumberField.AdeleRing.zero_discrete

There's an open subset of $\mathbb{A}_{K}$ whose intersection with $K$ is $\{0\}$.

## Depends on

- [Rat.AdeleRing.zero_discrete](rat-adelering-zero-discrete.md)
- [NumberField.AdeleRing.baseChangeEquiv](../base-change/part-02/numberfield-adelering-basechangeequiv.md)

## Proof

By a previous result, we have $\mathbb{A}_K=K\otimes_{\mathbb{Q}}\mathbb{A}_{\mathbb{Q}}$. Choose a basis of $K/\mathbb{Q}$; then $K$ can be identified with $\mathbb{Q}^n\subseteq(\mathbb{A}_{\mathbb{Q}})^n$ and the result follows from the previous theorem.

## Lean

Stated as [`NumberField.AdeleRing.zero_discrete`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.AdeleRing.zero_discrete); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 987](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L987)
