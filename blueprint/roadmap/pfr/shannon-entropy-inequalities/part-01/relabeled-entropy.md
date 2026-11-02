---
declaration: lemma
origin: cited
lean: ProbabilityTheory.entropy_comp_of_injective, ProbabilityTheory.entropy_of_comp_eq_of_comp
statement: formalized
proof: formalized
---

# Entropy and relabeling

- (i) If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ for some injection $f: S \to T$, then $\mathbb{H}[X] = \mathbb{H}[Y]$.
- (ii) If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, and $Y = f(X)$ and $X = g(Y)$ for some functions $f: S \to T$, $g: T \to S$, then $\mathbb{H}[X] = \mathbb{H}[Y]$.

## Depends on

- [Entropy](entropy-def.md)

## Proof

Expand out both entropies and rearrange.

## Lean

Formalized as [`ProbabilityTheory.entropy_comp_of_injective`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_comp_of_injective), [`ProbabilityTheory.entropy_of_comp_eq_of_comp`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_of_comp_eq_of_comp).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 14](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L14)
