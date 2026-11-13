---
declaration: theorem
origin: cited
lean: Erdos674.erdos_674, Erdos674.erdos_674.variants.infinite
statement: formalized
---

# Erdős Problem 674

> *References:*
> - [erdosproblems.com/674](https://www.erdosproblems.com/674)
> - [Ko40] Ko, Chao, *Note on the Diophantine equation $x^xy^y=z^z$*. J. Chinese Math. Soc.
>   (1940), 31-39.

*Quoted from [FormalConjectures/ErdosProblems/674.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/674.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/674](https://www.erdosproblems.com/674).

The file states 2 research or textbook statements: 2 solved.

## `Erdos674.erdos_674`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos674.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos674.lean).

> Are there any integer solutions to $x^xy^y=z^z$ with $x,y,z>1$?
>
> Ko [Ko40] proved there are none if $(x,y)=1$, but there are in fact infinitely many solutions in
> general - for example, $x=2^{12}3^6$, $y = 2^83^8$, and $z = 2^{11}3^7$.

```lean
theorem erdos_674 : solutionSet.Nonempty
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/674.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/674.lean#L45).

## `Erdos674.erdos_674.variants.infinite`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos674.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos674.lean).

> There are in fact infinitely many integer solutions to $x^xy^y=z^z$ with $x,y,z>1$.

```lean
theorem erdos_674.variants.infinite : solutionSet.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/674.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/674.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/674.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/674.lean)
- [erdosproblems.com/674](https://www.erdosproblems.com/674)
