---
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: IsFractionRing.stabilizerHom_surjective
---

# IsFractionRing.stabilizerHom_surjective

The map $g\mapsto \phi_g$ from $D_Q$ to $\operatorname{Aut}(L/K)$ defined above is surjective.

## Depends on

- [IsFractionRing.stabilizerHom](isfractionring-stabilizerhom.md)

## Proof depends on

- [FixedPoints.toAlgAut_surjective](../the-extension-l-k/fixedpoints-toalgaut-surjective.md)

## Proof

*Proof of main theorem.* The map $D_Q \to \operatorname{Aut}(L/L^{D_Q})$ is surjective by [FixedPoints.toAlgAut_surjective](../the-extension-l-k/fixedpoints-toalgaut-surjective.md). For surjectivity of $\operatorname{Aut}(L/L^{D_Q}) \to \operatorname{Aut}(L/K)$, let $\sigma$ be a field automorphism of $L$ fixing $K$ pointwise. We must show that $\sigma$ automatically fixes $L^{D_Q}$ pointwise. But this is exactly [fixed_of_fixed2](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/FrobeniusProject.tex#L318). Thus, the composition $D_Q \to \operatorname{Aut}(L/L^{D_Q}) \to \operatorname{Aut}(L/K)$ is surjective.

## Lean

Formalized as [`IsFractionRing.stabilizerHom_surjective`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/IsFractionRing.stabilizerHom_surjective).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/FrobeniusProject.tex, line 52](https://github.com/ImperialCollegeLondon/FLT/blob/019805815d7da565ed1e9f427b6fbd0cbc9d00d3/blueprint/src/chapter/FrobeniusProject.tex#L52)
