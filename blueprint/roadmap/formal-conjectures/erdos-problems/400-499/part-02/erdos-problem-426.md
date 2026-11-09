---
declaration: theorem
origin: cited
lean: Erdos426.erdos_426
statement: formalized
---

# Erdős Problem 426

> *References:*
> - [erdosproblems.com/426](https://www.erdosproblems.com/426)
> - [Er76b] Erdős, P., *Problems and results in graph theory and combinatorial analysis*.
>   Proceedings of the Fifth British Combinatorial Conference (1976), 169-192.
> - [EnEr72] Entringer, R. C. and Erdős, Paul, *On the number of unique subgraphs of a graph*.
>   J. Combinatorial Theory Ser. B (1972), 112-115.
> - [HaSc73] Harary, Frank and Schwenk, Allen J., *On the number of unique subgraphs*.
>   J. Combinatorial Theory Ser. B (1973), 156-160.
> - [Br75] Brouwer, A. E., *Note: "On the number of unique subgraphs of a graph"
>   (J. Combinatorial Theory Ser. B 13 (1972), 112-115) by R. C. Entringer and P. Erdős*.
>   J. Combinatorial Theory Ser. B (1975), 184-185.
> - [BrCh24] Bradač, D. and Christoph, M., *Unique subgraphs are rare*. arXiv:2410.16233 (2024).

*Quoted from [FormalConjectures/ErdosProblems/426.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/426.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/426](https://www.erdosproblems.com/426).

The file states 1 research or textbook statement: 1 solved. It also has 1 test statement, counted here but not shown.

## `Erdos426.erdos_426`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos426.lean](https://github.com/plby/lean-proofs/blob/68da20b96673899166e94638f5a7fffeb7231d35/src/latest/ErdosProblems/Erdos426.lean).

> We say $H$ is a unique subgraph of $G$ if there is exactly one way to find $H$ as a subgraph
> (not necessarily induced) of $G$. Is there a graph on $n$ vertices with
> $$\gg \frac{2^{\binom{n}{2}}}{n!}$$
> many distinct unique subgraphs?
>
> Bradač and Christoph [BrCh24] have proved the answer is no: if $f(n)$ is the maximum number of
> unique subgraphs in a graph on $n$ vertices then
> $$f(n) = o\left(\frac{2^{\binom{n}{2}}}{n!}\right).$$
>
> The $\gg$ below is read as: some constant $c>0$ works for arbitrarily large $n$. The negation
> of the proposition on the right is then exactly $f(n) = o(2^{\binom{n}{2}}/n!)$, the form in
> which Bradač and Christoph [BrCh24] resolved the problem.
>
> The linked file states the resolution in that negated form, as
> `Tendsto fSeq atTop (nhds 0)`. It counts the isomorphism classes occurring as unique subgraphs,
> whereas `uniqueSubgraphCount` counts their representatives $G\leq H$; uniqueness forces exactly
> one representative per class, so the two counts agree.

```lean
theorem erdos_426 :
    ¬ ∃ c : ℝ, 0 < c ∧ ∃ᶠ (n : ℕ) in atTop, ∃ H : SimpleGraph (Fin n),
      c * ((2 : ℝ) ^ n.choose 2 / n.factorial) ≤ (uniqueSubgraphCount H : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/426.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/426.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/426.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/426.lean)
- [erdosproblems.com/426](https://www.erdosproblems.com/426)
