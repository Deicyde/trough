---
declaration: theorem
origin: cited
lean: NormalNumber.pi_normal_base_ten
statement: formalized
---

# Normality of mathematical constants

> Despite extensive empirical evidence—billions of digits have been computed for $\pi$,
> $e$, and $\sqrt{2}$, all showing near-uniform digit distribution—it is an open problem
> whether any of the classical constants $\pi$, $e$, $\sqrt{2}$, $\ln 2$, or $\varphi$ is
> normal in any base.
>
> *References:*
> * [Wikipedia (Normal number)](https://en.wikipedia.org/wiki/Normal_number)
> * [Wikipedia (Pi)](https://en.wikipedia.org/wiki/Pi)

*Quoted from [FormalConjectures/Wikipedia/NormalityOfPi.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/NormalityOfPi.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open.

## `NormalNumber.pi_normal_base_ten`

Open: stated without proof.

> $\pi$ is normal in base 10.

```lean
theorem pi_normal_base_ten : IsNormalInBase 10 π
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/NormalityOfPi.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/NormalityOfPi.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/NormalityOfPi.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/NormalityOfPi.lean)
- [Wikipedia (Normal number)](https://en.wikipedia.org/wiki/Normal_number)
