---
declaration: theorem
origin: cited
lean: DiophantineTuple.isDiophantineTuple_of_subset, DiophantineTuple.noIntegralDiophantineFiveTuple, DiophantineTuple.hasUniqueExtension_of_forall, DiophantineTuple.noIntegralDiophantineFiveTuple_of_hasUniqueExtensionOfForall, DiophantineTuple.hasUniqueExtension_of_1_3_8, DiophantineTuple.rational_7_tuple
statement: formalized
---

# Diophantine $m$-tuples

> A **Diophantine $m$-tuple** is a set of $m$ distinct positive integers
> $\{a_1, \dots, a_m\}$ such that $a_i a_j + 1$ is a perfect square for every
> $i \neq j$.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Diophantine_quintuple)
> - [Du16] Dujella, Andrej,
>   [*What is... a Diophantine m-tuple?*](https://www.ams.org/journals/notices/201607/rnoti-p772.pdf),
>   Notices Amer. Math. Soc. 63 (2016), 772--774.
> - [Du] Dujella, Andrej,
>   [*Diophantine quintuple conjecture*](https://web.math.pmf.unizg.hr/~duje/quint.html).
> - [HTZ19] He, Bo, Togbé, Alain and Ziegler, Volker,
>   [*There is no Diophantine quintuple*](https://arxiv.org/abs/1610.04020),
>   Trans. Amer. Math. Soc. 371 (2019), 6665--6709.
> - [BD69] Baker, Alan and Davenport, Harold, The equations $3x^2-2=y^2$ and $8x^2-7=z^2$.
>   Quart. J. Math. Oxford Ser. (2) 20 (1969), 129--137.
> - [Gi99] Gibbs, Philip,
>   [*Some rational Diophantine sextuples*](https://arxiv.org/abs/math/9902081), (1999).

*Quoted from [FormalConjectures/Wikipedia/DiophantineTuple.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 2 open, 2 solved and 2 textbook results. It also has 2 test statements, counted here but not shown.

## `DiophantineTuple.isDiophantineTuple_of_subset`

Textbook result, proved here.

> The property of being a Diophantine tuple is closed under subsets. [Du16]

```lean
theorem isDiophantineTuple_of_subset (s t : Finset R) (h1 : IsDiophantineTuple t)
    (h2 : s ⊆ t) : IsDiophantineTuple s
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L71).

## `DiophantineTuple.noIntegralDiophantineFiveTuple`

Solved: stated here without proof.

> The Diophantine 5-tuple theorem: there does not exist an integral Diophantine 5-tuple. [HTZ19]

```lean
theorem noIntegralDiophantineFiveTuple : NoIntegralDiophantineFiveTuple
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L109).

## `DiophantineTuple.hasUniqueExtension_of_forall`

Open: stated without proof.

> The "strong Diophantine 5-tuple conjecture", so-called because it implies the Diophantine
> 5-tuple theorem (see `noIntegralDiophantineFiveTuple_of_hasUniqueExtensionOfForall`). [Du]

```lean
theorem hasUniqueExtension_of_forall : HasUniqueExtensionOfForall
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L150).

## `DiophantineTuple.noIntegralDiophantineFiveTuple_of_hasUniqueExtensionOfForall`

Textbook result, proved here.

> If every integral Diophantine triple has a unique extension by a larger element, then there
> is no integral Diophantine 5-tuple. [Du]
>
> Proof: suppose a 5-tuple $a < b < c < d_1 < d_2$ exists; then $d_1 = d_2$ by unique extension.

```lean
theorem noIntegralDiophantineFiveTuple_of_hasUniqueExtensionOfForall :
    HasUniqueExtensionOfForall → NoIntegralDiophantineFiveTuple
```

Category `textbook`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L159).

## `DiophantineTuple.hasUniqueExtension_of_1_3_8`

Solved: stated here without proof.

> `HasUniqueExtension` is known to hold for certain triples, including $\{1, 3, 8\}$: this is
> essentially the Baker–Davenport theorem [BD69], which states that $120$ is the only integer
> $d$ such that $\{1, 3, 8, d\}$ is a Diophantine tuple. Together with a finite check ruling out
> $d < 8$, this shows that no integral Diophantine tuple properly extends $\{1, 3, 8, 120\}$.

```lean
theorem hasUniqueExtension_of_1_3_8 : HasUniqueExtension 1 3 8
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L195).

## `DiophantineTuple.rational_7_tuple`

Open: stated without proof.

> Does there exist a rational Diophantine 7-tuple? [Du16]

```lean
theorem rational_7_tuple :
    ∃ t, IsRationalDiophantineTuple t ∧ t.card = 7
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/DiophantineTuple.lean, line 221](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean#L221).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/DiophantineTuple.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/DiophantineTuple.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Diophantine_quintuple)
