---
declaration: theorem
origin: cited
lean: OhbaConjecture.ohba_conjecture, OhbaConjecture.ohba_conjecture.variants.erdos_rubin_taylor
statement: formalized
---

# Ohba's conjecture (2002; proved by Noel, Reed and Wu 2015)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/List_coloring#Ohba's_conjecture)
> * [Oh02] Ohba, K. (2002). "On chromatic-choosable graphs." *J. Graph Theory* 40, pp. 130--135.
> * [NRW15] Noel, J. A., Reed, B. A. and Wu, H. (2015). "A proof of a conjecture of Ohba."
>   *J. Graph Theory* 79, pp. 86--102. [arXiv:1211.1999](https://arxiv.org/abs/1211.1999)
> * [ERT79] Erdős, P., Rubin, A. L. and Taylor, H. (1979). "Choosability in graphs."
>   *Congr. Numer.* 26, pp. 125--157.

*Quoted from [FormalConjectures/Wikipedia/OhbaConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/OhbaConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 2 API statements, counted here but not shown.

## `OhbaConjecture.ohba_conjecture`

Solved: stated here without proof.

> **Ohba's conjecture (2002), proved by Noel, Reed and Wu (2015).**
>
> Every graph $G$ with at most $2\chi(G) + 1$ vertices is *chromatic-choosable*: it is
> $\chi(G)$-choosable, so its choice number equals its chromatic number.

```lean
theorem ohba_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      (Fintype.card V : ℕ∞) ≤ 2 * G.chromaticNumber + 1 →
      Choosable G G.chromaticNumber.toNat
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/OhbaConjecture.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/OhbaConjecture.lean#L59).

## `OhbaConjecture.ohba_conjecture.variants.erdos_rubin_taylor`

Solved: stated here without proof.

> **Complete multipartite graphs with parts of size at most $2$ (Erdős–Rubin–Taylor 1979).**
>
> The complete multipartite graph $K_{2,2,\dots,2}$ with $k$ parts has $2k$ vertices
> and is $k$-choosable, as shown by Erdős, Rubin and Taylor.
>
> *Reference:* [ERT79].

```lean
theorem ohba_conjecture.variants.erdos_rubin_taylor (k : ℕ) :
    Choosable (completeMultipartiteGraph (fun _ : Fin k => Fin 2)) k
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/OhbaConjecture.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/OhbaConjecture.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/OhbaConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/OhbaConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/List_coloring#Ohba's_conjecture)
