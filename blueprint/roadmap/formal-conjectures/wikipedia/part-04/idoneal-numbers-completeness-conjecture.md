---
declaration: theorem
origin: cited
lean: Idoneal.idoneal_numbers_completeness
statement: formalized
---

# Idoneal numbers completeness conjecture

> An integer $D>0$ is **idoneal** if every
> integer that can be expressed in exactly one way (up to order and signs)
> as $x^2 + D y^2$ with gcd(x, Dy)=1 is a prime power or twice a prime power.
>
> The Idoneal Numbers Completeness Conjecture asserts that the following list of
> 65 numbers is complete:
> 1,2,3,4,5,6,7,8,9,10,12,13,15,16,18,21,22,24,25,28,30,33,37,40,42,45,48,
> 57,58,60,70,72,78,85,88,93,102,105,112,120,130,133,165,168,177,190,210,232,
> 240,253,273,280,312,330,345,357,385,408,462,520,760,840,1320,1365,1848.
> *References:*
> - [Wikipedia: Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
> - [OEIS A000926](https://oeis.org/A000926)

*Quoted from [FormalConjectures/Wikipedia/IdonealCompleteness.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IdonealCompleteness.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 1 test statement, counted here but not shown.

## `Idoneal.idoneal_numbers_completeness`

Open: stated without proof.

> Idoneal numbers completeness conjecture.

```lean
theorem idoneal_numbers_completeness :
    ∀ n : ℕ, IsIdoneal n → n ∈ knownIdonealNumbers
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/IdonealCompleteness.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IdonealCompleteness.lean#L102).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/IdonealCompleteness.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/IdonealCompleteness.lean)
- [Wikipedia: Idoneal number](https://en.wikipedia.org/wiki/Idoneal_number)
