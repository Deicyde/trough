---
declaration: section
origin: cited
lean: MathlibExt.Analysis.SendovRadiusConstantWanted.IsAdmissibleRadius, MathlibExt.Analysis.SendovRadiusConstantWanted.IsAdmissibleRadius.mono, MathlibExt.Analysis.SendovRadiusConstantWanted.sendovRadius, MathlibExt.Analysis.SendovRadiusConstantWanted.bddBelow_admissibleRadii, MathlibExt.Analysis.SendovRadiusConstantWanted.sendovRadius_le_of_isAdmissibleRadius, MathlibExt.Analysis.SendovRadiusConstantWanted.sendovConjecture, MathlibExt.Analysis.SendovRadiusConstantWanted.lowerBoundOne, MathlibExt.Analysis.SendovRadiusConstantWanted.upperBoundTwo
statement: formalized
---

# Sendov's conjecture

9 results, 8 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html).

## Admissible radius in Sendov's problem

A real number $R$ is an admissible radius if
$R > 0$ and, for every integer $n \ge 2$ and every complex polynomial $f$ of degree $n$ whose
zeros all lie in the closed unit disk $|z| \le 1$, every zero $\lambda$ of $f$ has a critical
point within distance $R$, that is, a zero $c$ of the derivative $f'$ with
$|c - \lambda| \le R$.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.IsAdmissibleRadius`, a definition declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#is-admissible-radius).

## Enlarging an admissible radius

If $R$ is an admissible radius and $R \le S$, then $S$ is
an admissible radius.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.IsAdmissibleRadius.mono`, a theorem declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#mono).

## The Sendov radius

The Sendov radius is the infimum, as a real number, of the set of
admissible radii in Sendov's problem.

By the convention for infima of real numbers, it would be $0$ if no radius were admissible.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.sendovRadius`, a definition declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#sendov-radius).

## The admissible radii are bounded below

The set of admissible radii is bounded below.

Zero is a lower bound, since every admissible radius is positive.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.bddBelow_admissibleRadii`, a theorem declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#bdd-below-admissible-radii).

## Admissible radii bound the Sendov radius

If $R$ is an admissible radius, then the Sendov
radius is at most $R$.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.sendovRadius_le_of_isAdmissibleRadius`, a theorem declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#sendov-radius-le-of-is-admissible-radius).

## Sendov's conjecture

Sendov's conjecture is the proposition that the Sendov radius is at
most $1$.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.sendovConjecture`, a definition declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#sendov-conjecture).

## Lower bound one for the Sendov radius

This is the proposition that the Sendov radius is at
least $1$.

The polynomials $z^n - 1$ with $n \ge 2$ give this lower bound.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.lowerBoundOne`, a definition declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#lower-bound-one).

## Upper bound two for the Sendov radius

This is the proposition that the Sendov radius is at
most $2$.

The geometric bound from the Gauss–Lucas theorem gives this upper bound.

Formalized by `MathlibExt.Analysis.SendovRadiusConstantWanted.upperBoundTwo`, a definition declared in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#upper-bound-two).

## Sendov's conjecture holds

Sendov's conjecture is true: the Sendov radius is at most $1$.

Sendov's conjecture was resolved in 2026 by Lech Mazur's computer-assisted proof.

## Sources

- Lech Mazur, A Computer-Assisted Proof of Sendov's Conjecture, ProofAtlas, August 5, 2026, https://www.proofatlas.ai/papers/sendov-conjecture/SENDOV_CONJECTURE_PROOF_AUGUST_5_2026.pdf; teorth/sendov, Sendov's conjecture in Lean, https://github.com/teorth/sendov/blob/1ddea92d89f951a0a7cbbffa6c267cf7e6640b1d/Sendov/Conjecture.lean.

Stated but not proved: `MathlibExt.Analysis.SendovRadiusConstantWanted.sendovConjecture_holds` is written with `theorem_wanted` in [WantedExt/Analysis/SendovRadiusConstantWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Analysis/SendovRadiusConstantWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html#sendov-conjecture-holds).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sendov's conjecture](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/zeros-of-polynomials/sendov-s-conjecture)
