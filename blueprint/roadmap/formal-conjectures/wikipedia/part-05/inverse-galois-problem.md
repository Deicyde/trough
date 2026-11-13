---
declaration: theorem
origin: cited
lean: InverseGalois.inverse_galois_problem, InverseGalois.inverse_galois_problem.variants.cyclic, InverseGalois.inverse_galois_problem.variants.abelian, InverseGalois.inverse_galois_problem.variants.symmetric_group, InverseGalois.inverse_galois_problem.variants.complex_rational_functions, InverseGalois.inverse_galois_problem.variants.complex_function_field
statement: formalized
---

# Inverse Galois problem

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Inverse_Galois_problem)

*Quoted from [FormalConjectures/Wikipedia/InverseGalois.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved.

## `InverseGalois.inverse_galois_problem`

Open: stated without proof.

> The **Inverse Galois Problem**: every finite group is
> isomorphic to the Galois group of a Galois extension of the
> rationals.

```lean
theorem inverse_galois_problem {G : Type*} [Fintype G] [Group G] :
    IsRealizable ℚ G
```

Category `research open`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L53).

## `InverseGalois.inverse_galois_problem.variants.cyclic`

Solved: stated here without proof.

> Every finite cyclic group is realizable.

```lean
theorem inverse_galois_problem.variants.cyclic
    {G : Type*} [Fintype G] [Group G] [IsCyclic G] :
    IsRealizable ℚ G
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L61).

## `InverseGalois.inverse_galois_problem.variants.abelian`

Solved: stated here without proof.

> Every finite abelian group is realizable.

```lean
theorem inverse_galois_problem.variants.abelian
    {G : Type*} [Fintype G] [CommGroup G] :
    IsRealizable ℚ G
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L70).

## `InverseGalois.inverse_galois_problem.variants.symmetric_group`

Solved: stated here; a Lean proof is at [https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/4e37e8779287010f34ffc6c817ea45fc26d8ba0a/Proofs/T_InverseGalois_inverse_galois_problem_variants_symmetric_group.lean#L392](https://github.com/anatoliiohorodnyk/lean-fc-proofs/blob/4e37e8779287010f34ffc6c817ea45fc26d8ba0a/Proofs/T_InverseGalois_inverse_galois_problem_variants_symmetric_group.lean#L392).

> Every finite symmetric group is realizable.

```lean
theorem inverse_galois_problem.variants.symmetric_group
    {S : Type*} [Fintype S] :
    IsRealizable ℚ (S ≃ S)
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L80).

## `InverseGalois.inverse_galois_problem.variants.complex_rational_functions`

Solved: stated here without proof.

> Every finite group is realisable over the field of rational functions
> with complex coefficients.

```lean
theorem inverse_galois_problem.variants.complex_rational_functions
    {G : Type*} [Fintype G] [Group G] :
    IsRealizable (RatFunc ℂ) G
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L90).

## `InverseGalois.inverse_galois_problem.variants.complex_function_field`

Solved: stated here without proof.

> Every finite group is realisable over the field of rational functions
> with coefficients `K`, where `K` is any algebraically closed field of characteristic 0.

```lean
theorem inverse_galois_problem.variants.complex_function_field
    {G K : Type*} [Field K] [IsAlgClosed K] [CharZero K] [Fintype G] [Group G] :
    IsRealizable (RatFunc K) G
```

Category `research solved`; AMS [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/InverseGalois.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/InverseGalois.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/InverseGalois.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Inverse_Galois_problem)
