---
declaration: theorem
origin: cited
lean: Erdos114.erdos_114, Erdos114.erdos_114.variants.large_n, Erdos114.erdos_114.variants.two, Erdos114.erdos_114.variants.one
statement: formalized
---

# Erdős Problem 114

> *References:*
> - [erdosproblems.com/114](https://www.erdosproblems.com/114)
> - [EHP58] Erdős, P., Herzog, F. and Piranian, G., *Metric properties of polynomials*.
>   J. Analyse Math. (1958), 125-148.
> - [ErHa99] Eremenko, A. and Hayman, W., *On the length of lemniscates*. Michigan Math. J. (1999),
>   409-415. [arXiv:0805.2295](https://arxiv.org/abs/0805.2295)
> - [Ta25] Tao, T., *The maximal length of the Erdős–Herzog–Piranian lemniscate in high degree*
>   (2025). [arXiv:2512.12455](https://arxiv.org/abs/2512.12455)

*Quoted from [FormalConjectures/ErdosProblems/114.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/114](https://www.erdosproblems.com/114).

The file states 4 research or textbook statements: 1 open, 2 solved and 1 textbook result.

## `Erdos114.erdos_114`

Open: stated without proof.

> If $p(z) \in \mathbb{C}[z]$ is a monic polynomial of degree $n$, is the length of the curve
> $\{z \in \mathbb{C} : \lvert p(z)\rvert = 1\}$ maximised when $p(z) = z^n - 1$?
>
> We require $n \geq 1$. For $n = 0$ the only monic polynomial is $1$, whose level set is all of
> $\mathbb{C}$, while $z^0 - 1 = 0$ has an empty level set.

```lean
theorem erdos_114 :
    ∀ n : ℕ, 1 ≤ n → ∀ p : ℂ[X], p.Monic → p.natDegree = n →
      lemniscateLength p ≤ lemniscateLength (X ^ n - 1)
```

Category `research open`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/114.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean#L53).

## `Erdos114.erdos_114.variants.large_n`

Solved: stated here without proof.

> Tao [Ta25] proved that $z^n - 1$ maximises the length of the lemniscate for all sufficiently
> large $n$.

```lean
theorem erdos_114.variants.large_n : ∀ᶠ n in atTop, ∀ p : ℂ[X], p.Monic → p.natDegree = n →
    lemniscateLength p ≤ lemniscateLength (X ^ n - 1)
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/114.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean#L63).

## `Erdos114.erdos_114.variants.two`

Solved: stated here without proof.

> Eremenko and Hayman [ErHa99] proved the case $n = 2$.

```lean
theorem erdos_114.variants.two (p : ℂ[X]) (hp : p.Monic) (hdeg : p.natDegree = 2) :
    lemniscateLength p ≤ lemniscateLength (X ^ 2 - 1)
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/114.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean#L69).

## `Erdos114.erdos_114.variants.one`

Textbook result, proved here.

> The case $n = 1$. A monic linear polynomial is $z - a$. Its lemniscate is a translate of the
> lemniscate of $z - 1$, and translations preserve Hausdorff measure.

```lean
theorem erdos_114.variants.one (p : ℂ[X]) (hp : p.Monic) (hdeg : p.natDegree = 1) :
    lemniscateLength p ≤ lemniscateLength (X ^ 1 - 1)
```

Category `textbook`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md), [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/114.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean#L78).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/114.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/114.lean)
- [erdosproblems.com/114](https://www.erdosproblems.com/114)
