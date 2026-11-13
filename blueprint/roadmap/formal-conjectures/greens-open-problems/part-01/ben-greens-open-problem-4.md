---
declaration: theorem
origin: cited
lean: Green4.green_4, Green4.large_green_4
statement: formalized
---

# Ben Green's Open Problem 4

> *Reference:* [Ben Green's Open Problem 4](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.4 Problem 4)

*Quoted from [FormalConjectures/GreensOpenProblems/4.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Green4.green_4`

Open: stated without proof.

> What is the largest product-free set in the alternating group $A_n$?

```lean
theorem green_4 (n : ℕ) :
    MaximalFor (ProdFree (M := alternatingGroup <| Fin n)) Set.ncard (green_4.answer n)
```

Category `research open`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/4.lean, line 38](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/4.lean#L38).

## `Green4.large_green_4`

Solved: stated here without proof.

> In the case of large n, the problem was solved in
> [On the largest product-free subsets of the alternating groups](https://arxiv.org/pdf/2205.15191).
> Specifically, this theorem formalizes the statement of theorem 1.1 in the mentioned paper

```lean
theorem large_green_4 : ∀ᶠ n in .atTop,
    ∀ S, MaximalFor (ProdFree (M := alternatingGroup <| Fin n)) Set.ncard S →
    ∃ x I, S = extremalFamily x I ∨ S = (extremalFamily x I).image (·⁻¹)
```

Category `research solved`; AMS [20 Group theory and generalizations](../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/GreensOpenProblems/4.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/4.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/4.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/4.lean)
- [https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.4](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#section.4)
