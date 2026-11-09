---
declaration: theorem
origin: cited
lean: LeanPool.PythagoreanPolynomialParametrization.exists_int_valued_parametrization
statement: formalized
proof: formalized
---

# Polynomial parametrizations of Pythagorean triples

> Formalizes Frisch and Vaserstein's result that Pythagorean triples are not parametrizable by one triple of integer-coefficient polynomials in any number of variables, but are parametrizable by a single triple of integer-valued rational polynomials, including the positive and sixteen-parameter variants.

*Quoted from the card [LeanPool/projects/pythagorean-polynomial-parametrization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pythagorean-polynomial-parametrization.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`LeanPool.PythagoreanPolynomialParametrization.no_int_poly_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/Obstructions.html#LeanPool.PythagoreanPolynomialParametrization.no_int_poly_parametrization) (theorem), declared in [LeanPool/PythagoreanPolynomialParametrization/Obstructions.lean, line 74](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/Obstructions.lean#L74): “Proves that no single triple of integer-coefficient polynomials in any number of variables parametrizes all Pythagorean triples.”
- [`LeanPool.PythagoreanPolynomialParametrization.exists_int_valued_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/IntegerValued.html#LeanPool.PythagoreanPolynomialParametrization.exists_int_valued_parametrization) (theorem; a main declaration), declared in [LeanPool/PythagoreanPolynomialParametrization/IntegerValued.lean, line 124](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/IntegerValued.lean#L124): “Gives the explicit four-variable integer-valued polynomial parametrization of all Pythagorean triples.”
- [`LeanPool.PythagoreanPolynomialParametrization.positive_triples_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/Positive.html#LeanPool.PythagoreanPolynomialParametrization.positive_triples_parametrization) (theorem), declared in [LeanPool/PythagoreanPolynomialParametrization/Positive.lean, line 146](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/Positive.lean#L146): “Formalizes the positive Pythagorean-triple parametrization with positive parameters and a nonnegative auxiliary parameter.”
- [`LeanPool.PythagoreanPolynomialParametrization.exists_16_param_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/Positive.html#LeanPool.PythagoreanPolynomialParametrization.exists_16_param_parametrization) (theorem), declared in [LeanPool/PythagoreanPolynomialParametrization/Positive.lean, line 351](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/Positive.lean#L351): “Converts the positive parametrization to an unrestricted sixteen-integer-parameter parametrization using the four-square theorem.”
- [`LeanPool.PythagoreanPolynomialParametrization.single_intValued_parametrization_yields_finite_intPoly_parametrization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/Explanatory.html#LeanPool.PythagoreanPolynomialParametrization.single_intValued_parametrization_yields_finite_intPoly_parametrization) (theorem), declared in [LeanPool/PythagoreanPolynomialParametrization/Explanatory.lean, line 203](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/Explanatory.lean#L203): “Proves the cited reduction from one integer-valued polynomial tuple to finitely many integer-coefficient polynomial tuples.”
- [`LeanPool.PythagoreanPolynomialParametrization.integerValued_polynomial_ring_not_uniqueFactorization`](https://leanpool.github.io/lean-pool/LeanPool/PythagoreanPolynomialParametrization/Explanatory.html#LeanPool.PythagoreanPolynomialParametrization.integerValued_polynomial_ring_not_uniqueFactorization) (theorem), declared in [LeanPool/PythagoreanPolynomialParametrization/Explanatory.lean, line 354](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization/Explanatory.lean#L354): “Records the integer-valued polynomial ring non-UFD phenomenon behind the paper's motivating discussion.”

## Project

- Authors: Lazar Milikic.
- Source: *Parametrization of Pythagorean triples by a single triple of polynomials* by Sophie Frisch, Leonid Vaserstein, [doi:10.1016/j.jpaa.2007.05.019](https://doi.org/10.1016/j.jpaa.2007.05.019), [arXiv:0706.0290](https://arxiv.org/abs/0706.0290).
- Project repository: [epfl-lara/AutoformalizedProjects](https://github.com/epfl-lara/AutoformalizedProjects).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11D09, 11D85, 13F20.
- In Lean Pool: [LeanPool/PythagoreanPolynomialParametrization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization), from the card [LeanPool/projects/pythagorean-polynomial-parametrization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pythagorean-polynomial-parametrization.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pythagorean-polynomial-parametrization.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pythagorean-polynomial-parametrization.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PythagoreanPolynomialParametrization](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PythagoreanPolynomialParametrization)
