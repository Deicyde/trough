---
declaration: lemma
origin: cited
lean: fourier_surjection_on_schwartz
statement: formalized
proof: formalized
---

# Bijectivity of Fourier transform

The Fourier transform is a bijection on the Schwartz class. \[Note: only surjectivity is actually used.\]

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is a standard result in Fourier analysis. It can be proved here by appealing to Mellin inversion, Theorem MellinInversion. In particular, given $f$ in the Schwartz class, let $F : \mathbb{R}_+ \to \mathbb{C} : x \mapsto f(\log x)$ be a function in the “Mellin space”; then the Mellin transform of $F$ on the imaginary axis $s=it$ is the Fourier transform of $f$. The Mellin inversion theorem gives Fourier inversion.

## Lean

Formalized as [`fourier_surjection_on_schwartz`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/fourier_surjection_on_schwartz).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
