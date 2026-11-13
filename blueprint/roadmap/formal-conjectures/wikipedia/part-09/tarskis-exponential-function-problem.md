---
declaration: theorem
origin: cited
lean: TarskiExponentialFunctionProblem.isDecidable_completeTheory_real_orderedField, TarskiExponentialFunctionProblem.tarski_exponential_function_problem, TarskiExponentialFunctionProblem.isDecidable_completeTheory_realExp_of_realSchanuelConjecture
statement: formalized
---

# Tarski's exponential function problem

> Tarski proved that the first-order theory of the real ordered field
> $(\mathbb{R}, +, \cdot, -, 0, 1, \le)$ is decidable, and asked whether the same holds for the
> real exponential field $\mathbb{R}_{\exp} = (\mathbb{R}, +, \cdot, -, 0, 1, \le, \exp)$.
> The problem is open. Macintyre and Wilkie proved that the theory of $\mathbb{R}_{\exp}$ is
> decidable if the real version of Schanuel's conjecture holds.
>
> Decidability of a theory is formalised in `FirstOrder.Language.Theory.IsDecidable`: the set of
> consequences of the theory is computable, with respect to the Gödel numbering of sentences from
> `FormalConjecturesForMathlib.ModelTheory.Encoding`. The theory in question is the complete
> theory of $\mathbb{R}_{\exp}$, which contains every sentence true in $\mathbb{R}_{\exp}$, so
> this is the same as asking for an algorithm deciding membership
> (`FirstOrder.Language.Theory.isDecidable_completeTheory_iff`). The statements use the language
> of ordered rings with the order symbol `≤` in place of `<`. Some sources state the problem for
> $(\mathbb{R}, +, \cdot, \exp)$ instead. Since $<$, $\le$, $-$, $0$ and $1$ are definable
> from $+$ and $\cdot$, all these structures are interdefinable, and the choice does not affect
> decidability.
>
> *References:*
> - [Wikipedia, *Tarski's exponential function problem*](https://en.wikipedia.org/wiki/Tarski%27s_exponential_function_problem),
>   listed in [Wikipedia, *List of unsolved problems in mathematics*](https://en.wikipedia.org/wiki/List_of_unsolved_problems_in_mathematics#Model_theory_and_formal_languages).
> - A. Tarski, *A decision method for elementary algebra and geometry*, 2nd ed., University of
>   California Press, Berkeley and Los Angeles, 1951.
> - A. Macintyre, A. J. Wilkie, *On the decidability of the real exponential field*, in:
>   P. Odifreddi (ed.), *Kreiseliana: about and around Georg Kreisel*, A K Peters, Wellesley, MA,
>   1996, pp. 441–467.
> - S. Kuhlmann, [*Model theory of the real exponential function*](https://encyclopediaofmath.org/wiki/Model_theory_of_the_real_exponential_function),
>   Encyclopedia of Mathematics.
> - A. Berarducci, F. Gallinaro, [*On the elementary theory of the real exponential field*](https://arxiv.org/abs/2603.08365),
>   arXiv:2603.08365 (2026). Assuming Schanuel's conjecture, gives an axiomatisation of the
>   theory of $\mathbb{R}_{\exp}$ and recovers the Macintyre–Wilkie decidability result.

*Quoted from [FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 API statement, counted here but not shown.

## `TarskiExponentialFunctionProblem.isDecidable_completeTheory_real_orderedField`

Solved: stated here without proof.

> **Tarski's theorem.** The first-order theory of the real ordered field
> $(\mathbb{R}, +, \cdot, -, 0, 1, \le)$ is decidable.

```lean
theorem isDecidable_completeTheory_real_orderedField :
    ((Language.ring.sum Language.order).completeTheory ℝ).IsDecidable
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean#L66).

## `TarskiExponentialFunctionProblem.tarski_exponential_function_problem`

Open: stated without proof.

> **Tarski's exponential function problem.** Is the first-order theory of the real exponential
> field $\mathbb{R}_{\exp} = (\mathbb{R}, +, \cdot, -, 0, 1, \le, \exp)$ decidable?

```lean
theorem tarski_exponential_function_problem :
    (Language.orderedExpField.completeTheory ℝ).IsDecidable
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean#L75).

## `TarskiExponentialFunctionProblem.isDecidable_completeTheory_realExp_of_realSchanuelConjecture`

Solved: stated here without proof.

> **Macintyre–Wilkie.** If the real version of Schanuel's conjecture holds, then the first-order
> theory of the real exponential field is decidable.

```lean
theorem isDecidable_completeTheory_realExp_of_realSchanuelConjecture
    (h : RealSchanuelConjecture) :
    (Language.orderedExpField.completeTheory ℝ).IsDecidable
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean#L112).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/TarskiExponentialFunctionProblem.lean)
- [Wikipedia, *Tarski's exponential function problem*](https://en.wikipedia.org/wiki/Tarski%27s_exponential_function_problem)
